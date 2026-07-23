---
tags: [★★★★★]
---

# 今天在 OpenAI 社区刷到一组 Codex 配置，可以彻底摆脱彻底摆脱 Codex 的废话连篇，试用了一下后回答清爽很多

---

今天在 OpenAI 社区刷到一组 Codex 配置，可以彻底摆脱彻底摆脱 Codex 的废话连篇，试用了一下后回答清爽很多。

又去官方文档核实了一圈，确定可以放心抄作业。

修改 `~/.codex/config.toml`

配置就这三行：

```toml

model\_reasoning\_summary = "concise" # 简短摘要

model\_verbosity = "low" # 输出极简

personality = "pragmatic" # 务实风格

```

具体每一项管什么，其实文档里面都有详细的介绍。

model\_verbosity输出详细程度

官方取值只有三档：`low | medium | high`。

设成 `low` 之后，Codex 会尽量只给代码和结论，砍掉铺垫、总结、鼓励式话术这些"废话"。

默认值其实是 `medium`，很多人嫌它啰嗦就是没改这项。

model\_reasoning\_summary推理摘要详略

这里要澄清一个常见误解：不管这项怎么设，Codex 展示给你的从来都只是"推理过程的摘要"，完整的思维链本来就不会输出。

这个参数控制的只是摘要本身写多长。

取值有 `auto | concise | detailed | none` 四档，`concise` 就是把摘要压到最短，`none` 则直接不显示推理过程。

personality人格风格

官方样例配置里明确写着可选 `"pragmatic"`、`"friendly"`、`"none"` 三种。

选 `pragmatic` 就是让 Codex 少寒暄、直接干活，风格偏向工程师之间的沟通方式，而不是助手式的客套。

三项组合起来，效果基本就是网上说的那样：

Codex 变得直给，代码和命令为主，不再有大段解释和重复总结。

[Codex App的超绝黄金搭档！GPT 5.6 + Grok build](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518855&idx=1&sn=4d4c0a9f0e30ae25d5ae09713613b2be&payreadticket=HG4FIkO_SV_fRyCXTIy4tEo4Xx975XVjEgx81m34rzLklymTxxLDvOT3puyoZtTepdjpPOQ&scene=21#wechat_redirect)

[您的Codex重置卡已到账，请注意查收！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518870&idx=1&sn=783b1d073f21690bdaeaa1342721b08a&scene=21#wechat_redirect)

[我都用 AI 了，你还跟我谈隐私？](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518874&idx=1&sn=6c7d3ae5c3878d4161eaedac37ffcf23&scene=21#wechat_redirect)

[🔗 原文链接](https://mp.weixin.qq.com/s/QG4keuRbIJddlvdY0sOFYA)

关闭

[📎 在印象笔记中打开](evernote:///view/207087/s1/7431ffe1-3b81-49c5-851e-f2b6691e454c/7431ffe1-3b81-49c5-851e-f2b6691e454c/)