# Matt Pocock Agent Skills 中文版

## 为什么需要这个中文版？

- 更好适配中文大语言模型
- 方便中文母语开发者
- 方便接入中文开发流程

## 关于这个中文版

这是 [`mattpocock/skills`](https://github.com/mattpocock/skills) 的简体中文本地化版本。文档和技能说明已翻译；目录名、技能名、命令、代码块、路径和工具标识保持不变，以免破坏安装和运行行为。

中文版本不只是为了阅读方便。对中文母语用户来说，中文说明能减少概念转换成本；对以中文为主要交互语言或中文语料优化的模型来说，中文 prompt 和 skill instructions 也更容易贴合中文上下文，减少中英混杂带来的歧义。

本仓库按内容刷新方式同步上游，不同步上游 Git 历史或仓库管理状态。维护规则见 [`.skills/translate-skill/SKILL.md`](./.skills/translate-skill/SKILL.md)。

本仓库的最近一次同步翻译由 OpenAI Codex（GPT-5 coding agent）执行，并由仓库维护者通过提交记录纳入 `main`。翻译策略是 **skill-guided content localization**：把上游 `mattpocock/skills` 当作英文内容来源，只翻译自然语言说明，保留目录名、skill name、frontmatter key、命令、代码块、路径、URL、package/tool/API identifiers 和行为关键 labels。用户可见的安装路径统一保持为 `vinvcn/mattpocock-skills-zh-CN`。

## 发布记录与验证

### 发布记录

- 2026-07-12：同步上游 `mattpocock/skills@391a270`，本地提交 `62cf4a9`。将 `to-prd`/`to-issues` 重组为 `to-spec`/`to-tickets`，把 `wayfinder` 提升到 engineering，新增 `setup-ts-deep-modules` 草稿，并刷新 prototype、setup 与公开索引。
- 2026-07-04：同步上游 `mattpocock/skills@272f99b`，本地提交 `042407b`。新增 human-facing skill docs，推广 `code-review`，新增 `research`，更新 `ask-matt` flow map、`tdd` seam 规则、`grilling` confirmation gate，并将 in-progress `decision-mapping` 刷新为 `wayfinder`。
- 2026-06-29：同步上游 `mattpocock/skills@5d78bd0`，本地提交 `79f92ff`。新增 `ask-matt`、`codebase-design`、`domain-modeling`、`diagnosing-bugs`、`grilling`、`writing-great-skills` 等内容，移除公开的 `caveman`、`zoom-out`、`write-a-skill`，并按 User-invoked / Model-invoked 刷新索引。
- 2026-06-16：同步上游 `mattpocock/skills@694fa30`，本地提交 `6b594d2`。将 `teach` 从 in-progress 提升到 productivity，并更新 teaching workspace 指南：`lessons/`、`reference/`、storage strength、primary source、follow-up questions 和 quiz 答案长度约束。
- 2026-06-05：同步上游 `mattpocock/skills@aaf2453`，本地提交 `0f36f6d`。更新 `to-prd` 的 seam-based 测试决策指导，并强化 in-progress `teach` explainers 的 citations 与 interactivity 要求。
- 2026-05-29：同步上游 `mattpocock/skills@e3b90b5`，本地提交 `fb2000f`。新增 in-progress `teach` skill 的中文翻译，并更新 `CONTEXT.md` template 规则。
- 2026-05-22：同步上游 `mattpocock/skills@b8be62f`，本地提交 `f0b4bd3`。新增 architecture HTML report 指南，更新 handoff 临时文件与 redaction 规则，并收紧 `CONTEXT.md` template。
- 2026-05-15：同步上游 `mattpocock/skills@e74f006`，本地提交 `c323a74`。收紧 `CONTEXT.md` glossary 边界，并更新 `prototype` 的设计细化表述。
- 2026-05-11：同步上游 `mattpocock/skills@9f2e0bd`，本地提交 `210cbac`。将 `handoff` 提升到 productivity，新增 `review` 草稿，并更新 writing skills。
- 2026-05-09：同步上游 `mattpocock/skills@733d312`，本地提交 `c9fe120`。新增 `prototype` 与 `in-progress` 内容的中文翻译，并更新公开 skill 索引。

### 最新 main 验证

针对 `mattpocock/skills@391a270` 的同步结果：

- [x] `node scripts/check-translation.mjs` 通过。
- [x] 公开 skill 索引一致：`engineering/`、`productivity/`、`misc/` 已同步到顶层 README 和 `.claude-plugin/plugin.json`；`personal/`、`in-progress/`、`deprecated/` 未进入 plugin 或顶层公开索引。
- [x] 顶层 README skill 条目均链接到对应 `SKILL.md`。
- [x] `engineering/` 与 `productivity/` 的 human-facing docs pages 已补齐到 `docs/engineering/` 和 `docs/productivity/`。
- [x] 新增和变更的 prose-bearing files 已按 skill-guided content localization 翻译；代码块、命令、路径、URLs 和 identifiers 保持行为关键内容不变。
- [x] 已对比上游 in-scope 文件清单：移除 `to-prd`、`to-issues` 和 in-progress `wayfinder` stale paths；新增 `to-spec`、`to-tickets`、engineering `wayfinder` 与 `setup-ts-deep-modules`，并保留中文仓库专用的翻译检查脚本。
- [x] `git diff --check` 和 `git diff --cached --check` 通过。
- [!] `node scripts/audit-english.mjs` 仍会列出合理保留的英文术语、命令、示例、触发词和 identifiers，作为人工复核队列，不作为阻塞项。

## 30 秒安装

```bash
npx skills@latest add vinvcn/mattpocock-skills-zh-CN
```

选择你想安装的 skills，以及要安装到哪些 coding agents。首次安装时请确保选择 [`/setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md)，然后在 agent 中运行它来完成 issue tracker、labels 和 docs 目录配置。

[![skills.sh](https://skills.sh/b/vinvcn/mattpocock-skills-zh-CN)](https://skills.sh/vinvcn/mattpocock-skills-zh-CN)

<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

## 原版 README 翻译

我每天用于真实工程工作的 agent skills，不是 vibe coding。

开发真实应用很难。GSD、BMAD、Spec-Kit 这类方法试图通过接管流程来帮你。但它们在接管流程的同时，也拿走了你的控制权，并让流程里的 bug 更难解决。

这些 skills 被设计得小、易改、可组合。它们适用于任何模型，背后是数十年的工程经验。你可以 hack 它们，让它们变成自己的东西。

如果你想跟进这些 skills 的更新，以及我后续创建的新 skill，可以加入大约 60,000 名开发者订阅的 newsletter：

[订阅 Newsletter](https://www.aihero.dev/s/skills-newsletter)

### Quickstart（30 秒 setup）

1. 运行 skills.sh installer：

```bash
npx skills@latest add vinvcn/mattpocock-skills-zh-CN
```

2. 选择你想安装的 skills，以及要安装到哪些 coding agents。**确保选择 `/setup-matt-pocock-skills`**。

3. 在你的 agent 中运行 `/setup-matt-pocock-skills`。它会：
   - 询问你要使用哪个 issue tracker（GitHub、Linear 或 local files）
   - 询问你 triage issues 时使用哪些 labels（`/triage` 会使用这些 labels）
   - 询问要把创建的 docs 保存到哪里

4. 完成后即可开始使用。

### 为什么这些 Skills 存在

我创建这些 skills，是为了解决我在 Claude Code、Codex 和其他 coding agents 中反复看到的常见失败模式。

#### #1: Agent 没有做我想要的东西

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**：软件开发中最常见的失败模式是 misalignment。你以为开发者理解了你想要什么；等看到做出来的东西，才发现对方完全没理解。

AI 时代也是一样。你和 agent 之间存在沟通缺口。修复方式是一次 **grilling session**，让 agent 针对你要构建的东西提出详细问题。

**解决方式**是使用：

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - 用于非代码场景
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) - 与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 类似，但会加入更多文档能力（见下文）

这些是我最常用的 skills。它们帮助你在开始前和 agent 对齐，并深入思考你要做的变更。每次想做变更时都值得使用。

#### #2: Agent 太啰嗦

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**问题**：项目开始时，开发者和真正使用软件的人（domain experts）通常说着不同语言。

我在 agents 身上也感受到同样张力。Agents 往往被丢进一个项目，然后被要求边做边弄懂术语。于是它们用 20 个词解释本来 1 个词就够的东西。

**解决方式**是 shared language。它是一份帮助 agents 解码项目术语的文档。

<details>
<summary>
示例
</summary>

这是我 `course-video-manager` repo 中的一个 [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) 示例。哪一个更容易读？

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

这种简洁性会在一次又一次 session 中持续回报。

</details>

这已经内置在 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它是一场 grilling session，同时帮助你和 AI 建立 shared language，并把难解释的决策记录到 ADR 中。

很难解释这件事有多强。它可能是这个 repo 里最酷的技术之一。试试看就知道。

> [!TIP]
> Shared language 除了减少啰嗦，还有很多其他好处：
>
> - **变量、函数和文件命名更一致**，因为都使用 shared language
> - 因此 **agent 更容易浏览 codebase**
> - Agent 也会 **花更少 tokens 思考**，因为它能使用更简洁的语言

#### #3: 代码跑不起来

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**：假设你和 agent 已经对要构建什么达成一致。那如果 agent 仍然产出一堆不能用的东西呢？

这时要看你的 feedback loops。没有对生成代码真实运行情况的反馈，agent 就是在盲飞。

**解决方式**：你需要常规的一组 feedback loops：static types、browser access 和 automated tests。

对 automated tests 来说，red-green-refactor 循环非常关键。Agent 先写一个失败测试，再修到测试通过。这能给 agent 稳定反馈，最终得到更好的代码。

我做了一个可以放进任何项目的 **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill**。它鼓励 red-green-refactor，并给 agent 足够多关于好测试和坏测试的指导。

调试方面，我也做了一个 **[`/diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md)** skill，把最佳调试实践包装成一个简单循环。

#### #4: 我们做出了 Ball Of Mud

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**问题**：大多数用 agents 构建的应用都复杂且难以修改。因为 agents 能极大加速编码，它们也会以空前速度加速软件熵增。Codebase 会变得越来越复杂。

**解决方式**是 AI-powered development 的一种新办法：关心代码设计。

这些 skills 的每一层都内置了这种思路：

- [`/to-spec`](./skills/engineering/to-spec/SKILL.md) 会在创建 spec 前追问你准备使用哪些 test seams

更重要的是，[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) 能帮助你拯救已经变成 ball of mud 的 codebase。我建议每隔几天就在你的 codebase 上跑一次。

#### Summary

软件工程基本功比以往任何时候都更重要。这些 skills 是我把这些基本功压缩成可重复实践的一次尝试，目标是帮你交付职业生涯中最好的应用。

### Reference

这些 skills 按一个维度区分：谁能调用它们。**User-invoked** skills 只有在你输入名称时才能触达（例如 `/grill-me`）；它们的工作是编排。**Model-invoked** skills 可以由你调用，也可以在任务匹配时由 agent 自动触达；它们承载可复用纪律。User-invoked skill 可以调用 model-invoked skills，但不能调用另一个 user-invoked skill。

#### Engineering

我每天用于代码工作的 skills。

**User-invoked**

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)** - 询问当前情境适合哪个 skill 或 flow；它是本仓库所有 skills 的 router。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** - 追问式访谈，同时构建项目的 domain model、打磨术语，并内联更新 `CONTEXT.md` 与 ADRs。
- **[triage](./skills/engineering/triage/SKILL.md)** - 通过 triage roles state machine 推进 issues。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** - 扫描 codebase 中的 deepening opportunities，生成可视化 HTML report，然后围绕你选中的候选项继续 grilling。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** - 配置 issue tracker、triage labels 和 domain docs 布局。每个 repo 运行一次。
- **[to-spec](./skills/engineering/to-spec/SKILL.md)** - 把当前对话整理成 spec 并发布到 issue tracker。不做访谈，只综合已经讨论过的内容。
- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)** - 把 plan、spec 或 conversation 拆成 tracer-bullet tickets，每个 ticket 声明 blocking edges。
- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)** - 把超出单个 agent session 的大块工作规划成 issue tracker 上的调查 ticket 共享 map，逐一解决直到通往 destination 的路清晰。
- **[implement](./skills/engineering/implement/SKILL.md)** - 基于 spec 或 ticket 集合实现一段工作。

