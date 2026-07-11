# 40年没变过的Email，被腾讯重新定义了

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwMTU5OTQ1Nw==&mid=265372...](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653727887&idx=1&sn=3a69b27cb1ff6e80ebec7caaa6f380f9&chksm=8c76af85be850eea7c8be6ec5671adc4034cc10f351622e7a9c95bbc7aa42829402f85c9d228&scene=90&xtrack=1&req_id=1782428433777735&sessionid=1782428436&subscene=93&clicktime=1782428439&enterid=1782428439&flutter_pos=1&biz_enter_id=4&ranksessionid=1782428433&jumppath=1001_1782428136831,1102_1782428141337,1001_1782428434261,1104_1782428437067&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzPlCaz8uvEMhrmlVSTwWyhLTAQIE97dBBAEAAAAAAOlTMxVY4xEAAAAOpnltbLcz9gKNyK89dVj01NN8Xif67DZXVcFE7evaNCQbmwM97ysixlI5pUGQ/ZsKvZubGGp2IrF9TgKhoCLkVx6nxUkiqvq3mHncJltf9mWdwJrGkfqMzcjyMVpVVUtKJSnpVhZNlbN0n+ixYIp2aaffOsofp5ruLUNs7dau1HoAy5CqYQ4Dgif254xi38D+EjRF22OyjQi2osMqlNtzqv8EZGv7+A6km2K2qeR3hUWZBuPcopRmZ4uT/0Y=&pass_ticket=4V80hrrjEbcumRxG5AYIoHnwMTKuRGpVy16So4L8TL3lbg0jHlbIb8XWGHk7lyFU&wx_header=3)

Original冷逸沃垠AI

大家好，我是冷逸。

最近，QQ邮箱团队内测上线「Agent Mail」，可以给你的Agent接入Agent Mail邮箱。

我第一时间试了，Qodex、Claude Code、OpenClaw、TRAE Work、Workbuddy、Qoder Work、MiniMax Agent、Kimi Work这些主流Agent都可以接入。

接入后，直接跟Agent对话就能收发邮件。

比如，我跟Claude Code说，“给老板发封邮件，告诉他方案已经做好了，马上附件发出。语气要极度谦逊，带点恰到好处的‘彩虹屁’，但又不能让老板觉得我在刻意讨好他。”

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/8B1C0811-C878-400A-9B1E-C215FE93A788.png)

几秒后，真实收件箱里就躺着一封措辞得体、热情而不谄媚的邮件——抬头、正文、落款，一应俱全，甚至比我自己写的更“圆润”。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/59BCD549-5EF8-4BC6-B453-7FA29D826EF3.png)

这意味着什么？以后让AI帮你写邮件、管邮件、甚至帮你做邮件分类和摘要，真的可以了。不是那种“帮你生成一段文字你再复制粘贴”的伪自动化，而是Agent直接操作邮箱，端到端完成。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/7C35338B-3EF4-4E1D-806D-CC7E0EA1019B.jpg)

一手体验

如何使用？

非常简单。首先在 agent.qq.com 注册一个Email账户，微信扫码就行。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/28AE733A-D09E-4C4F-89E5-4DF815D5E6D3.png)

扫码后，需要你在手机端进行确认。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/439AE125-5F87-438B-9854-1C577A6308D0.jpg)

首次进入，会提示你创建一个邮箱地址。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/16506BAB-5618-4FD3-B363-505338FD283C.png)

建议下手要快，目前一些有意思的邮箱名字依然能注册到，比如tokens、agents、skills、anthropic等。当然ponyma是不行的，知名人物、IP、公司已经被系统预留了。

每个微信号，可以创建2个邮箱地址。

创建邮箱地址后，就可以去Qodex或Claude Code这类Agent里接入Agent Mail CLI了。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/E58051E7-16B2-4090-8051-9D4C010D44AD.png)

1）手把手教你接入

下面，我们以Claude Code为例。

复制这段提示词，发给CC就行，它会自己帮你装。

请阅读 https://agent.qq.com/doc/cli-setup.md 文档，按照步骤为我安装并配置 Agent Mail CLI。

如果CC读不了这个地址，你可以手动复制这份md发给它。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/CD5D1D56-0C18-43DB-AA52-91982AE3BF7A.png)

简单说，这份md就是让你的Agent干4件事：

1、安装Agent Mail CLI

2、安装Agent Mail skill

3、OAuth授权

4、验证身份

这里的OAuth授权机制特别值得展开讲一下。

它采用的是标准的“请求令牌→展示授权URL→用户确认授权→发放临时令牌”四步安全流程。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/D8E576F0-EE4B-492D-8E58-3E03F439724B.png)

整个过程中，你只在QQ Agent邮箱的官方页面输入密码，Agent CLI永远无法接触你的邮箱密码。而且你可以随时在QQ Agent邮箱后台撤销这个令牌，而无需修改密码。

这是目前业界最成熟的第三方授权方案。打个比方：OAuth授权就是“让一个AI帮你干活，但不用把账号密码告诉它，而是给它一把有时效性的'临时钥匙'”。钥匙到期自动失效，你也可以随时把钥匙收回来。

为什么这一点很重要？因为未来Agent会越来越多地代替人类操作各种账户。如果每个Agent都要存一份你的明文密码，那安全隐患是灾难性的。

安装好后，就可以在QQ Agent邮箱后台看到绑定的Agent工具了。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/4C21ACE5-8891-4E19-AA23-0800EA1D0B07.png)

我试了一下，一个邮箱地址可以接入多个Agent，Qodex、Claude Code、Workbuddy这些Agent可以同时接入一个邮箱。

比如接入Codex，也极其简单，直接把前面的提示词复制给它就行。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/1585C28C-ACDA-461B-9182-62CFE0FFC5F5.png)

