---
title: 一套记忆系统，横跨所有Agent（Hermes_OpenClaw_Codex_ClaudeCode_etc.） 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/一套记忆系统，横跨所有Agent（Hermes_OpenClaw_Codex_ClaudeCode_etc.） 2.md
tags: [evernote, impression, yinxiang]
---

# 一套记忆系统，横跨所有Agent（Hermes/OpenClaw/Codex/ClaudeCode/etc.）

---

来源：[打开原文](https://mp.weixin.qq.com/s/9z2NVSurrx44RQDHpbq33A)

Hermes/OpenClaw终于“养熟了”，你有琢磨个下面这几个问题么？

1.
--

万一这些记忆丢失了咋办？
------------

2.
--

养熟的Hermes/OpenClaw的记忆和经验能移植给其他实例么？尤其是跨机器，甚至是跨Agent？

因为大多数 Agent 的记忆，都绑在自己的客户端、自己的框架里。

你今天用 Hermes 维护项目，明天切到 OpenClaw 跑自动化，后天又让 Codex 接着写代码，结果每个 Agent 都要重新解释一遍：这个项目是干什么的，你喜欢什么写法，哪些文件不能乱动，上次踩过什么坑等等。

这就很像你养熟了一个 AI 员工，结果一换工位，它又失忆了。

我开始意识到：

Agent 的记忆，已经不只是“让它更懂我”这么简单了，它记住的偏好、经验和项目上下文，本质上就变成了一种资产。

那么，这些资产：能不能备份？能不能迁移？能不能跨 Agent 复用？

今天遇到这么个项目，估计能解决这些问题：MemOS

它想做的不是再给 Agent 加一个聊天插件，而是把长期记忆抽出来，变成一层可以被不同 Agent 调用的记忆基础设施。

MemOS CLI则是给这些Agent记忆共用给出了一个最短路径。

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/E897591A-9D2A-4061-84A9-76C27D60276F.png)

他们这图画的就挺有意思：Hermes也好龙虾也罢，可以通过 MemOS插件 共享同一套记忆和经验。

MemOS CLI 是什么？
--------------

你可以先把它理解成一个命令行版的长期记忆入口。

普通 CLI 多半是给人敲的。MemOS CLI 有意思的地方是，它也能给 Agent 用。

未来的AI coding，需要控制你的Agent和别人交互、和别的Agent交互，Agent和Agent之间也有交互，所以必须让Agent、脚本能够看懂你，那么交流的语言就一定不是自然语言，而是命令行。

我前文提到的长期记忆也应该像代码仓库一样，可以备份、迁移、复用、隔离。

MemOS CLI 做的事情，就是用一套 memos 命令，为 AI记忆提供了一个人、Agent、脚本的共用最短路径。。

Hermes、OpenClaw、Codex、Cursor、Claude Code，都可以通过同一套 MemOS CLI 接入。

一、上手MemOS CLI
-------------

1.安装
----

•
-

在自己部署Hermes/OpenClaw的机器上直接复制粘贴执行下面这行命令，一分钟搞定：

npm install -g @memtensor/memos-cloud-cli

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/FD27DF2F-7D66-4453-B497-6DC445AA0246.png)

•
-

然后可以 memos --version 或者 memos --help一下，看看安装成功了没：

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/E6ABD0C3-0BB1-4E39-B525-A2F55FE8EE99.png)

•
-

然后去MemOS官网注册获取API KEY：

https://memos-dashboard.openmem.net/cn/login/?source=landing&from=/cn/quickstart/

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/434854BD-4377-4BA2-AEA6-12DD995EE6B2.png)

•
-

在这一步把API KEY复制出来：
-----------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/B474D78F-AC00-47FA-9363-0C40033BD8C9.png)

•
-

然后在终端里运行（把YOUR\_API\_KEY替换成你在上一步获取的MemOS的API KEY）：

memos config set platform.api\_key YOUR\_API\_KEY

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/219C15C4-D357-4572-B283-58B335F7FD0F.png)

2.写入第一条记忆
---------

•
-

然后试试MemOS是否能正常工作，在终端用memos add输入某个特别的记忆：
----------------------------------------

memos add "用户最爱的数字是996"

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/18F2C1D6-992F-40F8-932D-3692DDA98A34.png)

3.检索这条记忆
--------

•
-

然后用memos search查找：
------------------

memos search "用户最喜欢的数字"

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/1E255486-97D8-491D-A197-5BDBFE082657.png)

4.用 chat 验证记忆是否能被使用
-------------------

•
-

或者，用 memos chat 来直接问
--------------------

memos chat "你知道我最喜欢的数字么？"

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/F357B690-E8F8-4126-93FA-E4D1848B89C7.png)

到这里，第一轮就算跑通了。

以上几步的作用是：在接 Agent 之前，先判断记忆链路到底通没通。

如果这一步问题，就不是后面 Hermes / OpenClaw的问题

二、把 MemOS 装进Agent
-----------------

第一轮证明 MemOS 自己能记住。

第二轮就要看，它能不能进入 Agent 工作流。

•
-

OK，让我们把memos的能力给Hermes/OpenClaw打开（我是Hermes）：

memos init --agent hermes

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/DD3C99DF-C88F-4488-8999-439735394310.png)

还要输入一次API KEY；注意：这次粘贴API KEY不会显示，直接回车即可。

然后，最好 hermes gateway restart 一次确保新安装的Skill被正确加载

