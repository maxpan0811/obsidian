# 实测用Obsidian+Claude搭了套AI笔记系统，同事以为我开了挂。

---

原文链接: [https://mp.weixin.qq.com/s?chksm=ea91ec94dde665821a552c8ada595ab...](https://mp.weixin.qq.com/s?chksm=ea91ec94dde665821a552c8ada595ab37461c6705d8015861ac9b7bc25325572a4ec5e1274a5&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1775391857_1&req_id=1775391857551910&scene=169&mid=2247485705&sn=01338dbead128130efd2635e1c87b1ad&idx=1&__biz=MzI2NjI2OTkzOA==&sessionid=1775391210&subscene=200&clicktime=1775392282&enterid=1775392282&flutter_pos=13&biz_enter_id=5&jumppath=20020_1775392266961,1122_1775392268357,20020_1775392274504,1104_1775392275827&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/cJWkzOjO1mCxZozfiJ1qhLTAQIE97dBBAEAAAAAAEJPNpVVEmEAAAAOpnltbLcz9gKNyK89dVj0dj97LlmBKZdScWJA4/ekdumMGM3dyGOXN9us/cOuxuVZlnbzhU1iH2at1tKmI4amqf+V9/Hdm3/vQAeBO6yke4DBEka79GFfT91kWc4Qa/KyL8y9nFcmYGgQIxJVZaFYPskt+GbFGzMtkOqC7SuEvohgQAg7TtnQ+WeXMF6WVW/xaOEdDTxWKcOjMP+8+5Ii58gNLU4je6djfBReTXzhudnwFiN4vdCEdZzrbKk=&pass_ticket=Tsc//BWuvkkylYXp2PlRX6fcV6JiE0TOG5EeZvW8O0y6h2yNrL2EfLqIchAt53Dy&wx_header=3)

OriginalDavid 小行家AI陪跑

2026年3月，动手搭建实测先看结果：Obsidian（本地笔记）+ Claudian（AI插件）+ Skills（AI技能包）=一个会自己思考的笔记系统。每月成本：一杯美式（$3-5）。

![](.evernote-content/E8C1F989-8098-4CB6-A3DD-C1CC50E5FBF4/72F096F4-7DEA-490F-9C95-8ADD3F59FE6E.png)

**说实话，我之前也是个「笔记难民」。**

Notion太重，语雀锁数据，飞书文档AI能力拉胯，Apple Notes连个双链都没有。

直到我看了**Obsidian+Claude+Skills+云同步**跑通了——从此以后，我的笔记会「思考」了。

开完会，AI 2分钟整理好会议纪要并自动提取待办。周五下午输入/weekly，3秒一份周报。收件箱堆了50条碎片笔记，一句话全部归档。

这不是未来，这是现在就能用的东西。

今天我把完整搭建过程和6个真实使用场景全部拆解出来。

**照着做就行，不需要写一行代码。**

你的笔记系统，
-------

是不是也有这些病？
---------

![](.evernote-content/E8C1F989-8098-4CB6-A3DD-C1CC50E5FBF4/B57760CB-F86F-42C8-9797-6C789D701CEB.png)

左边的场景，**你中了几条？**

会议记录散落在微信、邮件、备忘录、飞书、钉钉五个地方。收藏的好文章越来越多，但你永远不会回头看。周五写周报的时候，怎么也想不起来这周到底干了什么。

核心问题就一个：

*你的笔记只会「存」，不会「想」。*

右边是加上AI之后的样子。不是你去整理笔记，而是笔记自己整理自己。

这套系统长啥样？
--------

四层架构，一张图说清
----------

![](.evernote-content/E8C1F989-8098-4CB6-A3DD-C1CC50E5FBF4/506A4D67-A82F-4284-B6D0-C26A6069CE7D.png)

**一句话总结每一层的分工：**

**存储层**（Obsidian）——你的笔记都是本地.md文件，永远不会被平台绑架。支持双链、Canvas画布、Base数据库。

**AI 引擎**（Claudian 插件）——在Obsidian里直接和Claude对话。支持Chat模式、内联编辑、Plan模式和自定义斜杠命令。

**技能层**（Skills）——教AI怎么正确操作你的Obsidian笔记。Obsidian CEO亲自开源的官方技能包，GitHub 18.5k stars。

**同步层** —— iCloud / 坚果云 / Remotely Save / Git，选一个就行。

还有一个贯穿全局的CLAUDE.md文件，相当于给AI写了一份「你的大脑使用说明书」，告诉它你的仓库结构、写作习惯和当前工作重点。

20分钟搭完，5步搞定
-----------

别被技术感吓到。整个过程比注册一个Notion账号还简单：

### Step 1：装Obsidian（2分钟）

去obsidian.md下载安装，创建一个仓库就行。

为什么选Obsidian？三个字：**不锁你**。

所有笔记都是你电脑上的.md文件。哪天Obsidian倒了，你的数据一个字都不会丢。而且双链系统天然形成知识图谱，加上2025年新出的Base数据库功能，已经有Notion 80%的能力了。

### Step 2：装Claudian插件（5分钟）

Claudian是让你在Obsidian里直接用Claude AI的插件。去GitHub下载三个文件，扔到插件目录，重启就好。

装完之后你能干什么？

* **Chat 模式**：侧边栏弹出对话窗口，自动带上当前笔记作为上下文
* 内联编辑：选中一段文字按快捷键，AI 直接在原文上改
* @**引用**：输入@拉入其他文件，说「参考那篇会议纪要帮我写总结」
* 斜杠命令：设置好 /weekly 一键生成周报，/today 一键日报
* Plan**模式**：按Shift+Tab，让AI先想清楚再动手

### Step 3：安装官方 Skills（3 分钟）

Skills 是关键一步——它们教AI怎么「正确地」操作Obsidian。

Obsidian CEO Stephan Ango亲自开源了一套：

cd /你的仓库路径

npx skills add git@github.com:kepano/obsidian-skills.git

5个技能包各管各的：

* Markdown ——理解 [[双链]]、Callouts、YAML属性
* Bases ——操作Base数据库，建看板、写公式
* Canvas ——在画布上画节点、连线、思维导图
* CLI——命令行批量操作数百个文件
* Defuddle ——从网页提取干净Markdown，省token

### Step 4：写CLAUDE.md（10分钟）

在仓库根目录创建CLAUDE.md，告诉AI你的仓库长什么样。

# 我的笔记系统

## 仓库结构

- /Daily/ - 每日日记，格式 YYYY-MM-DD.md

- /Projects/ - 项目笔记，按项目名分子文件夹

- /Knowledge/ - 知识卡片

- /Inbox/ - 待整理的临时笔记

## 写作习惯

- 中文书写，标题最多三级

- 每篇笔记用 YAML 属性标注 tags 和 date

- 用 [[双链]] 关联相关内容

## 当前重点

- 正在做：XXX 产品 v2.0

- 本周目标：完成用户调研报告

这一步越具体，AI 干活就越精准。

### Step 5：配云同步（5分钟）

* 苹果全家桶：iCloud，零配置
* 国内全平台：坚果云+官方插件，稳定靠谱
* 技术玩家：Remotely Save+腾讯云COS
* 程序员：Obsidian Git插件，自动push+版本控制

6个真实场景，看完你就离不开了
---------------

搭建只是开始。**真正让你上瘾的，是下面这些场景。**

![](.evernote-content/E8C1F989-8098-4CB6-A3DD-C1CC50E5FBF4/F6C2D4F1-C00E-4589-BCE7-5F9D4D8A34A3.png)

### 场景一：会议纪要——2分钟搞定

开完 1 小时的会，你随手记了一堆乱七八糟的要点。以前整理至少要 20 分钟。

现在打开 Claudian，说一句：

*帮我把这篇会议记录整理成结构化格式，提取 Action Items，在 /Projects/XXX/ 下给每个待办创建单独笔记，用双链关联回来。*

2 分钟，格式化纪要 + 待办清单 + 独立任务笔记 + 自动双链，全部搞定。

**省下来的不只是时间，是心智负担。**

---

### 场景二：周报 —— 输入 /weekly，下班

这是我最爱的功能。自定义一个斜杠命令 /weekly，背后的 Skill 模板会：

扫描本周修改过的所有笔记 → 按项目分组 → 提取关键进展和待办 → 生成标准周报格式

**每周五下午 3 秒钟一份周报。再也不用翻记录回忆这周干了啥。**

---

### 场景三：知识卡片 —— 读完即沉淀

看到一篇好文章，以前的流程：复制→粘贴→手动整理→打标签→找相关笔记→手动建链接。

现在一句话：

*把这篇文章的核心观点提取出来，创建知识卡片，自动添加标签，关联到仓库里已有的相关笔记。*

AI会扫描你的知识库，找到相关内容，帮你建好Wikilinks。

**知识不再是孤岛，而是自动编织成网络。**

---

### 场景四：Canvas 架构图 —— 边想边画

需要画一个功能模块图？别开Figma 了：

*根据 /Projects/feature-req.md 的需求文档，在 Canvas 上创建模块架构图，标注依赖关系。*

Claude 直接在 Obsidian Canvas 里画好节点和连线。**思考和记录在同一个地方完成。**

---

### 场景五：收件箱清零 —— 50 条笔记 5 分钟

收件箱堆了 50 条没整理的碎片笔记？以前你可能会假装看不到。

现在：

*把 /Inbox/ 里所有笔记按主题分类，移动到对应文件夹，给每篇添加tags和date。*

5 分钟，50 条笔记全部归档。

**AI 的耐心是无限的，你的不是。**

---

### 场景六：每日回顾 —— 输入 /today

下班前：

*/today*

Claude 自动汇总今天修改过的所有笔记，生成进展摘要，顺带给出明天的工作建议。

进阶：让系统更强的3个技巧
-------------

**自定义Skills**

在.claude/skills/下创建新文件夹，写一个SKILL.md定义专属技能。比如「客户邮件起草器」「读书笔记生成器」「技术方案评审模板」。

**MCP扩展**

通过MCP协议，Claude可以连接外部工具——Google Drive同步文档、YouTube提取视频做笔记、网页剪藏一键入库。

**安全分级**

* **Safe模式**（推荐）：每次操作都需要你确认
* Plan**模式**：先出方案，你批准了再执行
* YOLO**模式**：完全自动化，适合你完全信任的场景

费用？每月一杯咖啡钱
----------

![](.evernote-content/E8C1F989-8098-4CB6-A3DD-C1CC50E5FBF4/2EFB5144-9D16-431E-B10F-094A47754C1D.png)

* Obsidian个人免费，Skills 开源免费，云同步有免费额度
* 唯一的费用是Claude API，日常笔记整理大概每月$3-5

**总成本：每月一杯美式。**

你可能还想问的
-------

**Q：不会写代码也能用吗？**

完全可以。Claudian 有图形界面，Skills 一行命令装好，日常就是跟 AI 聊天。

**Q：AI 会不会把我笔记搞乱？**

建议用 Safe 模式，每次操作前都会让你确认。所有笔记都是本地文件，随时可以回退。

**Q：跟 Notion AI 比呢？**

最大区别：**数据在你手里。** Obsidian 的笔记就是本地 .md 文件，永远不会被平台绑架。而且 Claude 的能力目前显著强于 Notion AI。

**Q：手机上能用吗？**

Claudian目前支持桌面端。手机通过云同步查看和编辑AI整理好的笔记就行。

写在最后
----

这套系统的核心理念只有一句话：

*让AI处理机械劳动，让你专注于思考。*

你不需要一步到位。从装Obsidian+Claudian开始，用起来之后再慢慢加Skills和同步。

当你第一次用一句话整理好一篇杂乱的会议纪要时，你就会明白这套系统的价值。

**搭一次，用一辈子。**

*相关资源：*Obsidian官方Skills*|*Claudian插件*|*工作流指南

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=ea91ec94dde665821a552c8ada595ab37461c6705d8015861ac9b7bc25325572a4ec5e1274a5&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1775391857_1&req_id=1775391857551910&scene=169&mid=2247485705&sn=01338dbead128130efd2635e1c87b1ad&idx=1&__biz=MzI2NjI2OTkzOA==&sessionid=1775391210&subscene=200&clicktime=1775392282&enterid=1775392282&flutter_pos=13&biz_enter_id=5&jumppath=20020_1775392266961,1122_1775392268357,20020_1775392274504,1104_1775392275827&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/cJWkzOjO1mCxZozfiJ1qhLTAQIE97dBBAEAAAAAAEJPNpVVEmEAAAAOpnltbLcz9gKNyK89dVj0dj97LlmBKZdScWJA4/ekdumMGM3dyGOXN9us/cOuxuVZlnbzhU1iH2at1tKmI4amqf+V9/Hdm3/vQAeBO6yke4DBEka79GFfT91kWc4Qa/KyL8y9nFcmYGgQIxJVZaFYPskt+GbFGzMtkOqC7SuEvohgQAg7TtnQ+WeXMF6WVW/xaOEdDTxWKcOjMP+8+5Ii58gNLU4je6djfBReTXzhudnwFiN4vdCEdZzrbKk=&pass_ticket=Tsc//BWuvkkylYXp2PlRX6fcV6JiE0TOG5EeZvW8O0y6h2yNrL2EfLqIchAt53Dy&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6b8765ad-356d-4051-8af8-706c0116a39d/6b8765ad-356d-4051-8af8-706c0116a39d/)