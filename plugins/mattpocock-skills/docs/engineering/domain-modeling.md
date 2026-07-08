Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=domain-modeling
```

```bash
npx skills update domain-modeling
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/domain-modeling)

## What it does

`domain-modeling` 主动构建和打磨项目的 domain language：挑战模糊术语，用 edge-case scenarios 压测词汇，并在需要时更新 `CONTEXT.md` 与 ADRs。

它不是简单读取 glossary。只有主动 sharpen terms、记录决策、消除 overloaded words 时，才是在做 domain modeling。

## When to reach for it

输入 `/domain-modeling`，或当 agent 发现术语含混、领域词冲突、或 plan 需要共享语言时自动触发。

当问题在于 “我们到底怎么称呼这个概念” 时使用它。要针对计划持续访谈，用 [grilling](https://aihero.dev/skills-grilling) 或 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。

## Shared language

核心成果是更短、更准确的语言。好的 domain model 让人和 agent 用同一套词谈论系统，减少解释成本，也让代码命名更稳定。

## Where it fits

`domain-modeling` 是 vocabulary layer，常被 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 和 [wayfinder](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/in-progress/wayfinder) 使用。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
