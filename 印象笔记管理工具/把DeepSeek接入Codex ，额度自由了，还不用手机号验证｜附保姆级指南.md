# 把DeepSeek接入Codex ，额度自由了，还不用手机号验证｜附保姆级指南

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MjAyNDUyMA==&mid=265109...](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651093149&idx=1&sn=76eb639a5f3409a7d566a57b981a3394&chksm=bc7b62d4dd5d462e5564dec930234ff82914db578c7c2a7c3cf74ac1654dbf923a475f485183&scene=90&xtrack=1&req_id=1780476331106202&sessionid=1780476486&subscene=93&clicktime=1780476492&enterid=1780476492&flutter_pos=1&biz_enter_id=4&ranksessionid=1780476331&jumppath=1001_1780476360972,1102_1780476480909,1001_1780476483918,1104_1780476487622&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a25&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxi7wQjZ4X91ddU7vhpz9YRLTAQIE97dBBAEAAAAAAKFfA2NvmFMAAAAOpnltbLcz9gKNyK89dVj0ic0Iibaqv10C8KV1zhGRxC3eQ1sx/4GCssA0Upxp0lYVr4yTQNbY7wu97LscCUrT7ze8jD0gz/22o+YRE3ohReZ74l9UPLKqLdeTmO2pWHHc3hAXBuX95xswOhcHRY1Oe25kVi6x78ykUqMLV+TzfOByIKr6EmLhMxaTUBO0X4GbTolMgH3H3KB6lfCcMsPOVszXhc8cWx6OufiLwviFlu95OD6p6efg66yWqBI=&pass_ticket=5SnI5XTHwc0ewnqvIl00l6SmQ6TWhpRz7Bh75m9okbGurtfTpnxnjYfGREaYQtux&wx_header=3)

Original发现明日产品的 APPSO

Codex 又又又大更新，前一天负责人还在说，是不是要改名 ChadGPT，网友在下面评论说，不如直接将 ChatGPT 重新命名为 Codex。今天凌晨， [OpenAI 宣布 Codex 将并入 ChatGPT](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651093148&idx=1&sn=baeb27da26ea3efa1b07382111fdae5e&scene=21#wechat_redirect)。一边是刚刚达到 500 万用户的 Codex，一边是已经突破 10 亿的 ChatGPT 用户。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/82AA3EF7-FD34-4AF5-A013-ECACF68985D4.jpg)

早在之前，Codex 就已经部分整合进 ChatGPT，作为远程控制本地电脑的方式之一。当前的 Codex 有独立桌面版应用、CLI、IDE 扩展、网页访问以及移动端 SSH 连接，主要是为功能开发、代码重构和测试等软件任务提供支持。这次进一步的整合，直接将日常对话与专业级开发能力结合起来。

除了 Codex + ChatGPT 的合体，Codex 还为企业版和商业版用户率先推出了 Site 功能，预计之后会扩展到普通用户。有了 Site 功能，我们通过 Codex 一句话 Vibe Coding 构建的网页，现在都会有一个可以公开访问的链接。插件系统也进行了大更新，发布了六款全新的角色专属插件，包含 62 个热门应用程序和 110 项 Skills。六款角色专属插件分别是数据分析、创意制作、销售、产品设计、公开股权投资，以及投资银行。Codex 越更新越好用，就意味着 Token 消耗越大。这段时间以来，收紧的手机号验证和严格的使用额度控制，背后都是算力在疯狂地燃烧。有网友发现 Codex 现在会强制要求用户验证当时注册 ChatGPT 的手机号，但那个手机号一般又是从平台找来的，所以只能注册一个新账号。额度的限制同样如此，虽然伴随着时不时的额度重置，网友也开始叫苦。就算额度会重置，但消耗得越来越快，重置又有什么用呢，还不如直接让 Token 的消耗变慢一点。

不少开发者和老用户在说，现在 Codex 涌进了这么多的新用户，未来还要整合进 ChatGPT 的 10 亿用户里，Codex 的用量只会被不断压缩。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/FA0057C2-36B9-4F47-8867-DC083D2F5830.png)