**Model-invoked**

- **[prototype](./skills/engineering/prototype/SKILL.md)** - 构建 throwaway prototype，回答 state/business-logic 问题或探索 UI 变体。
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)** - 面向棘手 bug 和性能回退的纪律化诊断循环：reproduce -> minimise -> hypothesise -> instrument -> fix -> regression-test。
- **[research](./skills/engineering/research/SKILL.md)** - 对照 high-trust primary sources 调研问题，并把带引用的 findings 保存为 Markdown 文件。
- **[tdd](./skills/engineering/tdd/SKILL.md)** - 使用 red-green-refactor 循环做 test-driven development；一次一个 vertical slice 地构建功能或修复 bug。
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)** - 主动构建和打磨项目 domain model：挑战术语、用 edge-case scenarios 做压力测试，并内联更新 `CONTEXT.md` 与 ADRs。
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)** - 设计 deep modules 的共享纪律和词汇：小 interface、clean seam、通过 interface 测试。
- **[code-review](./skills/engineering/code-review/SKILL.md)** - 对 fixed point 以来的 diff 做双轴 review：Standards 与 Spec 分开检查，并用并行 sub-agents 运行。
- **[resolving-merge-conflicts](./skills/engineering/resolving-merge-conflicts/SKILL.md)** - 解决正在进行的 git merge/rebase conflicts。

