---
title: 我把Claude Code装进了微信，也当了一把审计合伙人的感觉
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/我把Claude Code装进了微信，也当了一把审计合伙人的感觉.html
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "我把Claude Code装进了微信，也当了一把审计合伙人的感觉"
source: evernote
type: note
export_date: 2026-06-27
guid: eccff49d-62d0-46f5-b115-77c305568746
---

# 我把Claude Code装进了微信，也当了一把审计合伙人的感觉

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0MjgxMzg1Mw==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzI0MjgxMzg1Mw==&mid=2247505526&idx=1&sn=bd3ce30d035cc9cba4830f1be4533f05&chksm=e83446740aa6f71aa7a5a66189e9d7ab65875ff8373932b10b3582f230bebadb8102dea0fddb&scene=90&xtrack=1&req_id=1778317482930140&sessionid=1778317478&subscene=93&clicktime=1778317521&enterid=1778317521&flutter_pos=6&biz_enter_id=4&ranksessionid=1778317482&jumppath=1001_1778317477215,1104_1778317478849,20020_1778317482335,1104_1778317498270&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004922&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQP0018/nC3iAADVxfX/Fk+xLVAQIE97dBBAEAAAAAAJ8FOdSpR7QAAAAOpnltbLcz9gKNyK89dVj0AagFNWG1Ni81YGdgC7f5VZmfBB8rTuxmrjQK1Opu1ddrCz2ltAk4TPPC2RKGgpvybiFnlrIvJQS7N2JFTOMsFrGKtngQ7A3eYB0d/pHkT6WdOfq0cAQJedJ6VQGFqdt5jbw3NQvdJjfoMlR9vw4RHTvWq63RyN27pAQOGRll6/iogA2Wl91zuZZn0cfHiOJRM3zCGe2ygQ7n3EFxGOhYv3BrdR0zj67+BvWb4XjFtw==&pass_ticket=OzhIhnnT7WwdA03ljlBLJIUXv3PfcOPpSjZyHeoztCXL9F0I/mWqd7z8xgcFXcae&wx_header=3)

Originalnigo逆行的狗

![](attachments/a00793fd84af532f.png)

当你在地铁上用微信说一句“帮我下载万科 2025 年审计报告”，你的“助理”就默默去干了。

## 从龙虾说起

前段时间 OpenClaw（龙虾）很火，很多同行在群里讨论。我当时看了下，觉得本质就是 AI Agent 加了个通讯壳子——用微信发消息调用 AI 而已。作为一个搞审计的，我不需要花哨的东西，能干活就行。所以没装。

但我一直在用 Claude Code 写代码、处理数据。说实话，用它清洗底稿数据、批量处理报表，效率提升不是一点半点。

唯一的痛点是——**得坐在电脑前才行**。

## 意外发现

今天正愁没有公众号素材，

发现一个叫 **cc-connect** 的开源项目，能把 Claude Code 桥接到微信上。关键是：不需要公网 IP，不需要服务器，本地跑就行。

我把项目地址给 claude code，它直接全部帮我安装好，中间我只微信扫了一次二维码给它：

![](attachments/bb6b82fba2fae1cb.png)

装好之后，我的微信里就多了一个“审计助理”。

我试了一下，用语音跟它说“帮我下载万科 2025 年审计报告”。过了一会儿，它就把文件发过来了。

![](attachments/8cb6710b5c92dd5b.png)

![](attachments/957c4e9ba5ee1271.png)

![](attachments/25833f4edab857ae.png)

全程在微信里完成，从发指令到收到结果，像是在给助理布置工作。

## 审计师的“合伙人”体验

做审计这行，最缺的就是人手。尤其是年报季，恨不得把自己掰成几瓣用。

现在我也体验了把合伙人的感觉：

- 通勤路上，发条微信让它帮我查某个公司的公告
- 出差途中，让它整理前一天的数据
- 晚上加班，让它先把底稿格式调好，我再检查

它不会抱怨加班，不需要工位，也不需要社保。

## 写在最后

最近田老师用 claude code 把审计计划阶段的活都写得差不多了，

有了这个 cc-connect 能力，

以后微信说个公司名称，发一点资料，

整个计划阶段就做完了。

离谱…

---

https://github.com/chenhg5/cc-connect
