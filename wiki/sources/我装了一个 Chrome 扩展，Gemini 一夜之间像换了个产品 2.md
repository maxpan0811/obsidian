---
title: 我装了一个 Chrome 扩展，Gemini 一夜之间像换了个产品 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/我装了一个 Chrome 扩展，Gemini 一夜之间像换了个产品 2.md
tags: [evernote, impression, yinxiang]
---

# 我装了一个 Chrome 扩展，Gemini 一夜之间像换了个产品

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjMzODE4NA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjMzODE4NA==&mid=2247489244&idx=1&sn=f35822530d3fb21061c74b918b72662a&chksm=f1e668680bcc5ee101c1da84b15df3a46fb05d7f71ba7ce528940652d14e7b73aba423515160&scene=90&xtrack=1&req_id=1777208463663323&sessionid=1777208476&subscene=93&clicktime=1777208481&enterid=1777208481&flutter_pos=0&biz_enter_id=4&ranksessionid=1777208463&jumppath=1001_1777208156389,1101_1777208462903,1001_1777208474296,1104_1777208477285&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=1800472c&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ41dohJvqVzq5ipT+e9/rTRLVAQIE97dBBAEAAAAAADu4MAjpp9MAAAAOpnltbLcz9gKNyK89dVj02epH2dsJ6IMrnMowcJrK0C2SyCA8tPVFyMAYf96RRUUeaI/JxLHHe6QeY8UQ5ttOeY6EuLqWbonrJk5Dyg89bluX3SdIiNeckvVU4IgIqeEvnSRre4UnUo6OstH+4wewP7cx6tBkvSWuv1N93RYy9ZhOCVHxJ7jnIR/bRB+QFCPB6VfvbYgNK3NLVTcD/qgbELe9WKwU+45fjj3ab0DTMwTxfY7rkbaPsq39waGWXg==&pass_ticket=MIz4r7+6qdI3pxHwH8KGPLPkohssLTYybqwG3fayOYPQbZm9c7futsZXrVyj5GiF&wx_header=3)

Original老刘的笔记本老刘的笔记本

---

我把日常 AI 主力从 ChatGPT 切到 Gemini，已经半年。

代码工作我还是用 Claude Code，但所有"思考型"的对话——研究、写作、菜谱、学习笔记、产品讨论——全都在 Gemini 上。

但有一件事一直让我憋着一股气——**Gemini 死活不做文件夹分类**。

ChatGPT 早就有了，连 Grok 都有了，**只有 Gemini 把所有对话全堆在一个滚动列表里**。

直到上周，我装了一个叫 **Voyager** 的 Chrome 扩展，前后用了一周——感觉 Gemini 像是被偷偷做了一次"系统级升级"。

下面这篇是我对它 7 个核心功能的实测笔记，外加一个我必须提醒你的真实风险。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/AC208409-5470-4DFC-B291-589AB104FB30.png)

一、缺了一年的"文件夹"，终于补上
-----------------

这是我装这个扩展的**唯一原因**，也是我留下来的唯一原因。

装好之后回到 Gemini，刷新一下页面，左侧的对话历史区多出了一个"+"按钮——点一下就能新建文件夹。

我立刻建了三个：

* • **菜谱** — 那些"用现有冰箱里这些食材做晚餐"的对话；
* • **研究** — 各种产品调研、技术调研的长对话；
* • **代码** — 偶尔丢给 Gemini 跑的小脚本和算法解释。

每一条历史对话点右边的三个点，会出来"移动到文件夹"选项。我花了 20 分钟，把过去半年积累的 200 多条对话**全部归类**——这是我半年来第一次能从历史记录里**快速找到东西**。

一个早就该有的功能，由一个第三方扩展补上，多少有点黑色幽默。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/1AB09796-A52A-4371-ACE2-DAAE460B2ECA.png)

二、多账号党的救星：硬隔离 + 手动同步
--------------------

我有两个 Gemini 账号——一个工作、一个个人。

光是文件夹分类还不够，**两个账号的文件夹必须互不污染**。否则我在工作账号里建好的"产品 A"文件夹，切到个人账号还会看到，那就乱套了。

Voyager 的"**硬隔离**"功能解决了这件事——它把每个账号的文件夹结构独立保存，**切换账号时文件夹也跟着切换**。

但同步是个权衡——它**不自动跨设备同步**。

它给的方案是：

* • 手动上传到我自己的 Google Drive；
* • 切到另一台电脑后，手动下载一次；
* • 或者更安全的方式——**导出 JSON 文件**，离线传到另一台电脑导入。

