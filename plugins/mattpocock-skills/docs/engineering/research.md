Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=research
```

```bash
npx skills update research
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/research)

## What it does

`research` 通过阅读拥有答案的 sources 来回答问题，并留下带引用的 Markdown 文件。

它只使用 **primary sources**：official docs、source code、specs、first-party APIs。它保存的不是二手总结，而是可追溯到权威来源的 findings。

## When to reach for it

输入 `/research`，或当任务变成阅读资料、查 API 事实、核对 specs 时由 agent 自动触发。

当下一步是 “弄清楚事实” 且你不想阻塞当前 thread 时使用它。要通过访谈打磨计划，用 [grilling](https://aihero.dev/skills-grilling)；要用 throwaway code 探索方案，用 [prototype](https://aihero.dev/skills-prototype)。

## Delegated legwork

核心动作是把阅读交给 **background agent**。你继续工作；它追溯 primary sources，并把结果写成一份带引用的文件。

## Where it fits

它是可随时调用的 standalone，产物会喂给 [grilling](https://aihero.dev/skills-grilling)、[to-prd](https://aihero.dev/skills-to-prd) 或 design work。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
