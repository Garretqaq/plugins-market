Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=grill-me
```

```bash
npx skills update grill-me
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/productivity/grill-me)

## What it does

`grill-me` 围绕计划或设计持续追问，直到 decision tree 的每个分支都被解决。

它是 stateless grilling：不写 `CONTEXT.md`，不创建 ADR，只通过对话让 plan 更清晰。

## When to reach for it

你通过输入 `/grill-me` 调用它；agent 不会自行触发。

当你没有 codebase，或这个计划不属于 repo，但仍想在执行前被严格追问时使用它。有 codebase 并希望留下文档痕迹时，用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。

## Where it fits

它是 standalone planning skill，底层使用 [grilling](https://aihero.dev/skills-grilling) 的访谈 loop。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