对一些不想把内部数据传到 Google Drive 的小公司用户来说，**JSON 离线方案是个非常体贴的备选**。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/61B9DFF6-8F40-4E8F-AF64-4598B02FE41D.png)

三、Prompt 管理器：我桌面上的便签全收编了
------------------------

我桌面上一直有一个叫 `prompts.txt` 的文件，存着我反复用的几十条 Prompt——SEO 标题模板、产品描述模板、SQL 优化提示词……

每次要用都得 Cmd+Tab 切窗口、复制、粘贴，繁琐到我自己都嫌弃。

Voyager 装好后，悬浮在 Gemini 页面右下角有一个绿色小图标——点开就是一个完整的 **Prompt 管理面板**：

* • 新增 Prompt，可加标签；
* • 按标签筛选；
* • 一键复制；
* • 云端同步（同样是手动上传到 Google Drive）。

我把 `prompts.txt` 的所有内容**全部迁了进去**，文件已经删了。

这种"小到不值得专门做一个产品"的功能，恰恰是 Chrome 扩展存在的最大意义。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/AC208409-5470-4DFC-B291-589AB104FB30.png)

四、引用回复：终于不用"复制-粘贴-再问"了
----------------------

这是一个我觉得**所有 AI 产品都该原生内置**的功能——但目前没有一家做。

以前我跟 Gemini 讨论一个长答案时，如果只想针对其中第二段追问，必须：

1. 1. 选中第二段；
2. 2. 复制；
3. 3. 粘贴到输入框；
4. 4. 加上引用符号；
5. 5. 再写追问。

Voyager 的方案优雅到让我合不上嘴：

* • 我**直接选中**回答里的某段文字；
* • 一个浮动的"引用回复"按钮跳出来；
* • 一点击，自动以 `>` 引用格式贴到输入框里；
* • 我直接接着写问题就行。

我后来意识到，**我每天和 AI 沟通有 60% 的时间，就是在做"针对某段追问"这件事**。这个小功能直接节省了我 30% 以上的对话时间。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/1AB09796-A52A-4371-ACE2-DAAE460B2ECA.png)

五、Fork 分支：从 Git 借来的优雅设计
-----------------------

如果你写过代码，Fork 这个词不用解释。

Voyager 把 Git 里的"分支"概念**搬到了对话里**。

具体场景：我和 Gemini 在讨论一个产品功能设计，已经聊到了第 12 轮。突然我想试一个完全不同的方向，但又**不想污染原来的对话主线**。

以前我会新开一个对话，把上下文重新粘一遍。

现在我点任何一条历史消息旁边的 **Fork 按钮**——它会自动:

* • 复制当前对话到这个分支点为止的所有上下文；
* • 开一个新对话；
* • 让我从这个分支点开始向另一个方向探索。

主线的对话**完全不被影响**。

我用它做了一件以前做不到的事——**一个对话同时探索 ABCD 四种产品方向**。每个分支独立成长，最后拉回主线对比哪条路径更优。这种"思维分形"的工作方式，**用任何其他 AI 工具都做不出来**。

这是一个**只有真正在重度使用 AI 的人**才会想出来的功能。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/61B9DFF6-8F40-4E8F-AF64-4598B02FE41D.png)

六、时间轴拖曳：长对话的回溯神器
----------------

我有一些对话已经长到 200+ 轮——比如那个聊了三周的"个人品牌策略"对话。

回溯里面某个观点是地狱级体验——上下滚屏一下就过头了。

Voyager 在右侧加了一个**可拖曳的时间轴**：

* • 每个轮次是一个节点；
* • 鼠标悬停显示问题预览；
* • 点节点直接跳到那一段；
* • 旁边还有一个搜索框，可以**搜历史问题里的关键词**。

我把"用户调研问卷的开放题怎么设计"这个问题在时间轴里搜出来——**3 秒**。

放在以前，我大概要滚 5 分钟。

更妙的是这个时间轴还支持**节点层级**——如果你的对话里有用 Fork 分出去过分支，时间轴上会清晰显示出"主线"和各个"侧支"的层次关系。我看了一眼自己最长的那个产品讨论对话，竟然已经分出了 5 个独立分支——**这是一种以前从未有过的思考密度可视化**。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/AC208409-5470-4DFC-B291-589AB104FB30.png)

七、一键导出 Markdown：Notion 用户的核武器
-----------------------------

这个功能我用得不多，但它出现的那一刻我意识到——**这才是真的懂用户的功能**。

