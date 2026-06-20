---
title: Claude Code进阶9步闭环
type: source
created: 2026-06-20
updated: 2026-06-20
source_path: 印象笔记管理工具/Claude Code进阶9步闭环.html
tags: [编程, AI]
---

Claude Code进阶9步闭环
原文链接: https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=224748...多数人把 Claude Code 当成需要盯着看的初级助手：提需求、看改动、人工检查、再继续。真正高效的用法，是把它纳入一套类似资深工程师的工作闭环。这套方法核心不是换更强模型，而是搭建流程：先用 Explore subagent 只读理解代码库；再进入 Plan Mode，列出改动文件、顺序和风险；把团队规范写进 CLAUDE.md；按小步构建，避免巨大 diff；用 hooks 强制执行 lint、test 等关键检查；让代码用测试证明有效；再启动独立 review subagent 审查安全、边界条件和规范违背；发现问题后修复、重测、复审，直到 clean；最后把整套流程封装成 /ship slash comma…

---
### 截图OCR提取（{today}）
### 截图1
识别结果:
### 截图2
识别结果:
### 截图3
识别结果:
### 截图4
识别结果:
### 截图5
识别结果:
### 截图6
识别结果:
### 截图7
识别结果:
### 截图8
识别结果:

---
### 截图OCR提取（2026-06-20）
### 截图1
The 9-Step Loop That Turns Claude Code Into a Senior Engineer
把 Claude Code
用成资深工程师的
9步闭环
多数开发者把Claude Code当成一个需要盯着看的初级助手：
提需求、看它改文件、人工检查、继续下一步。
这样能用，但远没发挥它真正的价值。
真正的资深工程师会先理解代码库，
再制定方案、分步实现、测试验证、独立审查，最后才交付。
Claude Code已经具备搭建这条工作流所需的原生能力。
关键差别不在模型，而在你是否围绕它搭好了一个可重复的闭环。
1
探索代码
9
| Explore
2
一键固化
方案规划
|/ship
|Plan Mode
8
3
修复复检
写入规范
| Re-check
CLAUDE.md
7
4
独立审查
小步构建
| Review
Build Small
6
5
测试证明
自动约束
| Tests
| hooks
一次搭好，之后每个任务都按同一条纪律化流水线运行。
。
。
1/8

### 截图2
01-02先理解，再动手
资深工程师不会一上来就改代码。先理解代码库，再决定怎么做。
1
1. Explore Before
Touching Anything
探索代码|Explore subagent
。.。
任何稍复杂的任务，都先让 Explore subagent
只读扫描相关区域。
它在独立上下文里工作：不污染主会话、
不冒然改动文件。
重点产出：相关文件、数据流、依赖关系、
脆弱点。
先理解真实结构，而不是靠猜。
>_Prompt 示例
Explore how authentication works across this codebase.
Map the files involved, the data flow, and anything
that looks fragile.
Don't change anything yet.
2
2. Make a Plan in Plan Mode
方案规划|Plan Mode
在写代码前，先产出完整方案：要改哪些文件、
√
顺序是什么、风险在哪里。
你先审阅并批准，再进入构建。
√
坏方案应在零成本阶段被发现，而不是在
半成品阶段返工。
先把错误路径扼杀在纸面上。
>_Prompt 示例
In plan mode: lay out exactly how you'd add rate
limiting to the API.
List the files you'll touch, the order, and the risks.
Wait for my approval before writing code.
结果：你得到的不是“会写代码的助手”，而是“先思考再执行的代理”。
2/8

### 截图3
03-04
把团队标准写进系统
先把规则写清楚，再让变更以小步、可审查的方式落地。
Put Your Standards in CLAUDE.md
3
写入规范|CLAUDE.md
CLAUDE.md 就是仓库级“工作宪法”：
CLAUDE.md
约定、命令、规则都写在这里。
TypeScript strict mode, no any
Claude Code 每次会话都会读取它，
从一开始就带着团队基线工作。
Every new function gets a test
Test:npm run test
≡
可写内容：代码风格、测试要求、
Lint:npm run lint
常用命令、禁止修改区域。
Never edit/generated
!
重要细节：CLAUDE.md是“高概率遵守”，不是100%强制；
绝对不能破的规则，交给 hooks。
默认值由 CLAUDE.md 提供，硬约束由 hooks 执行。
4
Build the Change in Small, Reviewable Pieces
小步构建|Main session
√
方案批准后再构建，
Prompt 示例
而且要拆成小而完整的改动。
Implement step 1 of the approved plan only.
每次只做一步，便于验证、
Keep the change small and self-contained.
回滚与人工审阅。
Follow the conventions in CLAUDE.md.
避免一次性吐出一个
Stop after step 1 so I can verify
巨大的 diff。
before you continue.
小改动更容易被信任，也更容易被修正。
3/8

