# Codex App 官方白皮书！10 个你今天就能抄的小技巧

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518462&idx=1&sn=c205704c5a2526e1f4e0c3d37ea1c17c&chksm=e9d8263a4bfabdbeff30da62eb822e8d04239f274847b0ace7edace59d435ccd8111476b8c77&scene=90&xtrack=1&req_id=1782464553151955&sessionid=1782464512&subscene=93&clicktime=1782464561&enterid=1782464561&flutter_pos=3&biz_enter_id=4&ranksessionid=1782464553&jumppath=20020_1782464516486,1104_1782464550531,20020_1782464552196,1104_1782464557566&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2c&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQY5pELai2EVMe2CMUL7Cm4RLTAQIE97dBBAEAAAAAAA8cLh3WybsAAAAOpnltbLcz9gKNyK89dVj0k2h8oEDlKlgG5iKOSh6zSKwBW0C/0lKIyW1BXGQq34r26eVHgTQM4wDLf7qOpy/75xP5KzF/tjWw3Ma21Mbd0K+vBlKs/EZj3/mpBewAo+CcnheH2ZGKJNNTJ11iCCkrJydyeOMD3gSp3dcvKruuAO2NcAHddcLWz+0k0EBoiHkGXXnMy1WWic5VI/zGbcQ8b0BJAQ8I2A4HiLZBhnGjJeUi0dDnTTAHMMHCSXE=&pass_ticket=/Qq1p0/jkR03akdW++oDug9OBe7QMM0K4DKb9j0zpRGTqs2ZuvMkiUEPXI/yjIZE&wx_header=3)

Original字节笔记本字节笔记本

OpenAI 发了一份 Codex 白皮书，标题叫"Codex-maxxing"。（下载见文尾）

这份白皮书的主要内容关于如何让桌面版 Codex真正替你干活的操作手册。

它在开篇就提出了一个判断：大多数人用 AI 还停留在"问一个问题，等一个回答"。

但工作不是这样运转的，工作是循环的，是跨天的，是需要记住昨天说了什么、今天还差什么的。

白皮书把这套思路拆成了 10 个具体动作，逐一拆分，每一条翻译成你今天就能照着做的步骤。

**01 给每条重要工作线开一个置顶对话**

打开 Codex，想想你手头有哪些事情是会反复回来处理的，它可以是一个正在推进的项目、一个需要持续跟进的客户、一个你在维护的代码库。

给它单独开一条对话，在对话列表里手动置顶。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/C83A677F-5F88-46F3-B7FB-944AC9C9B1A2.jpg)

然后在这条对话的第一条消息里，写清楚这件事的背景，它是什么、现在进展到哪、你的偏好和约束是什么。

之后每次回来，继续在这条对话里说，不要新建。

这样的好处是你不用每次都重新解释一遍"我这个项目是做什么的"。上下文在那里，接着说就行。

**02 用语音代替打字**

Codex APP 提供了免费的语音输入功能。

下次你有一个模糊的想法或者指令，不要等想清楚了再打字，直接按 Codex 输入框旁边的麦克风，说出来。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/806D60D9-1161-47E2-A612-7B5544D76C7D.png)

可以说"那个……上周好像有人提过一个方案……我记不清了……你帮我整理一下"。

也可以说"这个页面感觉哪里不对，但我说不清楚，你帮我看看"。

语音的价值不是速度，是你说出来的东西更接近真实想法，没有经过打字时的自我审查。

说完直接发，让它去处理。你会发现结果往往比你费尽心机打字来描述更好。

**03 在它还在跑的时候追加指令**

发出任务之后不要关掉窗口走人，边看它做，边随时插话。

Steering 是 GPT-5.3-Codex 就引入的实时交互功能。

Codex 在工作的过程当中会频繁更新进度，你完全不需要等待最终的输出，可以随时介入，随时提问，然后讨论它的思路以及方向，引导到你需要的地方。

Codex APP 会边做边说明自己在干什么，然后响应你的反馈，同时保持全程的同步。

