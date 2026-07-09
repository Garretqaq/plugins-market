# 创建号码查询批量任务

- **路径**：`POST /api/deliver-order/numberQuery/create`
- **鉴权**：`Authorization: ait_<hex>`
- **用途**：对一批交付订单发起「批量号码查询」异步任务，返回任务编码（`taskCode`），后台异步执行查号
- **实现**：`deliver-operate-web` `DeliverOrderWebApi#createNumberQueryTask` → Feign `DeliverOrderApi#createNumberQuery`
- **模型**：请求 `NumberQueryBatchTaskCreateRequest extends BatchTaskCreateRequest`，响应 `CommonResponse`

> ⚠️ **这是写操作**：会真实创建后台任务并以当前授权用户身份执行查号。调用前请让用户明确知晓 AI 正以其身份发起操作。
> 无时间范围强制（非分页查询），`deliver.py call` 可直接调用。

## deliver.py 调用

```bash
python3 deliver.py call /api/deliver-order/numberQuery/create \
  --body '{"taskType":1,"deliverOrderCodeList":["HK20260701182227295149523"]}'
```

## 请求字段

订单来源**二选一**：手动勾选订单号 `deliverOrderCodeList`，或筛选条件 `filterCondition`；两者都空会被拒绝（`deliverOrderCodeList 和 filterCondition 至少填写一个`）。

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `taskType` | int | 是 | 任务类型，号码查询固定传 `1`（服务端也会强制置为号码查询） |
| `deliverOrderCodeList` | string[] | 二选一 | 手动勾选的交付订单号列表 |
| `filterCondition` | string | 二选一 | 筛选条件，值为 **JSON 序列化后的 `DeliverOrderPageRequest`**（即 order-page.md 的请求体转成字符串） |
| `operator` | string | 否 | 操作人。**服务端会用当前登录用户覆盖**，无需传 |
| `remark` | string | 否 | 备注 |

## 响应

统一包装 `{"code":"0000","data":{...},"message":"..."}`，`data` 为 `CommonResponse`：

| 字段 | 说明 |
|---|---|
| `message` | 创建成功返回的任务编码 `taskCode`（形如 `BT<uuid>`） |

失败场景（走业务错误 / 异常）：两个来源都为空、筛选/勾选后无有效订单（`无有效订单，无法创建批量任务`）等。

## 示例

请求：
```json
{ "taskType": 1, "deliverOrderCodeList": ["HK20260701182227295149523"] }
```
响应 `data`：
```json
{ "message": "BT2f6c1a9e8b7d4c02a1e3f5079c6b4d21" }
```
