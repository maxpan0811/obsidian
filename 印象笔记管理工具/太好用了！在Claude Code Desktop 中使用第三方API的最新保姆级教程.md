# 太好用了！在Claude Code Desktop 中使用第三方API的最新保姆级教程

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515780&idx=1&sn=697703ee16351f82c3ca8922e8cdef0f&chksm=e9e68a79bb394bf3eefeb786025d25275d80a4b055084f5ed88154f8b7581c0c7376512b92d1&mpshare=1&scene=24&srcid=0601rM4fvPGz9vjyxMmWhrc7&sharer_shareinfo=4f24e8b37dc72d75b5466a23571238ae&sharer_shareinfo_first=4f24e8b37dc72d75b5466a23571238ae&clicktime=1780445397&enterid=1780445397&ascene=14&devicetype=iOS26.5&version=18004a25&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFVAa5DTQFYvxuJg4lBMAtRLTAQIE97dBBAEAAAAAAIfwOmYwkDIAAAAOpnltbLcz9gKNyK89dVj0trx7JphJO/VhCwszdCkLKWDey69gzXVpDAE1r8nAjmWaif96dQc0aJdQiXWiq9UTk/e4FsyltvZykFbegxxoxYDrEKUqS44N+FOlKN1ygmCQXsZUx8Q95E1tl+9H0cxaOgiwAAttF4PXMTfTdpGsQnaC41+UJ8gsik7mRhWrrPs1tM0rAHk8ax3Mu82lVhgOqeiJMQfxSrZ4Wed55VGynUYrrO5dhIMWw6KELMg=&pass_ticket=WA1zHysavFf8SQy5fDWsVsNkim0fcJxTsU31+M61KrfKZZS6xEdj4iQCxhbyw0T+&wx_header=3)

Original字节笔记本 字节笔记本

可以在官方 Claude Desktop 界面里直接调用其他厂商的模型了。

不需要付费订阅，不用考虑IP，更不用担心封号。

直接接入更便宜、更快、或者特定能力的模型，同事保留 Claude Desktop 的所有界面交互和体验的原汁原味。

具体的操作方法和步骤如下：

**第一步：启用开发者模式**

完全退出 Claude Desktop，右键托盘图标 → Quit，完全关闭。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/38D9BDF0-560D-478C-8280-AA04C7259287.png)

重新打开 Claude Desktop，先不要登录账号。

点击顶部菜单，按照下面的操作路径来：

Help（帮助） → Troubleshooting（故障排除） → Enable Developer Mode（启用开发者模式）

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/36272DA9-C355-4A1B-A78F-173FDB89C903.png)

点击后应用会自动重启。

**第二步：配置第三方 API**

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/DB47681B-65E8-4A40-8290-C9EA7CE94386.png)

重启后，你会看到顶部菜单多了一个 Developer开发者选项，如图所示。

点击 Developer → Configure third-party inference配置第三方推理 / 配置第三方接口。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/3C496E0F-F57F-4904-8D7B-BA611B1F945E.png)

会弹出一个设置窗口，填写以下内容：

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/74502C1C-BEA1-4FA6-8FDC-41A7488F1782.png)

我这里使用GLM Coding Plan：

https://link.bytenote.net/glm

选择左侧菜单的Collection，切换并点击Getway模式。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/4DB7EE15-490C-4897-B027-4E1B41418C09.png)

依次填入GLM适配的接口地址和相关的Key，其他第三方的国产模型或者是中转，只要是支持Anthropic的都可以正常的接入。

Deepseek：<https://api.deepseek.com/anthropic>

继续下拉这个页面，填入对应的模型名称，我这里填入的是glm-5-turbo，兼具了速度和智能度。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/3317CA95-37CB-4708-968B-612F331C300B.png)

填入完成之后，点击最下面的Apply，Claude Code Desktop会自动重启，重启完成之后，就可以正常使用了。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/52AEDC0F-2B93-4782-AFCB-DD6AB971A99D.png)

