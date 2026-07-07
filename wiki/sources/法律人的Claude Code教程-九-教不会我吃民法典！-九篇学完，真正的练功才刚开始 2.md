---
title: 法律人的Claude Code教程（九）（教不会我吃民法典！）：九篇学完，真正的练功才刚开始 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/法律人的Claude Code教程（九）（教不会我吃民法典！）：九篇学完，真正的练功才刚开始 2.md
tags: [evernote, impression, yinxiang]
---

# 法律人的Claude Code教程（九）（教不会我吃民法典！）：九篇学完，真正的练功才刚开始

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485900&idx=1&sn=d012ff7d486c322449269ed23bf7c891&chksm=c2547a11f523f3077eae069a529801bdbe3b34f141dda8dc597d685aabf2d413d35632faad84&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE07/6ct+NUCbYv9gVFRhCxLVAQIE97dBBAEAAAAAAG2BEHNA2hUAAAAOpnltbLcz9gKNyK89dVj0E8/Stl1o94AAJQcpfmbXQ5A/GyoUNa7YLsbJ50U7muyOOPjwMmWDEb4g9CSfztat6svyrrp4Gu9k5zF+i9Uie8kH1UwePUwDkG7+F6DVW4FABQU0RhCr6EbSpS0p50kal6aZSQXg/JNuy38ag+WkNTDrHBujDk/h9iW7rGRvhPXufzhnhulvs7epTko8gati+vJpXsgPL0epT0+JLrzQUocpL22/r518PGujmRboBg==&pass_ticket=aqdKK/dUkaYov6LSjykJdyLWDK8D186GU6OIBiEVnf4cMwxNwXMyvY+yWSOPFSrO&wx_header=3)

Original两眼一睁就是学呀 智律积成

完结：愿 Claude Code 成为你的"野球拳"
--------------------------

如果你玩过《金庸群侠传》，应该知道"野球拳"这个梗。

它一开始看起来不显山不露水，甚至有点像玩笑，但真练起来，后劲很大。Claude Code 也是这样。它不是摆着看的黑科技，不是拿来炫技的玩具，而是一门能真正嵌进你日常工作的"真功夫"。

如果你点开了这一篇，恭喜你走到了本系列教程的最后一篇。

还没学习前面教程的同学，赶快回去补补课吧：教程一到八，从安装配置到 Subagent 分身术，一步步带你走完从零到精通的路径。

首先说一下，这一篇**没有任何实操**。大家在教程一到八中已经操作很多了，其实到了 Skill 那一篇，你与 AI 的协同能力、AI 的提效效果应该会有一个很明显的提升。后面的，都是锦上添花。

"法律人的 Claude Code 教程"这个系列，核心在于**法律人的入门和实操**，所以很多部分省略掉了，比如 Claude Agent SDK，我抑制着非常强烈的冲动想和大家分享，还是最后去掉了。而 **Skill**，是本系列诞生的核心原因之一，目前来看也是法律人了解 Claude Code、了解 Agent、了解 AI 最有效的方式。

当然，如果你想进一步了解 Claude Code，需要进一步努力，因为你会越来越发现它的魅力。接下来的路是**实践的路**。

这个系列的主线已经完结，如果 Claude Code 还有一些重要的更新，我也会补充更新。

当然，你的实践之路开始之前，还是建议你看完这篇"科目四"，因为这也很重要。

---

一、Plugin：把你的配置打包成律所标准模板
-----------------------

简单说，**Plugin 就是一个安装包**。

你花了一周时间打磨了一套法律工作流——一个合同审查 Skill、一个法条校验 Hook、一个尽职调查 Agent。现在团队其他人也想用。

怎么办？难道让每个人都重新花一周时间配置？不用。把你的 Skill、Hook、Agent、MCP 配置打包成一个 Plugin，同事安装后立即可用。

**Plugin 的价值，就是把个人能力变成组织能力。** 对律所、法务团队来说，真正有价值的，从来都不是"某个人很会用"，而是"这套能力能不能复制、交接、升级"。

