Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=grill-with-docs
```

```bash
npx skills update grill-with-docs
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/grill-with-docs)

## What it does

`grill-with-docs` 围绕计划或设计持续追问，同时构建项目的 domain model，并把术语和决策写入 `CONTEXT.md` 与 ADRs。

它不是普通聊天。它是带文档痕迹的 grilling：每个问题都推动 shared understanding，重要决策会落地到 repo。

## When to reach for it

你通过输入 `/grill-with-docs` 调用它；agent 不会自行触发。

有 codebase、想在开始实现前打磨 idea 时使用它。没有 codebase 时，用 [grill-me](https://aihero.dev/skills-grill-me)；只需要底层访谈 loop 时，用 [grilling](https://aihero.dev/skills-grilling)。

## Prerequisites

它会写入或更新 repo 中的 `CONTEXT.md` 和 ADRs。第一次使用前通常先运行 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills)，让 docs 位置和 issue tracker 配置清楚。

## Where it fits

它是 main flow 的入口：

```txt
grill-with-docs -> to-prd -> to-issues -> implement -> code-review
```

完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
