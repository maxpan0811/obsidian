# 如何给 Claude + Codex 配 Obsidian 大脑

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwNjc2MTkyNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzIwNjc2MTkyNA==&mid=2247484577&idx=1&sn=fd3d57a27957964528b3e2a14a205f4d&chksm=971dfe0aa06a771cf650ebc264aab438b3ffb4f03cb47a78b630cad5d1e7dff0f95a8fbdb2b1&exptype=servicebox_1782053633073369&subscene=0&scene=288&clicktime=1782053643&enterid=1782053643&flutter_pos=1&biz_enter_id=5&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQkvW3mujxQEZk8+33QzNxxBLTAQIE97dBBAEAAAAAAIbFLoGkyfQAAAAOpnltbLcz9gKNyK89dVj0rxG2R4f74FojWlCPMO28/GrduKddTthgZI0bGW2wfvCM1wKdN13ivC/ovffrXKoZDZYk6XD3zwszpwYC3Y58Oc1pegv72IrPibyQor37NFYPfNJeVv1u1HpmS4agu3OtqTPftwDxZodQEQbbiWdoprjvqk/hOj5Vvbc9QNF66KyPJrGXyL1N9zWCEjLrlztG3Dqoco207K0esfRab29X09NVSrpLXKaeipf2oUk=&pass_ticket=3LxBHNd93oaD/OsWGAXh+Qh6YT1OOrKgyFuL4YIUZDm/WY8m6Lt7DRky6dAvWDOW&wx_header=3)

![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/B65C65F9-DEF8-45C1-B43A-8FC52E6DF07F.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/4E117B6D-17C4-4AFF-93AB-2CDB83242FFD.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/60B79493-B99C-44EA-B0B9-AC2C40D8C825.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/DC1DB122-3BA5-4962-81D2-52973270ACAE.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/84934B37-8CD2-4CC0-A34A-87CF410520B1.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/D1FE892C-D7ED-442A-BA20-D07D4E8536A8.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/87661ECC-FF89-46B2-9D88-B3E8213B7FED.png)![](.evernote-content/B973600C-8903-445B-9363-330BA9F0B7D8/7A87175F-50DD-4732-9492-F75D5F3C1482.png)

AI 客户端最烦的一点：

Claude Code 刚听懂项目背景，切到 Codex 又要重讲。

所以我把 Obsidian Vault 配成它们共用的大脑。

配好后：

- 少重复解释项目背景

- 两个 AI 能接着同一份上下文干活

- 规则、决策、避坑都沉淀成 Markdown

完整图文里写了：

- Node.js / Claude Code / Codex 安装

- CLAUDE.md 和 AGENTS.md 配置

- Mac / Windows 命令

- 30 秒验证共脑有没有跑通

建议先建 sandbox 测试，跑通后再接正式 vault。

#AI工具#Obsidian#ClaudeCode#Codex#AI工作流#知识管理#效率工具#小白教程#Mac效率#程序员工具#Markdown#个人知识库

Love the Author

感谢您的支持

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwNjc2MTkyNA==&mid=2247484577&idx=1&sn=fd3d57a27957964528b3e2a14a205f4d&chksm=971dfe0aa06a771cf650ebc264aab438b3ffb4f03cb47a78b630cad5d1e7dff0f95a8fbdb2b1&exptype=servicebox_1782053633073369&subscene=0&scene=288&clicktime=1782053643&enterid=1782053643&flutter_pos=1&biz_enter_id=5&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQkvW3mujxQEZk8+33QzNxxBLTAQIE97dBBAEAAAAAAIbFLoGkyfQAAAAOpnltbLcz9gKNyK89dVj0rxG2R4f74FojWlCPMO28/GrduKddTthgZI0bGW2wfvCM1wKdN13ivC/ovffrXKoZDZYk6XD3zwszpwYC3Y58Oc1pegv72IrPibyQor37NFYPfNJeVv1u1HpmS4agu3OtqTPftwDxZodQEQbbiWdoprjvqk/hOj5Vvbc9QNF66KyPJrGXyL1N9zWCEjLrlztG3Dqoco207K0esfRab29X09NVSrpLXKaeipf2oUk=&pass_ticket=3LxBHNd93oaD/OsWGAXh+Qh6YT1OOrKgyFuL4YIUZDm/WY8m6Lt7DRky6dAvWDOW&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c3ab651a-dae5-45ef-ad11-6ecbe3a5e66c/c3ab651a-dae5-45ef-ad11-6ecbe3a5e66c/)