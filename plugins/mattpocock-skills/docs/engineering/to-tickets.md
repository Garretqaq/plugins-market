Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=to-tickets
```

```bash
npx skills update to-tickets
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/to-tickets)

## What it does

`to-tickets` 把 plan、spec 或 conversation 拆成 **tickets**，每个 ticket 都是 tracer-bullet vertical slice，并声明 block 它的 tickets，然后发布到配置好的 tracker。

每个 tracer bullet 都是贯穿 schema、API、UI 和 tests 的窄而完整路径，不是只完成某一层的 horizontal slice。完成的 slice 能独立 demo 或 verify，因此可以安全交给 agent。

## When to reach for it

显式输入 `/to-tickets` 调用。已有 agreed plan 或 written spec、准备拆票时使用。可以直接基于 conversation，也可以传入 spec/issue reference；它会先读取完整 body 和 comments。还没有 spec 时先用 [to-spec](https://aihero.dev/skills-to-spec)。

## Prerequisites

先用 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置 issue tracker 和 triage label vocabulary。真实 tracker 上发布时会应用 `ready-for-agent`。

## One artifact, two readings

- **Local files** → `.scratch/<feature>/issues/` 下每 ticket 一个文件，按 blockers-first 编号，edges 写成文本；由人类从上到下处理。
- **真实 tracker（GitHub、Linear）** → 每 ticket 一个 issue，使用 native blocking links（或 sub-issues）。所有 blockers 都完成的 ticket 位于 **frontier**，可由多个 agents 并行领取。

## The wide-refactor exception

Wide refactor 无法保持每个 vertical slice 独立 green，因此改用 **expand–contract**：先在旧形式旁添加新形式，再按 blast radius 分批迁移 call sites，最后在所有 batches 完成后删除旧形式。如果 batches 无法独立 green，就共享 integration branch，并由最终 integrate-and-verify ticket 承诺 green。

## Where it fits

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```
