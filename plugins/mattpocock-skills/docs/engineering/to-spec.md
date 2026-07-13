Quickstart:

```bash
npx skills add vinvcn/mattpocock-skills-zh-CN --skill=to-spec
```

```bash
npx skills update to-spec
```

[Source](https://github.com/vinvcn/mattpocock-skills-zh-CN/tree/main/skills/engineering/to-spec)

## What it does

`to-spec` 把当前 conversation 和对 codebase 的理解整理成 spec（也常称为 PRD），再发布到 issue tracker。它**不会**重新访谈；alignment 应该已经完成，这一步只综合已知内容。

## When to reach for it

显式输入 `/to-spec` 调用。适合在 change 已充分讨论、domain language 已确定，并希望写代码前固化共同理解时使用。尚未对齐时先用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)；要把 spec 拆成 tickets，使用 [to-tickets](https://aihero.dev/skills-to-tickets)。

## Prerequisites

它会发布到 issue tracker，因此要先用 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置 tracker 和 triage labels。它自行应用 `ready-for-agent`，不需要额外 triage。

## What the spec includes

- **Problem statement** — 用项目 vocabulary 说明缺失或损坏的内容及其价值。
- **Solution** — 不含 implementation detail 的高层 solution shape。
- **User stories** — 完整、编号、可独立检查的 behaviors。
- **Implementation decisions** — 对话中已经确定、不应再次争论的 choices。
- **Testing decisions** — test seams 与 done 的含义。
- **Out-of-scope items** — 明确不处理的内容。
- **Further notes** — 其他需要延续的 context。

## Deep modules

写 spec 前，`to-spec` 会草拟 feature 的 test **seams**，寻找 **deep module** 机会。它优先使用 existing seam、尽可能高的 seam，并尽量只保留一个。稳定 interface 让 tests 有持久 target，使内部 code 可以变化而 tests 不必跟着移动。

## Where it fits

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```