•
-

配置好之后去问问Hermes他是否已经拥有了MemOS的能力：
-------------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/ADD2991D-C4C7-4247-8317-17729266AF15.png)
![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/12E6D62A-3638-4392-8245-FCD171B70BDD.png)

•
-

OK，Hermes也认得MemOS了！
-------------------

装好之后，Hermes 就多了一个记忆 Skill。

它可以在对话前检索 MemOS，把相关记忆放进上下文。

也可以在对话后，把新的偏好、事实和项目经验写进 MemOS。

•
-

另外，目前MemOS支持的Agent有HermesCodex/Cursor/ClaudeCode/OpenClaw，对应的初始化命令行如下：

memos init --agent hermes    # ~/.hermes/skills/memos/  
memos init --agent codex     # ~/.codex/skills/memos/  
memos init --agent cursor    # ~/.cursor/skills/memos/  
memos init --agent claude    # ~/.claude/skills/memos/  
memos init --agent openclaw  # ~/.openclaw/skills/memos/

•
-

官方宣称接入MemOS CLI之后，token消耗会大幅度下降，准确率会中等幅度提升，这个让我们在后续的时候时持续观察吧～

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/D5D2E809-231F-4108-999E-C25868EC32DA.png)

•
-

强烈建议让Hermes写入一个agent\_id：
-------------------------

注意，MemOS CLI不直接支持写入agent\_id，你可以把我这个截图喂给一个多模态大模型，让它自己学习一下如何写入

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/389007C4-3741-42A6-9058-925160E78B07.png)

•
-

然后，我让Hermes把之前的记忆都dump到MemOS里：
------------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/D58D242D-5DE0-498F-93E0-2C25490FA682.png)

•
-

几分钟之后，Hermes已经将之前的重要Memory都存入了MemOS里：
-------------------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/6BC88CFB-1AB9-401F-9F65-D7BF90893EF1.png)

•
-

可以在MemOS后台查看已经被dump进来的记忆
------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/FCC51F3E-622A-4630-87CA-4D49CBF8225F.png)

•
-

此外，还有知识库的功能（不过我这次没测）
--------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/88A8B05C-64F1-4041-8930-690F938A7622.png)

•
-

由于Hermes的local记忆系统和MemOS是平行运行的，可以让Hermes自己写一份“双写策略”，确保本地保存的记忆和MemOS是同步的

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/2AE28E60-48F4-4F42-9B46-3F10CD8973D2.png)

哦对了，以上演示基于腾讯云Lighthouse服务器上的Hermes + MiniMax (Token Plan) M3

三、跨Agent使用
----------

•
-

在另一台机器上安装和配置好MemOS CLI（我用的是MacBook Pro上Hermes Agent）

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/3647C23B-9D59-410F-BE7B-9A8C8F01EFF0.png)

•
-

配置好之后让这台MacBook上的Hermes确认下能否读到刚才腾讯云服务器上的Hermes dump给MemOS的记忆

注意，需要是使用相同的user\_id和相同API KEY的账户～ 跨账户不行

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/1CBD3A9F-2E26-4DE0-A083-EF123ABC867F.png)

•
-

让它个自己也配置好agent\_id，这样两台机器上的记忆就不会混淆了（并且，也验证一下本地能否分辨出另一个Agent的id是啥）

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/5F18AE9F-1223-4F65-8B74-F5B3F40D5157.png)

•
-

让当前Agent从MemOS中检索并总结另一个Agent的Memory，OK，没毛病：

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/80D4CB53-6425-4940-B5D4-3C1122323A96.png)
![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/56C6B0E4-41EA-4472-BBD6-24452A51A013.png)

这样你就实现了跨Agent的Memory共享（并且可以清晰隔离 -- 一定要记住给每个Agent实例都配置好自己特定的MemOS里的agent\_id!!!）

四、关于用量和费用
---------

MemOS给的默认额度
-----------

•
-

addMessage：5万次
--------------

•
-

searchMemory：2万次
----------------

•
-

Chat Token：300万/输入；100万/输出；
---------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/7A016972-150C-493E-849B-DE171E4A5370.png)

提供的模型：
------

•
-

对话模型是DeepSeek R1和Qwen3-32b/Qwen3.6-flash
----------------------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/E4FBE1BD-8094-4B6E-BAB7-BB23D138C6E9.png)

•
-

记忆提取/Rerank/embedding模型是MemOS团队自研的：
-----------------------------------

![](.evernote-content/8FB21309-1E23-457A-93A1-91C4E8BF9B11/6FBB7529-D5A9-4D1E-BA7E-F436F766ED8B.png)

你看，绕来绕去，又回到我最近一直说的那个问题：你用AI/Agent做的事本身究竟有没有价值...

补充资料
----

更多关于MemOS的资料：

•
-

MemOS CLI文档站：

https://memos-docs.openmem.net/cn/mcp\_agent/cli/guide

•
-

MemOS插件站：https://memos-claw.openmem.net/
----------------------------------------

•
-

MemOS官网：https://memos.openmem.net/cn/
-------------------------------------

•
-

MemOSGithub仓库：

https://github.com/MemTensor/MemOS
----------------------------------

[📎 在印象笔记中打开](evernote:///view/207087/s1/b3f3a302-7248-468a-9f20-e92530df3149/b3f3a302-7248-468a-9f20-e92530df3149/)
