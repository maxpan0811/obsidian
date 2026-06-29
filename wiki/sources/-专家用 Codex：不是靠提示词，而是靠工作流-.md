---
title: "专家用 Codex：不是靠提示词，而是靠工作流"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/专家用 Codex：不是靠提示词，而是靠工作流.md
tags: [evernote, impression]
---

---
title: "专家用 Codex：不是靠提示词，而是靠工作流"
source: evernote
type: note
export_date: 2026-06-23
guid: 8dec0a8d-032a-47ec-931b-488790b47200
---

# 专家用 Codex：不是靠提示词，而是靠工作流

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA5NDA1MDYwNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzA5NDA1MDYwNA==&mid=2247485038&idx=1&sn=298123491c2765e61f90c6fd9ffeae38&chksm=9055c62da7224f3b959a9b5a3c30c6c825f100cb99bc20b4757d132246b53f0172f63b1c7d65&exptype=servicebox_1782171823058596&subscene=0&scene=288&clicktime=1782171973&enterid=1782171973&flutter_pos=2&biz_enter_id=5&ascene=56&devicetype=iOS26.5&version=18004b29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQQ/S/LYD3m0iYFIIKzN2etRLTAQIE97dBBAEAAAAAAEhzOKZcW1gAAAAOpnltbLcz9gKNyK89dVj0/7wVetfRpNVrVH32HaQD42sFzRYcpHaTPht6v4nyz2Yu/pJZy2FJAHXiYKa4uMSe1kn5RpXsYTPK4aIybD+q3OQnXO+EZ0OeRCDPBcb1NxZfGbElKLsAINi0xgrkFkAJ4vwTT1g2mvDNIJWuSyI49mQ50fGb+W9grlmxEDFXJq3XGNSLukQO7zXMnP2l7ZFrEYW3z6RND67WrEyGA7TuR/bUwUrhI6pSr+OBffE=&pass_ticket=n+OIEPt7JlYs54u+orMp7esIxy0V46bxI+chaq9DAAfTmYJGynAsGdXc2EnAiKpt&wx_header=3)

![](attachments/25e142d6b9d0775e.png)

很多人用 Codex 的方式是：“帮我写个登录功能。”

但高手不会这样用。

真正高效的方法是：

👉 Codex负责执行、探索、验证、整理

👉 你负责目标、边界、验收和最终判断

1. 先定义任务，再写代码

每个需求都要明确：

✅ 目标

✅ 范围

✅ 约束

✅ 验收标准

例如：

目标：增加邮箱密码登录

约束：

不新增大型依赖

保持现有UI风格

不直接提交commit

验收：

登录成功跳转Dashboard

错误密码有提示

不泄露用户是否存在

测试全部通过

2. 新项目先读，不要先改

进入项目第一件事：

“只阅读项目，不要修改代码。”

要求输出：

项目作用

技术栈

目录结构

关键流程

启动/测试命令

风险模块

先理解，再动手。

3. 必须维护 AGENTS.md

把团队规则写进去：

默认最小改动

不随意新增依赖

改逻辑必须补测试

完成后汇报风险

lint/typecheck/build必须通过

Codex犯过一次错，就把规则沉淀进去。

4. 大任务先 Plan

不要直接重构。

先让Codex输出：

目标理解

涉及文件

风险点

分阶段方案

验收标准

计划没确认，不允许改代码。

5. 长任务用 Goal

例如：

“迁移到 Zustand，直到：

行为一致

测试通过

Build成功

文档完成”

停止条件必须可验证。

6. 权限按风险切换

常用三档：

🔒 只读分析

🔧 常规开发

⚠️ 高风险操作（数据库、支付、认证、部署）

不要一直开最高权限。

7. 永远要求验证

修改后必须执行：

npm run lint

npm run typecheck

npm test

npm run build

不要接受：

“看起来应该没问题。”

只接受：

“验证通过。”

8. Review 是第二双眼睛

提交前执行：

/review

重点检查：

Bug

安全问题

边界条件

性能

测试缺失

是否违反AGENTS.md

按P0/P1/P2输出。

9. 用 Subagents 并行审查

A：业务逻辑

B：安全权限

C：测试覆盖

D：性能维护性

E：UI/UX

最后汇总成一份审查报告。

10. 把经验沉淀下来

重复流程不要反复写提示词。

封装成：

Skill

Slash Command

AGENTS.md规则

让团队经验持续复用。

我的Codex工作流

明确目标 → 明确范围 → 明确验收 → 只读分析 → 输出计划 → 人工确认 → 小步实现 → 跑测试 → Review → 更新文档 → 沉淀规则

记住一句话：

不要让 Codex 自由发挥。

把它放进一套可复用、可验证、可审计的工程工作流里。

Codex负责高强度执行，你负责工程判断。

Close
