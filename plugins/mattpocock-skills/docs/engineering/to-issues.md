Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=to-issues
```

```bash
npx skills update to-issues
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/to-issues)

## What it does

`to-issues` 把 plan、spec 或 PRD 拆成可独立领取的 issue tracker issues。

它的约束是 vertical slices：每个 issue 都应有用户可观察的结果，能在 fresh session 中独立完成，而不是按技术层横切。

## When to reach for it

你通过输入 `/to-issues` 调用它；agent 不会自行触发。

当 PRD 已经存在，而工作大到需要多个 sessions 或多个 agents 时使用它。PRD 还不存在时，先用 [to-prd](https://aihero.dev/skills-to-prd)。

## Prerequisites

Issue tracker 应该已经通过 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置好；否则它不知道应该创建什么格式的 issues。

## Where it fits

它位于 main chain 中 PRD 与 implementation 之间：

```txt
grill-with-docs -> to-prd -> to-issues -> implement -> code-review
```

完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
