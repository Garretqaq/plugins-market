Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=ask-matt
```

```bash
npx skills update ask-matt
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/ask-matt)

## What it does

`ask-matt` 是本仓库 skills 的 router。你描述当前情境，它告诉你应该走哪个 skill 或 flow，以及按什么顺序运行。

它本身不执行工作，不 grill、不写 PRD、不修 bug，只负责定位。它尤其用于 user-invoked skills，因为这些 skills 不会被模型自动触发，需要你知道何时输入它们。

## When to reach for it

你通过输入 `/ask-matt` 调用它；agent 不会自行使用它。

当你不确定该用哪个 skill 或 flow 时使用它：有一个 idea 但不知道从哪里开始，bug reports 堆积但不确定是否需要 `/triage`，或两个 skills 看起来相近但边界不清。如果你已经知道要用哪个 skill，直接调用那个 skill。

## Flows, not just skills

`ask-matt` 的核心概念是 **flow**：穿过多个 skills 的路径，而不是单个工具。大多数工作走 idea -> ship 的 main flow；triage 和 codebase health 是两个入口；其他 skills 则是 standalone 或 vocabulary layer。

## Where it fits

`ask-matt` 是整套 skills 之上的地图。它不属于某条 chain，而是把你指向 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)、[triage](https://aihero.dev/skills-triage)、[tdd](https://aihero.dev/skills-tdd) 等入口。
