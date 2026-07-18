---
title: agents-md-structure-update-2026
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 改动

2026-06-13 参照 Obra superpowers AGENTS.md 模板，优化 `~/AGENTS.md`：

### 项目索引增强
- 新增 **Tech Stack** 和 **Key Paths** 两列，项目信息一次看全
- 更新 `~/Project/` 描述 → 从废弃的 "chatbot/feishu-analyzer/personal-web/yinxiang-deduplicator" 改为 `OpenMAIC/`（实际唯一项目）

### 新增 ★ 行为铁律
- **先沟通再动手**：新功能/跨文件修改前必须先输出理解摘要+拟修改文件列表+确认
- **模糊请求追问模板**：1. 输入输出边界 2. 验收标准 3. 不能动的文件
- **约束红线**：禁止自行加依赖、禁止大重构、禁止擅自改无关代码
- **执行纪律**：每子任务后跑 lint+typecheck+测试、task done 明确定义、失败先找替代方案

### 去重精简
- 执行流程从 6 条 → 2 条（仅保留「先读后改」「保存经验」，其余移入 ★）
- 边界与约束从 6 条 → 1 条（仅保留「模板化输出」，其余移入 ★）
- 数据与文件节保持不变（它讲的是数据分析手法，不是行为约束）

## 为什么

原有 AGENTS.md 的工程约定散在"执行流程"和"边界与约束"两个节里，没有一处集中的最核心纪律入口。新会话容易忽略重要规则。Obra 模板的 ★ 区设计让关键约束一眼可见。

## 第二次改动（2026-06-13，参照用户提供的 OpenAI AGENTS.md + Anthropic 官方最佳实践模板）

同日进行第二轮升级，核心变化：

- **Commands 精确化**：新增 Commands 块，install/dev/build/test/lint/typecheck 命令按技术栈写死，不再需要问"用什么命令跑"
- **Checkpoints 机制**：定义5个精确触发条件替代笼统的"复杂任务先计划"（DB变更/加依赖/3+文件/protected paths/rm-sudo-env）
- **Boundaries 过删除测试**：每条规则附"删了会犯什么错"注释，通不过就删
- **Common Gotchas**：按项目列出学到的坑
- **完成报告模板**：每个任务后固定 Changed/Verify/Outstanding 三行输出
- **元自检**：问"你加载了什么文件"可验证配置是否生效
- **三文件同步**：AGENTS.md（内容）+ ~/CLAUDE.md（桥接）+ ~/.claude/CLAUDE.md（全局）

## How to apply

1. 新项目初始化时直接用这套模板结构占位
2. 每次 Agent 干蠢事后往 Common Gotchas 或 Boundaries 补一条精确规则
3. 维护时每条规则过删除测试：删了会犯具体错误吗？通不过就删
4. 用元自检验证配置生效
