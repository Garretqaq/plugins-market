# deliver-operate 接口清单（interfaces/）

每个接口一个文件，记录：路径、用途、请求/响应字段、`deliver.py` 调用示例。
**新增接口时：在本目录加一个 `<接口名>.md`，并在下表追加一行。** 授权令牌通用，无需改授权逻辑。

| 接口文件 | 路径 | 用途 |
|---|---|---|
| [order-page.md](order-page.md) | `POST /api/deliver-order/page` | 交付订单分页查询 |
| [number-query-create.md](number-query-create.md) | `POST /api/deliver-order/numberQuery/create` | 创建号码查询批量任务（写操作） |

> 模型源码位置：请求/响应对象多在 deliver-service 仓库的 `deliver-api` 模块 `com.junbo.deliver.model` 下；接口实现在 `deliver-operate-web` 的 `api/*WebApi.java`。
