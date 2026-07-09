#!/usr/bin/env python3
"""
deliver-operate 调用助手：把调用地址(baseUrl)与授权令牌(aiToken)维护在同目录 config.json，
授权一次后下次直接复用，令牌失效(401)再重新授权。零第三方依赖（仅标准库）。

用法：
  python3 deliver.py authorize                  # 跑设备授权流程，把 aiToken 写入 config.json
  python3 deliver.py whoami                      # 用已存令牌做一次轻量调用，验证是否有效
  python3 deliver.py orders [--page N] [--size N] [--body '<json>']
                                                 # 调订单分页查询 /api/deliver-order/page
  python3 deliver.py call <path> [--body '<json>']
                                                 # 通用：带已存令牌 POST 任意 deliver-operate 接口

@author sgz
@since 2026-06-17
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
import webbrowser

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")


def post(url, body, token=None):
    """POST JSON。返回 (http_status, parsed_json_or_text)。HTTP 错误也返回其 status 与 body。"""
    data = json.dumps(body or {}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = token
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, _try_json(raw)
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        return e.code, _try_json(raw)
    except urllib.error.URLError as e:
        print(f"[网络错误] {e}", file=sys.stderr)
        sys.exit(2)


def _try_json(raw):
    try:
        return json.loads(raw)
    except Exception:
        return raw


def unwrap(payload):
    """校验统一响应包装 {code,data,message}；成功返回 data，失败打印并退出。"""
    if isinstance(payload, dict) and "code" in payload:
        if str(payload.get("code")) == "0000":
            return payload.get("data")
        print(f"[业务错误] code={payload.get('code')} message={payload.get('message')}", file=sys.stderr)
        sys.exit(1)
    return payload


def cmd_authorize(cfg, args):
    base = cfg["baseUrl"].rstrip("/")
    client = args.client or cfg.get("clientName") or "Claude MCP"

    status, payload = post(f"{base}/api/ai-auth/device/code", {"clientName": client})
    data = unwrap(payload)
    device_code = data["deviceCode"]
    verification_url = data["verificationUrl"]
    interval = int(data.get("interval") or 5)
    expires_in = int(data.get("expiresIn") or 600)

    print("=" * 60)
    print("请在浏览器打开以下链接，登录并点「确认授权」：")
    print(f"\n  {verification_url}\n")
    print("（无登录态会自动跳 SSO 登录，登录后回到确认页）")
    print("=" * 60)
    try:
        webbrowser.open(verification_url)
    except Exception:
        pass

    deadline = time.time() + expires_in
    print("等待授权中", end="", flush=True)
    while time.time() < deadline:
        time.sleep(interval)
        st, pl = post(f"{base}/api/ai-auth/device/token", {"deviceCode": device_code})
        if isinstance(pl, dict) and str(pl.get("code")) != "0000":
            print(f"\n[失败] {pl.get('message')}（链接可能已过期，请重试 authorize）", file=sys.stderr)
            sys.exit(1)
        d = pl.get("data") if isinstance(pl, dict) else None
        if d and d.get("status") == "authorized" and d.get("accessToken"):
            cfg["aiToken"] = d["accessToken"]
            save_config(cfg)
            print(f"\n[成功] 令牌已保存到 {CONFIG_PATH}")
            print(f"       有效期约 {int(d.get('expiresIn', 604800)) // 86400} 天，下次直接调用无需再授权。")
            return
        print(".", end="", flush=True)
    print("\n[超时] 用户未在有效期内完成授权，请重试 authorize", file=sys.stderr)
    sys.exit(1)


# 强制带时间范围的接口（避免无界全量查询）
TIME_REQUIRED_PATHS = {"/api/deliver-order/page"}


def _require_time_range(body):
    if not body.get("createTimeLeft") or not body.get("createTimeRight"):
        print("[拒绝] 查询订单数据必须带时间范围：createTimeLeft 与 createTimeRight"
              "（格式 yyyy-MM-dd HH:mm:ss）。\n"
              "  示例：orders --from '2026-06-01 00:00:00' --to '2026-06-17 23:59:59'，"
              "或在 --body 里带上这两个字段。", file=sys.stderr)
        sys.exit(1)


def _require_token(cfg):
    token = cfg.get("aiToken")
    if not token:
        print("[未授权] config.json 里没有 aiToken，请先运行：python3 deliver.py authorize", file=sys.stderr)
        sys.exit(1)
    return token


def _call(cfg, path, body):
    base = cfg["baseUrl"].rstrip("/")
    token = _require_token(cfg)
    status, payload = post(f"{base}{path}", body, token=token)
    if status == 401:
        print("[令牌失效] HTTP 401——令牌已过期/被吊销，请重新运行：python3 deliver.py authorize", file=sys.stderr)
        sys.exit(1)
    return unwrap(payload)


def cmd_orders(cfg, args):
    body = json.loads(args.body) if args.body else {}
    if args.start:
        body["createTimeLeft"] = args.start
    if args.end:
        body["createTimeRight"] = args.end
    body.setdefault("pageNum", args.page)
    body.setdefault("pageSize", args.size)
    _require_time_range(body)  # 强制时间范围
    data = _call(cfg, "/api/deliver-order/page", body)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_call(cfg, args):
    body = json.loads(args.body) if args.body else {}
    if args.path in TIME_REQUIRED_PATHS:
        _require_time_range(body)  # 强制时间范围
    data = _call(cfg, args.path, body)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_whoami(cfg, args):
    # 用订单查询接口拉 1 条做最轻量的有效性探测（带近 1 天时间范围以满足强制约束）
    import datetime
    now = datetime.datetime.now()
    body = {
        "pageNum": 1, "pageSize": 1,
        "createTimeLeft": (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "createTimeRight": now.strftime("%Y-%m-%d %H:%M:%S"),
    }
    data = _call(cfg, "/api/deliver-order/page", body)
    total = data.get("total") if isinstance(data, dict) else "?"
    print(f"[有效] 令牌可用，近 1 天订单数(当前权限范围) total={total}")


def main():
    p = argparse.ArgumentParser(description="deliver-operate 调用助手")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("authorize", help="设备授权，写入 aiToken")
    pa.add_argument("--client", help="客户端名称（确认页/审计展示）")

    sub.add_parser("whoami", help="验证当前令牌是否有效")

    po = sub.add_parser("orders", help="订单分页查询（强制带时间范围）")
    po.add_argument("--from", dest="start", help="创建开始时间 yyyy-MM-dd HH:mm:ss（必填）")
    po.add_argument("--to", dest="end", help="创建结束时间 yyyy-MM-dd HH:mm:ss（必填）")
    po.add_argument("--page", type=int, default=1)
    po.add_argument("--size", type=int, default=20)
    po.add_argument("--body", help="完整查询 JSON（可替代 --from/--to 提供时间范围）")

    pc = sub.add_parser("call", help="通用 POST 任意接口")
    pc.add_argument("path", help="如 /api/deliver-order/pageOrderStats")
    pc.add_argument("--body", help="请求体 JSON")

    args = p.parse_args()
    cfg = load_config()
    {"authorize": cmd_authorize, "whoami": cmd_whoami, "orders": cmd_orders, "call": cmd_call}[args.cmd](cfg, args)


if __name__ == "__main__":
    main()
