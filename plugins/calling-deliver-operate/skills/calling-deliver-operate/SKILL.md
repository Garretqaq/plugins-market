---
name: calling-deliver-operate
description: Use when an AI/MCP client needs to call deliver-operate APIs (order queries, etc.) on behalf of a user and must first obtain authorization — covers the device-auth flow to get an ait_ token and the order query API.
---

# Calling deliver-operate (AI/MCP)

## Overview

deliver-operate 用 header 会话（`Authorization`）鉴权。外部 AI/MCP 自己没有登录态，必须先走**设备授权流程**让用户登录授权，拿到一个不透明令牌 `ait_<hex>`，之后用它当 `Authorization` 调任意查询接口——后端会把它换回该用户的真实会话，AI 即以该用户身份、继承其角色/区域权限读数据。

**核心原则：先授权拿 `ait_` 令牌，再带令牌调业务接口。令牌 7 天有效，401 即失效需重新授权。**

⛔ **硬性规则：查询订单/数据必须带创建时间范围（`createTimeLeft` + `createTimeRight`），禁止无界全量查询。** `deliver.py` 已强制校验，缺时间范围直接拒绝。

所有接口都是 `POST` + JSON body；统一响应包装 `{"code":"0000","data":...,"message":"..."}`，`code == "0000"` 为成功。

## Quick Start（推荐：令牌已缓存，下次免授权）

本 skill 目录自带助手脚本 `deliver.py` 与 `config.json`，**调用地址 `baseUrl` 与授权令牌 `aiToken` 都持久化在 `config.json`**，授权一次后长期复用。

> **首次使用**：仓库不含 `config.json`（它存令牌，已 `.gitignore`）。先从模板复制一份：
> ```bash
> cd <本 skill 目录>
> cp config.json.example config.json      # Windows: copy config.json.example config.json
> ```
> 模板里 `baseUrl` 默认指向生产 `https://deliveradmin.jetmobo.com`，测试环境改成 `http://test-deliveradmin.jetmobo.com`；`aiToken` 留空，`authorize` 后自动写入。

```bash
cd <本 skill 目录>
# 仅首次 / 令牌失效时：跑设备授权，自动把 aiToken 写入 config.json
python3 deliver.py authorize
# 之后直接查数据（用缓存令牌，无需再授权）
python3 deliver.py orders --page 1 --size 20
python3 deliver.py orders --body '{"status":[1,2],"cityList":["广州市"],"pageNum":1,"pageSize":20}'
python3 deliver.py whoami                       # 验证令牌是否仍有效
python3 deliver.py call /api/deliver-order/pageOrderStats --body '{"pageNum":1,"pageSize":20}'
```

**判定逻辑**：`config.json.aiToken` 为空 → 先 `authorize`；任何调用返回 **HTTP 401** → 令牌失效，重新 `authorize`。`baseUrl` 改环境时直接改 `config.json`。
**跨平台**：脚本零第三方依赖，macOS / Linux / Windows 通用。Windows 上若没有 `python3` 命令，把命令里的 `python3` 换成 `python` 或 `py`（如 `py deliver.py authorize`）。授权时会用标准库 `webbrowser` 自动打开验证链接；打不开就手动复制终端里打印的链接到浏览器。
**安全**：`config.json` 存的是 7 天有效的用户级令牌，**切勿提交到任何 git 仓库**（它在 `~/.claude/skills/` 下，不在项目仓库内）。

下面是底层接口契约（脚本不可用、或要手动/MCP 直连时参考）。

## When to Use

- AI/MCP 需要查询 deliver-operate 的订单等数据，但还没有有效的 `ait_` 令牌
- 已持有 `ait_` 令牌但调用返回 **HTTP 401** → 令牌失效/被吊销，需重新走授权
- 要接入 deliver-operate 的新查询接口（见「扩展新接口」）

不适用：内部服务间调用（用 Feign）；需要写操作时同样适用，但务必让用户清楚 AI 会以其身份操作。

