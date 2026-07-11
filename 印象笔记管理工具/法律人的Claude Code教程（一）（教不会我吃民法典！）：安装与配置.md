# 法律人的Claude Code教程（一）（教不会我吃民法典！）：安装与配置

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485751&idx=1&sn=33d24ddf860b6bdfd0fb9211a4cb979c&chksm=c3062dfbea6214ed29fc51aa341563d4449dd95d11dfeb3905939e346c55c29761011c3c5ee1&scene=231&sessionid=0&clicktime=1776654331&enterid=1776654331&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQrQQemvyuEV8+moaIHq5wehLVAQIE97dBBAEAAAAAAJXSKRSJ6xwAAAAOpnltbLcz9gKNyK89dVj04lAjuyESXeVbjKQyK1hvqgDhBTdIeAjx45940xfp/YwK8lE0iMr91gWfOG+lXmrp/ocymChvu5xDt5tdwVxMHMdFquBmOxrmuiy0TiO5Ez1vB8GjNzT/1cSSWV8Hvs4yucgOAZA4daI40N9X1KkjeHq8jqIRhLQXBZQPwebW6IaXN9aTb3O3JFkjL5xgKkEZEcMVdCZnSXSu+FUfTRgljYSd+/GNjMnN7opBCFwXvA==&pass_ticket=uChoo265B1dqFzQrF2qmOwcCyR2zPIgm/wyQza6Qdg3Q0lT5dqyif7VHeDexnvS0&wx_header=3)

法律人的Claude Code教程（一）（教不会我吃民法典！）：安装与配置
=====================================

Original积成 智律积成

我们有个群，非常活跃，一天到晚都在讨论与法律相关的 AI 内容。

其中很大一部分，都和 Claude Code 有关。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/786A6E90-4A25-4BD8-A091-17A811CF95B7.png)

群里经常有朋友加我问：怎么安装和使用 Claude Code？

问的人多了，我就想，不如做一个系列教程。一个**法律人视角**的 Claude Code 教程。

我打算从安装配置写到日常使用，再到法律场景的实战应用，一步步来，预计10+文章，欢迎持续关注。

为什么值得做？

1. 在我心中，Claude Code 是 2025 年以及 2026 年至今最推荐的通用 AI Agent 工具。法律垂直 AI 谁是第一还有争议，但 Claude Code 的优秀是毫无争议的
2. Claude Code 太通用了，虽然名字里有 Code，但能做的远超 Coding，就看你的想象力和创造力
3. 太多教程都是以 Coding 为视角，我想以法律人的视角来做，更合口味
4. 我希望做一个**有手就行**的教程，真正能让法律人学会的教程，毕竟标题已经承诺了：教不会我吃民法典！
5. 以 Claude Code 作为起步，法律人可以进一步了解现在 AI 的应用全貌，而不是仅仅学会一个工具。因为你会了 Claude Code，Codex、Obsidian、OpenClaw 这些都能顺畅地学会

那么，发车！

---

为什么不能只用豆包？
----------

首先解决第一个问题：我们为什么要用 Claude Code？豆包不够吗？

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/C61E3DCB-19FC-4F60-8497-06218472AB80.png)

如果你没有上手过 Claude Code，很难体会这个简单的界面能有什么魔力。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/01049A1C-D84D-49C2-BDFB-67157C3DE90F.png)

豆包，我奶奶都会用的 AI 工具。

如果我们让豆包来审核合同，一般的流程是：

上传合同 → 输入审核要求 → 等待输出 → 获取结果 → 核查结果 → 打开文档进行修订和批注 → 保存

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/5D49FEE3-8FA1-4620-BC53-F938822E0646.png)

但 Claude Code 能做的是：**直接对你电脑中某个文件夹里的合同文件进行审核、修订、批注**，你只需要喝杯咖啡，然后打开文档复核。

所以，我们需要豆包，也需要 Claude Code。

---

简单来说，豆包是你的**聊天搭子**，Claude Code 是你的**工作搭子**。

豆包像那个随叫随到的助理，你丢给它一个问题，它马上回你一段话。

但 Claude Code 更像你团队里一个沉默靠谱的实习生——你不用把文件一份份传给它，也不用手动把它的输出粘贴回去。你只需要告诉它"把桌面上那份协议审一下，重点关注竞业限制条款"，它就自己去找文件、读文件、审文件、改文件，完事了你直接打开 Word 看结果。

