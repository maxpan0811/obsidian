# Agent Mail，AI 的专属邮箱，小白接入教程来了！

---

来源：[打开原文](https://mp.weixin.qq.com/s/j8heN_5ktCcED_hfRxyXGg)

Datawhale干货

作者：筱可，Datawhale成员

Agent 今天可以有自己的专属邮箱了！

最近，腾讯 Agent Mail 很火。它是腾讯 QQ 邮箱专为 Agent 推出的独立邮箱服务，可以为每个 Agent 分配一个专属的 @agent.qq.com 邮箱。

有了这个邮箱，Agent 不仅能自己收验证码、接通知、发邮件、处理附件，更重要的是，Agent 和 Agent 之间也有了更方便的协作方式。以后不同 Agent 可以通过邮件互相传递任务、同步结果、协同工作，不再只是单个工具各干各的。

跟着做，10 分钟后，你的 Agent 就能拥有自己的邮箱，走起！

一、开通：给你的 Agent 创建一个邮箱
---------------------

进入产品与登录
-------

打开 agent.qq.com，页面显示 Agent Mail 服务介绍，左上角标注 内测中。页面中部是微信扫码登录区域，底部有一个 Agent 一键接入 按钮。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/42523889-6B91-41BD-8177-CD9CBBE8034B.png)

Agent Mail 首页

点击 Agent 一键接入 后，弹出一个模态框，提供一段提示词。你可以把这段提示词复制给任意支持 CLI 的 Agent，让它自动完成后续安装。如果你想自己掌控每一步，继续往下看。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/070BBE93-E96A-4E7A-AB01-0E29363B11AE.png)

一键接入弹窗

创建邮箱地址
------

扫码登录成功后，页面左侧显示 暂未创建邮箱地址，点击 立即创建。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/912F89E8-B515-42AB-A073-7A2FA7D236AC.png)

邮箱列表页（未创建）

进入 新建邮箱地址 弹窗。系统默认生成一个前缀，完整地址为 前缀@agent.qq.com。规则：以字母开头，6 到 18 个字符，只能包含字母和数字。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/7CDF6844-9D2E-4B64-96AB-13F440FD2076.png)

新建邮箱地址弹窗

确认后创建成功。页面显示邮箱地址和 未接入 Agent 状态标签。此时邮箱已存在，但尚未和任何 Agent 绑定。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/6EC01D1F-80F0-46BA-AE24-FFA76C2B1D10.png)

邮箱创建成功

二、配置：让 Agent 连上邮箱
-----------------

安装 CLI 工具
---------

在你的终端执行：

npm install -g @tencent-qqmail/agently-cli

安装完成后，你会得到一个全局命令行工具 agently-cli，后续所有操作都通过它完成。

注意：如果你用的是 Git Bash，可能会提示 npm: command not found。切换到 PowerShell 再执行即可。

安装 Skill
--------

CLI 装好后，执行：

npx skills add https://agent.qq.com --skill -g -y

这一步会把 Agently Mail 的 Skill 安装到你的 Agent 配置目录。安装完成后，你的 Agent 就具备了收发邮件的技能。

OAuth 授权
--------

执行：

agently-cli auth login

命令会输出一个授权链接。复制链接到浏览器打开，用微信扫码确认。授权成功后，命令自动退出。

整个授权流程采用 OAuth 设备码模式：CLI 生成临时 code，浏览器完成身份验证，服务端交换 token。你的微信密码不会暴露给 CLI。

验证接入状态
------

授权完成后，执行：

agently-cli +me

看到类似下面的输出，说明接入成功：

{

"ok": true,

"data": {

"aliases": [

{

"email": "lixiuqi@agent.qq.com",

"is\_primary": true

}

],

"scopes": ["alias:read", "mail:delete", "mail:read", "mail:send"]

}

}

关键信息：邮箱地址、是否主邮箱、权限范围。默认权限包含读取、发送、删除邮件和别名管理。

三、使用：收发与管理邮件
------------

管理邮箱地址
------

在 agent.qq.com 页面左侧点击 管理邮箱地址，可以查看：

• 发信昵称

• 接入工具

• 连接状态（运行中 / 已断开）

• 创建时间

• 解绑 / 注销地址

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/0F4135AB-92C0-4F49-AB36-1A9DC3F690D7.png)

管理邮箱地址页

收发邮件
----

接入完成后，有两种使用方式。

方式一：通过 Agent 自然语言操作

直接在 Agent 对话窗口说：

• “帮我给 xxx@example.com 发一封邮件，内容是……”

• “看看我最近收到了哪些邮件”

• “找一下上周关于项目进度的那封邮件”

• “把主题为 xxx 的邮件的附件下载到本地”

方式二：通过 CLI 命令操作

agently-cli message +list # 查看收件箱

agently-cli message +send --to <收件人> --subject <主题> --body <正文> # 发送邮件

