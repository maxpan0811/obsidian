---
title: "用 HyperFrames 做视频的第二节课"
type: source
created: 2026-06-28
updated: 2026-06-28
source_path: 印象笔记管理工具/用 HyperFrames 做视频的第二节课.md
tags: [evernote, impression]
---
---
title: "用 HyperFrames 做视频的第二节课"
source: evernote
type: note
export_date: 2026-06-28
guid: 0dab7049-f722-448f-9984-0e12ce62dc9b
---

# 用 HyperFrames 做视频的第二节课

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI2NTI4MDczMA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzI2NTI4MDczMA==&mid=2247490075&idx=1&sn=89f0a4a383808398cef2eaad86333c54&chksm=eba1bde1cfc6100f05568b228dbcaef75e16377c291bab3700959c25f6306c70bcaf62865b5e&scene=90&xtrack=1&req_id=1782205385197482&sessionid=1782205475&subscene=93&clicktime=1782206090&enterid=1782206090&flutter_pos=4&biz_enter_id=4&ranksessionid=1782205489&jumppath=WAWebViewController_1782206013871,WAWebViewController_1782206014445,20020_1782206079186,1104_1782206083727&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8vvyNDn1IRQ4rjKWsjoRQBLTAQIE97dBBAEAAAAAAHqkKrdnnsAAAAAOpnltbLcz9gKNyK89dVj0DXKP8dZIHgD5Mb7AvOk+Ab3qMNtPBHSSCdt5bKMud/I0fM8l6XLZRSVx3ASv1UvFaSP8KoQwSBQNugnWHOY+kGBnj3anQO53qYPPQA35eP3zY89obbRLJ/tTB/tFF9TxUAIAqB5kxu+YWU8g/W20SVQyQUSE5LhF++Yxfk8AWoIvjnCGKe4I92bAg9BfHE2Jw0Abgh+SBa90zlh2LBKKh2bUbTZkajCcQQxDrQ4=&pass_ticket=+IVOjiT+vd3k2g/EPdFhoeOZItkXVJDVIpLK6rC90x34TT+kxvNf+mNn/C+8IzYm&wx_header=3)

![](attachments/5ea9ee41eeaa09a6.jpg)

第一节课，我们学习了最简单的方式，使用Codex + HyperFrames 一句话 做视频（[用 Codex + HyperFrames 做视频的第一天](https://mp.weixin.qq.com/s?__biz=MzI2NTI4MDczMA==&mid=2247488702&idx=1&sn=6154930eac3461bd882dbf2d4441cf17&scene=142#wechat_redirect)）。但是，这种场景生成的结果过于简单，只能作为 demo。

接下来，我们向前一步，使用 HyperFrames 预设的工作流来生成视频。

首先，有一些读者反馈，平时常用的是 Claude Code，其实，HyperFrames 也可以和 Claude Code 一起使用。 使用以下命令安装 HyperFrames skill：

npx skills add heygen-com/hyperframes

HyperFrames 预设了一些工作流，/product-launch-video, /website-to-video, /faceless-explainer 等等。

使用以下命令安装 HyperFrames 的全套 skill：

npx skills add heygen-com/hyperframes --all

这样，你可以直接使用这些预设的工作流来生成视频。一句话介绍：

product-launch-video

适合产品发布、SaaS 推广、 功能展示视频。输入是产品 URL 或 brief/脚本，通过 HyperFrames 全流程（抓取品牌资产 → 设计系统 → 脚本 → 配音 → 场景合成 → 渲染）产出成品视频。默认 30-90 秒。

website-to-video

把任意网站做成视频（站点导览、展示、社交短片）。如果你有自己的独立站，可以直接把产品页给它，电商卖家的商品页也可以，SaaS 产品页也可以变成产品 Demo。它会从网站自身的视觉素材出发，7 步协作流程（抓取 → 品牌识别 → 策略 → 故事板 → 配音 → 合成 → 交付）。

faceless-explainer

如果你想做知识科普、概念解释类内容，可以试一下这个，它适合无产品、无网站、无真人出镜的纯文本生成视频。输入可以是文章/笔记/话题/brief，AI 自动生成脚本、配音、并自己设计所有视觉（排版/抽象图形/图表/数据可视化）。5 套预设风格（block-frame / capsule / claude / pin-and-paper / scatterbrain），脚本阶段自动选择。

马上找一篇文章或者用自己的网站试试吧！

Close