想象几个场景。新人入职，以前要老律师手把手教、逐个传文件，现在安装 Plugin，五分钟上手，审查标准统一。标准更新，以前要发通知、改模板、盯着大家更新，现在更新 Plugin，全员同步。多人协作，以前大家各做各的，格式五花八门，现在用同一套工具，输出整齐划一。

再往前走一步，你会发现 Plugin 不只是"方便安装"，它其实是在做知识资产化。以前你的经验只存在你脑子里、聊天记录里、某个散落的文件夹里；现在，它可以被固化、分享、迭代、交接。谁离职了，标准不会跟着走；谁加入了，能力不会从零开始。

**这就是 Plugin 的价值：把你的经验，变成团队的能力。**

![](.evernote-content/8955171C-6BF5-4DA8-821B-ACAFCB349510/FD7A0907-C189-4C3A-9D18-12D374126F28.png)

---

二、Git：给你的工作上个保险
---------------

Git 是版本控制系统，简单说就是**文档的时光机**。每次修改都留一个"存档点"，随时可以回去。就像打游戏存档一样，只不过存的是你的文档。

你有没有过这种经历：起诉状改了八版，文件名变成"起诉状\_v8\_最终\_打死不改.docx"，找不到之前的版本在哪，不知道改了什么，想回滚到某个版本只能凭感觉回忆。

Git 解决的就是这些问题。修改留痕，谁改的、改了什么、什么时候改的，清清楚楚。随时回滚，不满意？一秒回到之前任何版本。分支实验，想尝试新写法？开个分支，不影响原文。

尤其是 AI 时代，你会比以前更频繁地试错。你会让 Claude Code 改结构、换表述、补论证、重写一版、再重写一版。如果没有 Git，你很快就会陷入一种奇怪的状态：改得很快，但不敢放手改，因为你怕回不去。

你不是为了当程序员才学 Git，你是为了让自己的判断过程可追溯、可比较、可撤销。法律工作不是一次成稿，而是一轮轮推敲。Git 只是把这个过程保存得更干净一点。

AI 时代，必须 Git。**不 Git，不 CC。**

**这就是 Git 的价值：不怕试错，随时回头。**

---

三、隐私安全：律师的红线
------------

律师这个职业，有一道不可逾越的红线：**客户保密**。用 AI 工具也不例外。如果因为使用 Claude Code 导致客户信息泄露，那完蛋了。

所以这一部分，我要多叮嘱几句。AI 能帮你提效，但保密义务不能外包给 AI。

第一层，**绝对不要碰**。密码、密钥、银行账号、身份证号、未公开商业秘密、内幕信息，这类东西不要抱有任何侥幸心理，别输就是了。

第二层，**可以处理，但必须先脱敏**。客户姓名改成"甲方""乙方"，公司名称做匿名化，交易金额做区间化，案件细节只保留分析所必需的部分。你让 AI 处理的，应该是问题结构，不是原样材料。

第三层，**AI 的输出不能直接外发**。哪怕它写得再像样，发给客户前、进合同正文前、进法院材料前，都要人工复核。AI 可以生成初稿，可以帮你思考，但不能代替你承担责任。

养成一个习惯：**脱敏 → AI 处理 → 人工复核 → 还原**。记住：AI 是辅助工具，最终责任由你承担。拿不准时，默认不要输入。别因为图省事，把不该给的东西给出去。

![](.evernote-content/8955171C-6BF5-4DA8-821B-ACAFCB349510/D133E10B-A45E-4A60-8FCA-64B1FF722520.png)

---

四、实践建议：与 Claude Code 协作的心法
--------------------------

学完功能怎么用？这部分是"心法"，是我用 Claude Code 一段时间后结合网络中的帖子总结的经验。

第一条，**给验证标准**。Claude Code 自己能验证的事，别让它"自由发挥"。无论什么任务，你都要设定一个判断标准。如果它没做到，就继续调；如果这个任务天生没法客观验证，那你至少要先告诉自己：这次得到的是"辅助意见"，不是"标准答案"。

