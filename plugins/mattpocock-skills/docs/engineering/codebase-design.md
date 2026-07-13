Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=codebase-design
```

```bash
npx skills update codebase-design
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/codebase-design)

## What it does

`codebase-design` 提供 deep modules 的共享纪律和词汇：module、interface、depth、seam、adapter、leverage 和 locality。

它不负责直接实现功能，而是帮助你判断代码应该长成什么形状：把大量 behavior 放在小而稳定的 interface 后面，并让 tests 能通过这个 interface 验证它。

## When to reach for it

输入 `/codebase-design`，或当 agent 需要设计 module shape、寻找 seam、评估 interface 深度时自动触发。

当问题不是 “写哪个 test”，而是 “这个 interface 应该是什么样” 时使用它。要 test-first 构建具体 behavior，用 [tdd](https://aihero.dev/skills-tdd)。

## Deep module vocabulary

它的 leading idea 是 **deep module**：小 interface 后面藏着大量清晰行为。好的 design 会提高 leverage 和 locality，让 change 聚集在一个地方，而不是散落到很多 files。

## Where it fits

`codebase-design` 是 vocabulary layer。它被 [tdd](https://aihero.dev/skills-tdd) 和 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 使用，也可独立调用。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
