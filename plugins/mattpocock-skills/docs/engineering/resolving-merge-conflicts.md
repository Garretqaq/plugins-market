Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=resolving-merge-conflicts
```

```bash
npx skills update resolving-merge-conflicts
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/resolving-merge-conflicts)

## What it does

`resolving-merge-conflicts` 处理正在进行的 git merge 或 rebase conflicts，并让每个 resolution 尊重两边 intent。

它不是机械选择 ours/theirs。它要求理解冲突双方为什么改动，再生成一个同时满足当前 branch 和目标 branch 的结果。

## When to reach for it

输入 `/resolving-merge-conflicts`，或当当前 repo 处于 merge/rebase conflict 状态时由 agent 自动触发。

当冲突需要语义判断而不是简单接受某一边时使用它。若你只是想 review 完成后的 diff，用 [code-review](https://aihero.dev/skills-code-review)。

## Where it fits

它是 standalone recovery skill，通常发生在 implement 或 PR 准备期间。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
