Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=handoff
```

```bash
npx skills update handoff
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/productivity/handoff)

## What it does

`handoff` 把当前对话压缩成 handoff document，让另一个 agent 或 fresh session 可以继续。

它不是继续当前 thread 的 compact；它创建一个可引用的文件，把 context 从一个 session 桥接到另一个 session。

## When to reach for it

你通过输入 `/handoff` 调用它；agent 不会自行触发。

当 context window 快满、需要分支到 prototype/research session，或需要把工作交给另一个 agent 时使用它。

## Where it fits

它是 crossing-sessions bridge。main flow 中常用于 planning thread 与 [prototype](https://aihero.dev/skills-prototype) detour 之间。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