***这个差距，本质上是"对话式 AI"和"AI Agent"的差距。豆包活在聊天框里，Claude Code 活在你的电脑里。***

所以，记住这个关键点：**把 Claude Code 当作你的律师助理去看待，去"培训"。**

当然，Claude Code 的强大是有门槛的，它需要你花一点点时间来安装和配置。

别慌，这也是本篇教程存在的意义。

接下来，一步一步来。

---

安装前，你需要准备什么？
------------

### 一个好的网络环境

有时候，是一个"特殊"的网络环境。

懂的都懂。

### Windows 用户还需要：Git for Windows

如果你是 Windows 用户，还需要额外安装 Git for Windows。

下载地址：https://git-scm.com/install/windows

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/B2362710-E65C-4DA9-953D-F8D9D15BD97C.png)

*你可能在其他教程中看到过"需要先安装 Node.js"。好消息是，现在 Claude Code 已经推出了原生安装器（native installer），****不再需要 Node.js****，一条命令搞定，零依赖。*

---

怎么安装 Claude Code？
-----------------

在电脑上找到**终端（Terminal）**，打开它。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/35FF1C01-4E2A-42F5-98CB-34A7804CA304.png)

不要害怕。

从现在开始改变认知：这个简单的窗口，就是你电脑中最强大的 AI 助手入口。

在终端中粘贴下面的命令，然后回车：

claude install

如果行不通、各种报错，换一种方式：

**macOS / Linux / WSL：**

curl -fsSL https://claude.ai/install.sh | bash

**Windows PowerShell：**

irm https://claude.ai/install.ps1 | iex

---

这一步，会难倒很多人。

但不要自己硬扛，推荐两种方式解决：

1. 如果你已经安装了 AI 编程工具（比如 TRAE、Cursor），就在这些工具中安装 Claude Code，它们会帮你搞定所有环境问题
2. 如果你没有装过任何编程工具，不要慌，豆包姐还在呢。把终端里显示的报错内容全部发给豆包，她会告诉你怎么解决。请相信豆姐！

安装完成后，在终端输入以下命令验证：

claude --version

出现版本号，就代表安装成功。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/0FD78384-CA10-4211-AA0A-0AB2C804F725.png)

---

安装好了身体，接下来给它灵魂
--------------

安装好 Claude Code，你的律师助理有了"身体"。

接下来配置模型，给它装上"灵魂"。

### 如果你订阅了 Claude

直接登录就可以。

当然，如果你订阅了 Claude Pro/Max，大概率不需要看这篇教程。

略~

### 国产模型才是正解

国产模型好啊！

GLM、Kimi 和 MiniMax 都可以非常顺畅地接入 Claude Code。

为了统一管理，我们选择 **CC Switch** 作为 Claude Code 的模型管理工具（Coding Tool Helper 或类似工具也可以）。

这个工具的作者是 Jason Young，不是程序员，因为喜欢编程，从外贸转做编程开发。

感谢 Jason！感谢每个充满热爱的人！

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/1E5D8B6D-29E2-4C9B-9E33-8FE94508037A.png)

---

### 怎么安装 CC Switch？

中文介绍地址：https://github.com/farion1231/cc-switch/blob/main/README\_ZH.md

按照指引可以顺畅安装。

**Windows 用户**：在 Releases[1] 页面下载安装包。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/548694F7-C1D0-42A8-96BF-A6CEA95A054F.png)

**Mac 用户**：除了下载安装包，还可以通过 Homebrew 安装：

brew tap farion1231/ccswitch
brew install --cask cc-switch

安装好之后打开。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/C23784EA-CEF6-48BB-9FBC-B734317122A3.png)

在设置中，建议按下图配置：

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/40F8FDB2-F3AE-4DC3-AD67-83C7A748E28B.png)

接下来，把国产模型通过 CC Switch 配置到 Claude Code 中。

---

### 配置 GLM

进入：https://bigmodel.cn

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/974BB795-9351-444D-BB0F-0DA7F7C49149.png)

注册账号后，选择"特惠专区" → "特惠 Coding"套餐。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/DC787966-75A7-4215-AA1B-BE354E501747.png)

选择适合你的套餐。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/F8963604-A67D-4CD2-853A-2043C64189D7.png)

生成新的 API Key。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/86375F44-9F43-405B-8B21-95BA8CC07CA3.png)

