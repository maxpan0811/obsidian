---
title: Claude Code Superpowers：14个技能完整拆解
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?chksm=f0bb4e2bc7ccc73d3a20223b3e5f042...]
source_path: 印象笔记管理工具/Claude Code最佳搭档Superpowers：14个技能完整拆解，装上就是另一个AI.md
tags: [claude-code, superpowers, skill, workflow, plugin]
updated: 2026-06-27
---

---
title: "Claude Code最佳搭档Superpowers：14个技能完整拆解，装上就是另一个AI"
source: evernote
type: note
export_date: 2026-06-27
guid: 0ebf3087-b3d4-4535-9988-1f4d19629b8e
---

# Claude Code最佳搭档Superpowers：14个技能完整拆解，装上就是另一个AI

原文链接: [https://mp.weixin.qq.com/s?chksm=f0bb4e2bc7ccc73d3a20223b3e5f042...](https://mp.weixin.qq.com/s?chksm=f0bb4e2bc7ccc73d3a20223b3e5f042324a4c6603e707c9b95551534a355be2c5ef6ce04acf7&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1774916204_1&req_id=1774911368136129&scene=169&mid=2247484012&sn=b29e458236153f82a9c3e5bb28333fe6&idx=1&__biz=MzYzMjY1OTI0MA==&sessionid=1774917255&subscene=200&clicktime=1774919601&enterid=1774919601&flutter_pos=11&biz_enter_id=5&jumppath=30024_1774919555535,1104_1774919587896,30024_1774919591138,1104_1774919596069&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004629&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQyIhXaBrVU5MYrk4RUBKFXxLKAQIE97dBBAEAAAAAAI8/Jm1qxHcAAAAOpnltbLcz9gKNyK89dVj0AxdN0QiE9o9jGEA5M7TvZ3c/TRwszZCfOCOx+jSJLi+YUaQUn06ZY8aMDuIXnkTFPWkCbtP787ZKbFAG08IJ31+GvTp6QFjblX1JKTHiKlq++cvffujZpoBL2E3u8qqle6VTJjdzSo5W5X70luuxMNiMdHFeW8yfwQOj8ngICuVsm370K7gQU2ME3IWjuNxhwQj+/922aG/roQJl0KvJfAUUCQY=&pass_ticket=bk9+lZs//EhGnuk++8kmQcNLFz8cUn+92pL8LCd94hryckHwVnVZz+lgRL6aFu7W&wx_header=3)

Original莲花明AI落地手记

你好，这里是AI落地手记。

上一篇聊了200个Skills。今天拆一个具体的插件——Superpowers。

![](attachments/d45c038694704891.jpg)

它是Claude Code的一个开源插件，装上之后AI多了14个"职业技能"。不是花哨的概念，是真正改变AI工作方式的底层规则。

装之前，AI接到需求就动手写代码。装之后，它会先想需求、先写测试、先出方案、写完自查、自己做代码审查、出了bug按流程排查。

**这篇把14个技能全部拆开，每一个是什么、怎么工作、为什么有效。**

— — —

## **先看全局：14个技能的完整链路**

![](attachments/cf1e24a81fe6e4bb.png)

这14个技能不是散装的，它们形成了一条完整的开发流水线：

需求进来

-> 1 using-superpowers（路由：该调哪个技能？）

-> 2 brainstorming（需求分析：问问题、出方案、确认）

-> 3 writing-plans（写实施计划：拆成小任务）

-> 4 using-git-worktrees（开隔离环境）

-> 5 executing-plans / 6 subagent-driven-development（执行）

-> 7 dispatching-parallel-agents（并行派遣）

-> 8 test-driven-development（先测试后写码）

-> 9 systematic-debugging（四阶段排查bug）

-> 10 verification-before-completion（验证才能说完成）

-> 11 requesting-code-review（请求审查）

-> 12 receiving-code-review（技术评估审查意见）

-> 13 writing-skills（封装新技能）

-> 14 finishing-a-development-branch（收尾）

**每个技能都有一条"铁律"——违反就停，不能绕过。不是建议，是强制规则。**

— — —

## **1 using-superpowers —— 路由器**

**每条消息进来，先判断该调哪个技能。**

**哪怕只有1%的可能性某个技能适用，也必须先调用。**

内置"反合理化"表，堵住AI想偷懒跳过技能的每一条借口：

"这个问题很简单" -> 问题也是任务，查技能

"我先了解一下情况" -> 技能告诉你怎么了解，先查

"这个技能太重了" -> 简单的事也会变复杂，用它

"我先快速做一件事" -> 先查技能再做任何事

— — —

## **2 brainstorming —— 需求分析师**

**动手之前，先把需求想清楚。**

**铁律：在用户确认方案之前，不准写任何代码。**

1. 先看项目现状 — 读文件、读文档、读git提交

2. 一次问一个问题 — 尽量给选项

3. 给2-3个方案 — 带优缺点对比，带推荐理由

4. 分段确认 — 架构/组件/数据流每段确认一次

5. 写设计文档 — 保存到 docs/plans/ 并提交git

**以前AI接到"做个数据看板"就直接写代码。现在它先问5个问题，出3个方案，选完才动手。**

— — —

## **3 writing-plans —— 计划工程师**

**把需求拆成2-5分钟一个的小任务，精确到文件路径和命令。**

真实格式示例：

### Task 2: 添加验证函数

文件:

- 创建: src/validator.py

- 修改: src/main.py:45-60

- 测试: tests/test\_validator.py

Step 1: 写失败测试

def test\_validate\_email():

result = validate("bad-email")

assert result.error == "Invalid email"

Step 2: 跑测试确认失败

运行: pytest tests/test\_validator.py -v

期望: FAIL "validate not defined"

Step 3: 写最小实现

Step 4: 跑测试确认通过

Step 5: git commit

**每步精确到命令和期望输出。文件路径精确到行号。代码直接写在计划里。严格TDD。**

— — —

## **4 using-git-worktrees —— 隔离环境**

**开一个独立工作目录，不动主分支。**

git worktree add .worktrees/feature-auth -b feature/auth

cd .worktrees/feature-auth

npm install

npm test # 确认基线干净

自动检查 .worktrees/ 是否在 .gitignore 里，没有就自动加上。

创建后自动跑测试确认基线干净。

**AI写崩了？主分支不受影响，一键删除重来。**

— — —

## **5/6 两种执行模式**

### **executing-plans —— 分批执行**

每3个任务一批，做完暂停汇报等反馈，适合需要人类检查的场景。

### **subagent-driven-development —— 子agent驱动**

**Superpowers最精妙的设计。**

**核心：每个任务派一个全新的子agent，做完两轮审查。**

**每个任务过3关：**

1. 实现子agent — 写代码、跑测试、自审、提交

2. Spec审查子agent — 代码是否符合计划（不多做、不漏做）

3. 质量审查子agent — 安全/性能/命名/规范

审查不通过？打回改。改完再审。循环直到通过。

**为什么用全新子agent？防上下文污染。Task 1的agent脑子里全是Task 1的代码，做Task 2会硬套。全新agent，干净上下文。**

— — —

## **7 dispatching-parallel-agents —— 并行指挥**

**多个独立任务，同时派多个agent做。**

真实案例：6个测试失败分布在3个文件，bug互不相关。

串行修30分钟。并行派3个agent，10分钟全搞定，零冲突。

**关键：给agent的任务描述要具体到测试名、错误信息、约束条件。**

修复 agent-tool-abort.test.ts 的3个失败测试：

1. "should abort with partial output" - 期望包含 interrupted at

2. "should handle mixed completed/aborted" - fast tool被错误abort

3. "should track pendingToolCount" - 期望3个结果得到0

这是时序问题。用事件等待替换超时。不要只增大超时。

返回：根因分析 + 修改摘要

— — —

## **8 test-driven-development —— 先测试后写码**

**铁律：没有失败测试，不准写任何生产代码。违反了？删掉从头来。**

**RED-GREEN-REFACTOR：**

RED -> 写失败测试，确认失败原因是"功能不存在"

GREEN -> 写最少代码让测试通过，不多写一行

REFACTOR -> 只在绿灯下重构，保持测试通过

**反例对比：**

// 测试只要求"重试3次"

// BAD: 过度设计

async function retryOperation<T>(

fn, options?: { maxRetries?, backoff?, onRetry? }

) { ... }

// GOOD: 刚好够用

async function retryOperation<T>(fn) {

for (let i = 0; i < 3; i++) {

try { return await fn(); }

catch (e) { if (i === 2) throw e; }

}

}

— — —

## **9 systematic-debugging —— 四阶段排查**

**铁律：没有完成根因调查，不准尝试修复。**

**Phase 1: 根因调查**

逐行读错误 -> 稳定复现 -> 查最近改动 -> 多层系统加诊断日志

echo "=== Layer 1: Workflow ==="

echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

echo "=== Layer 2: Build ==="

env | grep IDENTITY || echo "not in env"

echo "=== Layer 3: Signing ==="

security find-identity -v

# 逐层打印，立刻看到哪层断了

**Phase 2: 模式分析**

找"能跑的类似代码"和"坏掉的代码"逐项对比

**Phase 3: 假设+测试**

一次一个假设，一次只改一个变量

**Phase 4: 实施修复**

**修了3次都没成功？停！这不是bug，是架构问题。**

— — —

## **10 verification-before-completion —— 不验证不准说完成**

**没有当场跑验证命令并看到输出，不准说"完成"。**

X "应该可以了" -> 跑验证命令

X "我很有信心" -> 信心不等于证据

X "Linter通过了" -> Linter不等于编译器

O 跑测试 -> 看到 34/34 pass -> 才能说"全部通过"

**最狠要求：写回归测试 -> 跑通 -> 回退修复 -> 确认测试失败 -> 恢复 -> 再跑通。证明测试真的能抓bug。**

— — —

## **11/12 代码审查：请求 + 接收**

**做完一个任务就派审查agent，给它git SHA范围和计划要求。**

收到审查意见后的规则：

X "你说得太对了！" -> 禁止，技术讨论不表演

X 直接照做 -> 先验证建议在当前代码库是否正确

O 该反驳就反驳，用技术理由

**YAGNI检查：审查人说"功能该做完善" -> 先grep看有没有调用方 -> 没人调就删（YAGNI）。**

— — —

## **13 writing-skills —— 把经验变成技能**

**和TDD一样的铁律：没先测试就写出来的技能，删掉重来。**

RED -> 没有技能时AI怎么做？记录错误行为

GREEN -> 写技能让AI行为正确

REFACTOR -> AI找到绕过方式？堵上再测再堵

**设计细节：技能的description只能写"什么时候用"，不能写"怎么用"。测试发现AI会按description走捷径跳过正文。**

# BAD: AI不读正文了

description: 用于TDD - 先写测试，看到失败，写最小代码

# GOOD: 只写触发条件

description: Use when implementing any feature, before writing code

— — —

## **14 finishing-a-development-branch —— 收尾**

1. 跑测试 -> 失败不准继续

2. 给4个选项：本地合并 / 创建PR / 保持不动 / 丢弃

3. 丢弃需要输入完整单词"discard"确认（不是y/n防手滑）

4. 清理worktree

— — —

## **安装方法**

claude install-plugin superpowers-marketplace/superpowers

一行命令，14个技能自动注入，无需额外配置。

**如果你不用Claude Code，核心思路也可以搬。本质7条规则：**

1. 接到需求先问清楚，不准直接动手

2. 先写测试再写代码

3. 出了bug四阶段排查，不准乱改

4. 做完必须验证，不准口头说"搞定了"

5. 自己审查自己的代码

6. 独立任务并行做

7. 修3次修不好就停下来质疑方向

**这7条规则，不管你用什么AI，都能让它的工作质量翻倍。**

— — —

Superpowers开源地址：github.com/obra/superpowers

想深入了解可以直接去读源码，14个skill的完整实现都在里面。

**关注「AI落地手记」，后续继续分享干货。**

一个用AI管理20+客户项目的项目经理，记录真实的AI落地经验。

不卖课，不吹牛，只写自己真正在用的东西。
