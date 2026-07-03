# deliver-operate AI 调用助手

> 通过设备授权流程（Device Authorization Flow）获取 `ait_` 令牌，安全地代表用户调用 deliver-operate 订单查询接口。

## 快速开始

```bash
# 1. 设备授权（首次 / 令牌失效时）
python3 deliver.py authorize

# 2. 查询订单（自动复用缓存令牌）
python3 deliver.py orders --from '2026-06-11 00:00:00' --to '2026-06-17 23:59:59' --page 1 --size 20

# 3. 验证令牌是否有效
python3 deliver.py whoami

# 4. 通用调用任意接口
python3 deliver.py call /api/deliver-order/pageOrderStats --body '{"pageNum":1,"pageSize":20}'
```

## 项目结构

```
.
├── deliver.py              # 主脚本：授权 + 查询 + 通用调用
├── config.json             # 本地配置（baseUrl + aiToken），已加入 .gitignore
├── interfaces/
│   ├── _index.md           # 接口清单索引
│   └── order-page.md       # 订单分页查询接口文档
├── SKILL.md                # Skill 元数据（Claude Code 用）
└── README.md               # 本文件
```

## 核心流程

1. **设备授权** → 获取 `deviceCode` + `verificationUrl`
2. **用户确认** → 浏览器打开链接，登录并点「确认授权」
3. **轮询换令牌** → 获取 `ait_<hex>` 令牌，写入 `config.json`
4. **带令牌调用** → 所有业务请求带 `Authorization: ait_<hex>`

## 安全提示

- `config.json` 中的 `aiToken` 是**用户级敏感令牌**，已加入 `.gitignore`，**切勿提交到 git**
- 令牌 7 天有效，HTTP 401 即失效，需重新 `authorize`
- 查询订单**必须带时间范围**（`createTimeLeft` + `createTimeRight`），脚本已强制校验

## 环境要求

- Python 3.6+（零第三方依赖，仅标准库）

## 接口文档

详见 [`interfaces/_index.md`](interfaces/_index.md)。