Gemini 左上角多了一个导出按钮，下拉菜单里有：

* • PDF；
* • 图片；
* • **Markdown**。

Markdown 那个选项让我直接坐直了身体。

我把和 Gemini 聊出来的"竞品分析"对话**一键导出 Markdown**，扔进 Notion——格式干干净净，标题、列表、代码块全部正确解析，**几乎不需要二次整理**。

对所有用 Notion / Obsidian / Logseq 的用户来说，**这个功能本身就值这个扩展的价值**。

我现在的工作流变成了——**用 Gemini 做发散和讨论 → Voyager 一键导出 Markdown → Notion 二次整理成结构化资料**。整个链路从原来的 30 分钟手动复制粘贴，缩短到 2 分钟。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/1AB09796-A52A-4371-ACE2-DAAE460B2ECA.png)

八、一个我必须告诉你的真实风险
---------------

写到这里我必须做一个**冷静的提醒**——这个扩展是**第三方免费产品**。

它不是 Gemini 官方的功能，意味着：

* • Gemini 一旦有大版本 UI 更新，**Voyager 可能立刻失效**；
* • 失效时表现可能是文件夹消失、按钮错位、整个 Gemini 界面卡顿；
* • 排查方法很简单——**先把 Voyager 禁用一下**看 Gemini 是否恢复正常；
* • 然后等作者更新（通常一两周内会跟进）。

更深一层的风险是——**这是一个独立开发者的"公益项目"**。

万一哪天他不更新了，Gemini 又升级了——**我们手里的所有文件夹分类、Prompt 库、对话备份都可能瞬间用不了**。

我的建议是：**用 JSON 离线导出做定期本地备份**，至少不会丢数据。

![](.evernote-content/B6D1B0C9-EF90-48E6-831A-6DAFFFA3BF5A/61B9DFF6-8F40-4E8F-AF64-4598B02FE41D.png)

九、写在最后：给所有 Gemini 重度用户的建议
-------------------------

如果你和我一样把 Gemini 当作日常主力 AI——**强烈建议立刻装一下 Voyager**。

它补齐的不是"锦上添花"的功能，而是**Gemini 本该自带、但偏偏没做的核心生产力工具**。

如果你只是偶尔用一下 Gemini，没什么积累——你可能感受不到它的价值。

但如果你的对话历史已经多到滚不到底，Prompt 复制粘贴已经成了肌肉记忆——**装上它的第一天，你会有一种"原来 Gemini 该长这样"的恍惚感**。

一个产品该有的功能没做出来，反而被第三方补全——这件事本身，比 Voyager 的任何一个功能都更值得思考。

如果你看完觉得有启发，**请点赞、在看、转发**，让更多还在 Gemini 滚动列表里苦苦寻找历史对话的朋友看到这篇文章。

防止走丢，记得给我加个⭐️。

#Gemini #Chrome扩展 #AI工具 #生产力 #Voyager

作者提示: 内容由AI生成

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjMzODE4NA==&mid=2247489244&idx=1&sn=f35822530d3fb21061c74b918b72662a&chksm=f1e668680bcc5ee101c1da84b15df3a46fb05d7f71ba7ce528940652d14e7b73aba423515160&scene=90&xtrack=1&req_id=1777208463663323&sessionid=1777208476&subscene=93&clicktime=1777208481&enterid=1777208481&flutter_pos=0&biz_enter_id=4&ranksessionid=1777208463&jumppath=1001_1777208156389,1101_1777208462903,1001_1777208474296,1104_1777208477285&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=1800472c&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ41dohJvqVzq5ipT+e9/rTRLVAQIE97dBBAEAAAAAADu4MAjpp9MAAAAOpnltbLcz9gKNyK89dVj02epH2dsJ6IMrnMowcJrK0C2SyCA8tPVFyMAYf96RRUUeaI/JxLHHe6QeY8UQ5ttOeY6EuLqWbonrJk5Dyg89bluX3SdIiNeckvVU4IgIqeEvnSRre4UnUo6OstH+4wewP7cx6tBkvSWuv1N93RYy9ZhOCVHxJ7jnIR/bRB+QFCPB6VfvbYgNK3NLVTcD/qgbELe9WKwU+45fjj3ab0DTMwTxfY7rkbaPsq39waGWXg==&pass_ticket=MIz4r7+6qdI3pxHwH8KGPLPkohssLTYybqwG3fayOYPQbZm9c7futsZXrVyj5GiF&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/016315d7-1e44-4006-863b-0c570166cda3/016315d7-1e44-4006-863b-0c570166cda3/)
