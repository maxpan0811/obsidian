---
name: iphone-kuai-jie-zhi-ling-she-ji-wei-xin-gong-zhong-hao-wen-zhang-dao-ai-ji-qi-ren
type: source
tags: [ios, shortcuts, wechat, ai-bot, automation-design]
source_path: /Users/panbo/Obsidian/程序开发/iPhone快捷指令设计-微信公众号文章到AI机器人.md
---

[摘要]
本文记录了设计iPhone快捷指令（Shortcuts）将微信公众号文章链接发送到微信AI机器人的分析与结论。

用户背景：有一个接入Claude的微信AI机器人，想把公众号文章链接快速发到bot对话里。分析了三种使用场景：看到好文章随手转给bot（场景A）、攒一批文章定期发（场景B）、定时自动推送（场景C）。

方案探索对比了4种路径：Share Sheet直通（Safari分享菜单选bot联系人）——bot不在Share Sheet列表不可行；URL Scheme打开特定对话（weixin://带对话参数）——微信不支持不可行；HTTP API直连bot（绕过微信POST到bot服务）——取决于bot是否有外部API暂不确定；剪贴板+跳微信（复制链接打开微信手动粘贴）——唯一可行方案。

核心限制确认：iOS Shortcuts对微信的能力边界包括不能打开特定微信对话（weixin://不支持对话参数）、不能向指定对话写入消息、AI机器人不在Share Sheet联系人列表、但可以复制URL到剪贴板和打开微信app。

用户的实际工作流在微信内部：公众号文章点"..."复制链接、切到bot对话、粘贴发送。这个流程已经是当前限制下的最优解，Shortcuts只能替代复制这一步。

最终结论：Shortcuts对微信AI机器人场景价值有限。对比各接收方类型发现，普通微信联系人和微信群支持Share Sheet可选，但微信AI机器人不在Share Sheet列表。真正的解法是如果bot有外部webhook/API（HTTP POST到bot-server/send），可以完全绕过微信UI实现全自动。

设计决策记录：Why不做全自动——微信对iOS Shortcuts的限制是平台级硬约束无法绕过；Why不做Safari分享菜单入口——用户实际场景全在微信内不会用Safari打开公众号文章；Why没有创建新skill——是平台限制问题非skill可解决。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/iPhone快捷指令设计-微信公众号文章到AI机器人.md