---
title: DeepSeek V4 + Claude Code + Obsidian 搭建知识库
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd...]
source_path: 印象笔记管理工具/保姆级教程：DeepSeek V4 + Claude Code+ Obsidian搭建个人知识库.html
tags: [deepseek, claude-code, obsidian, knowledge-base, tutorial]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "保姆级教程：DeepSeek V4 + Claude Code+ Obsidian搭建个人知识库"
source: evernote
type: note
export_date: 2026-06-25
guid: 308aaba8-94bb-44a2-a864-04a479257c7e
---

# 保姆级教程：DeepSeek V4 + Claude Code+ Obsidian搭建个人知识库

原文链接: [https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd...](https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd630c630fa04c71d50183d68fcc13c849ff6ac4b5a1be1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1779622957_1&req_id=1779346571881990&scene=169&mid=2247499086&sn=eaae27c36c9085179a3704e440147ad1&idx=1&__biz=MzkyMTI3Mjc2MQ==&sessionid=1779624830&subscene=200&clicktime=1779624974&enterid=1779624974&flutter_pos=5&biz_enter_id=5&jumppath=20020_1779624916986,1104_1779624950003,20020_1779624956074,1104_1779624967973&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8H+vH5sKjkvY6pIAyEqScBLTAQIE97dBBAEAAAAAAA7mEkxeODwAAAAOpnltbLcz9gKNyK89dVj0PTfr+3VoTp5voLaiHRZTtbPFuuCIx9IoMryp6wd6M8eXejmfAJJXQpG/NMeeBtU+biRKl0BITZAsZqI8rMO1vB4/JHD6oGbOKk6rf0w7sh1ZCkQodTST492m/dm1XlPe325UlX9rEwAzlpHc1ibcOEXQsgIu+YpjNBe2n9cWlnPcz0lqsr0n6i+SY34uJ8fQYipKb16KALcqfuT0X2WuhyEoXyZ5mnMPBwLke/s=&pass_ticket=exDE/Rrctj6w0/LEDYYOGuAHmrOcQIABFMS4z0hsNmgn12lCixIC+ACnwi5tMWTY&wx_header=3)

Original库森 程序员库森

DeepSeek V4 刚出的时候我就盯上了，文字能力对标 Claude Opus 4.6，百万 token 价格不到 Claude 的十分之一，性价比直接拉满。

我通过DeepSeek V4+  Obsidian + Claude Code建立了知识库，让 AI 直接读我的文件、搜笔记、跨文件关联回答问题，发现效果很不错。

今天就教大家怎么接入，0 基础四步走，跟着做就行 。

## **第一步：装 Obsidian**

官网下载安装包，Mac 和 Windows 都有，免费的，双击装上。它是本地 Markdown 笔记软件，所有文件存你自己电脑上，不用担心数据安全。插件生态非常强大，今天用到的 Claudian 就是其中一个。

![](attachments/a4c6b7b73a587b7c.png)

---

## **第二步：装 Claudian 插件**

Claudian 把 Claude Code 嵌进 Obsidian，笔记仓库直接变成 AI 工作目录，能读能写能搜索。

先打开 Obsidian 设置（左下角齿轮图标），找到「第三方插件」，把安全模式关掉。

![](attachments/992ae2e404b81c7d.png)

---

关闭安全模型

![](attachments/e5204c4438e26049.png)

点开社区插件市场

![](attachments/b1cf3bfd9b3e4f61.png)

---

Claudian 还没上官方插件市场，需要通过 BRAT 装。在社区插件里搜 BRAT，安装启用。

![](attachments/788ad3261040d45d.png)

然后回到设置找到 BRAT，点 Add beta plugin，输入 Claudian 的仓库地址就能装上。

![](attachments/36e0effcbdbe455b.png)

---

输入 claudian 的地址

![](attachments/a1a1b7418110d118.png)

<https://github.com/YishenTu/claudian>

最后回到第三方插件列表，把 Claudian 开关打开就好了。

![](attachments/9cd6d4bf3df41842.png)

---

## **第三步：装 Claude Code + 配置 DeepSeek V4**

先装好 Node.js（Mac 终端跑 brew install node，Windows 去官网下安装包），然后一行命令装 Claude Code，国内用 npm 镜像源也能装。

![](attachments/bf77081390f2c63c.png)

然后用 CC Switch 桌面工具配置 DeepSeek V4 做后端。安装后新建配置，供应商选 DeepSeek，粘贴 API Key，填好模型名称，保存启动就行。

这部分我之前写过超详细的图文教程，包括怎么拿 API Key、CC Switch 每一步怎么配、踩坑细节全都有，看我主页那篇「DeepSeek 接入 Claude Code」就行，已经配过的直接下一步。

---

cc switch 的安装配置（已经配过的直接下一步）

先去 GitHub 下载一个桌面工具叫 CC Switch，专门管理 Claude Code 的供应商配置，不用记环境变量，新手友好。

macOS 选 dmg，Windows 选 msi 安装包。

![](attachments/2db3bded56f1f3c6.png)

安装运行后，点 "+" 新建配置。供应商选 DeepSeek，

![](attachments/b6df1e6821e85e68.png)

---

然后粘贴deepseek 开放平台拿到的 API Key。

![](attachments/61f493fb26b4e9f1.png)

---

进行配置，添加两个模型

deepseek-v4-pro[1m] 做主模型，

deepseek-v4-flash 做轻量任务和子代理。

名称严格按图里来，点添加保存。

![](attachments/1827775a359aa66d.png)

---

点启动，配置就生效了 🎉

![](attachments/ed5dc8fd42f87c46.png)

## **第四步：配置路径，开始用**

终端输入 where claude 拿到路径，粘贴到 Claudian 设置里就行。

![](attachments/63793f986ecba698.png)![](attachments/bd0aa5ddadddef81.png)

---

找到 Claudian 图标，点开就能跟 AI 对话了。

![](attachments/5f5dba5d17dcf2b5.png)

---

**实际体验**

让它整理知识库内容、回答问题，它是真的在你本地文件里搜索关联的，不是瞎编。跨文件检索、知识关联、内容总结全能搞定，比单纯搜索强太多了。

![](attachments/7ee817928b7ce11b.png)![](attachments/43c915af481cc9ff.png)

---

整套方案搭下来，Obsidian 管数据、Claudian 接 AI、DeepSeek V4 省钱还好用。不管是整理学习笔记、管项目文档还是搞内容创作，都非常趁手。

现在搞个人 AI 知识库门槛真的低了，本地加 AI，数据安全又智能，是真的香。
