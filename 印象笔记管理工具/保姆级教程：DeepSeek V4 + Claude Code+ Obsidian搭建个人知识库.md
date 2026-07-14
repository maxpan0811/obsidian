---
tags: [★★★★★]
---

# 保姆级教程：DeepSeek V4 + Claude Code+ Obsidian搭建个人知识库

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd...](https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd630c630fa04c71d50183d68fcc13c849ff6ac4b5a1be1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1779622957_1&req_id=1779346571881990&scene=169&mid=2247499086&sn=eaae27c36c9085179a3704e440147ad1&idx=1&__biz=MzkyMTI3Mjc2MQ==&sessionid=1779624830&subscene=200&clicktime=1779624974&enterid=1779624974&flutter_pos=5&biz_enter_id=5&jumppath=20020_1779624916986,1104_1779624950003,20020_1779624956074,1104_1779624967973&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8H+vH5sKjkvY6pIAyEqScBLTAQIE97dBBAEAAAAAAA7mEkxeODwAAAAOpnltbLcz9gKNyK89dVj0PTfr+3VoTp5voLaiHRZTtbPFuuCIx9IoMryp6wd6M8eXejmfAJJXQpG/NMeeBtU+biRKl0BITZAsZqI8rMO1vB4/JHD6oGbOKk6rf0w7sh1ZCkQodTST492m/dm1XlPe325UlX9rEwAzlpHc1ibcOEXQsgIu+YpjNBe2n9cWlnPcz0lqsr0n6i+SY34uJ8fQYipKb16KALcqfuT0X2WuhyEoXyZ5mnMPBwLke/s=&pass_ticket=exDE/Rrctj6w0/LEDYYOGuAHmrOcQIABFMS4z0hsNmgn12lCixIC+ACnwi5tMWTY&wx_header=3)

Original库森 程序员库森

DeepSeek V4 刚出的时候我就盯上了，文字能力对标 Claude Opus 4.6，百万 token 价格不到 Claude 的十分之一，性价比直接拉满。

我通过DeepSeek V4+  Obsidian + Claude Code建立了知识库，让 AI 直接读我的文件、搜笔记、跨文件关联回答问题，发现效果很不错。

今天就教大家怎么接入，0 基础四步走，跟着做就行 。

**第一步：装 Obsidian**
------------------

官网下载安装包，Mac 和 Windows 都有，免费的，双击装上。它是本地 Markdown 笔记软件，所有文件存你自己电脑上，不用担心数据安全。插件生态非常强大，今天用到的 Claudian 就是其中一个。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/7BD3A771-7D98-4BFE-BA2B-53AB4CF78E7F.png)

---

**第二步：装 Claudian 插件**
---------------------

Claudian 把 Claude Code 嵌进 Obsidian，笔记仓库直接变成 AI 工作目录，能读能写能搜索。

先打开 Obsidian 设置（左下角齿轮图标），找到「第三方插件」，把安全模式关掉。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/9FC12C14-6C70-46D0-9AA1-E0A4670C1175.png)

---

关闭安全模型

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/494C3DFE-3D5F-4F01-97B4-E577E8877DD8.png)

点开社区插件市场

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/A14BCE2B-5AC2-4F24-B0A7-D92D60F87CDE.png)

---

Claudian 还没上官方插件市场，需要通过 BRAT 装。在社区插件里搜 BRAT，安装启用。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/7CE230C7-E287-451E-8387-4BF468862486.png)

然后回到设置找到 BRAT，点 Add beta plugin，输入 Claudian 的仓库地址就能装上。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/031AF8F6-6195-4574-88B1-3F7CBBD242AF.png)

---

输入 claudian 的地址

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/749925DA-2EAF-4F10-B54D-60797C8EA17C.png)

<https://github.com/YishenTu/claudian>

最后回到第三方插件列表，把 Claudian 开关打开就好了。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/10F24FFB-3DB4-493C-AB0C-5D20FD4C8634.png)

---

**第三步：装 Claude Code + 配置 DeepSeek V4**
--------------------------------------

先装好 Node.js（Mac 终端跑 brew install node，Windows 去官网下安装包），然后一行命令装 Claude Code，国内用 npm 镜像源也能装。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/AE4FEDB8-1A55-4384-99D2-B5A7E5CA266F.png)