#### Productivity

通用工作流工具，不限于代码。

**User-invoked**

- **[grill-me](./skills/productivity/grill-me/SKILL.md)** - 围绕计划或设计持续追问，直到 decision tree 的每个分支都被解决。
- **[handoff](./skills/productivity/handoff/SKILL.md)** - 把当前对话压缩成 handoff document，让另一个 agent 可以继续。
- **[teach](./skills/productivity/teach/SKILL.md)** - 使用当前目录作为 stateful teaching workspace，在多个 sessions 中教用户一个新 skill 或概念。
- **[writing-great-skills](./skills/productivity/writing-great-skills/SKILL.md)** - 编写和编辑优秀 skills 的 reference：让 skill 可预测的词汇和原则。

**Model-invoked**

- **[grilling](./skills/productivity/grilling/SKILL.md)** - 围绕计划或设计持续访谈用户，直到 decision tree 的每个分支都被解决。它是 `grill-me` 和 `grill-with-docs` 背后的 reusable loop。

#### Misc

本地保留但很少使用的工具。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** - 设置 Claude Code hooks，在危险 git 命令（push、reset --hard、clean 等）执行前阻止它们。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** - 将测试文件中的 `as` 类型断言迁移到 @total-typescript/shoehorn。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** - 创建包含 sections、problems、solutions 和 explainers 的练习目录结构。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** - 设置 Husky pre-commit hooks，集成 lint-staged、Prettier、type checking 和 tests。
