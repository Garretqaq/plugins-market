# 交付订单分页查询

- **路径**：`POST /api/deliver-order/page`
- **鉴权**：`Authorization: ait_<hex>`
- **用途**：按时间/状态/地区/商户/号码等条件分页查询配送订单
- **实现**：`deliver-operate-web` `DeliverOrderWebApi#page`
- **模型**：请求 `DeliverOrderPageRequest extends PageInfo`，响应 `PageInfo<DeliverOrderPageResponse>`

> ⛔ **强制：必须带创建时间范围 `createTimeLeft` + `createTimeRight`**，禁止无界全量查询。`deliver.py` 已硬性校验，缺失直接拒绝。

## deliver.py 调用

```bash
python3 deliver.py orders --from '2026-06-01 00:00:00' --to '2026-06-17 23:59:59' --page 1 --size 20
python3 deliver.py orders --from '2026-06-01 00:00:00' --to '2026-06-17 23:59:59' \
  --body '{"status":[1,2],"cityList":["广州市"]}'
# 等价通用写法（同样强制时间范围）
python3 deliver.py call /api/deliver-order/page \
  --body '{"createTimeLeft":"2026-06-01 00:00:00","createTimeRight":"2026-06-17 23:59:59","pageNum":1,"pageSize":20}'
```

## 请求字段

分页字段与**创建时间范围（`createTimeLeft`+`createTimeRight`）必填**，其余为可选筛选条件，多条件之间是 AND。时间字段格式 `yyyy-MM-dd HH:mm:ss`（时区 GMT+8）。

**分页（来自 PageInfo 基类）**

| 字段 | 类型 | 说明 |
|---|---|---|
| `pageNum` | int | 页码，从 1 开始 |
| `pageSize` | int | 每页条数 |

**时间**

| 字段 | 类型 | 说明 |
|---|---|---|
| `createTimeLeft` / `createTimeRight` | string | 创建时间 起 / 止 — **必填，两者都要带** |
| `allocateVendorTimeStart` / `allocateVendorTimeEnd` | string | 分配商户时间 起 / 止（可选） |

**订单 / 号码 / 用户**

| 字段 | 类型 | 说明 |
|---|---|---|
| `bizOrderCode` | string | 业务订单号，多个用英文逗号分隔 |
| `contactNumber` | string | 联系号码 |
| `handleNo` | string | 办理号码 |
| `custId` | string | 客户编码 |
| `userStatus` | string | 用户状态 |

**地区**

| 字段 | 类型 | 说明 |
|---|---|---|
| `provinceList` | string[] | 省名称集合 |
| `cityList` | string[] | 城市名称集合 |
| `districtList` | string[] | 区/县名称集合 |

**商户 / 配送员 / 操作员**

| 字段 | 类型 | 说明 |
|---|---|---|
| `vendorId` | long | 商户 id |
| `vendorIdList` | long[] | 商户 id 集合 |
| `deliveryPersonId` | long | 配送员 id |
| `deliveryPersonName` | string | 配送员名称 |
| `operName` | string | 操作员姓名 |

**商品 / 渠道 / 运营商**

| 字段 | 类型 | 说明 |
|---|---|---|
| `productName` / `productCode` | string | 商品名称 / 编码 |
| `operateCode` | string | 运营商编码 |
| `channelCode` | string | 渠道编码 |
| `channelCodeList` | string[] | 渠道编码集合 |
| `orgId` | string | 受理渠道 |

**状态 / 标记**

| 字段 | 类型 | 说明 |
|---|---|---|
| `status` | int[] | 订单状态码数组，见下方状态码表 |
| `unblockResult` | int | 解黑结果：0-未解黑，1-成功，2-失败，3-无须解黑 |
| `unassignedReason` | string | 未分配原因 |
| `numberStatus` | int | 号码查询结果：1-号码不存在，2-可结算，3-门店不匹配 |
| `isUrge` | bool | true-只查催派订单（urgeCount>0） |
| `secondFollowFlag` | bool | true-只查二次跟进订单 |
| `operatorPlatform` | enum | 操作端：`商户端`(10) / `运营端`(20) |

### 订单状态码（`status` / 响应 `status`）

| 码 | 含义 |
|---|---|
| 1 | 待分配交付商 |
| 2 | 待分配配送员 |
| 3 | 待领取 |
| 9 | 待二次跟进 |
| 4 | 待处理 |
| 5 | 订单挂起 |
| 6 | 预约配送 |
| 7 | 交付成功 |
| 8 | 交付失败 |

## 响应

`data` 为分页对象：

```json
{ "pageNum": 1, "pageSize": 20, "total": 135, "list": [ /* DeliverOrderPageResponse */ ] }
```

