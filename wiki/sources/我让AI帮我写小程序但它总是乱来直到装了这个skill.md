---
title: 我让AI帮我写小程序，但它总是乱来——直到装了这个skill
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/我让AI帮我写小程序，但它总是乱来——直到装了这个skill.html
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "我让AI帮我写小程序，但它总是乱来——直到装了这个skill"
source: evernote
type: note
export_date: 2026-06-26
guid: 76e0afe3-f0e1-4b50-84d0-ecd3e435fa5b
---

# 我让AI帮我写小程序，但它总是乱来——直到装了这个skill

来源：[打开原文](https://mp.weixin.qq.com/s/4G5eNOHKiO2X0OPvSQwIQw)

![](attachments/984b27de000363fb.jpg)

你好，我是元小二，专注分享 AI 提效、一人公司实践和个人成长。这里有 OpenClaw、Claude Code、自动化流程、虚拟产品，也有理财、思考和生活系统。

欢迎关注，也欢迎后台留言告诉我，你对哪部分内容感兴趣。

朋友们，这是一个喜大普奔的好消息：

前两个星期，我用3天时间做出了一个微信小程序，叫「AK萌牙记录」。

专门帮爸爸妈妈记录孩子换牙进度的——哪颗牙掉了、哪颗新牙长出来了，全都清清楚楚记录好。换牙期的父母，这个小程序你一定用得上。

![](attachments/894c38feddc66a70.png)

但今天我不是来推销小程序的（先看看成果）：6-12岁娃的妈妈看过来！换牙管理就该这么做

![](attachments/816c35a234ec325a.png)

我要说的是：做这个小程序的过程中，有一个工具救了我。没有它，3天根本做不完。

## 一、先说说我踩过的坑

用 Claude Code 写代码，你可能有这种体验：

你描述一个需求，AI 直接就开始写代码了。写了一大堆，你发现方向不对。推倒重来，又写了一大堆，又不对。

来来回回，一下午没了。

我做「AK萌牙记录」之前也是这样。脑子里有想法，但就是说不清楚，AI 理解偏了，做出来的东西鸡肋得很。

后来我装了一个 Skill，彻底改变了这个局面。

## 二、这个Skill叫 Superpowers

![](attachments/5995f26825b244b3.png)

它本质上是一套完整的 AI 编程方法论，把 14+ 个结构化技能打包在一起，塞进了 Claude Code 里。

你可以把它理解成：给 AI 程序员配了一个靠谱的项目经理。

它不会让 AI 一上来就乱写代码。它会强迫走完整流程：

## 1. 先逼你把需求说清楚（Brainstorming）

描述模糊需求时，它会反问你一堆问题——边界是什么？有没有漏掉的情况？真的需要这个功能吗？

我描述「萌牙记录」的需求时，它问了我：「要记录换牙时间吗？要支持多个孩子吗？要提醒功能吗？」

我一下想明白了一半。

![](attachments/07f6b5193a08dcb0.png)

## 2. 再帮你拆任务、写计划（Write Plan）

需求确认后，它会把工作拆成一个个小步骤，每步指定文件路径、代码片段、验证方式。

生成一份 PLAN.md，你过一遍，确认，开干。

## 3. 最后才写代码，而且写完自己会检查（Execute + Review）

写代码的过程中，有两轮自动 review：符合需求吗？代码质量过关吗？

我之前用别的方式弄一个功能，来回改了好几次；用 Superpowers 走完整流程，一次过。

## 三、怎么安装？两行命令搞定

在 Claude Code 会话里直接输入：

/plugin marketplace add obra/superpowers-marketplace

/plugin install superpowers@superpowers-marketplace

或者用官方市场（更稳定）：

/plugin install superpowers@claude-plugins-official

安装完之后，运行 /help，看到 brainstorm、write-plan 这些新命令出现，就成功了。

安装后几乎零维护，Claude Code 启动时自动加载。其他编程软件也可以接入的，这是它的官方仓库：

https://github.com/obra/superpowers

## 四、怎么用？一句话就够

新会话直接说：

「用 Superpowers 帮我实现 [你的功能]」

剩下的事它来。你只需要回答它的问题、批准方案、偶尔做个选择。

我对那些一上来就让 AI 无脑写代码的做法评价是：可以毕业了。

## 五、写在最后

如果你要学 AI 编程，其他 Skill 可以慢慢装，但 Superpowers 必须第一个装。

它不是让你写代码更快，而是让你少走弯路。对我们这种非职业程序员来说，这才是最值钱的。

如果你家孩子正在换牙期，欢迎关注「AK萌牙记录」小程序，扫码就能用，免费的。