**04 把记忆变成一个你能打开、能编辑的文件**

在你的 GitHub 上新建一个仓库，就叫 `memory` 或者 `vault`。里面建几个文件：`people.md` 记你经常的偏好和背景，`projects/` 文件夹下每个项目一个文件记进展和决定，`decisions.md` 记重要决策和原因，`todo.md` 记跨项目的待办。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/F80EC561-5531-4B10-85FF-DCE574215262.png)

然后告诉 Codex，"我有一个记忆库在 GitHub 上，链接是 XX。每次对话结束前，把这次对话里值得记住的东西更新进去。"

这样你能用 GitHub 的 diff 功能看到它每次记了什么，记错了就改，记漏了就补。

这比对话历史靠谱得多。

**05 搞清楚它能用什么工具，分别用在什么场景**

在给 Codex 布置任务之前，先判断这个任务需要什么：

如果是本地跑起来的网页、预览页面、想让它截图标注，就在任务里写"用浏览器打开 localhost:3000"。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/1753DFA8-19D3-4E4E-A0FB-2393BE0122BE.png)

如果任务需要登录你的账号才能操作，比如在你的 GitHub 里提 Issue、在你的 Notion 里新建页面，就在 Codex 设置里先连好对应的连接器，然后直接说"去我的 GitHub 仓库把这个 Issue 关掉"。

如果实在只能通过点界面来完成，才考虑用 computer use，但要把权限控制清楚，不要让它随便乱点。

**06 手机远程**

把一个需要跑一段时间的任务发给 Codex，然后去干别的事。

在任务描述里提前说好"做到哪一步需要我确认，做到哪一步可以自己决定"。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/A25A77F9-38AE-4ADD-84BB-EFDCD6FDABCB.png)

等你去吃饭或者开完会回来，用手机打开 Codex，看它做到哪了。

如果需要你拍板，说"批准，继续"或者"这里改一下，改成 XX，然后继续"。

要让这个流程跑通，有一个前提，任务描述里要把"什么情况需要暂停等我"写清楚，不然它要么一直等你。

**07 定时任务**

在 Codex 的对话里直接说"设置一个定时任务"，然后描述你想要的频率和内容。

比如白皮书里的例子："每 30 分钟检查一次我的 Slack 和 Gmail，找出可能需要我回复的未读消息，整理背景，起草回复，但不要发送，等我批准。"

或者针对你的场景："每天早上 9 点检查我们的 GitHub 仓库，看看有没有新的 Issue 或者 PR，给我一个摘要，标出哪些需要我今天处理。"

说完之后 Codex 会创建这个定时器，告诉你它叫什么名字、频率是多少。之后它就会按节奏自己跑，不需要你每次手动触发。

**08 loop 循环**

白皮书给了三个真实的使用循环，照着自己的场景找一个最像的，直接复制这个结构：

**幕僚助手循环**：你每天要处理大量消息。让 Codex 按时去巡查，整理出需要回复的，查清楚背景，起草回复，然后等你来拍板发不发。你只做最后的判断，不做整理和起草。

**监控反馈循环**：你有一个持续迭代的作品（代码、设计、文章）需要收集外部反馈。让 Codex 定时去指定地方（Slack 频道、表单、评论区）汇总反馈，整理成摘要，标出需要改动的地方，你来做创意判断。

**等待处理循环**：你有一件事卡在等别人那里，比如等客服回复、等审批通过、等对方更新文档。让 Codex 每隔几分钟检查一次状态，一旦有变化就准备好下一步动作等你批准，而不是你自己去一遍一遍刷新。

三个循环的共同逻辑：它准备，你决定。

**09 Goal 指令**