X 上的消息显示 Codex 在 6 月 1 日前后，结束了一项 2 倍使用量的促销，付费套餐恢复为基于 Token 的标准额度限制。同时，免费用户和 Go 会员用户的 Codex 用量从周重置修改为了月重置，这意味着额度直接砍了 75%。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/6D7AD84D-AB6F-4D0D-818C-E3C07555BA1A.png)

我们在免费账户上尝试了一波，在让 Codex 完成一个简单的可视化分析网页时，中间追加过一次需求，任务完成之后，月额度就从一开始的 95% 降到了 2%。

最近社交媒体上出现了很多用第三方模型接入 Codex 的教程，能直接避开 Codex 的 5 小时限制、周额度限制、月额度限制，完全根据 Token 用量来决定。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/29975006-5DB3-4919-8BA4-C1AEB4D4A1B7.jpg)

在 Codex 终端里配置了第三方的模型之后，我们还发现了 **Codex App 可以不用登录就能使用**，直接绕过「无法通过」的手机号验证。一般情况下，打开安装好的 Codex App 就是「登录」或者「注册」，无论哪一项，现在都必须经过严格的邮箱验证和手机号验证，但在 Codex 终端配置好第三方模型之后，再重新打开 Codex，就能直接使用了。详细的教程可以看我们制作的视频，图文配合视频，一步一步来，你也能快速上手 Codex。介绍一下 CC SwitchCC Switch 最早使用在 Claude Code 里，用来切换不同的模型提供商。一般来说，我们需要修改 Claude Code 的配置文件，输入自定义的 API KEY，模型名字，以及用来处理请求的 BASE\_URL。CC Switch 则是把这套偏硬核的流程打包成一个可视化的界面，我们可以像使用一般软件一样，鼠标点击就能直接修改，切换不同的模型的 API。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/CCCA96AC-8E68-4A92-84D3-615504AEC9E5.png)

目前，CC Switch 已经能做到 Claude Code、Codex、OpenCode、OpenClaw、Gemini CLI 和 Hermes Agent 多款热门 Agent 产品的模型切换。支持的模型供应商更是包含了 Claude 官方、DeepSeek、智谱、阿里云百炼、Kimi、阶跃、MiniMax、小米 MiMo、豆包 Seed、OpenRouter、硅基流动等将近 30 款官方或中转大模型服务。用 CC Switch 免登录 Codex在使用 CC Switch 之前， 我们需要先确保电脑上已经顺利安装了 Codex App。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/B810E7A4-7968-4114-82FB-886C10C4018C.png)

Codex 官网并且 Codex 的终端版本也必须先安装好，在 Codex 官网的最下方，找到「在终端中继续操作」，复制这行命令到电脑上的终端中执行，如果提示不能识别 npm 命令，意味着电脑需要先安装 Node.js。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/4666C0F4-BDC6-466E-97F4-BCBC6ACFB512.png)

Node.js 是之前 OpenClaw、Claude Code 等工具必安装的一款软件包，Node.js 官网会自动识别当前的电脑系统版本，复制对应的命令到终端就能安装好。处理好 Codex 的安装后，安装 CC Switch 的方法也很简单。在官网 ccswitch.io 找到免费下载的按钮，页面会自动跳转到 GitHub 的 Release，往下滚动到 Assets 资产二级标题处， 选择自己的系统（Windows、macOS、Linux）直接下载安装。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/D107B3E7-28C6-4AF8-9F2A-BC04183167A8.png)

目前（2026年6月3日）最新版本 是 3.16.1我们使用的电脑是 MacBook Air M2，所以直接下载了 CC-Switch-v3.16.1-macOS.dmg。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/714F77D2-421F-42FE-A6EA-539EAAC02621.png)

安装完成之后，在应用顶部有 7 款不同的 Agent 产品，选择 ChatGPT 的 logo，点击右上角的橙色➕。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/40A43ACC-6E41-47C0-94B7-EDD26F057D9A.png)

再选择对应的大模型供应商，例如 DeepSeek，我们只需要输入从 DeepSeek 开放平台获取的 API KEY。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/759AEEE0-CB10-48EF-915A-FD2D3B89AA16.png)

添加 API 之后，在启用界面，会被提示「此供应商使用 OpenAI Chat 接口格式，需要路由服务才能正常使用，请先启动路由」。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/4D1524F7-996E-4463-9308-3406F027211B.png)

