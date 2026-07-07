---
title: "claude-howto：Claude Code 从入门到精通官方教程，5.9k star 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/claude-howto：Claude Code 从入门到精通官方教程，5.9k star 2.md
tags: [evernote, impression, yinxiang]
---

# claude-howto：Claude Code 从入门到精通官方教程，5.9k star

---

原文链接: [https://mp.weixin.qq.com/s?chksm=ffea2aa9c89da3bfd17696ce74546df...](https://mp.weixin.qq.com/s?chksm=ffea2aa9c89da3bfd17696ce74546df1c4eece0bb9fcf0baa74bee43c436ed287b138bf5228c&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1775479208_1&req_id=1775479208077827&scene=169&mid=2247484153&sn=8de77143da7deea65ae3b050a0cb8cda&idx=1&__biz=MzYyMTAzNTgzOQ==&sessionid=1775478910&subscene=200&clicktime=1775479672&enterid=1775479672&flutter_pos=14&biz_enter_id=5&jumppath=30024_1775479639362,1104_1775479646663,30024_1775479650983,1104_1775479653463&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004632&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/LfYJnolR0TwsaBSuBiFxBLTAQIE97dBBAEAAAAAADkmDtjmDkUAAAAOpnltbLcz9gKNyK89dVj0/roJPUJSEAoUaq1kYFa3xnmGEIE4e10WofPOPmF0ojed7HIz3h0C+4HeST3RF21Z/yNkYh8m+sJe9PwRpd9hnLeSuqYJhq/DI8mYfSi+OFGgfQsFNU4fmqhTTepQ+pIVAf9IUOsilyZ8a4PXsWf8ngZOO3vCu3gjt6N1mo7Svuk63oXRfz9Cxh+kWal8D38Qi/12K9jRPD4gfLjoAonaJUWOauTXuLmGQNg9GIw=&pass_ticket=r9i0jyTxKiSSXz6ebT+yhwaXLdu0+VGAySAHUBBY9IpQ0ukWCoXVXrSzMdAS97uf&wx_header=3)

Original结构派AI 结构派 AI

Claude Code 装完不知道怎么玩？这个开源项目给你准备好了循序渐进的学习路径和复制就能用的模板。

目前项目已经收获 5.9k+ GitHub stars，最近更新到v2.2.0，完美适配最新 Claude Code 2.1+。

![](.evernote-content/01861756-4694-4298-BCAB-E5501B4D38AC/B93736EB-2434-4194-B8A1-34B6D99C15E4.jpg)

---

为什么需要这个教程

很多人装完 Claude Code 只会聊天，90%的功能根本用不上。

官方文档只列功能，不说怎么组合起来干活。

- 你知道有 slash 命令，但不知道怎么把 slash + 记忆 + 子代理拼成自动化工作流

- 不知道学习路径：应该先学 MCP 还是 Hooks？技能还是子代理？

- 例子都是 Hello World，没人给你生产环境能用的代码审查模板

claude-howto 解决的就是这个问题：它不是功能列表，是\*\*带图、带模板、带学习路径的实战教程\*\*，从入门到高级，11-13 小时学完直接变成 Claude Code 高手 。

---

它到底提供了什么

|  |
| --- |
| 核心亮点    ✅结构化学习路径  从入门到高级，10个模块，循序渐进，每个模块学完就能用    ✅复制就能用的模板  slash 命令、CLAUDE.md 记忆、技能、子代理、MCP 配置、Hooks 全部给你写好，直接 copy 到项目里    ✅Mermaid 流程图  每个功能都给你画了内部流程图，讲明白原理，不只教你怎么用，还教你为什么这么用    ✅自测 quizzes  每个模块学完可以做题，直接定位知识盲区，个性化推荐学习路径    ✅保持更新  每个 Claude Code 版本更新都会同步，当前适配 Claude Code 2.1+，支持 Sonnet 4.6 / Opus 4.6 |

|  |
| --- |
| 10个模块全覆盖    1.Slash Commands— 自定义快捷命令  2.Memory— 跨会话持久化上下文  3.Skills— 可复用的自动化能力  4.Subagents— 专业化分工子代理  5.MCP Protocol— 外部工具接入  6.Hooks— 事件驱动自动化  7.Plugins— 打包完整解决方案  8.Checkpoints— 会话快照和回滚  9.Advanced Features— 高级特性配置  10.CLI Reference — 命令行完整参考 |

---

五分钟就能用上

操作非常简单，克隆项目就能开始学，复制粘贴就能用模板：

|  |
| --- |
| `# 1. 克隆项目`  git clone https://github.com/luongnv89/claude-howto.git  cd claude-howto    `# 2. 复制第一个 slash 命令`  mkdir -p /path/to/your-project/.claude/commands  cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/    `# 3. 在 Claude Code 里直接用`  /optimize    就是这么简单。15分钟就能搞定基础 setup，拿到立即可用的提升。    完整一分钟 setup 流程：  - 复制所有 slash 命令  - 添加项目记忆  - 安装第一个技能 |

---

功能组合例子：全自动代码审查

claude-howto 最牛的地方是教你把多个功能拼起来解决实际问题。

比如自动代码审查这个工作流：

1. Slash 命令 /review-pr

2. 加载项目编码规范记忆

3. 通过 MCP 获取 PR 代码

4. 自动委派给 code-reviewer 子代理

5. 最后给你汇总审查结果

整个流程不用人工干预，交给 Claude 全自动搞定。

类似这样可直接复制的生产级模板，项目里给你准备好了一大堆。

---

适合谁学

- 初学者：有清晰学习路径，从 0 开始，不用自己摸索

- 已经在用的人：自测帮你找出知识盲区，把没用上的功能用起来

- 团队：可以直接 fork 改成自己团队的 Claude Code 规范

按水平分了三个级别，直接对应起点：

|  |  |  |  |
| --- | --- | --- | --- |
| 级别 | 你能做到 | 推荐起点 | 总耗时 |
| Beginner | 会启动 Claude Code 聊天 | Slash Commands | ~2.5h |
| Intermediate | 会用 CLAUDE.md 自定义命令 | Skills | ~3.5h |
| Advanced | 会配置 MCP 和 Hooks | Advanced Features | ~5h |

---

最后说两句

Claude Code 最大的魅力就是可以把你的开发流程自动化，从编码到审查到部署，AI 可以帮你搞定大部分重复工作。

但大部分人只用到了它 10% 的能力，这套教程帮你把剩下 90% 挖出来，真正做到 10x 效率。

项目 MIT 协议，完全免费，可商用。现在去克隆下来，15 分钟就能拿到第一个可复用的模板：

项目地址：luongnv89/claude-howto

关注我们，获取最新AI工具与开源观察 🤖

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=ffea2aa9c89da3bfd17696ce74546df1c4eece0bb9fcf0baa74bee43c436ed287b138bf5228c&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1775479208_1&req_id=1775479208077827&scene=169&mid=2247484153&sn=8de77143da7deea65ae3b050a0cb8cda&idx=1&__biz=MzYyMTAzNTgzOQ==&sessionid=1775478910&subscene=200&clicktime=1775479672&enterid=1775479672&flutter_pos=14&biz_enter_id=5&jumppath=30024_1775479639362,1104_1775479646663,30024_1775479650983,1104_1775479653463&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004632&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/LfYJnolR0TwsaBSuBiFxBLTAQIE97dBBAEAAAAAADkmDtjmDkUAAAAOpnltbLcz9gKNyK89dVj0/roJPUJSEAoUaq1kYFa3xnmGEIE4e10WofPOPmF0ojed7HIz3h0C+4HeST3RF21Z/yNkYh8m+sJe9PwRpd9hnLeSuqYJhq/DI8mYfSi+OFGgfQsFNU4fmqhTTepQ+pIVAf9IUOsilyZ8a4PXsWf8ngZOO3vCu3gjt6N1mo7Svuk63oXRfz9Cxh+kWal8D38Qi/12K9jRPD4gfLjoAonaJUWOauTXuLmGQNg9GIw=&pass_ticket=r9i0jyTxKiSSXz6ebT+yhwaXLdu0+VGAySAHUBBY9IpQ0ukWCoXVXrSzMdAS97uf&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3cdc8223-a832-4d73-9d14-d59c669b2735/3cdc8223-a832-4d73-9d14-d59c669b2735/)