发送邮件时，CLI 会先返回一个确认 token，你需要把 token 带回命令中再次执行，才能完成发送。这是为了防止误操作。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/339B65D1-BC09-4A8B-B32D-111B0BDF91F4.png)

收件箱界面

查看邮件详情
------

在收件箱中点击任意邮件，可以查看完整内容，包括发件人、收件人、大小、时间和正文。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/727C3A9F-05F8-4133-9C3F-1E25C801BE87.png)

邮件详情页

发件箱与测试邮件
--------

通过 CLI 发送的邮件，会在发件箱中留下记录。点击 发信记录 可以查看。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/A7E4797E-6FFD-47A3-B660-3639E2E61038.png)

发件箱（空）

发送测试邮件后，发件箱中会出现对应记录，显示发件人、主题、内容预览和时间。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/66EE3AF7-F9F1-473B-921B-5C3FF55118DC.png)

发件箱（测试邮件）

四、进阶：Agent 之间怎么对话
-----------------

A2A（Agent-to-Agent）指的是不同 Agent 之间的自主协作。过去谈到 A2A，大家默认需要 API、消息队列或 MCP 这类专用协议。腾讯这次选择让邮件直接承担 A2A 通道的角色。

这个选择有四个好处：

• 异步协作：邮件天然不要求双方同时在线。一个 Agent 发完询价邮件后可以继续做别的事，对方 Agent 处理完再回复，整个过程不用保持长连接。

• 兼容性强：SMTP/IMAP 是企业用了几十年的标准协议，跨组织、跨平台时不需要对方额外部署中台。

• 全程可追溯：每一封邮件都是一条带时间戳、发件人、主题、正文的记录，纠纷排查和审计比瞬时消息更容易。

• 无需新协议学习成本：对已有系统来说，Agent 只是一个新的发件人/收件人，不需要重写接口。

一次典型的 A2A 协作通常包含以下环节：

1. 能力发现：每个 Agent 通过 Agent Card 公开自己能做什么、需要什么输入、如何鉴权，相当于一张数字名片。

2. 任务派发：一个 Agent 向另一个 Agent 的邮箱发送任务请求，比如请报 A 产品 100 件的价格。

3. 进度追踪：双方围绕同一个 Task ID 或邮件主题往来，状态、附件、结果都落在一串邮件里。

4. 结果交付：对方 Agent 处理完后，把报价单、订单确认或处理结果回复过来。

实际应用场景举例：

• 采购询价：采购 Agent 同时向多家供应商 Agent 发询价邮件，收集报价后自动比价。

• 订单对接：电商平台的订单 Agent 把订单信息发给仓储 Agent，仓储 Agent 确认库存后回传物流单号。

• 发票报销：财务 Agent 接收供应商 Agent 发来的发票邮件，自动提取字段、录入系统、触发审批。

所有通信默认加密，并通过 OAuth 鉴权，只有被授权的 Agent 才能参与协作。对个人用户来说，这意味着你可以让不同 Agent 像发邮件一样互相委托任务，而不必把每个 Agent 都接进同一个封闭系统。

五、参考与限制
-------

帮助中心
----

如果遇到问题，可以访问 help.agent.qq.com。页面顶部有搜索框，左侧是问题分类导航，正文包含产品简介、支持的 Agent 列表和接入步骤说明。

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/CD5BDFC7-05E1-4BB6-9C6D-93F96249E760.png)

帮助中心

CLI 文档参考
--------

完整的 CLI 安装和配置说明可以在官方文档查看：

![](.evernote-content/C1231B4C-BF12-445C-A422-EE5EF521CDAD/3FBD2B4F-CEB4-4757-B6B4-245E379CBED7.png)

CLI 安装文档

文档地址：https://agent.qq.com/doc/cli-setup.md

当前限制与注意事项
---------

这个服务还在内测，有一些限制值得注意：

• 发送额度：每天最多 50 封，每小时 200 次请求，每分钟 10 次请求。日常使用足够，批量场景需要控制节奏。

• 附件限制：单封邮件最多 50 个附件，总大小 20MB。大文件需要另想办法。

• 数据隔离：Agently Mail 和你的个人 QQ 邮箱完全隔离，互不影响。你在 agent.qq.com 管理页可以查看发信昵称、接入工具、连接状态、创建时间，也支持解绑和注销地址。

写在最后
----

Agently Mail 目前只是一个邮箱服务，但它的定位很明确：给 Agent 一个独立于人类的通信身份。后续如果腾讯把微信、企业微信、公众号的消息能力都接进来，这张邮箱地址可能会变成 Agent 在整个腾讯生态里的数字身份证。

现在内测阶段，建议先注册一个地址，把 CLI 跑通，熟悉基本操作。等正式版上线时，你已经有了现成的接入经验。

一起“点赞”三连↓

[📎 在印象笔记中打开](evernote:///view/207087/s1/5d019120-20a8-4865-818c-8ef9afe32794/5d019120-20a8-4865-818c-8ef9afe32794/)