第二条，**先了解再动手**。复杂任务，先规划再执行。探索 → 规划 → 执行 → 交付。遇到复杂案件，先用 Plan Mode 让 Claude Code 阅读材料、整理信息、制定策略，你确认方案后再执行。简单任务就不用了，比如"这个法条在哪"，直接问就行。不是所有事都值得先开战略会，但复杂任务值得。

第三条，**给具体，别给模糊**。Claude Code 不会读心术，你指哪它打哪。不要说"为这个合同添加条款"，要说"为这个**采购合同**的**知识产权保护**章节添加条款"。不要说"这个案子有什么风险"，要说"查阅文件夹中的**证据清单**，结合你指定的司法解释，分析诉讼风险"。具体一点，结果靠谱一点。

第四条，**配置即记忆**。把常用规则固定下来，Claude Code 每次都能自动加载。你有几种选择：`CLAUDE.md` 写项目级别的规则，Skill 写可复用的工作流，Hook 写自动触发的操作。配置一次，长期有效。别每次都重复说一样的话，重复说明是最浪费律师时间的事之一。

第五条，**像助手一样沟通**。把 Claude Code 当成可培养的 junior 律师，不是搜索引擎，你怎么带教的，就怎么沟通 Claude Code。给背景、给边界、给判断标准，也给反馈。（如果教不好，请反思自己）

第六条，**及时纠偏**。发现跑偏，立刻说。如果它正在执行你发现方向错了，按 `Esc` 中断，然后说"停，方向不对"。如果做完了但你发现不对，说"撤销刚才的修改"。如果对话太长它开始"遗忘"，用 `/clear` 清空重新开始。经验法则：如果你纠正了两次以上，上下文已经被污染了，这时候直接清空重开更高效。不要和一个已经跑偏的上下文恋战。

第七条，**扩大产能**。一个 Claude Code 不够用，就多开几个。查法条一个窗口，改文书一个窗口，整理知识一个窗口，各干各的，效率会明显上来。但前提是你知道每个窗口在做什么、谁有权限、哪个能碰真实材料。效率和风险，从来都是一起出现的。

---

五、终端美化
------

终端美化，表面上是换个皮肤换个心情，实际上是在降低你的使用阻力。界面顺眼一点、信息清楚一点、错误醒目一点，你就更愿意打开它，也更不容易犯低级错误。

不过别把它搞成太过于花里胡哨。对法律人来说，终端最重要的不是炫，而是清楚、稳定、耐看。我自己的建议很简单：字体看得清，当前目录和 Git 分支一眼能看到，报错信息能高亮。够用了。工具是拿来干活的。

如果你还不知道选哪个终端，可以先从几个知名选手里挑一个顺眼的。`iTerm2` 是 mac 上的老牌选择，稳。`Ghostty` 这两年很火，快，而且原生感很好。`Warp` 更现代一点，对很多新手更友好。`WezTerm` 和 `Alacritty` 都是跨平台路线，前者配置能力更强，后者更偏简洁和性能。

![](.evernote-content/8955171C-6BF5-4DA8-821B-ACAFCB349510/C928B1AA-AF14-4EC0-A6FD-EC9CB526DA2A.png)

---

六、Obsidian 集成
-------------

如果你用 Obsidian 管理知识，它和 Claude Code 确实很搭。Obsidian 负责沉淀，Claude Code 负责加工；一个像你的第二大脑，一个像愿意干活的助理。

法律人的知识，本来就不是一篇文档，而是一张网：法条摘录、案例笔记、谈判复盘、审查口径、尽调清单、常用提示词、固定规则，彼此之间都是有关系的。Obsidian 擅长把这些东西连起来，Claude Code 擅长把这些材料读进去、整理成结构、改写成可交付内容。

一个很实用的工作流是：案件材料放项目文件夹，长期规则写进 `CLAUDE.md` 或 Skill，复盘和知识沉淀放进 Obsidian。这样你不是每接一个新项目都从零开始，而是在调用自己过去积累下来的判断。

**第二大脑一旦和 AI 助手接上，复利会很明显。**

---

七、优秀的开源工具
---------

别把自己绑死在某一个工具名上。真正值得学的，不是"这个软件怎么点"，而是"AI 怎样进入你的工作流"。这套方法一旦掌握，平台会变，思路不会变。