复制 API Key，回到 CC Switch，选择右上角的"+"。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/E1E1B0EC-2831-408A-8778-DE29DD9FD9B2.png)

按照下图进行选择：

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/2C310CD5-BDD3-4373-9374-D5F6B3000858.png)

将 API Key 粘贴到红框中，选择"+添加"。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/159F0ADA-15BE-4601-A5B7-D38D9404A8F5.png)

启用刚刚添加的 GLM。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/8B659F3E-8AC8-4F89-A608-860FCD557BEE.png)

测试一下模型。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/1AB29725-0A7E-4901-B7AE-C0A2D35B1B3A.png)

恭喜你，模型配置成功！

通过这种方式配置的 Claude Code，可以看到相应的模型名称（和 CC Switch 中的设置有关）。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/9C6DB7D8-F30E-4D93-BFB5-66570A9AF361.png)

---

### 配置 MiniMax

方式和 GLM 类似。

进入官网注册账号：https://www.minimaxi.com/

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/7F39CA71-891E-4557-8611-CC56F93CC219.png)

在开放平台中选择"Coding Plan"。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/0229E46B-EBA4-42D6-BFB6-E35F9E33D7ED.png)

购买套餐后生成 API Key。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/FD5009A6-471F-4ED2-882D-57883B0B7B82.png)

在 CC Switch 中配置，选择"MiniMax"。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/7B1EE2C6-0C57-4C5C-A939-D7042476DA1E.png)

**注意**：这里默认是 2.1。如果你订阅的是极速版，修改为 `MiniMax-M2.5-highspeed`；如果订阅的是 Starter、Plus 或 Max，修改为 `MiniMax-M2.5`。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/75602F23-AC49-408E-8B12-1FFC149850D9.png)

---

### 配置 Kimi

方式也类似。

进入 **Kimi Code**（不要走错了哦）：https://www.kimi.com/code

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/6A696FD7-B524-4D18-BD04-7F66B5319D5A.png)

选择套餐。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/85BBE379-89A7-4107-8ADD-AA50290C6A2F.png)

在 CC Switch 中要选 **Kimi For Coding**。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/3A0EFEDE-11DA-4552-97B1-07C0E6323AAB.png)

---

你已经迈出了最关键的一步
------------

配置好模型后，打开终端，输入：

claude

你可以开始和 AI 对话了。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/E9731661-302D-47D1-98B6-4E6F40A3969D.png)

恭喜你，这是属于你的 Moment！😄

你的"律师助理"已经诞生。

接下来的文章，我们一起把它培养成一个融入团队的好伙伴！

---

**说实话，安装配置是整个过程中最枯燥的一步，但也是最关键的一步。**

迈过这道坎，后面的世界，比你想象的大得多。

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。

![](.evernote-content/69E4B523-5132-4120-9F3D-EAFC849A4ECD/74C556BB-118A-4897-8E55-BEB9B46C88D2.png)

参考链接

[1] Releases: https://github.com/farion1231/cc-switch/releases

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485751&idx=1&sn=33d24ddf860b6bdfd0fb9211a4cb979c&chksm=c3062dfbea6214ed29fc51aa341563d4449dd95d11dfeb3905939e346c55c29761011c3c5ee1&scene=231&sessionid=0&clicktime=1776654331&enterid=1776654331&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQrQQemvyuEV8+moaIHq5wehLVAQIE97dBBAEAAAAAAJXSKRSJ6xwAAAAOpnltbLcz9gKNyK89dVj04lAjuyESXeVbjKQyK1hvqgDhBTdIeAjx45940xfp/YwK8lE0iMr91gWfOG+lXmrp/ocymChvu5xDt5tdwVxMHMdFquBmOxrmuiy0TiO5Ez1vB8GjNzT/1cSSWV8Hvs4yucgOAZA4daI40N9X1KkjeHq8jqIRhLQXBZQPwebW6IaXN9aTb3O3JFkjL5xgKkEZEcMVdCZnSXSu+FUfTRgljYSd+/GNjMnN7opBCFwXvA==&pass_ticket=uChoo265B1dqFzQrF2qmOwcCyR2zPIgm/wyQza6Qdg3Q0lT5dqyif7VHeDexnvS0&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f3915ee7-96d9-4c3f-9549-63d6e77a004a/f3915ee7-96d9-4c3f-9549-63d6e77a004a/)