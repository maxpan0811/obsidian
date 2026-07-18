---
title: harness-6-components-framework
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-20 用户分享"2026大模型圈最大错觉"文章。核心论点：AI 真正护城河从模型转向 Harness（工程框架），DeepSeek 5/20 组建 Harness 团队招聘是行业拐点信号。

## 核心框架：Agent Harness 6 Components

| 组件 | 含义 | 用户当前体系评分 |
|------|------|:---:|
| **E** Execution Loop | Plan→Act→Observe→Reflect 连续多步骤 | ⭐⭐⭐ 人工启动，缺乏自动循环 |
| **T** Tools | 文件读写/Shell/API/MCP 扩展能力 | ⭐⭐⭐⭐⭐ MCP 15+ server |
| **C** Context | 记忆/知识库/历史/Skills | ⭐⭐⭐⭐⭐ CLAUDE.md 3层+76 skills+memory+rules |
| **S** State | 任务状态/检查点/回滚/子任务协调 | ⭐⭐ active-task.md 基本、无检查点 |
| **L** Limits | 权限边界/沙盒/速率/敏感操作守护 | ⭐⭐⭐ hooks+permissions+review subagents |
| **V** Verification | 测试/Lint/安全扫描/PR review验证层 | ⭐⭐⭐⭐ 双 review subagent + double check checklist |

## 验证 vs 缝隙

### 已验证
- 当前体系的 85%+ 工作量的确在 LLM 外（与文章 "LLM is smallest part" 一致）
- 6 components 的 C（Context）和 T（Tools）已行业领先
- 当前 skills 体系 = 文章说的 "Context层"最佳实践
- Verification 层的双审查 subagent 比大多数团队强

### 未覆盖的缝隙

1. **E（执行循环）** — 已在上次循环工程讨论中识别。缺自动触发 + 闭环自运行能力。
2. **S（状态管理）** — 当前只有 active-task.md 做任务状态记录。缺：
   - 检查点（checkpoint）：长任务中间失败后可回滚重试
   - 子任务状态显式跟踪：当前 subagent 跑完返回，"成功了没有"靠人看
3. **6 components 思维框架** — 文章最有用的不是技术细节，而是这套评估维度。以后评估新工具/新技能时，可以先问"这个组件补的是 E/T/C/S/L/V 里的哪个？"

**关联记忆：** [[loop-engineering-why-rule]] [[insights-from-harness-research]]