然后用 CC Switch 桌面工具配置 DeepSeek V4 做后端。安装后新建配置，供应商选 DeepSeek，粘贴 API Key，填好模型名称，保存启动就行。

这部分我之前写过超详细的图文教程，包括怎么拿 API Key、CC Switch 每一步怎么配、踩坑细节全都有，看我主页那篇「DeepSeek 接入 Claude Code」就行，已经配过的直接下一步。

---

cc switch 的安装配置（已经配过的直接下一步）

先去 GitHub 下载一个桌面工具叫 CC Switch，专门管理 Claude Code 的供应商配置，不用记环境变量，新手友好。

macOS 选 dmg，Windows 选 msi 安装包。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/E70CCFCD-A345-48DC-8D00-B9F76A428EC9.png)

安装运行后，点 "+" 新建配置。供应商选 DeepSeek，

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/3F50988E-B61A-43A5-9259-6CDEFC9697CE.png)

---

然后粘贴deepseek 开放平台拿到的 API Key。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/AE614DE7-C417-4EB1-83B2-1F9B6A2DDB19.png)

---

进行配置，添加两个模型

deepseek-v4-pro[1m] 做主模型，

deepseek-v4-flash 做轻量任务和子代理。

名称严格按图里来，点添加保存。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/16E4624B-DF58-4D31-8BC6-E3F97B40C912.png)

---

点启动，配置就生效了 🎉

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/F8BF2042-CBF6-49BA-B8D3-2977D5B3BE87.png)

**第四步：配置路径，开始用**
----------------

终端输入 where claude 拿到路径，粘贴到 Claudian 设置里就行。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/3CE88460-3D3C-4288-AF5E-581A347D106C.png)![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/A2D18A14-1D62-4DEB-A4E2-95612ED926EB.png)

---

找到 Claudian 图标，点开就能跟 AI 对话了。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/10670047-2DA5-42FC-A7A6-9E7E6C2F3A98.png)

---

**实际体验**

让它整理知识库内容、回答问题，它是真的在你本地文件里搜索关联的，不是瞎编。跨文件检索、知识关联、内容总结全能搞定，比单纯搜索强太多了。

![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/C169E1C1-6EBF-47CF-B1F9-F5343C1359F8.png)![](.evernote-content/EFE5A19C-B50C-468D-8B63-C6A1A203484B/0C50DCFF-5E57-4893-B7B8-DD0B42605A38.png)

---

整套方案搭下来，Obsidian 管数据、Claudian 接 AI、DeepSeek V4 省钱还好用。不管是整理学习笔记、管项目文档还是搞内容创作，都非常趁手。

现在搞个人 AI 知识库门槛真的低了，本地加 AI，数据安全又智能，是真的香。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c1849598f6f31c8e2f3a409e20e1dcd630c630fa04c71d50183d68fcc13c849ff6ac4b5a1be1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1779622957_1&req_id=1779346571881990&scene=169&mid=2247499086&sn=eaae27c36c9085179a3704e440147ad1&idx=1&__biz=MzkyMTI3Mjc2MQ==&sessionid=1779624830&subscene=200&clicktime=1779624974&enterid=1779624974&flutter_pos=5&biz_enter_id=5&jumppath=20020_1779624916986,1104_1779624950003,20020_1779624956074,1104_1779624967973&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8H+vH5sKjkvY6pIAyEqScBLTAQIE97dBBAEAAAAAAA7mEkxeODwAAAAOpnltbLcz9gKNyK89dVj0PTfr+3VoTp5voLaiHRZTtbPFuuCIx9IoMryp6wd6M8eXejmfAJJXQpG/NMeeBtU+biRKl0BITZAsZqI8rMO1vB4/JHD6oGbOKk6rf0w7sh1ZCkQodTST492m/dm1XlPe325UlX9rEwAzlpHc1ibcOEXQsgIu+YpjNBe2n9cWlnPcz0lqsr0n6i+SY34uJ8fQYipKb16KALcqfuT0X2WuhyEoXyZ5mnMPBwLke/s=&pass_ticket=exDE/Rrctj6w0/LEDYYOGuAHmrOcQIABFMS4z0hsNmgn12lCixIC+ACnwi5tMWTY&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/308aaba8-94bb-44a2-a864-04a479257c7e/308aaba8-94bb-44a2-a864-04a479257c7e/)