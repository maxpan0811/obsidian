---
name: claude-code-ch5-mcp
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（五）（教不会我吃民法典！）：MCP—连接外部工具.md

updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "法律人的Claude Code教程（五）（教不会我吃民法典！）：MCP—连接外部工具"
source: evernote
type: note
export_date: 2026-06-27
guid: b1d78811-8ec8-4cef-a5c3-211db305a42b
---

# 法律人的Claude Code教程（五）（教不会我吃民法典！）：MCP—连接外部工具

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485821&idx=1&sn=f3007a9c7616a110bc68f02ad6c9eaea&chksm=c2547aa0f523f3b6b11cc138cd4f7153bd31e6594f0416e399072eaf4a310a3254999485ec63&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQfwpD3EUGxdgfjuWBwm2kDBLVAQIE97dBBAEAAAAAADsQBoLIrMgAAAAOpnltbLcz9gKNyK89dVj09MCc927NRm9FNDI0aeF5HFyjzlvWgSVQC0z6hOiGjCx7LOdg6DMBub2X85cT+9W3HmaFuUhDapwzSfLutO3VngbBJzX8Eg5i/3l5LQefa17IkKY2gXduL9wZ1yG2RO/tmEphTGUKX1L3EE2A0faUjnUERezbq6CTJ/x3q1w4v9w26wi9QK08nVgNyl36DrFwxsO22xniWWqrD0msJhP5jeTxnJymQRU1k7Q7xCS28g==&pass_ticket=v6//kcViVHJuoUM2hbNjYr9SLZCkm6oWzkpSsJJ2CDy23DN/ZacgW3lRnmmTHmep&wx_header=3)

# 法律人的Claude Code教程（五）（教不会我吃民法典！）：MCP—连接外部工具

Original积成 智律积成

上一篇我们学了怎么用 CLAUDE.md 给 Claude Code 写"岗位说明书"，没看过的同学赶紧补补课：

相信你已经学会了通过配置 CLAUDE.md 把 Claude Code 训练成你的工作助手。

我们还是以合同审核为例。

通过 CLAUDE.md，你的 Claude Code 已经知道了你的审核要求和步骤，基础审核、业务条款审核、法律条款审核，最后出综合意见。

但有一个关键的审核环节它做不到：**主体审核**。

如果是你在审合同，看到了合同里的公司名称，你会怎么做？

打开企业信息查询网站，查一下：

- 公司名称是不是写对了
- 公司状态是不是正常经营

但 Claude Code 做不到。

它可能会靠猜，根据模型训练时学到的知识来判断，但数据可能早就过时了。也可能联网搜一下，但搜索结果零散，准确性无法保证。

![](attachments/9a5ebb4ec5e5c887.png)

你心想：**如果 Claude Code 能直接去企业信息查询网站查一下就好了。**

当然可以。

这就是 MCP。

---

## 先看效果

先不解释原理，直接看配好之后是什么体验。

直接指令。

![](attachments/0a92507604627cbf.png)

Claude Code自动调用MCP进行查询。

![](attachments/25bb88b4b3fee05c.png)

反馈查询和核对的结果。

![](attachments/56469a0c4af9591c.png)

当然，MCP可能反馈的结果不准确，我们换一个公司查询以验证服务正常运行。

![](attachments/dee672269303fbc8.png)![](attachments/e6fcfa6ec50f4c24.png)

看到了吗？

**Claude Code 不再是只会读文件中的内容，它可以自己出去查资料了。**

真棒！

---

## MCP 到底是什么？

**MCP = Model Context Protocol（模型上下文协议）**

先说人话版结论：

***MCP 就是一套标准接口，让 Claude Code 能调用外部工具和数据源。***

![](attachments/401ead898ab16469.png)

### 用张无忌来理解

前四篇教程下来，你的 Claude Code 已经：

| 教程 | 掌握的能力 | 武侠比喻 |
| --- | --- | --- |
| 教程一 | 安装配置 | 拜入师门 |
| 教程二 | 基本操作和命令 | 扎马步、练基本功 |
| 教程三 | 工作模式和权限管理 | 学习内功心法 |
| 教程四 | CLAUDE.md 与上下文管理 | 调息吐纳，稳固根基 |

现在张无忌九阳神功练成了，内力深厚。

但光有内力没有武器，面对千军万马还是要肉搏。

MCP，就是让张无忌拥有了倚天剑屠龙刀（外部兵器）。

后面教程还会继续"升级"：

- **教程六** Skill/Command/Plugin → 太极拳法（学会特殊场景的具体招式）

不过那是后面的事。今天先把兵器库打开。

### 它是怎么工作的？

不需要理解技术细节，但知道基本流程有助于你判断什么时候该用、安不安全：

你：审查这份合同，核查一下主体信息
  ↓
ClaudeCode：读完合同，发现需要查"XX科技有限公司"
  ↓
ClaudeCode → 调用 MCP 工具（企业信息查询）
  ↓
MCP 服务（你电脑上运行的小程序）→ 去企业信息服务查询
  ↓
查到结果 → 返回给 Claude Code
  ↓
ClaudeCode：把查询结果整合进审核意见

两个关键点：

**你可以同时装多个 MCP**，查企业的、搜网页的、管文件的，各管各的，互不干扰。

**Claude Code 会自动判断什么时候用哪个**，你不需要手动指定"去调用XXX"，它自己知道。

---

## 怎么装？用起来才是关键

知道 MCP 是什么之后，最重要的是：**装上，用起来。**

### CC-Switch：点点鼠标就搞定（推荐）

如果你是从教程一过来的，应该已经安装了 CC-Switch。

配置 MCP 就是点点鼠标的事：

