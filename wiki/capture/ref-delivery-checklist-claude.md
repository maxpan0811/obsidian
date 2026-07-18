---
title: ref-delivery-checklist-claude
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 交付前强制步骤写入全局 CLAUDE.md

**时间**: 2026-06-15
**位置**: `~/.claude/CLAUDE.md` 第 61-70 行

**内容**: 6 步强制检查（缺任何一步=违规）：

1. 验证存在性 — 产出文件真实存在
2. 验证正确性 — 核心数据/行为符合预期
3. 变更清单 — 逐一列出修改文件
4. 清理现场 — 删除临时文件残留
5. 经验保存 — 有意义的工作写入 memory
6. 格式输出 — 按完成报告格式输出

**Why**: 之前的"完成报告格式"只定义了输出格式，没定义输出前必须执行的验证步骤。没有验证步骤，"完成"的判断依赖模型主观评估，在长对话中会逐渐松弛。

**How to apply**: 这条是全局规则，所有会话自动加载。如果有项目需要额外的交付前步骤（如部署确认），在项目级 CLAUDE.md 补充，不要改动全局清单。

**Related**: [[reference-constraints-system-article]], [[config-stack-hooks-rules]]
