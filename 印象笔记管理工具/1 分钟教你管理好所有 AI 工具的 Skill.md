# 1 分钟教你管理好所有 AI 工具的 Skill

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzNDg3NDg2OQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzNDg3NDg2OQ==&mid=2247484719&idx=1&sn=dffde1022fa006a55bff5841770c917b&chksm=f1049b55a266a53b04472348bf203d08888f0a4ff9552b620c1fe53062fc6c1afccbe7cfb3a9&scene=90&xtrack=1&req_id=1781248420557644&sessionid=1781248873&subscene=93&clicktime=1781248961&enterid=1781248961&flutter_pos=1&biz_enter_id=4&ranksessionid=1781248420&jumppath=20020_1781248892653,1104_1781248911346,20020_1781248914609,1104_1781248954222&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQJ12SNea2RzDd3gIs1NxNdhLTAQIE97dBBAEAAAAAABJ4NR0GEeMAAAAOpnltbLcz9gKNyK89dVj0y4yNFTJVuL/5+bAsFiRTQaLM60sDEx3toSKL9GwxdePn0e5QVz6yzo2s06dXLxHPp1zuKFkVzXoOG+RXw9UEVC9H4UJVeosT92TiO1QfmrVd0FSrwJs2camqxOgcyF5fBmcdAlHP6y5dRncAXLgd8tJaBUBjuchEQf9zGcqLhN65ixmYeFUrZs404JfP6gKrND5UuSc8hKHzr32jF0ArkNPhkDJIEzyfSNBqWPM=&pass_ticket=aVWeqr3iRnTT2y9Wc+pugjlUhHFFrk0KbEzHVp6QImAMj6kybM9ODaWyquYBq4Yq&wx_header=3)

![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/F885D758-39F8-45A3-8415-1E75E4328EE4.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/4D19D6E2-0926-4136-AB87-C47CFFC0A836.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/A295DC36-6A98-449F-8D22-83DD97E80834.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/46992D5A-AC0B-4729-92BB-E537C8BEA499.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/586782FF-F10D-460F-9EC6-C63673CAB2D4.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/B35A263D-498D-4EA5-AD04-37D86923402C.png)![](.evernote-content/A078F452-7964-4496-8FB2-4D6A7FDB828E/9859B15A-D7D8-40D5-9CC8-B7805C8074F8.png)

同时用 Codex 和 Claude Code，最容易乱的往往不是模型，而是它们读着两套 Skill 仓库

多 AI 工具用久了，规则会放得到处都是。Codex 一份 Skills，Claude Code 一份，项目里再放一份；哪天只改了一边，任务表现不一样，你还可能先怀疑模型。

1 分钟教你个好办法，先把 Skills 当成一个源头来管。真实文件放在统一目录里，不同工具入口只负责指向它。这样你改的是同一份规则，不靠记忆复制。

但别一上来就删目录。软链接指向路径，源目录挪走就会断；Windows、团队协作和公司项目，还要确认权限、路径、Git 和工具支持。先让 AI 盘点结构、列影响面、给迁移方案，再动手。工作说明书收拢后，多个 AI 工具才有接力基础。

#Codex#ClaudeCode#AI工具#AI工作流#Skills#Agent#AI编程#效率工具

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzNDg3NDg2OQ==&mid=2247484719&idx=1&sn=dffde1022fa006a55bff5841770c917b&chksm=f1049b55a266a53b04472348bf203d08888f0a4ff9552b620c1fe53062fc6c1afccbe7cfb3a9&scene=90&xtrack=1&req_id=1781248420557644&sessionid=1781248873&subscene=93&clicktime=1781248961&enterid=1781248961&flutter_pos=1&biz_enter_id=4&ranksessionid=1781248420&jumppath=20020_1781248892653,1104_1781248911346,20020_1781248914609,1104_1781248954222&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQJ12SNea2RzDd3gIs1NxNdhLTAQIE97dBBAEAAAAAABJ4NR0GEeMAAAAOpnltbLcz9gKNyK89dVj0y4yNFTJVuL/5+bAsFiRTQaLM60sDEx3toSKL9GwxdePn0e5QVz6yzo2s06dXLxHPp1zuKFkVzXoOG+RXw9UEVC9H4UJVeosT92TiO1QfmrVd0FSrwJs2camqxOgcyF5fBmcdAlHP6y5dRncAXLgd8tJaBUBjuchEQf9zGcqLhN65ixmYeFUrZs404JfP6gKrND5UuSc8hKHzr32jF0ArkNPhkDJIEzyfSNBqWPM=&pass_ticket=aVWeqr3iRnTT2y9Wc+pugjlUhHFFrk0KbEzHVp6QImAMj6kybM9ODaWyquYBq4Yq&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/59c14515-b678-4d48-a378-17ab5cc49fb1/59c14515-b678-4d48-a378-17ab5cc49fb1/)