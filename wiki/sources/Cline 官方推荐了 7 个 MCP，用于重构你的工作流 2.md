---
title: Cline 官方推荐了 7 个 MCP，用于重构你的工作流 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Cline 官方推荐了 7 个 MCP，用于重构你的工作流 2.md
tags: [evernote, impression, yinxiang]
---

# Cline 官方推荐了 7 个 MCP，用于重构你的工作流

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI1MjU1MjU0NA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzI1MjU1MjU0NA==&mid=2247489746&idx=1&sn=e8e992b6d02758c4aeda4a6391ca9890&chksm=e865d11a8821e952932c6a8edfd6aa6de31388c901912fc2f08083b64fd11fd95a5051b9a33f&mpshare=1&scene=24&srcid=05178WBh0ai4UrsBpnQVKFrn&sharer_shareinfo=e23e89b03a49a03e4c8ce453ce662783&sharer_shareinfo_first=e23e89b03a49a03e4c8ce453ce662783&clicktime=1778992796&enterid=1778992796&ascene=14&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQKMEHPlgN1XSSUPvKdTOdlRLTAQIE97dBBAEAAAAAAE/BJcL5FiYAAAAOpnltbLcz9gKNyK89dVj0t0FSbLdjBKvtLyX9KzdQPuwmpOE2TTI52j+QQJYMwyA996AERkxm+ScbZ1QXzoqMZfydf0BJBgWNMhFzNmN+s63fwE0tH7bXjGsIDbZNiHWv52SCFV+21+zBrbUY46cx2G0PkBwRQe6bNgLW8Ct6AckZKBzdj3PMOv7xczchabYaLhwj1/dD1S3bnpfaOT1IdnOI19hxrH0fhrblV0GlE1LsDBKoXwX5yIUn1W0=&pass_ticket=B7ojbRd2JKa0Js+cfBkTSYfDiV/5oa+u+mXTB5QNm8+c7otqKvPsCmgNskFkiIST&wx_header=3)

Original雨飞 雨飞AI笔记

**点击上方🔺公众号🔺关注我✅**

你好啊，我是雨飞，见字如面。感谢阅读，期待我们下一次的相遇。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/DA25273A-8182-49EA-8C06-11D0D8308F2C.png)

最近 Cline 官方更新了自己的 blog，在文中提到了 7 个 关键的 MCP 服务，用于改善和提升在 Cline 中的使用体验。这些 MCP 能够显著的提升 Cline 的使用体验，可以让其从一个编程 Agent 转变为真正的多功能开发中心。

MCP 的概念，我们以前已经提过很多次了，有不懂的，可以翻下以前的文章。我们这里简单介绍下 MCP。 MCP 有客户端、服务端和协议三部分组成，MCP Server，它们是独立的应用，通过标准化协议向客户端（Cline等）暴露自己所拥有的工具或者特定数据资源。我们可以根据自己的需求去连接任意 MCP Server。

这 7 个 有价值的 MCP 分别是，

1、网络交互和搜索 

Hyperbrowser、Firecrawl：爬取最新的网站，可以进行自动化浏览器交互，并输出干净的 HTML 或者 Markdown。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/540D5959-44F9-4E75-BF20-3A56AD510934.png)

地址： 

Hyperbrowser：https://github.com/hyperbrowserai/mcp 

Firecrawl：https://github.com/mendableai/firecrawl-mcp-server

Perplexity：搜索复杂的技术问题，并获取答案。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/EBB4CFF7-4E8C-4082-8E51-6DD5F55D7E19.png)

地址： https://github.com/ppl-ai/modelcontextprotocol

2、前端开发

21st Dev Magic UI：根据自然语言生成漂亮的 UI 组件，并直接将代码插入到项目中。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/08B3FD0A-2E64-470E-A26A-7E45D58A88A4.png)

地址： https://github.com/21st-dev/magic-mcp

3、规范化内容和数据集成

Markdownify：将各种文件类型和网页内容转换为干净的 Markdown。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/09B23E5A-8859-44E8-BBF5-E7EF1AE76E80.png)

地址： https://github.com/zcaceres/markdownify-mcp

4、音乐、生成式3D领域

ableton-mcp：通过自然语言生成音乐创意，设置音轨，并且可以控制播放。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/62348BF1-82E9-40A7-BF88-E34C9CED96E5.png)

地址： https://github.com/ahujasid/ableton-mcp

Blender-mcp：可以执行复杂的 Python 脚本，利用polyhaven 快速填充场景，或者从文本描述中利用 hyper3d 生成模型。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/4CE42486-3BA9-47E6-BFDD-966DAEDF0252.png)

地址：https://github.com/ahujasid/blender-mcp

在 Cline 中使用 MCP 的优势

1）减少上下文切换，可以在同一个界面中编码，访问外部工具和数据

2）更快的迭代：快速进行研究，生成代码，整合内容和自动化

3）更多专业功能：利用 MCP 可以完成网页爬取，UI生成，数据转换等复杂工作。

4）自定义工作流：构建符合自己特定需求和项目的开发流程

如果你在 Cline 中进行使用，可以在 MCP 市场中一键下载上面的服务，就不需要额外进行安装了。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/4C0DB3A0-4584-40CD-96ED-26AA9CCE80BB.png)

其他关于 Cline 的使用技巧，见文章，[Cursor高手进阶|Cline与MCP集成指南，让你的AI更强大](https://mp.weixin.qq.com/s?__biz=MzI1MjU1MjU0NA==&mid=2247488538&idx=1&sn=35f5e13d2802313b15af82bcafa894c7&scene=21#wechat_redirect)

有想一起交流学习 Cursor 的可以添加下方的微信，备注「编程」，邀你一起学习。

![](.evernote-content/79B6387D-736C-4B5C-BA44-B94A8F5888DF/25C3E4C4-950A-482C-AF3B-9A860AB43F9E.png)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI1MjU1MjU0NA==&mid=2247489746&idx=1&sn=e8e992b6d02758c4aeda4a6391ca9890&chksm=e865d11a8821e952932c6a8edfd6aa6de31388c901912fc2f08083b64fd11fd95a5051b9a33f&mpshare=1&scene=24&srcid=05178WBh0ai4UrsBpnQVKFrn&sharer_shareinfo=e23e89b03a49a03e4c8ce453ce662783&sharer_shareinfo_first=e23e89b03a49a03e4c8ce453ce662783&clicktime=1778992796&enterid=1778992796&ascene=14&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQKMEHPlgN1XSSUPvKdTOdlRLTAQIE97dBBAEAAAAAAE/BJcL5FiYAAAAOpnltbLcz9gKNyK89dVj0t0FSbLdjBKvtLyX9KzdQPuwmpOE2TTI52j+QQJYMwyA996AERkxm+ScbZ1QXzoqMZfydf0BJBgWNMhFzNmN+s63fwE0tH7bXjGsIDbZNiHWv52SCFV+21+zBrbUY46cx2G0PkBwRQe6bNgLW8Ct6AckZKBzdj3PMOv7xczchabYaLhwj1/dD1S3bnpfaOT1IdnOI19hxrH0fhrblV0GlE1LsDBKoXwX5yIUn1W0=&pass_ticket=B7ojbRd2JKa0Js+cfBkTSYfDiV/5oa+u+mXTB5QNm8+c7otqKvPsCmgNskFkiIST&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8a5e85ac-cb45-4114-9919-8ec0f95739d1/8a5e85ac-cb45-4114-9919-8ec0f95739d1/)
