---
name: agentsmd和claudemd的最佳写法
type: source
tags: [CLAUDE.md, AGENTS.md, Codex, 提示工程, 项目管理]
source_path: /Users/panbo/Obsidian/程序开发/Agents.md和claude.md的最佳写法.md
---

[摘要]

本文档深入对比了Claude Code的CLAUDE.md和OpenAI Codex的AGENTS.md两种项目指令文件体系。核心发现：Codex"照抄了"CLAUDE.md的写作范式（项目指令该写什么、怎么排、写多长），但没有抄它的解析语法。

具体差异包括：CLAUDE.md支持的`@import path.md`语法Codex不认识（会把@import当普通文本念）；allowed-tools机器可读字段Codex没有；disable-model-invocation控制开关Codex不存在；hooks事件钩子Codex有自己的系统。因此CLAUDE.md中的自然语言规则可一字不改搬到AGENTS.md使用，但`@import`、YAML frontmatter、工具白名单等"Claude方言"Codex只会默默忽略。

推荐的最佳架构是**拆分共享真理层和工具专属层**：AGENTS.md放工具无关的内容（技术栈/命令/硬约束，任何agent都能读）；CLAUDE.md做桥接层（首行@AGENTS.md，下面只加Claude-only的如allowed-tools、plan模式偏好、thinking级别）。具体的目录布局为项目根目录放AGENTS.md（Codex原生读）和CLAUDE.md（首行@AGENTS.md引入通用规则），再分别建立.claude/和.codex/子目录。

提供了完整的AGENTS.md模板（80~150行最佳），涵盖Project、Commands、Project Structure、Boundaries、Workflow Rules、Style Conventions、Common Gotchas等章节。以及CLAUDE.md桥接模板和CLAUDE.local.md个人本地覆盖模板。强调了`.claude/settings.json`作为权限确定性层（不走CLAUDE.md）的重要性。

验证方法：Codex中用`--print-instructions`查看加载的指令；Claude Code中直接询问加载的上下文文件和AGENTS.md内容。

原文链接：/Users/panbo/Obsidian/程序开发/Agents.md和claude.md的最佳写法.md