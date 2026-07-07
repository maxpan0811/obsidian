---
title: 用了三个月Claude Code和Cursor，我发现90%的人选错了
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/用了三个月Claude Code和Cursor，我发现90%的人选错了.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "用了三个月Claude Code和Cursor，我发现90%的人选错了"
source: evernote
type: note
export_date: 2026-06-24
guid: 57ddc69e-7cad-4c0e-ab7e-92db8d6ba540
---

# 用了三个月Claude Code和Cursor，我发现90%的人选错了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484490&idx=1&sn=b1d213843c15ebb02247087689cc5210&chksm=f1644b7dd6cbdd138c5dc4c6414c51bc39265d5eda3e6cd4f16097bc7d84b1708731d55c7b06&scene=90&xtrack=1&req_id=1776158080028632&sessionid=1776157823&subscene=93&clicktime=1776158251&enterid=1776158251&flutter_pos=5&biz_enter_id=4&ranksessionid=1776158080&jumppath=WAWebViewController_1776158217837,WAWebViewController_1776158218319,20020_1776158237680,1104_1776158238893&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004637&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ74f66lJV1AO5Pt5YFWVJeRLVAQIE97dBBAEAAAAAAPQpCQ5FOokAAAAOpnltbLcz9gKNyK89dVj0aEpS1sAL36r0DsJTBp+zemZfvOndksocPTEtAiNPKsjC13ofKDAzwbCrf/Qxq1LXdutVYqmhw5WfUVqW03BbmXRTWr6XR4O6eCCAem36wVtTDEToec7W5LWtckSy0/G0MeM2iFAChz1gqX3zuk3FD3FwIBi4fSjBdV97WxYi7XEjrj16gFGNQoJyAnxd2qq6N6rmDMcb1JmfKDr/vQt+HQjUHIretVPEN9t/6Esd0Q==&pass_ticket=ZNDwokyoHT+CjZYpyIvctQWyW9qUHkcpu9sgVsg84CHHZNuxX85nz5tyyJ4SUZWI&wx_header=3)

Original莲花明 AI落地手记

我不是程序员。

说出来有点丢人——我连 Python 语法都记不全，for 循环写完经常忘加冒号。

但过去三个月，我同时用 Claude Code 和 Cursor 管了二十多个客户项目。两个都充了年费，一个月烧 40 美元。

今天把结论摊开说：90% 的人选错了。

不是工具不好。是你用买锤子的思路，选了一个该买员工的场景。

---

## 先说结论

Cursor 是一把超级锤子。你挥锤子，它帮你锤得更快更准。

Claude Code 是一个员工。你说"把这面墙拆了重砌"，它自己去干，干完叫你验收。

区别不在功能列表。区别在——谁是干活的那个人。

---

## 晚上十一点，客户改需求

群里弹消息："那个筛选条件加一个限制，已通过的不允许再申请。"

用 Cursor 的流程：打开 IDE → 找文件 → 定位代码 → 改逻辑 → 跑测试 → 手动部署。**你是干活的人。**

我打开终端，敲了一句话：

资源申请列表加个校验，已通过状态的不允许重复申请。改完部署到测试环境。

它自己读了代码，改了三个文件，跑通测试，部署上去了。

我回了客户一句"已更新，您刷新看看"。

全程没打开任何编辑器。

---

## 周一早上，上次改到哪了？

我同时管着五个不同客户的项目。周一早上切进某个项目——上次改到哪了？上下文是什么？待办有哪些？

Cursor 不记得。每次打开都是一张白纸。

Claude Code 记得。它有 Memory 系统，每个项目有自己的上下文文件。上次会话结束时自动写交接文档。我说"继续"，它就知道从哪接着干。

这不是功能差异。这是**工具**和**员工**的本质区别。

员工记得昨天的事。

---

## 不会写代码，要交付数据看板

客户要一个月度销售数据看板。我不会前端。

Cursor 的逻辑：你写代码，它帮你补全。问题是——**你得先会写，它才知道补什么。**

Claude Code 的逻辑：你描述需求，它生成整个项目。

做一个月度销售看板，按区域筛选，能导出 Excel，用 ECharts 做图表。

它建了目录，写了前后端，连部署脚本都准备好了。

一个需要你会写代码。一个需要你会说话。

---

## 说句公道话

Cursor 不是差。有些场景它碾压 Claude Code。

&bull; **写一个函数**——Tab 一下代码就出来了。Claude Code 得开终端、输指令、等它思考。杀鸡用牛刀。

&bull; **实时补全**——Cursor 的 inline 补全是真的丝滑，敲着敲着灵感来了 Tab 就行。这种手感 Claude Code 没有。

&bull; **入门门槛**——Cursor 下载即用，5 分钟上手。Claude Code 要装命令行工具，第一次得折腾半小时。

如果你是每天写 8 小时代码的程序员，Cursor 可能更适合你的手。

---

## 那为什么说90%选错了

因为 90% 的人是这么选的：

"我要一个 AI 编程工具" → 搜索 → 看评测 → Cursor 评分高 → 下载 → 选完了。

问题出在第一步。

你把需求定义成了"AI 编程工具"。但你真正要的可能是"让 AI 帮我干活"。

数据说话——

&bull; JetBrains 今年 1 月调了 10000 多个开发者：Cursor 和 Claude Code 采用率**打平，都是 18%**。但 Claude Code 9 个月从 3% 飙到 18%，**翻了 6 倍**。Cursor 增长已经放缓。

&bull; Pragmatic Engineer 调了 900 多个开发者：**71% 经常用 AI Agent 的人选了 Claude Code**。

&bull; 满意度？Claude Code CSAT **91%**，NPS **54**，市场最高。

意思是——用过的人，不回去了。

选工具看功能对比表。选员工看它能不能独立干活。

**90% 的人用选工具的方式，错过了一个员工。**

---

## 一张图帮你选

|  |  |
| --- | --- |
| 你是谁 | 选什么 |
| 全职程序员，每天写代码 | 两个都用。Cursor 写代码，CC 做架构重构 |
| 项目经理 / 产品 / 运营 | Claude Code。你要的是员工不是锤子 |
| 想让 AI 独立干活 | Claude Code |
| 只要代码补全快 | Cursor |
| 预算只够一个 | Claude Code。锤子好买，员工难找 |

---

锤子好买，员工难找。

选哪个不重要。想清楚你要什么才重要。

关注「AI落地手记」

一个人 + AI 管 20 个项目的真实记录