### 截图4
The 9-Step Loop That Turns Claude Code Into a Senior Engineer.
05-06
把要求变成自动化
真正成熟的工作流，不靠“记得做”，而靠“系统必然发生”。
A
5. Enforce the Non-Negotiables With hooks
自动约束|hooks
>
hooks 是 Claude Code 生命周期中的确定性 shell 命令。
⊕
它把“建议”变成“强制”：例如每次编辑后自动跑
lint 和 tests。
与CLAUDE.md 不同，hooks 是100%会触发的。
重要规则要设计成“跳不过去”，而不是“记得遵守”。
.claude/settings.json
PostToolUse: matcher = Edit|Write
自
command = npm run lint && npm run test
含义：每次写代码后，自动执行 lint+test。
B
6. Make It Prove the Change Works
测试证明|tests + hooks
任何改动都要补测试，并实际运行。
0
“看起来没问题”不算通过；只有测试通过才算完成。
第5步的 hooks 会把这件事自动化。
Prompt 给 Claude
Write tests that cover this change, including the
edge case where the token is expired.
Run the full suite and show me the results.
If anything fails, fix it before continuing.
“Done”不是主观感觉，而是客观通过。
4/8

### 截图5
The 9-Step Loop That Turns Claude Code Into a Senior Engineer
07-08
让第二双眼睛盯住风险
写代码的人最容易为自己的代码辩护，所以必须引入一个独立审查者。
A
7. Have a Second Agent Review the First
独立审查
review subagent
PROMPT
启动一个 review subagent,让它
只做一件事：像挑剔的资深工程师
Launch a review subagent.
那样审查 diff。
Its job: review the diff I just made
重点检查：安全问题、遗漏的
as a skeptical senior engineer.
边界条件，是否违背CLAUDE.md。
Check for security issues,
missed edge cases, and anything
that violates CLAUDE.md.
它拥有独立上下文，因此更容易
发现主代理忽略的问题。
Report problems, do not fix
them yet.
旁观者比作者更容易发现风险。
B
8. Fix What the Review Found, Then Re-Check
修复复检 「 the loop
PROMPT
把审查意见逐项修复。
Address every issue the reviewer raised.
After fixing, re-run the tests AND
修复后重新跑测试，再重新
launch the review subagent again
发起 review。
on the updated diff.
Repeat until the review comes
√
只有 review 结果 clean,
back clean.
才允许进入下一步。
Show me the final review verdict.
不是“看到问题”，而是“修掉并复核通过”。
这一步让流程从直线变成闭环。
5/8

### 截图6
The 9-Step Loop That Turns Claude Code Into a Senior Engineer
09把整套流程
封装成/ship
当变更已经 clean,最后一步不是再手动拼流程，
而是把整个闭环固化成一个可复用命令。
一键固化|slash command
把9步闭环写进自定义 slash command。
以后每个任务都不必重新组织流程，只需触发一次。
输出目标：清晰 commit、规范PR描述、稳定交付。
一次搭建，长期复用。
>_
.claude/commands/ship.md
1
1. Explore the relevant code
·2
2. Plan the approach and wait for approval
3-3
4
3. Build per CLAUDE.md, in small pieces
5
4. Write + run tests
8
5. Launch a review subagent on the diff
7-99-33
6. Fix issues, re-test, re-review until clean
7. Commit with a clear message and open a PR
当 /ship 成为默认入口，
“资深工程师工作流”就不再依赖记忆，而变成基础设施。
。
。
6/8

### 截图7
The 9-Step Loop That Turns Claude Code Into a Senior Engineer.
为什么这套
方法有效
?
这不是技巧堆砌，而是把资深工程师的工作纪律，
逐一映射到Claude Code 已有的原生能力上。
1
探索先行：
先理解再编辑，减少瞎改。
×-×
Plan Mode:
x
2
坏方案在零成本阶段被淘汰。
CLAUDE.md+hooks:
.md
3
标准被加载，关键规则被强制。
4
Tests+独立 Review:
“完成”必须被证明，而不是被宣称。
5
/ship:
工作流一次搭好，之后稳定复用。
初级用法
资深闭环
→
→
→
VS
→
</>
狂
提要求→改文件→人工看看→
Explore → Plan → Build → Test →
继续下一步
Review →Re-check →Ship
66
把 Claude Code从“需要盯着看”
变成“可以放心交办”，靠的不是更强模型，
而是更强闭环。
模型能力一直都在，缺的是围绕它搭建的工作系统。
7/8

### 截图8
The 9-Step Loop That Turns Claude Code Into a Senior Engineer
落地清单：
一次搭好，长期复用
如果你想把 Claude Code从“会写代码的助手”
升级成“可托付任务的工程代理”，
至少先搭好这4件事。
最小落地配置
1
在仓库根目录写好CLAUDE.md:
约定风格、命令、禁区。
2
配置 hooks:
把 lint、tests 等关键检查自动化。
3
固化流程顺序：
Explore →Plan → Build →Test →Review →
Re-check →/ship。
4
先拿一个中等复杂任务演练，
调顺后再推广到日常开发。
4句最有价值的提示模板
先 Explore:
进 Plan Mode:
开 Review:
闭环复检：
别改，先把
列出改动文件、
像挑剔的资深
修完后重新测试、
相关文件、
顺序和风险，
工程师一样
重新 review,
数据流和脆弱点
等我批准再写。
审查 diff,
直到 clean。
摸清。
只报问题先不修。
66
这套方法不会让 Claude Code 变得万无一失；
但它会显著缩小“初级助手”与
“资深工程师工作方式”之间的差距。
真正的杠杆，不是更神奇的模型，
而是更严谨的流程。
Build the loop once-then let every task run through it.
8/8