`DeliverOrderPageResponse` 字段（按主题分组）：

**订单基本**

| 字段 | 说明 |
|---|---|
| `id` | 订单 id |
| `deliverOrderCode` | 交付订单号 |
| `bizOrderCode` | 业务订单号 |
| `bizResource` | 来源，1-酬金 |
| `bizType` | 业务类型，1-号卡 |
| `bizOrderTime` | 业务系统下单时间 |
| `status` / `statusStr` | 状态码 / 状态文案 |
| `createTime` / `updateTime` | 创建 / 更新时间 |
| `firstCloseTime` | 一次闭环时间（首次变更为交付成功/失败） |

**号码 / 用户（含脱敏）**

| 字段 | 说明 |
|---|---|
| `contactNumberMask` / `contactNumber` | 联系号码 脱敏 / 明文 |
| `handleNo` / `handleNoOriginal` | 办理号码 脱敏 / 明文 |
| `customerNameMask` / `customerName` | 用户姓名 脱敏 / 明文 |
| `userTags` / `userTagNotice` | 用户标签列表 / 提示文案 |

**地址**

| 字段 | 说明 |
|---|---|
| `province` / `city` / `district` | 配送省 / 市 / 县 |
| `addressMask` / `address` | 详细地址 脱敏 / 明文 |
| `resolveProvince` / `resolveCity` / `resolveDistrict` / `resolveTown` | 解析后 省/市/区县/街道 |

**商品 / 渠道 / 运营商**

| 字段 | 说明 |
|---|---|
| `productCode` / `productName` / `productInfo` | 产品编码 / 名称 / 套餐信息 |
| `displayProductName` | C 端产品别名 |
| `beforeChangeProductCode` / `beforeChangeProductName` / `changeReason` / `productChangeTime` | 产品变更前编码/名称/原因/时间 |
| `operateCode` / `operateName` | 运营商编码 / 名称 |
| `channelCode` / `channelName` | 渠道编码 / 名称 |

**商户 / 配送员 / 流转时间**

| 字段 | 说明 |
|---|---|
| `vendorId` / `vendorName` | 商户 id / 名称 |
| `allocateVendorTime` | 分配商户时间 |
| `deliveryPersonId` / `deliveryPersonName` | 配送员 id / 名称 |
| `allocateDeliveryPersonTime` | 分配配送员时间 |
| `collectionTime` / `reserveTime` / `activateTime` / `deliveryTime` | 领取 / 预约 / 激活 / 交付时间 |
| `poolType` | 抢单池类型：STREET_POOL / REGION_POOL |

**金额 / 欠费 / 催派 / 解黑 / 二次跟进**

| 字段 | 说明 |
|---|---|
| `rechargeAmount` | 充值金额 |
| `unpaidAmount` / `isUnpaid` | 欠费金额 / 是否欠费 |
| `urgeCount` / `lastUrgeTime` / `lastUrgeRemark` / `isUrge` | 催派次数 / 最后催派时间 / 备注 / 是否催派 |
| `unlockBlackCount` / `unblockResult` / `unblockRemark` / `unblockFeedbackTime` | 解黑次数 / 结果 / 备注 / 反馈时间 |
| `secondFollowFlag` / `secondFollowRemark` / `secondFollowTime` / `secondDeliverRemark` | 二次跟进 标记/备注/时间/二次交付备注 |

**号码状态 / 其它**

| 字段 | 说明 |
|---|---|
| `numberStatus` / `numberStatusStr` / `numberQueryResult` | 号码状态码 / 文案 / 查询结果对象 |
| `errorFlag` | 异常标记：1-异常（号码状态1或3），0-正常 |
| `deliverRemindFlag` | 线下交付是否提醒：0-否，1-是 |
| `unassignedReason` | 未分配原因代码 |
| `certificateUrlList` | 办理凭证 URL 数组 |
| `invoiceSubject` | 开票主体 |
| `remark` / `reason` / `oldOrderMsg` | 备注 / 原因 / 上一笔订单备注 |

## 示例

请求：
```json
{ "pageNum": 1, "pageSize": 20, "createTimeLeft": "2026-06-01 00:00:00", "createTimeRight": "2026-06-17 23:59:59", "status": [1, 2], "cityList": ["广州市"] }
```
响应 `data`：
```json
{ "pageNum": 1, "pageSize": 20, "total": 2,
  "list": [ { "deliverOrderCode": "HK...", "bizOrderCode": "BIZ...", "status": 1, "statusStr": "待分配交付商",
             "vendorName": "xx商户", "productName": "xx套餐", "city": "广州市", "createTime": "2026-06-10 09:12:33" } ] }
```
