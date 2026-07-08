Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=to-prd
```

```bash
npx skills update to-prd
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/to-prd)

## What it does

`to-prd` 把当前对话整理成 PRD，并发布到项目 issue tracker 或配置好的 docs 位置。

它不重新访谈用户。它只综合当前 thread 已经讨论过的内容，把 decisions、scope、seams 和 acceptance criteria 写清楚。

## When to reach for it

你通过输入 `/to-prd` 调用它；agent 不会自行触发。

当 grilling 已经让方向足够清楚，需要把讨论固化成实现前的 spec 时使用它。讨论还不清楚时，先回到 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。

## Prerequisites

Issue tracker 和 docs layout 应通过 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置。

## Where it fits

它是 main chain 中把对话变成 spec 的步骤：

```txt
grill-with-docs -> to-prd -> to-issues -> implement -> code-review
```

完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