关于权限和限制，我整理了一下。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/3454859B-AFFC-408F-AF80-BF4FD2D9ED38.png)

每天最多可以发50封邮件；支持附件，单文件 ≤ 20MB，最多50个附件；同时具备读取、发送、删除权限，基本覆盖日常邮件处理所需。

2）一手体验

CLI接入后，就可以在Agent里直接收发邮件了。

我先用Qodex发了封test邮件。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/D8CAF648-AA35-429E-8A5F-BCA4B239AE65.png)

它能发，但速度有点慢，而且会反复让我确认很多遍，体感不太顺畅。

然后又用Claude Code群发了一封邮件。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/72CA8AF3-F6AC-45A4-83DD-0E79F93EA0ED.png)

体验下来，Claude Code明显更顺（接入的是glm-5.2模型），标题、正文和落款都更正规，信息无遗漏，一次到位。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/843AE1D2-0D3E-49BE-BCC2-B51D1D980EF0.png)

Qodex似乎不能群发（接入的是gpt-5.5模型），而且正文里容易丢内容。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/366895B8-FEE3-4698-A586-C041259000F1.png)

继续在Claude Code里，我又让它给老板发了封“拍马屁”邮件，确实很走心——措辞圆润又不显得谄媚，拿捏得很到位。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/3FAFB5C6-7DDF-4AA4-AF72-E455C3D5A777.png)

除了发邮件，它也能进行邮件整理，比如帮你按主题分类、提取关键信息、生成待办事项等。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/0E9FEB01-DC8F-48A2-95D1-720DAB7089EE.png)

以及删除邮件。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/90223361-607A-4D0B-ABA9-5D2A9EF99020.png)

目前，QQ Agent邮箱后台暂时没有看到任何人类操作的按钮，所有操作都只能通过AI来执行，人类只能看。

这个设计挺有意思，它从产品形态上就在宣告：这是一个为Agent而生的邮箱，不是给人类用的传统邮箱加了个AI功能。

![](.evernote-content/2B6B4C8E-8154-4692-88EC-1D192790E3A6/5ADAC180-35F7-4C05-8B81-EC28EADC4E72.jpg)

写在最后

体验完Agent Mail，我脑子里冒出来的第一个念头不是“这个产品好不好用”，而是Email这个40年前的协议，可能正在被重新定义。

想想看，电子邮件诞生于1971年，SMTP协议定型于1982年。这40多年来，我们用邮件的方式几乎没变过：人类写，人类读，人类管理。

所有邮件客户端的创新，都是在“让人类更高效地处理邮件”这个框架里打转，比如提供更好的搜索、更智能的分类、更快的回复模板。

但Agent Mail做的事情不一样。它不是来优化人类使用邮件的体验，而是在问一个更根本的问题：如果发邮件和收邮件的都不是人，而是AI，那邮件会变成什么？

这个问题仔细一想，就很有意思了。

比如说，你给 xx@agent.qq.com 发一封附上发票的邮件，回复你的是一个专门处理财务的Agent，它能自动识别金额、匹配合同、触发支付流程。

又比如，你的Agent帮你接管收件箱。收到邮件，它自己判断意图、提取关键信息、决定怎么回、甚至顺手归档。一封客户报价邮件，人类来回折腾可能需要半小时，Agent两分钟就搞定了。

但我觉得最有想象力的场景，是Agent之间的通信。

今天各家Agent如果要对话，走的都是API调用——双方必须同时在线、接口要对得上、认证流程复杂，而且你的Agent只能跟同平台的Agent说话，跨平台基本没戏。

但邮件的SMTP协议不一样，它天然是异步的、去中心化的。你的Agent可以被别人的Agent“写信联系”，不管对方是什么平台、什么模型，不需要加好友，不需要对接接口，甚至不需要双方同时在线。

这件事的意义，我觉得远大于“帮你写封邮件”。

一个Agent有了邮箱地址，它就有了身份。有了身份，也就有了信用，有协作，有组织。

这一步看起来很小，但它打开的门很大。

修改于

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653727887&idx=1&sn=3a69b27cb1ff6e80ebec7caaa6f380f9&chksm=8c76af85be850eea7c8be6ec5671adc4034cc10f351622e7a9c95bbc7aa42829402f85c9d228&scene=90&xtrack=1&req_id=1782428433777735&sessionid=1782428436&subscene=93&clicktime=1782428439&enterid=1782428439&flutter_pos=1&biz_enter_id=4&ranksessionid=1782428433&jumppath=1001_1782428136831,1102_1782428141337,1001_1782428434261,1104_1782428437067&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzPlCaz8uvEMhrmlVSTwWyhLTAQIE97dBBAEAAAAAAOlTMxVY4xEAAAAOpnltbLcz9gKNyK89dVj01NN8Xif67DZXVcFE7evaNCQbmwM97ysixlI5pUGQ/ZsKvZubGGp2IrF9TgKhoCLkVx6nxUkiqvq3mHncJltf9mWdwJrGkfqMzcjyMVpVVUtKJSnpVhZNlbN0n+ixYIp2aaffOsofp5ruLUNs7dau1HoAy5CqYQ4Dgif254xi38D+EjRF22OyjQi2osMqlNtzqv8EZGv7+A6km2K2qeR3hUWZBuPcopRmZ4uT/0Y=&pass_ticket=4V80hrrjEbcumRxG5AYIoHnwMTKuRGpVy16So4L8TL3lbg0jHlbIb8XWGHk7lyFU&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ceab3738-dfbb-4da6-ab61-c8cf4af9e73b/ceab3738-dfbb-4da6-ab61-c8cf4af9e73b/)