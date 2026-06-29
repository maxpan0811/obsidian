---
title: Claude Code 用了这个 Skill，终于不失忆了！
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/Claude Code 用了这个 Skill，终于不失忆了！.md
tags: [evernote, impression]
---

---
title: "Claude Code 用了这个 Skill，终于不失忆了！"
source: evernote
type: note
export_date: 2026-06-22
guid: 4914f266-e151-4aca-90e6-61ec6c0d141c
---

# Claude Code 用了这个 Skill，终于不失忆了！

来源：[打开原文](https://mp.weixin.qq.com/s/SekEIr5cthJNVprt28vvnQ)

## 每次打开 Claude Code，第一件事不是写代码，而是交代背景。

比如这个项目用的什么框架，上次为什么改了认证方式，那个奇怪的 bug 最后是怎么绕开的，哪些地方看起来能改但其实不能动……

要把它倒给 Claude，就得拆散、整理、重新组织。快的话 5 分钟，复杂的项目可能要半个小时。

这也不是 Claude Code 这种 Code Agent 的问题。

因为每一次对话都是一个独立的上下文窗口。

在这个窗口里跟它聊了两个小时，建立起来的项目认知，架构决策、踩过的坑、命名习惯、某个绕开方案的原因，只在当前的对话里。

窗口关掉，全没了。

那么怎么把项目记忆从上下文窗口里接管出来，放到一个持久的地方，每次新会话再装回去？

/memory 解决的就是这个问题。

## 它在底层做了什么

/memory 是一个 Claude Code Skill，但它背后挂着一套完整的本地 CLI 工具。

原理分三层：

第一层：结构化扫描。 第一次使用时，CLI 扫描你的项目目录，提取技术栈、目录结构、Git 信息、主要依赖、README 摘要，把这些整理成结构化的项目快照，存在本地。不是把所有文件内容都存进去，只提取关键信号。

第二层：知识沉淀。 整个开发过程里，你做的每个架构决策、踩的每个坑、记的每条备注，都通过 memory decision add、memory pitfall add、memory note 写进本地的知识库。这个知识库跟项目绑定，基于 Git remote URL 做项目 ID，换路径不会丢，换机器可以导出迁移。

第三层：按需注入。 新会话开始时，/memory 触发 memory inject --compact，把项目快照和知识库里的内容打包成一段结构化的上下文提示词，注入当前对话。Claude 从这段提示词里读到项目的完整背景，然后接着上次的状态继续干。

所有的记忆存在本地，不需要重新建立。

## 装上之后第一次用

初始化当前项目：

memory init

memory scan

scan 会自动读取目录结构、技术栈、Git 信息、主要依赖、README，生成结构化快照。

不需要手动写一个字。

打开 Claude Code，输入：

/memory

Claude 立刻执行：

memory status

memory inject --compact --max-tokens 1500

输出项目名称、路径、技术栈、Git 分支、README 摘要，以及已记录的决策和踩坑条目。

从输入 /memory 到 Claude 进入状态：10 秒。

## Skill 在对话里自动做什么

触发 /memory 之后，改变的不只是开局，而是整个对话方式。

问项目背景，它先查记忆再回答。

比如我问"这个项目的认证中间件在哪里"，Claude 没有直接翻文件，而是先执行：

memory query "认证中间件在哪里"

记忆里有一条备注说认证统一放在 app/middleware/auth.py，用的 pyjwt。Claude 直接回答，没有猜测，没有废话。

做了决策，它自动记录。

我说"我们把 JWT 认证改成 Session 吧"，Claude 确认之后执行：

memory decision add "认证方式从 JWT 改为 Session" \

--why "减少前端 token 管理复杂度，后端状态可控" \

--details "使用 Flask-Session + Redis，JWT 相关代码逐步下线"

我没有说"记录一下"，它自己判断这是一个值得记的决策，然后记了。

踩了坑，它自动存档。

本地测试通过，线上挂了。排查一小时，发现是 SESSION\_USE\_SIGNER 没设。我说"终于搞定了，是这个配置的问题"，Claude 执行：

memory pitfall add "Flask-Session 线上会话丢失" \

--solution "配置 SESSION\_USE\_SIGNER=True" \

--details "本地默认 False 能跑，线上 HTTPS + 多实例时 cookie 解析失败"

这条记录从此留在这个项目的知识库里。下次遇到同样的情况，不用再花一小时。

## 第二天开新会话

这是整个 Skill 最关键最实用的地方。

第二天打开 Claude Code，重新输入 /memory。Claude 重新注入了所有背景，包括昨天记录的那条决策和那条踩坑。

它知道选了 Session 认证，知道为什么选，知道有个 SESSION\_USE\_SIGNER 的坑。接着干，没有断层。

以前没有 /memory 的时候，新会话就是一张白纸。不管上次聊了多久、配合得多顺，关窗口就全没了。

## 关于搜索的两个小细节

/memory 触发时用的是 inject，把项目完整背景一次性装进来。适合开局建立全局认知。

但日常对话里，遇到具体问题时 query 更好：

memory query "连接池满了怎么办"

它基于你的问题去检索相关的决策、踩坑、备注，只返回真正有关的部分。Token 更少，回答更准。

主动说"先查一下记忆里有吗"，Claude 就会走 query。项目记录积累多了之后，比全量注入更实用。

## 项目结构变了后

引入新依赖、新增重要文件之后，说一句"更新一下项目扫描"，Claude 执行：

memory scan

重新扫描，下次注入的上下文就包含最新状态。不更新也能用，只是注入的可能是旧快照。

## 这其实是一个重构版

之前其实我是手动维护或者使用 KB 知识库来进行上下文的管理的。

作为纯文本的存储形式，其实还是有诸多的问题的。

首先是维护成本极高。随着项目的推进，本地纯文本的 Markdown 的文件会越来越多，如果不加以维护，很容易造成新旧知识的混乱，旧的得不到更新，新的内容直接和旧有的发生冲突。

再就是虽然建立了本地的索引，注入上下文的时候，还是会进行文件的全量加载，极其浪费 Token。

第二个是认知负担。你得决定写什么、写多细、什么时候更新。写太细 Token 爆，写太简单 AI 抓不住重点，而且没人有耐心一直更新。

这是重构的/memory 的设计绕开了这些问题。

扫描是自动的，记录发生在对话里，注入是结构化的，你不需要单独维护一堆文档，知识是在开发过程里自然沉淀下来的。

这个差别在长期项目上特别明显，积累了几十条决策记录和踩坑记录，每次新会话能直接继承这些，等于把半年的项目经验都迁移进来。

/memory Skill 的源码，安装方式和完整文档如下。

我用夸克网盘给你分享了「memory」，点击链接或复制整段内容，打开「夸克APP」即可获取。

链接：<https://pan.quark.cn/s/18b5b15b6e32>
