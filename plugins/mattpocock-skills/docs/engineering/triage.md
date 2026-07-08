Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=triage
```

```bash
npx skills update triage
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/triage)

## What it does

`triage` 通过一组 triage roles state machine 推进 issues，把原始 bug reports 和 feature requests 变成 agent-ready work。

它只处理你没有创建的原始 incoming issues。由 `to-issues` 生成的 tickets 已经是 agent-ready，不应该再 triage。

## When to reach for it

你通过输入 `/triage` 调用它；agent 不会自行触发。

当 issue tracker 中积累了 raw bugs、requests 或未分类 work，需要判断、补信息、标记和准备给 agent 执行时使用它。

## Prerequisites

Issue tracker 和 triage labels 应通过 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置。

## Where it fits

它是 main flow 的 on-ramp：把 incoming work 转成可由 [implement](https://aihero.dev/skills-implement) 领取的 issues。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