## 授权流程（一次性，拿 ait_ 令牌）

```
1. POST /api/ai-auth/device/code         → 拿 deviceCode + verificationUrl
2. 把 verificationUrl 交给用户在浏览器打开 → 登录(SSO) + 点「确认授权」
3. 轮询 POST /api/ai-auth/device/token    → 用户确认后返回 accessToken(ait_...)
4. 之后所有业务请求带 Authorization: <accessToken>
```

**① 申请设备码**（匿名）
```
POST /api/ai-auth/device/code
{ "clientName": "Claude MCP" }
→ data: { deviceCode, verificationUrl, interval(秒), expiresIn(秒,600) }
```
把 `verificationUrl` 原样给用户打开。设备码 10 分钟内有效。

**② 用户授权**：用户打开链接 → 未登录会自动跳 SSO 登录 → 看到确认页点「确认授权」。AI 这边无需操作，继续轮询。

**③ 轮询换令牌**（匿名，按 `interval` 间隔）
```
POST /api/ai-auth/device/token
{ "deviceCode": "<上一步的 deviceCode>" }
→ 未确认: data.status == "pending"     （继续轮询）
→ 已确认: data.status == "authorized", data.accessToken == "ait_xxx", expiresIn=604800
→ 过期/不存在: 业务错误 expired_token   （重新从 ① 开始）
```
`accessToken` 只能换取一次（换走即失效），AI 需自行保存复用。

**吊销**（可选）：`POST /api/ai-auth/revoke { "aiToken": "ait_..." }`，删除后该令牌立即 401。

## 用令牌调业务接口

所有业务请求加 header：`Authorization: ait_<hex>`。后端透明换回真实会话。

**令牌失效信号**：响应 **HTTP 401** → 令牌无效/被吊销/过期 → 重新走授权流程。

## 业务接口（按接口分文件维护）

每个可调用接口的路径、请求/响应字段、`deliver.py` 示例，单独维护在 `interfaces/` 文件夹，一个接口一个文件。先看索引：

- **[interfaces/_index.md](interfaces/_index.md)** —— 接口清单 + 路径速查表
- [interfaces/order-page.md](interfaces/order-page.md) —— 配送订单分页查询 `POST /api/deliver-order/page`
- [interfaces/number-query-create.md](interfaces/number-query-create.md) —— 创建号码查询批量任务（写操作）`POST /api/deliver-order/numberQuery/create`

需要某个接口时，读对应文件拿到 body 字段，再用 `python3 deliver.py call <path> --body '<json>'`（或封装好的子命令）调用。

## 扩展新接口

授权令牌通用，新增接口**无需改授权逻辑**。步骤：
1. 在 deliver-operate 找到目标 `@PostMapping` 接口的路径与请求/响应模型（模型多在 `deliver-api` 模块 `com.junbo.deliver.model`）。
2. 在 `interfaces/` 新建 `<接口名>.md`（仿 order-page.md 的格式），并在 `interfaces/_index.md` 表格追加一行。
3. 带同一个 `ait_` 令牌 `POST` 调用即可（`deliver.py call <path> --body ...`）。

## Common Mistakes

| 错误 | 纠正 |
|---|---|
| 直接调订单接口、没先拿令牌 | 必须先完成授权流程拿 `ait_` |
| 把 `verificationUrl` 自己请求/爬取 | 必须由**真人用户**在浏览器打开登录确认，AI 不能代登 |
| 轮询太频繁 | 按返回的 `interval` 间隔轮询 |
| 401 后继续重试原令牌 | 401=令牌失效，必须重新走授权流程换新令牌 |
| 用 GET / form 提交 | 全部 `POST` + JSON body |
| 误判成功 | 看 `code == "0000"`，不是 HTTP 200 就算成功 |
| 查订单不带时间范围 | **必须带 `createTimeLeft`+`createTimeRight`**，否则脚本拒绝、也避免拉爆全量 |
