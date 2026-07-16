---
title: "非程序员的Claude Code实战：3个月，从这是啥到离不了"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/非程序员的Claude Code实战：3个月，从这是啥到离不了.md
tags: [evernote, impression]
---

---
title: "非程序员的Claude Code实战：3个月，从这是啥到离不了"
source: evernote
type: note
export_date: 2026-06-23
guid: 00f4ec00-9104-4e73-84e0-ec4e784cdfb0
---

# 非程序员的Claude Code实战：3个月，从这是啥到离不了

原文链接: [https://mp.weixin.qq.com/s?chksm=8804b9c4bf7330d22189ae3cbcdf41e...](https://mp.weixin.qq.com/s?chksm=8804b9c4bf7330d22189ae3cbcdf41e4a793e9dd22b7f9fd3651fdd2e65fd8ddfd6feace89d1&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_3&req_id=1782034214604406&scene=169&mid=2649444824&sn=09ca6dbe853f0d4d547178720c762552&idx=1&__biz=MzA4OTQxNjA1MQ==&sessionid=1782032739&subscene=200&clicktime=1782034818&enterid=1782034818&flutter_pos=29&biz_enter_id=5&jumppath=20020_1782034796304,1104_1782034796877,20020_1782034803949,1104_1782034815915&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzvFK4FR6jJffNKPKK7nLQhLTAQIE97dBBAEAAAAAAMo7IkkqN68AAAAOpnltbLcz9gKNyK89dVj0M+Yew8o9R3/vsNTF596HE8o7gWkZggV0DDSPIAOUluGSXTp+5EyKWNNTxgjktka2TD2+iK32yIhH5XUhLk37Ys+hUMIyeClP6ZEUUtH8/Rtbe+8mNOEkOirMIRWhe7nLwoVNs36hvkwGdlFvSlPSwvJARO2cbx/YLevjArcubgJCpsPqNsoTCAgLvn5dHv7NXESpJHpcfXyQlomhzXkTgNuKByi5KG6patdiUok=&pass_ticket=Pmh24WZtf4efjjIo3ksiqm+N+i/JSNZtL+nh0Aw+tge4+mgF5ScQYPPrvuSTdlqh&wx_header=3)

洛书低等动物研究社

从事广告投放行业也有一段时间了，本身是跨行业转行过来的，**不会写一行代码**。

三个月前我第一次打开 Claude Code，脑子里只有一个想法："这玩意儿跟我有什么关系？"

三个月后，我每天打开电脑第一件事就是启动它。自动汇总各项目消耗数据、生成趋势图推飞书、写邮件整理会议纪要、做竞品分析——以前要花半天的活，现在几分钟搞定。

但我发现一个残酷的事实：大部分非程序员听到"Claude Code"三个字，第一反应是——"这不是给程序员用的吗？"

错了。大错特错。Claude Code 最被低估的价值，恰恰是给不会写代码的人用的。

## 01 · 它和豆包，根本不是一个物种

很多人把 Claude Code 理解成"另一个豆包"。

豆包是什么？你问它答，但它碰不到你的电脑。

Claude Code 是什么？它住在你电脑里，能直接读写你的文件、运行命令、创建项目。

一个是嘴，一个是手。差距就在这。

## 02 · 非程序员用 Claude Code，记住三个原则

用了三个月，踩了无数坑，最后总结出三条铁律：

### 原则一：先给它一个人设

在用户主目录创建一个 `CLAUDE.md` 文件，告诉 AI 你是谁、你做什么、你希望它怎么跟你沟通。比如我的就写着：

"我是广告投放行业的，跟我说原因和对投放的影响，别只讲实现。结论先行，默认中文。"

这一步看似简单，却是 80% 的人跳过的步骤。没有人设的 AI 就像没有岗位说明的新员工——它很聪明，但它不知道你要什么。

### 原则二：每次只做一件事

新手最大的错误就是一口气提十个需求，然后发现改都改不过来。

正确的节奏：先出方案 → 确认后写核心功能 → 加错误处理 → 优化打包。每一步做完验证，再走下一步。

听起来慢，实际上快。因为改一个小 bug，比推翻重来省十倍时间。

### 原则三：把成功的操作存成指令

在 `.claude/commands/` 目录下创建 `.md` 文件，就能用 `/指令名` 一键触发。我存了 `/new`（创建新项目）、`/todo`（查看进度）、`/check`（目录健康检查），每次输入两个字符就搞定，不用重复描述。

好用的 prompt 存模板，踩过的坑记下来——这才是用 AI 的正确姿势，不是每次都从零开始，而是让经验自动复用。

## 03 · 五个场景，拿来就用

别光听我讲道理，直接看怎么用——

### 场景一：汇总消耗数据 + 推送飞书

以前每月初我要手动把各项目的消耗数据从十几个 Excel 里抠出来，按项目汇总、画趋势图、再截图发群里。现在一句话搞定：

帮我写一个脚本：

输入：某目录下所有 Excel 文件  
处理：按项目汇总消耗数据  
输出：汇总表 + 趋势图  
推送：飞书群通知

要求：用 Pillow 画图（matplotlib 中文渲染有问题），用 openpyxl 操作 Excel，加错误处理和进度显示

先出方案，不要写代码

**关键技巧：** 先说"输入 → 处理 → 输出"，再说技术约束，最后加一句"先出方案"。它不会上来就写代码，而是先给你方案确认，确认后再动手，避免方向跑偏。

### 场景二：修 Bug

脚本跑着跑着报错了？别只说"报错了"，这样：

这段代码报错了，帮我修复。  
错误信息：[粘贴完整的 Traceback]  
相关文件：main.py  
期望：应该正常运行  
实际：报了上面的错误

贴完整错误信息，它一次就能定位。少说一句"报错了"，省掉三轮回合。

### 场景三：竞品分析

帮我分析这份数据：  
文件：[路径]  
分析目标：按投放渠道汇总消耗，找出 ROI 异常的渠道，生成对比图表  
输出：Excel 表格 + PNG 图表 + 文字摘要

三件套一次出齐，不用你再去 Excel 里拉数据、截图、写总结。

### 场景四：写邮件 / 文档

帮我写一封邮件：  
收件人：[姓名]（[关系]）  
目的：[要达成什么]  
关键信息：[数据 / 要点]  
语气：[正式 / 友好 / 委婉]  
给我两个版本。

说清收件人、目的、关键信息、语气，甚至可以让它给你两个版本挑。

### 场景五：深度研究（感谢卡神开源的横纵分析法）

用横纵分析法研究 [主题]：  
纵轴：从诞生到现在的发展历程  
横轴：当前与竞品的系统对比  
输出：PDF 报告

横轴纵轴一拉，结构就出来了，比你自己从零写大纲快十倍。

## 04 · 一个提问公式，覆盖 90% 的场景

上面五个场景看着多，其实都遵循同一个公式：

[我是谁] + [我要做什么] + [输入是什么] + [输出格式]

❌ "帮我做个报表"

✅ "我是广告投放的，需要分析上月各项目消耗。数据在 [路径]，输出 Excel + 趋势图。"

差一个公式，差十倍效果。

## 05 · 最关键的一句话

很多人问我："我不会写代码，怎么用 Claude Code？"

我的回答是：**你不需要会写代码，你需要会用"工作流的思维"跟 AI 对话**。

这本身也是接入 AI 最好的启动方式——先学会精准表达需求，拆解传统工作流。个人认为：这是 AI 时代最重要的能力。

你每天的工作其实都是流程：拿到消耗数据 → 按项目汇总 → 出表 → 发群。你不需要知道 Python 怎么写 openpyxl，你只需要说清楚"拿到什么 → 怎么处理 → 输出什么 → 推到哪里"。

Claude Code 帮你把"想到"变成"做到"。剩下的，交给它。

别怕，动手试。最坏的结果不过是 `git reset --hard` 回滚重来。

作者提示: 内容由AI生成


---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=8804b9c4bf7330d22189ae3cbcdf41e4a793e9dd22b7f9fd3651fdd2e65fd8ddfd6feace89d1&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_3&req_id=1782034214604406&scene=169&mid=2649444824&sn=09ca6dbe853f0d4d547178720c762552&idx=1&__biz=MzA4OTQxNjA1MQ==&sessionid=1782032739&subscene=200&clicktime=1782034818&enterid=1782034818&flutter_pos=29&biz_enter_id=5&jumppath=20020_1782034796304,1104_1782034796877,20020_1782034803949,1104_1782034815915&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzvFK4FR6jJffNKPKK7nLQhLTAQIE97dBBAEAAAAAAMo7IkkqN68AAAAOpnltbLcz9gKNyK89dVj0M+Yew8o9R3/vsNTF596HE8o7gWkZggV0DDSPIAOUluGSXTp+5EyKWNNTxgjktka2TD2+iK32yIhH5XUhLk37Ys+hUMIyeClP6ZEUUtH8/Rtbe+8mNOEkOirMIRWhe7nLwoVNs36hvkwGdlFvSlPSwvJARO2cbx/YLevjArcubgJCpsPqNsoTCAgLvn5dHv7NXESpJHpcfXyQlomhzXkTgNuKByi5KG6patdiUok=&pass_ticket=Pmh24WZtf4efjjIo3ksiqm+N+i/JSNZtL+nh0Aw+tge4+mgF5ScQYPPrvuSTdlqh&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/00f4ec00-9104-4e73-84e0-ec4e784cdfb0/00f4ec00-9104-4e73-84e0-ec4e784cdfb0/)
