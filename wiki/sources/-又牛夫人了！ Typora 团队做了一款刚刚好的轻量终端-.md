---
title: "又牛夫人了！ Typora 团队做了一款刚刚好的轻量终端"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/又牛夫人了！ Typora 团队做了一款刚刚好的轻量终端.md
tags: [evernote, impression]
---

---
title: "又牛夫人了！ Typora 团队做了一款刚刚好的轻量终端"
source: evernote
type: note
export_date: 2026-06-23
guid: 36c56fb8-d111-4a0d-95ea-17ac6fd9d97f
---

# 又牛夫人了！ Typora 团队做了一款刚刚好的轻量终端

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518318&idx=1&sn=57a3876ffc42004d9c8d330103ccdd34&chksm=e99df7802de2c81d2ba612f340cde9176a1fa21b6c9f6bc6ab86e31b375c1fe7bf53ddb14690&scene=90&xtrack=1&req_id=1782085210518524&sessionid=1782085036&subscene=93&clicktime=1782085379&enterid=1782085379&flutter_pos=3&biz_enter_id=4&ranksessionid=1782085210&jumppath=20020_1782085059955,1104_1782085202601,20020_1782085210052,1104_1782085358464&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQPzt7EvqSMJm4g0RCXePtfhLTAQIE97dBBAEAAAAAAHhrEpeYrQcAAAAOpnltbLcz9gKNyK89dVj0dExSzoN2jxkPR7XHdlli+gywlYvsLGybnt25EQFJpVdHjpzUxoaUsTOV1MICH/A0aQQQAaoNijGffFs8J5pTF8aKCduxYxbIy5Nw/g6KJ4ggddQ2F6RcvTAIH1uaMH84gcVaUXz4Q+y0zMkvc5kBA1zEdGCTj8QDPcSF8LQAO6QcTV68L01XaCi5GA7kA8RQWLF8kHI/P68KrCnX+WSmtOQfVm95UlhqcUGgXwI=&pass_ticket=54E4Eaokac/bwVtLNFKhdC8F8oseekeHytt6fzhppwxf9qF4HLqXoi6mgQC2hcqG&wx_header=3)

Original字节笔记本 字节笔记本

这几个月我大概试了不下十几款的 Agent 的 CLI 工具。

开源的、闭源的都有，不过用下来还是回到 iTerm2， 像 Warp、Superset、Orca 等等这些功能都很强，跑Codex、看日志、临时改配置时，还是太重了。

今天试了 Otty，第一感觉是，这才是我的小甜甜。

![](attachments/f5a5dc89ffc30e2a.png)

Otty 来自 Typora 背后的团队。继承了 Typora 一贯的气质，界面克制，细节柔和，不瞎堆功能。

打开Otty就找到了我最需要的一个需求，多标签不用再选择是侧栏还是顶栏，横竖都可以。

各种小细节拉满。在测试项目里跑了常规命令：进入目录、查看文件、执行 `git status`，再跑一段 Node 脚本。输出的提示符里能看到分支、脏文件和运行环境信息全部一览无余。

![](attachments/a6d0efc6592e002c.png)

让我最有感觉的是标签页和分屏。

多个标签可以保留不同任务上下文，左右分屏后，一个窗口里同时放服务日志、Git 状态和临时命令，切换成本很低。它比普通终端多一点工作台感，没有完整 IDE 的负担。

![](attachments/5ffe1aca559fc0ba.png)

Otty 的标签详情入口也很实用。

点开后能看到当前工作目录、复制路径、在 Finder 中显示、Git、分屏、查找、命令面板等操作。

非常适合多个项目之间切换，很多原本要靠 `pwd`、Finder、编辑器来回配合的动作，现在可以直接在终端里完成。

![](attachments/6ce0c54badf336f4.png)

文件浏览器不是完整 IDE 的项目树，更像一个轻量文件视图，看 README、确认目录结构、找配置文件很方便。

对只是想临时看一眼，不想打开编辑器的场景，它刚好够用。

![](attachments/8cae63a88aa5afea.png)

还试了内置文件编辑器，写 Markdown、临时改 TOML 配置都没问题。

Otty不是准备做专业代码编辑器的替代品，适合记录命令笔记、改小配置、快速检查文本。

![](attachments/7a05596fb2db0511.png)

菜单里还能看到 Recipe、主题、快速打开、Git、文件、详情面板等入口，说明它的目标很清楚，服务多项目、多命令、多 Agent 的现代开发工作流。

Otty 比 iTerm 这类传统终端更现代，比 Agentic IDE 更轻，又比纯终端多了一点必要上下文，极低的内存占用。

天天用 Claude Code、Codex、OpenCode 这类工具，又不想每天开一个沉重的 IDE，Otty 值得试一下，目前完全免费，全端可用。
