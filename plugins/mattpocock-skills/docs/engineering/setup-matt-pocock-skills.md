Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=setup-matt-pocock-skills
```

```bash
npx skills update setup-matt-pocock-skills
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/setup-matt-pocock-skills)

## What it does

`setup-matt-pocock-skills` 为当前 repo 配置其他 engineering skills 依赖的本地约定：issue tracker、triage labels 和 domain docs layout。

它只做 setup。运行一次后，`triage`、`to-prd`、`to-issues` 等 skills 才知道应该把 artifacts 写到哪里。

## When to reach for it

你通过输入 `/setup-matt-pocock-skills` 调用它；agent 不会自行触发。

第一次在一个 repo 使用这套 engineering flow 前运行它，尤其是在使用 [triage](https://aihero.dev/skills-triage)、[to-prd](https://aihero.dev/skills-to-prd) 或 [to-issues](https://aihero.dev/skills-to-issues) 前。

## Where it fits

它是 run-once setup step，不属于 main build chain，但支撑 main chain。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。