![](attachments/7fd4661aed23a07a.png)![](attachments/3f96346aed3e5ae1.png)

感谢 Jason 和开源社区！CC-Switch 让不写代码的法律人也能轻松管理 MCP。

*CC-Switch 的安装可以回过头看下教程一，也可以去 GitHub 上看：https://github.com/farion1231/cc-switch*

### 命令行：给想多了解一点的你（可以不学）

如果你还没装 CC-Switch，或者想知道底层发生了什么，命令行也就三句话的事：

bash

*# 添加一个 MCP 服务器*
claude mcp add <名称> -- <启动命令> [参数...]
*# 查看已安装的 MCP*
claude mcp list
*# 删除一个 MCP 服务器*
claude mcp remove <名称>

装完之后，重启 Claude Code 就生效了：

### 还有更简单的方法吗？

有！

如果你找到了一个想安装的MCP。

比如这个“Howtocook”。

![](attachments/89dba4ecd7433fa2.png)

把配置复制下来告诉Claude Code。

当然，如果涉及到API Key的，还需要自备。

完成！

![](attachments/cb368f48c412b62f.png)

### 装好之后怎么用？

**什么都不用做。**

装好之后，你正常跟 Claude Code 对话就行。它会自动判断什么时候需要调用 MCP 工具。

---

## 法律人装哪些 MCP？

先说实话：**目前专门为中国法律场景开发的 MCP 有，但还不多，而通用型 MCP 在法律工作中已经非常实用。**

以下是一些值得关注的MCP

| 名称 | 功能 | 评价 |
| --- | --- | --- |
| 企查查 MCP或同类选择（非常多） | 企业信息查询，知识产权、诉讼、工商、执行等都能查 | 一般都是付费的，但是对工作效率提升效果非常明显 |
| 法宝MCP | 查询案例和法规 | 基于北大法宝数据库，可以先去法宝MCP官网申请一个月试用 |
| 高德/百度地图MCP | 地理信息服务 | 对于工作和生活都很有用，可用于规划行程，初步调查侵权门店等 |
| Arxiv 论文助手 | 搜论文、解读论文 | 持续学习必备 |
| AntV 可视化图表 | 生成可视化图表 | 不想做自己的可视化SKill，可以选择这个 |
| 麦当劳 | 点餐、领券 | 1. 工作再忙别忘吃饭；2. 别忘了领券，8090也有自己的鸡蛋要领 |
| context7 | 获取最新代码和文档 | Vibe Coding神器 |

好的MCP非常多，但是适合自己的才是最好的，推荐几个网站可以查询MCP：

- **ModelScope MCP 广场**：https://modelscope.cn/mcp
- **阿里云百炼 MCP 广场**：https://bailian.console.aliyun.com/cn-beijing/?tab=app#/mcp-market
- **MCP.SO**：https://mcp.so/

---

## 安全问题必须说清楚

法律人对数据安全天然敏感。

这部分不长，但很重要。

### 数据怎么流动的？

![](attachments/d12331b2b2d385a6.png)

你的提问
  ↓
ClaudeCode → API（云端处理）
  ↓
Claude 决定调用 MCP
  ↓
MCP 服务（本地运行）→ 去外部获取数据
  ↓
数据返回 → 作为上下文发送给 API
  ↓
Claude 处理后回复你

**一句话概括：MCP 拿回来的数据，最终会和你的对话一起发送到 API 云端。**

### 哪些能查，哪些不能？

| 场景 | 能不能用 MCP | 原因 |
| --- | --- | --- |
| 查公开法规、司法解释 | ✅ 放心用 | 本来就是公开信息 |
| 查公开的工商信息 | ✅ 放心用 | 公示信息，无保密义务 |
| 查公开的裁判文书 | ✅ 放心用 | 公开信息 |
| 查律所内部案件数据库 | ⚠️ 慎重 | 客户信息可能通过 API 传输 |
| 查包含客户个人信息的系统 | ❌ 不建议 | 涉及个人信息保护和律师保密义务 |

***MCP 获取的数据 = 你手动粘贴给 Claude Code 的数据，安全等级相同。****你不会把客户身份证号粘贴给 Claude Code，同样也不要让 MCP 去查。*

---

## 如果你还有更多想法

也许你已经在想：

- "我们律所有自己的案件管理系统，能不能让 Claude Code 直接查？"

这些都是可以实现的。MCP 服务器本质上就是一个程序，声明自己能提供什么工具，等 Claude Code 来调用。

如果你的团队有技术人员，可以参考 MCP 开发文档[1] 自建。如果你自己想尝试，其实也可以直接让 Claude Code 帮你写一个，毕竟，写代码是它的老本行。

期待你的创新🎉

---

## 这一篇讲了什么？

**核心概念：** MCP 是一套标准接口，让 Claude Code 能调用外部工具，就像给张无忌配了兵器库。MCP 服务器跑在你自己电脑上，Claude Code 自动判断什么时候调用。

**实操要点：** 推荐用 CC-Switch 管理，也可以用 `claude mcp add` 命令行安装。先装几个常用的，用起来再说。

**安全原则：** MCP 获取的数据 = 你手动粘贴给 Claude Code 的数据，安全等级相同。公开信息放心查，客户敏感信息别让 MCP 碰。

---

## 下一篇预告

**教程六**：Command、Skill 与 Plugin

*把你的经验封装成"一键操作"，从个人快捷指令到团队能力包*

MCP 解决的是"Claude Code 能接触到什么工具"，Command/Skill/Plugin 解决的是"Claude Code 怎么把这些工具组合成你想要的工作流"。

兵器有了，下一篇学招式。

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。

参考链接

[1] MCP 开发文档: https://modelcontextprotocol.io