[Codex&Claude Code的 /goal 指令的高级进阶使用技巧](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516287&idx=1&sn=b09eacc8e7f33cc93a927bc063a28fe7&payreadticket=HPoyFC56AkoAFTqo7xMk_kce2-_Pm-34miD29rMceIIT3A2rECPVdBpGml2WsR9oFkMyDnE&scene=21#wechat_redirect)

下次布置任务时，在最后加一句"完成的标准是 XX"。

比如不要说"帮我重构这个模块"，改成"帮我重构这个模块，完成标准是：原有的单元测试全部通过，没有新增测试失败，改动点都有注释说明，然后给我看 diff"。

不要说"帮我写一篇文章"，改成"帮我写一篇文章，完成标准是：不超过 1500 字，有一个开头场景，三个核心论点各有一个具体例子，结尾有明确行动建议，写完给我看"。

有了可核验的标准，它可以自己检查自己做没做到，不用你来反复提醒。

**10 侧边面板当成协作界面**

当 Codex 在侧边面板里生成了一个文档、网页或者表格，不要只是看完关掉。

![](.evernote-content/E4CF8548-676A-496E-845C-3529D69933AA/E4C65F33-82FB-44D3-BF21-23F6E4267E67.png)

直接在侧边面板上点评论或者回到对话框说"第三段逻辑有问题，改成从用户视角出发"，"这个表格第二列的公式不对，应该是 XX"，"这个颜色太亮了，换成深色系"。

你的评论直接变成它的下一条指令，成品本身就是下一轮迭代的上下文。

Markdown 文档可以在里面直接批注。表格可以渲染公式和编辑单元格。

HTML 页面可以在应用内浏览器里跑起来交互。

幻灯片可以不离开应用就创建和审阅。

这十个动作，本质上是同一件事的十个切面，把 AI 从一个回答问题的工具，变成一个能持续推进工作的系统。

单次提示能解决单个问题，但循环才能推进项目。[Loop Engineering 解析&应用案例](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518081&idx=1&sn=8882884596a51004fe5b9a3d68e4aeb9&payreadticket=HD6_gyxFybY3uqr_m1wcLR1lda013pN7_o9rOWQ3QieIJlwJvOhLc_0oc5-zU64JAURYqnA&scene=21#wechat_redirect)

白皮书的英文标题叫 Codex-maxxing。Maxxing 的意思是把某件事用到极致。

掌握这十个最最基础的技巧，可以帮助你更好地发挥 Codex 的极致功能。

原版的中英文白皮书下载地址：

https://link.bytenote.net/note

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518462&idx=1&sn=c205704c5a2526e1f4e0c3d37ea1c17c&chksm=e9d8263a4bfabdbeff30da62eb822e8d04239f274847b0ace7edace59d435ccd8111476b8c77&scene=90&xtrack=1&req_id=1782464553151955&sessionid=1782464512&subscene=93&clicktime=1782464561&enterid=1782464561&flutter_pos=3&biz_enter_id=4&ranksessionid=1782464553&jumppath=20020_1782464516486,1104_1782464550531,20020_1782464552196,1104_1782464557566&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2c&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQY5pELai2EVMe2CMUL7Cm4RLTAQIE97dBBAEAAAAAAA8cLh3WybsAAAAOpnltbLcz9gKNyK89dVj0k2h8oEDlKlgG5iKOSh6zSKwBW0C/0lKIyW1BXGQq34r26eVHgTQM4wDLf7qOpy/75xP5KzF/tjWw3Ma21Mbd0K+vBlKs/EZj3/mpBewAo+CcnheH2ZGKJNNTJ11iCCkrJydyeOMD3gSp3dcvKruuAO2NcAHddcLWz+0k0EBoiHkGXXnMy1WWic5VI/zGbcQ8b0BJAQ8I2A4HiLZBhnGjJeUi0dDnTTAHMMHCSXE=&pass_ticket=/Qq1p0/jkR03akdW++oDug9OBe7QMM0K4DKb9j0zpRGTqs2ZuvMkiUEPXI/yjIZE&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/638db8e6-1c1a-419c-b07c-8fc44d123ddd/638db8e6-1c1a-419c-b07c-8fc44d123ddd/)