这里的原因是**大多数模型提供的 API 服务仍然是 OpenAI Chat Completions，即 /chat/completions 的接口格式**。这套接口传回的数据格式不能被新版的 Codex CLI 使用，所以会出现各种问题。在阿里云的 Codex 官方接入指南里也清楚地写着，有 Responses API 和 Chat/Completions API 两种类型，不同的模型会有不同的调用格式。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/F80D815B-0FA1-4A01-BB41-0CCAA4899436.png)

CC Switch 会使用本地路由的方式，让那些即便是不支持 Response API 的模型，也可以接入到 Codex 正常使用。开启本地路由的方法是在 CC Switch 的设置界面，点击主页面左侧顶部的设置按钮，找到路由，打开对应的路由总开关和 Codex 的启用按钮。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/64614EE8-FFC7-4BDB-BC47-73ADA81BD23A.png)

回到启用 DeepSeek 的界面，我们将 Codex 完全退出后再重新打开，输入「你好」，就能看到 Codex 已经可以正常回复了。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/C8E74B54-0201-4E78-AA71-5B2484330F7B.png)

同样的方式，选择 Xiaomi MiMo Token Plan（China），输入对应的 Token Plan API，我们也能切换模型到小米。不过在 Codex App 界面显示模型名称，似乎仅在第一次配置时能正常显示，随着添加的模型供应商增加，Codex 有时还是会显示自定义，而不是具体的模型名字。而且，使用自定义的 API 服务，也无法使用远程连接的 Codex mobile，当我们点击 Codex Mobile，Codex 会闪一下连接的界面，然后快速闪回到主页。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/0F65485B-F313-4E29-BCC2-0F55819E322D.gif)

我们在 CC Switch 作者 Jason Young 发布的 X 博客，有看到最新的教程，关于 CC Switch 如何解锁 Codex 在使用 DeepSeek 等第三方 API 的时候的远程操作和官方插件等能力。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/E3CE6F79-1767-486F-91B6-4E344D8A01FE.jpg)

来源 X@Jason\_Young1231里面提到最新版本的 CC Switch 中有一项「应用增强」的功能，开启之后，会保留 Codex 的登录状态和第三方 API 两种模式。即远程操作 Codex 这项功能，是依赖于 ChatGPT 的登录状态，如果没有登录，就无法连接到手机上的 ChatGPT。而按照第三方 API 配置的方式，如果 Codex 打开之后还是提示要求登录；这个时候我们先完全退出 Codex，关闭 CC Switch 里面的本地路由，然后启用 DeepSeek 这一第三方模型，再打开 Codex，就能正常进入 APP 页面。其他配置方法CC Switch 使用的本地路由，和 DeepSeek 官方教程里使用的 Moon bridge 类似，本质上都是通过一层转发层，让 Codex 以为处理的大模型请求，是符合最新版本的 OpenAI Responses API 格式。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/C290D6B3-7187-4534-8B20-DA9DDB86750B.png)

Moon Bridge 的方法就更极客了，光是在这份 GitHub 的教程里，除了常规的安装 Codex、获取 DeepSeek API Key，以及修改配置文件。我们还需要额外安装 Go，配置 Moon Bridge，教程里仅提供了 Moon Bridge 的默认配置，如果需要图片输入、Web Search 或多 Provider 路由，需要再参考 Moon Bridge 的 config.example.yml 扩展配置。接下来还有启动 Moon Bridge，保持其在终端运行，再启动 Codex 使用。这其中可能出现的问题也很多，我们在 Moon Bridge 的 Issue 问题界面，看到一些待处理的问题包括像是无法使用 Codex 的插件功能、会出现突然的会话中断，以及权限方面的问题。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/9C313184-D82B-4168-B648-848D0AE6468C.png)

因此，使用 CC Switch 仍是目前看来配置第三方模型的最佳途径。现在也有一些模型开始主动支持 Codex 的 OpenAI Responses API。像是 Qwen3.7-Max 和 Qwen3.6-Plus 都支持 Responses API，可使用最新版 Codex；旧模型就还是得通过 Chat/Completions API 接入，需安装旧版本 Codex 才能使用。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/17456601-6F58-46D7-BCE0-0569BA8F14CF.png)

