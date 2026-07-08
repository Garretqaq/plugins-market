Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=prototype
```

```bash
npx skills update prototype
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/prototype)

## What it does

`prototype` 构建 throwaway code 来回答一个设计问题。问题决定形状：state/business-logic 用可运行 terminal app，UI 问题用同一路由里的多个差异化 variations。

它从第一天就是 throwaway。目标是学习并保留答案，而不是把 prototype 慢慢变成 production。

## When to reach for it

输入 `/prototype`，或当你想 sanity-check data model、state machine、UI 方向，或说 “prototype this” / “let me play with it” 时由 agent 自动触发。

当纸面讨论无法回答 “它感觉对吗” 时使用它。要把已经确定的 plan 实现到 production，用 [implement](https://aihero.dev/skills-implement)。

## Two branches

核心分支是 **logic** 与 **UI**。Logic prototype 暴露 state transitions；UI prototype 提供多个可切换 variants。选错分支会浪费整个 prototype。

## Where it fits

它是 main flow 中的 detour，也可以独立使用。用 [handoff](https://aihero.dev/skills-handoff) 在 prototype session 和原始 planning session 之间传递 context。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