如果硬要分，其实就三种入口：喜欢桌面界面的，看 GUI；习惯在终端里推进任务的，看 CLI Agent；长期待在 VS Code 里的，看编辑器插件。法律人不必站队，选自己最顺手的入口就行。

* CodePilot[1]：藏师傅开发，适合想用桌面 GUI、又不想长期泡在纯终端里的人，上手更轻一点。
* SuitAgent[2]：杨律做的诉讼场景项目，法律人尤其值得看它怎么把 Claude Code 接进具体法律服务流程。
* OpenCode[3]：适合想保留模型和供应商选择权的人，开源、终端路线也比较清晰。
* Codex CLI[4]：OpenAI家的。
* Gemini CLI[5]：Google家的。
* Cline[6]：适合长期在 VS Code 里工作的人，不想切出编辑器也能把 AI 接进日常修改流程。当然，Claude Code也有VS Code扩展。

这些工具背后其实是同一件事：把模型接进文件、终端、规则和流程。对法律人来说，重点不是站队，而是找到最顺手的入口：终端、编辑器，还是桌面界面。你一旦学会把模型接进文件、规则、知识库和交付流程，换工具只是换界面，不是换脑子。

---

八、学习拓展
------

想进一步了解，去官方文档进修吧：https://code.claude.com/docs

第一站一定是官方文档。命令怎么用、权限怎么管、Hook、Skill、Agent 怎么协同，官方文档最全。你越早养成看文档的习惯，越早从"会用"走向"会搭"。

---

系列完结
----

![](.evernote-content/8955171C-6BF5-4DA8-821B-ACAFCB349510/2961D5C8-AB5C-4BD6-9B92-082C09B1D300.png)

我们用了九篇教程，走完了从零到开始的完整路径。

**系列教程完结，但你的法律 AI 之旅才刚刚开始。**

真正厉害的，不是会几个命令，而是你能不能让它稳定地参与真实工作。愿你用好 Claude Code，把法律工作做得更快、更好、更轻松。

**愿 Claude Code 成为你的"野球拳"**：也许初看不起眼，但只要你真把它带进日常工作里反复练，它就会像《金庸群侠传》里的野球拳一样，"天下无难事，只怕野球拳"！

![](.evernote-content/8955171C-6BF5-4DA8-821B-ACAFCB349510/00AAD730-5CB6-4EDF-B7B7-8CB6FAC7F9BD.png)

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。

参考链接

[1] CodePilot: https://github.com/op7418/CodePilot

[2] SuitAgent: https://github.com/cat-xierluo/SuitAgent

[3] OpenCode: https://github.com/nichochar/opencode

[4] Codex CLI: https://github.com/openai/codex

[5] Gemini CLI: https://github.com/google-gemini/gemini-cli

[6] Cline: https://github.com/cline/cline

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485900&idx=1&sn=d012ff7d486c322449269ed23bf7c891&chksm=c2547a11f523f3077eae069a529801bdbe3b34f141dda8dc597d685aabf2d413d35632faad84&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE07/6ct+NUCbYv9gVFRhCxLVAQIE97dBBAEAAAAAAG2BEHNA2hUAAAAOpnltbLcz9gKNyK89dVj0E8/Stl1o94AAJQcpfmbXQ5A/GyoUNa7YLsbJ50U7muyOOPjwMmWDEb4g9CSfztat6svyrrp4Gu9k5zF+i9Uie8kH1UwePUwDkG7+F6DVW4FABQU0RhCr6EbSpS0p50kal6aZSQXg/JNuy38ag+WkNTDrHBujDk/h9iW7rGRvhPXufzhnhulvs7epTko8gati+vJpXsgPL0epT0+JLrzQUocpL22/r518PGujmRboBg==&pass_ticket=aqdKK/dUkaYov6LSjykJdyLWDK8D186GU6OIBiEVnf4cMwxNwXMyvY+yWSOPFSrO&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3cd9ae8e-36e1-459d-a4e0-502a03db1464/3cd9ae8e-36e1-459d-a4e0-502a03db1464/)
