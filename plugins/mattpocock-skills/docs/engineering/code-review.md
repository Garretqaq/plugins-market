Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=code-review
```

```bash
npx skills update code-review
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/code-review)

## What it does

`code-review` 对 `HEAD` 与你给定 fixed point 之间的 diff 做双轴 review：**Standards** 检查代码是否符合仓库约定，**Spec** 检查它是否实现了来源 issue 或 PRD。

它不会把两组 findings 合并成一个总 verdict。分开报告是核心约束，因为一个变更可能代码风格正确但做错需求，也可能需求正确但破坏约定。

## When to reach for it

输入 `/code-review`，或当你要求 review branch、PR、work-in-progress changes，或说 “review since X” 时由 agent 自动触发。

当你有一个 diff 和一个 known-good point，并想独立回答 “built right?” 与 “right thing?” 时使用它。写代码本身用 [tdd](https://aihero.dev/skills-tdd)；按完整 spec 构建用 [implement](https://aihero.dev/skills-implement)。

## Prerequisites

Spec 轴线需要找到来源 spec：commit message 中的 issue reference、你传入的路径，或 `docs/` / `specs/` 下的 PRD。Issue tracker 配置来自 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills)。找不到 spec 时，Spec 轴线会跳过并说明。

## Two axes

Standards 使用仓库 standards，并始终带有 Fowler smell baseline；repo 自己的 documented standards 优先于 baseline。Spec 则只检查需求是否完整、是否有 scope creep，以及看似实现但行为不对的地方。

## It's working if

- 它先确认 fixed point 能解析，并确认 diff 非空。
- Standards 和 Spec findings 分成两个清晰区块，并各自引用来源。
- 没有 spec 时，它报告 “no spec available”，而不是编造需求。

## Where it fits

`code-review` 是 main build chain 的尾部 review step：

```txt
grill-with-docs -> to-prd -> to-issues -> implement -> code-review
```

它最接近 [implement](https://aihero.dev/skills-implement)；后者构建并在提交前调用它。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
