Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=wayfinder
```

```bash
npx skills update wayfinder
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/wayfinder)

## What it does

`wayfinder` 接手单个 agent session 装不下、从当前位置到 destination 的路仍被 fog 包围的 effort，把它绘制成 issue tracker 上的调查 tickets **shared map**，再逐个解决直到路径清晰。它负责 planning，不直接执行：每个 ticket 解决一个 decision，最终产出 decisions，不是 deliverables。

## When to reach for it

显式输入 `/wayfinder` 调用。Effort 超出一个 session 且 route 仍模糊、还无法直接写 spec 或 plan 时使用。Thread 已经清晰时用 [to-spec](https://aihero.dev/skills-to-spec)；plan 已理解、只需拆票时用 [to-tickets](https://aihero.dev/skills-to-tickets)。

## Prerequisites

Map 和 tickets 位于 repo issue tracker，因此需要 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 写入 tracker wiring 和 “Wayfinding operations”。没有 tracker doc 时默认 local-markdown map。

## The map is an index, fog is the frontier

Map 是一个 `wayfinder:map` issue，tickets 是 child issues。它是 **index, not a store**：每个 decision 只存在对应 ticket 中，map 只写 gist 和 link。Live tickets 之外是 **fog of war**；判断 ticket 或 fog 的标准，是现在能否精确说出 question，而不是现在能否回答。解决 ticket 会让 fog 中现在可说明的内容 **graduate** 成新 tickets。

**Frontier** 是 open、unblocked、unclaimed tickets。Fog 只聚集在通往 **destination** 的方向，超出 destination 的工作属于 **out of scope**，会关闭且永不 graduate。每个 ticket 是 **HITL**（grilling、prototype）或 **AFK**（research）；HITL 只能通过 live exchange 解决，agent 不替人类自问自答。

## It's working if

- 创建 ticket 前先命名 **destination**，固定 scope。
- 一个 map 对应一个 `wayfinder:map` issue，child tickets 通过 name 引用，不只写 `#42`。
- 每个 session 最多解决一个 ticket，答案写 resolution comment，随后 close，并在 Decisions so far 追加一行 pointer。
- Opening grill 没有发现 fog 时停止，说明 effort 足够小、不需要 map。

## Where it fits

`wayfinder` 是 big-idea on-ramp。Fog 清除、路径明确后进入 [to-spec](https://aihero.dev/skills-to-spec)，effort 足够小时也可直接 implement。
