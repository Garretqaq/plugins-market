Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=diagnosing-bugs
```

```bash
npx skills update diagnosing-bugs
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/diagnosing-bugs)

## What it does

`diagnosing-bugs` 用纪律化循环处理棘手 bug 和性能回退：reproduce -> minimise -> hypothesise -> instrument -> fix -> regression-test。

它拒绝在没有 tight feedback loop 时空想。先拿到一个能稳定变红的命令，再缩小、验证、修复，并用 regression test 锁住行为。

## When to reach for it

输入 `/diagnosing-bugs`，或当用户报告 broken、throwing、failing、flaky、regression 等问题时由 agent 自动触发。

适合一眼看不出的 bug、间歇性失败、或两个 known-good states 之间出现的 regression。若只是要 test-first 构建新 behavior，用 [tdd](https://aihero.dev/skills-tdd)。

## Tight feedback loop

核心词是 **tight**：一个最小、快速、可重复的反馈命令。没有这个命令，所有 hypothesis 都只是猜测；有了它，修复才有速度上限和验证边界。

## Where it fits

它是 bug on-ramp，发现真正问题是 bad seam 或 architecture debt 时，会把后续交给 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture)。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