昨天刚刚发布的 MiniMax M3 也能直接兼容 OpenAI Responses API，修改配置文件，不需要额外的本地路由或者 Moon Bridge 就能在 Codex 里正常使用。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/BBB9B38E-5626-43F8-9D83-FC70EE1C2636.png)

图片由 AI 生成OpenAI 在推出 Responses API 时，是考虑到 Codex 作为一个复杂的编程 Agent，继续使用普通的文本对话接口，一问一答式的 Chat Completions API，无法维护多轮状态、管理工具调用、处理复杂的上下文窗口等。像 DeepSeek 这类模型的接口目前没有直接兼容这套协议，即便在配置文件里修改了 base\_url，Codex 发出去的请求，DeepSeek API 也无法接收。Moon Bridge 和 CC Switch 的本地路由，本质上都是作为一个翻译器。它们在本地发起一个服务，监听 Codex 发出的 Responses API 请求，再把它转换成 DeepSeek 能理解的格式，拿到响应之后再翻译回 Codex 能理解的格式，返回给 Codex。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/8FD8B4E6-4A0E-42C5-B406-D1D24EDA3AAD.png)

图片由 AI 生成解决了接入的问题，也只是兼容的第一步。即便是像 Qwen 3.7 这种支持 Responses API 格式的模型，在 Codex 中的使用还是会出现各种问题。之前也有读者分享，接入 DeepSeek 模型也会出现断连的问题。CC Switch 的开发者在 Codex 宣布要并入 ChatGPT 之后，也在 X 发文说，「CC Switch 对 Codex 的适配不会全噶了吧。」

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/8C3D7463-1694-42E7-AD9B-8D476784700B.png)

虽然配置第三方模型能解决额度焦虑，绕过手机登录，但要是追求最极致的稳定性和原生 Agent 体验，和 Codex 官方建议的一样，使用 GPT-5.5 大概仍是最好的选择。也有新的爆料显示，OpenAI 正在准备一款名为 GPT-5.5-Codex-Spark 的快速模型，能够更快更好地处理每日的编程任务。

![](.evernote-content/273546CE-4C99-4A51-BDC2-956F78B1F130/CF4C7DC3-E7C8-467E-ADCF-5407BC5B5705.png)

或者最后就跟 OpenClaw 成为年初的现象级产品一样，Codex 是眼下的热门。随着其他模型厂商的跟进，纯聊天的 APP、API 都会成为过去式，我们也会有更多选择，找到适合自己的，能真正干活的 Agent。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651093149&idx=1&sn=76eb639a5f3409a7d566a57b981a3394&chksm=bc7b62d4dd5d462e5564dec930234ff82914db578c7c2a7c3cf74ac1654dbf923a475f485183&scene=90&xtrack=1&req_id=1780476331106202&sessionid=1780476486&subscene=93&clicktime=1780476492&enterid=1780476492&flutter_pos=1&biz_enter_id=4&ranksessionid=1780476331&jumppath=1001_1780476360972,1102_1780476480909,1001_1780476483918,1104_1780476487622&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a25&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxi7wQjZ4X91ddU7vhpz9YRLTAQIE97dBBAEAAAAAAKFfA2NvmFMAAAAOpnltbLcz9gKNyK89dVj0ic0Iibaqv10C8KV1zhGRxC3eQ1sx/4GCssA0Upxp0lYVr4yTQNbY7wu97LscCUrT7ze8jD0gz/22o+YRE3ohReZ74l9UPLKqLdeTmO2pWHHc3hAXBuX95xswOhcHRY1Oe25kVi6x78ykUqMLV+TzfOByIKr6EmLhMxaTUBO0X4GbTolMgH3H3KB6lfCcMsPOVszXhc8cWx6OufiLwviFlu95OD6p6efg66yWqBI=&pass_ticket=5SnI5XTHwc0ewnqvIl00l6SmQ6TWhpRz7Bh75m9okbGurtfTpnxnjYfGREaYQtux&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c23a66fa-7910-4a3d-9c8c-ef51f9bd043a/c23a66fa-7910-4a3d-9c8c-ef51f9bd043a/)