# 仓库指南

Skills 按 bucket folder 组织在 `skills/` 下：

- `engineering/` - 日常代码工作
- `productivity/` - 日常非代码工作流工具
- `misc/` - 保留但很少使用
- `in-progress/` - 仍在开发，暂不推广
- `personal/` - 绑定我自己的设置，不推广
- `deprecated/` - 不再使用

`engineering/`、`productivity/` 或 `misc/` 中的每个 skill，都必须在顶层 `README.md` 中有引用，并在 `.claude-plugin/plugin.json` 中有条目。`personal/` 和 `deprecated/` 中的 skills 不得出现在这两个位置。
`in-progress/` 中的 skills 在毕业到稳定 bucket 前，必须留在顶层 `README.md` 和 `.claude-plugin/plugin.json` 之外。

顶层 `README.md` 中的每个 skill 条目都必须把 skill 名称链接到对应的 `SKILL.md`。

每个 bucket folder 都有一个 `README.md`，列出该 bucket 中的所有 skills，并给出一行描述；skill 名称需要链接到对应的 `SKILL.md`。Bucket `README.md` 和顶层 `README.md` 都按 **User-invoked** 与 **Model-invoked** 分组。

每个 `SKILL.md` 要么是 user-invoked（frontmatter 中设置 `disable-model-invocation: true`，只能由人类显式调用），要么是 model-invoked（模型和用户都可以调用）。完整定义、description 约定，以及为什么 user-invoked skill 可以调用 model-invoked skills 但不能调用另一个 user-invoked skill，见 [docs/invocation.md](./docs/invocation.md)。

## 翻译刷新

从 `mattpocock/skills` 刷新上游内容时，改文件前先使用 `.skills/translate-skill/SKILL.md`。本仓库采用 skill-guided content localization，不做 Git fork-sync：保留简体中文本地化身份，安装命令保持指向 `vinvcn/mattpocock-skills-zh-CN`，不要导入上游 repository-management state。
