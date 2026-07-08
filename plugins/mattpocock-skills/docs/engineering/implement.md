Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=implement
```

```bash
npx skills update implement
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/implement)

## What it does

`implement` 把 PRD 或 issue 集合描述的工作落成代码：通过 test-driven development、typechecking 和测试套件推进，然后交给 review 并提交到当前 branch。

它不决定要构建什么。Spec 和 seams 应该已经确定；`implement` 执行计划，而不是重新打开计划。

## When to reach for it

你通过输入 `/implement` 调用它；agent 不会自行触发。

当工作已经写成 PRD 或拆成 issues，并准备转成代码时使用它。如果 spec 还不存在，用 [to-prd](https://aihero.dev/skills-to-prd)；只想 test-first 写一个具体 behavior，用 [tdd](https://aihero.dev/skills-tdd)。

## Pre-agreed seams

核心概念是 **seam**：在写代码前选定的稳定 public interface。`implement` 不在 build 中途发明 seams，而是使用上游 plan 中已经认可的 seams，并通过 [tdd](https://aihero.dev/skills-tdd) 写测试。

## Where it fits

它是 main chain 末段的 build step：

```txt
grill-with-docs -> to-prd -> to-issues -> implement -> code-review
```

它的邻居是 [to-issues](https://aihero.dev/skills-to-issues)、[tdd](https://aihero.dev/skills-tdd) 和 [code-review](https://aihero.dev/skills-code-review)。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
