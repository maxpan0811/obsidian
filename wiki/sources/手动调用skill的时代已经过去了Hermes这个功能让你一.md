---
title: 手动调用skill的时代已经过去了！Hermes这个功能让你一条命令跑完整套工作流！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/手动调用skill的时代已经过去了！Hermes这个功能让你一条命令跑完整套工作流！.md
tags: [印象笔记, 其他]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "手动调用skill的时代已经过去了！Hermes这个功能让你一条命令跑完整套工作流！"
source: evernote
type: note
export_date: 2026-06-24
guid: 14a87329-e1c7-406e-aa9d-dc2b26c526a9
---

# 手动调用skill的时代已经过去了！Hermes这个功能让你一条命令跑完整套工作流！

来源：[打开原文](https://mp.weixin.qq.com/s/2aXOCOsGGkFrFxK4n9P1xA)

![](attachments/984b27de000363fb.jpg)

你好，我是元小二，专注分享 AI 提效、一人公司实践和个人成长。这里有 OpenClaw、Claude Code、自动化流程、虚拟产品，也有理财、思考和生活系统。

欢迎关注，也欢迎后台留言告诉我，你对哪部分内容感兴趣。

朋友们，这是一个喜大普奔的好消息：以前我每次发公众号，都要在 Hermes 里一条一条输命令——去 AI 味、起标题、配插图、做首图、搞分享素材……光命令就得打七八条，还得在中间手动等着，生怕哪步顺序搞错。

做了两个月之后，我终于忍不了了。

然后我发现了 Hermes 的 Skill Bundle。

![](attachments/257978c873938f4a.png)

我对之前那种工作方式的评价是：纯纯的傻瓜操作，可以退休了。

## 一、Bundle 是个什么东西

一句话说清楚：Skill Bundle 是一个 YAML 文件，把你常用的一套 Skill 打包成一条斜杠命令。

以前发一篇文章，我要输：

/humanizer-zh

/headline

/inline-diagram

/cover-hero

/share-card

五条命令，每条执行完还要手动切下一条。

做成 Bundle 之后，我只需要输一条：

/yuanxiaoer-article-publish

然后 Hermes 把七个 Skill 全部加载进来，按我定义的顺序一步一步推进，每个阶段交付完了停下来等我确认，确认了再继续。

真的绝了。

## 二、Bundle 不是工具箱，是流水线

![](attachments/8d911207d274bab3.png)

这里有个坑我踩过，给你省时间：

不要把所有常用 Skill 一股脑塞进一个 Bundle。

我刚开始就犯了这个错——把十几个觉得”以后可能用到”的 Skill 全部列进去，结果 Hermes 读到一堆互不相关的指令，完全不知道该先做什么，输出质量乱成一团。

正确的用法是：Bundle 要有因果链。

好的 Bundle 长这样：

初稿 → 终稿 → 标题 → 插图 → 首图 → 分享素材

每一步自然接住上一步的结果，这才是 Bundle 该干的事。

判断一个 Skill 要不要放进 Bundle，就问自己三个问题：

1. 它跟其他 Skill 属于同一个流程吗？

2. 前一步的产出会成为它的输入吗？

3. 需要统一的顺序来约束它们吗？

三个都是”是”，进 Bundle。否则，单独调用。

## 三、instruction 字段才是 Bundle 的灵魂

Bundle 的 YAML 里有个 instruction 字段，很多人写了个空的就算了。

错了，这才是最值钱的地方。

一个好的 instruction 要写清楚：每个阶段做什么、用哪个 Skill、交付什么、哪里停下来等确认、哪些任务可以并行。

我的公众号 Bundle 里写的是这样的：

instruction:|

Phase 1 — 文稿终审

使用 skill: yuanxiaoer-humanizer-zh

交付：去 AI 味后的终稿

完成后停下来确认

Phase 2 — 标题与摘要

使用 skill: yuanxiaoer-headline

交付：主推标题 x1、备选标题 x2、摘要 x1

完成后停下来确认

...

把 instruction 理解成这个 Bundle 的临时项目说明书——它定义的不是 Agent 的永久身份，而是这次工作流的执行节奏。

写得越清楚，Agent 跑得越稳。

## 四、两种方式创建 Bundle

## 1. 命令行直接创建

如果你已经想好要打包哪些 Skill：

hermes bundles create yuanxiaoer-article-publish \

--skill yuanxiaoer-humanizer-zh \

--skill yuanxiaoer-headline \

--skill yuanxiaoer-cover-hero \

-d"公众号文章发布流水线"

执行后，Hermes 在 ~/.hermes/skill-bundles/ 下自动生成 YAML 文件。

## 2. 让 Hermes 帮你规划

如果你还不确定该组合哪些 Skill，直接跟 Hermes 说你的目标就行：

“我的公众号文章初稿已经写好了，帮我规划一个技能包，每个阶段要有交付清单，完成后需要向我确认。”

Hermes 会根据现有 Skill 列表帮你设计阶段、选工具、定交付物。第一次设计工作流用这种方式省事很多。

## 五、跑完之后记得验一遍

Bundle 创建好了别急着用，先用一篇测试材料跑一遍，看几件事：

• 所有 Skill 有没有正确加载

• 是不是按阶段顺序推进的

• 确认点有没有真的停下来

• 有没有 Skill 指令互相打架

• 最终交付物是不是完整的

我第一次跑的时候，发现 Phase 5 里有两个子任务的指令有冲突，调整了一下才顺起来。先测试，少踩坑。

Skill 是可复用的能力块，Bundle 是把多个 Skill 编排成标准流程的 YAML 配置。

不要用 Bundle 堆工具，要用 Bundle 固化有前后依赖的工作流。

现在去打开你的 ~/.hermes/skill-bundles/ 目录，把你最常跑的那套流程做成一个 Bundle 吧，我的朋友。

人生是一场无限游戏，乾坤未定，你我均是黑马。

【元小二学AI】👇公众号后台回复关键词【hermes】，领取从小白到高手的Hermes全套教程。
