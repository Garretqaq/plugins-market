# Engineering

我每天用于代码工作的 skills。

## User-invoked

只有在你显式输入名称时才能调用（`disable-model-invocation: true`）。

- **[ask-matt](./ask-matt/SKILL.md)** - 询问当前情境适合哪个 skill 或 flow；它是本仓库 user-invoked skills 的 router。
- **[grill-with-docs](./grill-with-docs/SKILL.md)** - 追问式访谈，同时构建项目的 domain model、打磨术语，并内联更新 `CONTEXT.md` 与 ADRs。
- **[triage](./triage/SKILL.md)** - 通过 triage roles state machine 推进 issues。
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)** - 扫描 codebase 中的 deepening opportunities，生成可视化 HTML report，然后围绕你选中的候选项继续 grilling。
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)** - 为 engineering skills 配置本仓库需要的 issue tracker、triage labels 与 domain docs 布局。每个 repo 运行一次。
- **[to-issues](./to-issues/SKILL.md)** - 用 vertical slices 把计划、spec 或 PRD 拆成可独立领取的 issue tracker issues。
- **[to-prd](./to-prd/SKILL.md)** - 把当前对话整理成 PRD 并发布到 issue tracker。
- **[implement](./implement/SKILL.md)** - 基于 PRD 或 issue 集合实现一段工作。

## Model-invoked

模型或用户都可以调用（description 包含足够丰富的触发措辞，方便模型自动找到它们）。

- **[prototype](./prototype/SKILL.md)** - 构建 throwaway prototype：可以是回答 state/logic 问题的可运行终端 app，也可以是多个可切换的 UI 变体。
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)** - 面向棘手 bug 和性能回退的纪律化诊断循环：reproduce -> minimise -> hypothesise -> instrument -> fix -> regression-test。
- **[research](./research/SKILL.md)** - 对照高可信 primary sources 调研问题，并把带引用的 findings 保存为 repo 中的 Markdown 文件。
- **[tdd](./tdd/SKILL.md)** - 使用 red-green-refactor 循环做 test-driven development；一次一个 vertical slice 地构建功能或修复 bug。
- **[domain-modeling](./domain-modeling/SKILL.md)** - 主动构建和打磨项目的 domain model：挑战术语、用场景做压力测试，并内联更新 `CONTEXT.md` 与 ADRs。
- **[codebase-design](./codebase-design/SKILL.md)** - 用于设计 deep modules 的共享纪律和词汇：小 interface、清晰 seam、通过 interface 测试。
- **[code-review](./code-review/SKILL.md)** - 双轴 review `HEAD` 与固定点之间的 diff：Standards 和 Spec 分开检查，并并行运行。
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)** - 解决正在进行的 git merge/rebase conflicts。
