---
title: reference-constraints-system-article
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Claude Code 七层约束系统 · 系列文章

**URL**: https://github.com/lh180lh-sys/claude-code-constraints
**作者**: 墨染（主导&审校），AI（Claude）撰写
**篇数**: 共4篇，本文是第2篇

## 第2篇核心内容（输入端三层）

### Hook 层
- **解决的问题**: CLAUDE.md 规则在长对话中被注意力稀释，依赖模型的"记忆力"
- **解决方案**: 系统级强制注入，不依赖模型记忆力
- **核心机制**: `UserPromptSubmit` 事件在每条用户消息处理前注入纪律
- **输出格式**: 特定 JSON 结构 `{hookSpecificOutput: {hookEventName, additionalContext}}`
- **技术细节**: 用 `process.stdout.write` 而非 `console.log`；条件性注入用 `process.exit(0)` 静默退出
- **支持事件**: 31 个，涵盖会话生命周期、用户输入、工具调用、子代理等
- **边界**: 不能拦截/修改模型输出，不能拦截文件写入，不能修改用户消息

### Skill 层
- **解决的问题**: 方法论需要每次重新建立，一次性提示不稳定
- **解决方案**: 工作方法持久化为协议，通过语义匹配自动激活
- **安装**: `enabledPlugins` + `extraKnownMarketplaces` 配置
- **激活**: description 字段的语义匹配（非关键词精确匹配）
- **三类 skill**: 刚性（不可跳过，二元规则）、流程（结构化框架内有灵活度）、审查（检查点触发，不干预主流程）
- **Superpowers 清单**: 刚性3个(TDD/调试/验证) + 流程4个(计划/执行/头脑风暴/子代理) + 审查1个(代码审查) + 基础3个(基础/工作树/分支收尾) + 写作1个(技能写作)

### CLAUDE.md 层
- **解决的问题**: 需要大量背景上下文才有意义的规范
- **结构**: 个人哲学层(~/.claude/) → Workspace层 → 项目层，三级叠加
- **加载机制**: 从 cwd 向上遍历目录树，从最外层到当前目录，后加载同类规则优先级更高
- **不该写**: 当前任务进度、代码模式细节、频繁变更的内容、临时性规则

### 三层协同
- Hook: 每次对话都需要激活的简短纪律（强制注入消除遗忘）
- Skill: 特定任务类型的完整工作流程（语义触发确保方法论自动就位）
- CLAUDE.md: 需要背景上下文才能正确执行的规范（分层组织确保规则覆盖精确）

**Why**: 这篇文章完整描述了我运行的底层架构——七层约束系统的输入端三层。理解这个架构有助于诊断行为漂移、优化配置、评估新 skill 的价值。

**How to apply**: 
- 作为自身运行环境的元级参考，遇到行为退化时先检查三层配置
- 写新 hook 时参考文章中的技术细节（输出格式、错误处理、条件注入模式）
- 评估 skill 时按三类区分（刚性/流程/审查），不同类用不同标准判断
- CLAUDE.md 不写进度和代码细节，坚持写持久性规范

**Related**: [[feedback_context_management]], [[claude-hierarchy]], [[config-stack-hooks-rules]]
