---
name: hui-hua-zi-dong-bao-cun-san-ceng-jia-gou-20260718
type: source
tags: [claude-code, auto-save, hook, wiki, memory]
source_path: /Users/panbo/Obsidian/程序开发/会话自动保存三层架构20260718.md
---

[摘要]
本文记录了Claude Code会话自动保存到Obsidian vault的三层架构设计与实现。

背景：日常Claude Code会话中产生大量有价值信息（数据口径定义、新事实、用户纠错、工作流偏好），之前只保存到memory/（Claude Code内部记忆），用户Obsidian里看不到，会话关闭就蒸发。而且/compact和/clear命令会导致pending的记忆丢失。

设计了三层兜底架构，层层独立：L1是CLAUDE.md双写规则（主动执行），判断到有价值信息后同时写入memory/和wiki/capture/；L2是PostToolUse hook（每步工具调用后自动执行sync-memory-to-capture.sh，idempotent同步）；L3是Stop hook（会话正常结束时触发同一脚本二次确认）。

关键设计决策：目标目录选wiki/capture/作为自动抓取临时区，不跟人工整理的cards/混在一起，定期筛选后迁入cards/analyses/concepts；PostToolUse为主力兜底因为Stop在/compact和/clear时不触发，而PostToolUse每步都跑覆盖compact/clear/崩溃；Idempotent设计（同名跳过）让L2和L3可共存不会重复写入；历史memory一次性批量同步210条旧条目全量迁入后续只同步新条目。

涉及文件变更：~/.claude/CLAUDE.md新增双写规则（memory写什么wiki/capture就同样写一份）；~/.claude/settings.json注册Stop+PostToolUse两个hook点；新建~/.claude/hooks/sync-memory-to-capture.sh脚本解析memory frontmatter写入capture目录；新建/Users/panbo/Obsidian/20260520/wiki/capture/README.md说明文档；capture/目录首次填充210条历史memory。

讨论过的备选方案包括bborbe/semantic-search MCP（轻量本地语义搜索90MB模型中文OK但偏检索非自动保存）和Smart Connections MCP（绑定插件且中文略弱），均已存档作为下一步考虑。Hook脚本需注意set -e与grep无匹配冲突需用|| true兜底，且memory/里有旧格式文件需fallback兼容。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/会话自动保存三层架构20260718.md