相较于黑漆漆的命令行而言，Desktop客户端提供了更加友好的交互界面。

左侧提供了项目的会话列表，中间为对话和输出模块，在右侧可以看到详细的修改内容。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/2262084C-DA62-4F38-BA8D-E99E95306B46.png)

Desktop当中最大的功能亮点Cowork也可以正常的使用，各种Plugin和Skills也可以正常的被驱动，和官方正式的订阅几乎没有任何的区别。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/C1459C8F-1859-47BF-9E47-984E99E267E1.png)

对日常的工作，其实命令行就够了，Cowork 是我愿意继续这个桌面使用的最大原因。

Claude Cowork可以看成是龙虾的桌面版，基于与 Claude Code 完全相同的代理架构，但无需终端、无需编程知识，直接在 Claude Desktop 桌面应用 中使用。

只需描述想要什么结果，Claude Cowork 就能自主规划步骤、在电脑上读写文件、操作应用，最终交付完整成品。

Cowork可直接访问指定的文件夹，读写 Word、PDF、Excel、PowerPoint、图片、CSV、JSON 等各种文件。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/A8B195C3-33EA-4B4D-820E-5F5A867AC02F.png)

具备自动拆分任务、并行使用子代理、调用浏览器的能力，全自动完成从研究、整理、合成到输出全流程。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/875B16A4-C62E-48C7-9F2C-023D75C55138.png)

你只需要关心最终的交付结果，彻底地做一个甩手掌柜，等着它给你整理好的文件夹、格式化报告、带公式的表格、专业演示文稿等真实文件就行了。

所以它就是包装成普通人也能轻松使用的桌面 AI 代理，不用操心环境配置，也不用学习命令行，上手就能干。

并且安全性更好，所有代码和 shell 命令都在本地隔离的虚拟机中运行，重要操作如删除文件会弹出确认，仅访问你授权的文件夹。

![](.evernote-content/BFD01DD9-4455-4712-B88B-EB8BEAB39A54/27411B60-BD30-4110-8B6E-C01FABFAEC9D.png)

它更适合于非技术知识工作者，象是市场、运营、财务、法律、研究员等。

简直就是牛马打工人的必备，比OpenClaw龙虾更稳定，更加的实用，也会比市面上所有的xxxClaw功能更完善。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515780&idx=1&sn=697703ee16351f82c3ca8922e8cdef0f&chksm=e9e68a79bb394bf3eefeb786025d25275d80a4b055084f5ed88154f8b7581c0c7376512b92d1&mpshare=1&scene=24&srcid=0601rM4fvPGz9vjyxMmWhrc7&sharer_shareinfo=4f24e8b37dc72d75b5466a23571238ae&sharer_shareinfo_first=4f24e8b37dc72d75b5466a23571238ae&clicktime=1780445397&enterid=1780445397&ascene=14&devicetype=iOS26.5&version=18004a25&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFVAa5DTQFYvxuJg4lBMAtRLTAQIE97dBBAEAAAAAAIfwOmYwkDIAAAAOpnltbLcz9gKNyK89dVj0trx7JphJO/VhCwszdCkLKWDey69gzXVpDAE1r8nAjmWaif96dQc0aJdQiXWiq9UTk/e4FsyltvZykFbegxxoxYDrEKUqS44N+FOlKN1ygmCQXsZUx8Q95E1tl+9H0cxaOgiwAAttF4PXMTfTdpGsQnaC41+UJ8gsik7mRhWrrPs1tM0rAHk8ax3Mu82lVhgOqeiJMQfxSrZ4Wed55VGynUYrrO5dhIMWw6KELMg=&pass_ticket=WA1zHysavFf8SQy5fDWsVsNkim0fcJxTsU31+M61KrfKZZS6xEdj4iQCxhbyw0T+&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f6659422-2d08-46b4-b2c6-e665a7418932/f6659422-2d08-46b4-b2c6-e665a7418932/)