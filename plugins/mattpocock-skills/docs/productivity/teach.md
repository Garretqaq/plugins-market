Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=teach
```

```bash
npx skills update teach
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/productivity/teach)

## What it does

`teach` 使用当前目录作为 stateful teaching workspace，在多个 sessions 中教用户一个新 skill 或概念。

它会保留学习记录、资源、glossary 和 follow-up 状态，让教学不依赖单次对话记忆。

## When to reach for it

你通过输入 `/teach` 调用它；agent 不会自行触发。

当你想系统学习一个概念，并希望 agent 记住学习进度、复习点和资源时使用它。一次性解释不需要它。

## Where it fits

它是 standalone learning workflow，不属于 engineering build chain。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
