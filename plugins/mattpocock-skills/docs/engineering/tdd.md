Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=tdd
```

```bash
npx skills update tdd
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/tdd)

## What it does

`tdd` 用 test-first 的方式构建 feature 或修 bug：一次一个 behavior，通过 red-green loop 推动代码长出来。

它不会先写完所有 tests。先批量写 tests 是 horizontal slicing，会测试想象中的 behavior。`tdd` 使用 vertical slices：一个 test、刚好足够通过的代码、再下一个 test。

## When to reach for it

输入 `/tdd`，或当任务适合 test-first、用户提到 “red-green-refactor”，或需要 integration tests 时由 agent 自动触发。

当有具体 behavior 要构建，并希望 tests 能承受 refactor 时使用它。Behavior 还没钉住时，先用 [to-prd](https://aihero.dev/skills-to-prd)；问题主要是 interface shape 时，用 [codebase-design](https://aihero.dev/skills-codebase-design)。

## Red-green, one slice at a time

核心是 **red-green loop**：写一个 failing test，写刚好足够通过的代码，然后为下一个 behavior 重复。第一个 cycle 是 **tracer bullet**，证明一条路径 end-to-end 可用。

## It's working if

- 它一次写一个 test，并先让它通过，再写下一个。
- Tests 命名 behavior，而不是 internals。
- Expected values 来自 spec、worked example 或 literal，而不是按代码同样方式推导。

## Where it fits

`tdd` 是 [implement](https://aihero.dev/skills-implement) 内部使用的 red-green engine，也可直接调用。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
