# Claude是真高产啊……

---

原文链接: [https://mp.weixin.qq.com/s?ranksessionid=1782032740\_6&chksm=...](https://mp.weixin.qq.com/s?ranksessionid=1782032740_6&chksm=967f2673a108af65d537db4281ba29c23710c51d4d5781c970de1cf2a78ea3e67ebb343b0dcc&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&req_id=1782035691364054&scene=169&mid=2247484810&subscene=200&sn=d4c84a37d6d1a3d394575b931c190f1d&idx=1&__biz=MzE5MTk2ODkxOA==&sessionid=1782032739&clicktime=1782036095&enterid=1782036095&flutter_pos=0&biz_enter_id=5&jumppath=WAWebViewController_1782036065817,WAWebViewController_1782036066316,20020_1782036091877,1104_1782036093623&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVVUgqSdD7hVGBXTEBlmm0RLTAQIE97dBBAEAAAAAAONRACKt99YAAAAOpnltbLcz9gKNyK89dVj0TWmS1DBm6/8w7SranSAhQ8gTuXwKz/LPnN6+7zI1wwNXwdrM4vSpXECqe5QzrwiCpm0KfHy8aGBQX4qTuS+xEFIBxb7UKoRDoKXV+dFPwgMNx8FIPL9qTrq9y/wBZzliuIWWmAAU1LzRLAlDPRonKayrjfWOYbbMdwpDbPTXuHBIwIVKjkpyEo244sgiRA/0MizwkgT6dWkMkYFbWG+LR5/9Zg7vyVP24wJMSO0=&pass_ticket=kMQ5zDy/0o1iowP5FPrUqgPgC3h8j+3Ryj96nBVogXk9LLpPOUvrCEltvAtPtKxp&wx_header=3)

![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/FD9543FD-8AE1-4BC1-8435-4976E4C8E640.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/1F5B2564-6AC4-495C-8DF2-454C8DBD11D6.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/E80C0570-D0AC-4F82-8334-12536AE955EB.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/D3D71371-D350-4FB0-97D1-19845CD2CB32.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/4B1E6070-1D00-452D-B3B6-BD3F58159AE1.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/927D90DA-2BC7-44B0-89D1-2E8CDB5F111C.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/11178D3B-6A27-4E07-808E-10E13E64AAD6.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/F3A2FA62-1E7D-4C7F-83AB-5182D5589E40.jpg)![](.evernote-content/A4493EE4-05CB-40DB-A5F7-E9AF9967C092/48867262-BDBE-418F-A5F1-2A5B40016CD2.jpg)

昨天 Claude 官方发了篇动态工作流的实战指南，细看下来确实有些启发。

核心讲的是：怎么让 AI 处理复杂任务时不掉链子。传统单线程 AI 容易偷懒、自我偏好、目标漂移，Dynamic Workflows 通过多代理协作解决这些结构性问题。

我之前也用过 workflow，但没有系统化地把它融入日常工作流。这篇文章提到的 6 种协作模式（分类路由、拆分汇总、对抗验证、生成筛选、锦标赛、循环收敛）和 Bun 代码库迁移的案例，给了我一些新思路：

workflow 不应该只是"遇到复杂任务时想起来用一下"，而是可以沉淀成 skill，形成可复用的长线能力。比如大规模分类、多轮验证、根因调查这些场景，完全可以固化成标准流程。

分享给大家，原文链接：

https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code。

如果你也在摸索怎么让 AI 更靠谱地处理复杂任务，这篇值得去小小琢磨一下。

#废话老洪#ai#vibecoding#ai工作流

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?ranksessionid=1782032740_6&chksm=967f2673a108af65d537db4281ba29c23710c51d4d5781c970de1cf2a78ea3e67ebb343b0dcc&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&req_id=1782035691364054&scene=169&mid=2247484810&subscene=200&sn=d4c84a37d6d1a3d394575b931c190f1d&idx=1&__biz=MzE5MTk2ODkxOA==&sessionid=1782032739&clicktime=1782036095&enterid=1782036095&flutter_pos=0&biz_enter_id=5&jumppath=WAWebViewController_1782036065817,WAWebViewController_1782036066316,20020_1782036091877,1104_1782036093623&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVVUgqSdD7hVGBXTEBlmm0RLTAQIE97dBBAEAAAAAAONRACKt99YAAAAOpnltbLcz9gKNyK89dVj0TWmS1DBm6/8w7SranSAhQ8gTuXwKz/LPnN6+7zI1wwNXwdrM4vSpXECqe5QzrwiCpm0KfHy8aGBQX4qTuS+xEFIBxb7UKoRDoKXV+dFPwgMNx8FIPL9qTrq9y/wBZzliuIWWmAAU1LzRLAlDPRonKayrjfWOYbbMdwpDbPTXuHBIwIVKjkpyEo244sgiRA/0MizwkgT6dWkMkYFbWG+LR5/9Zg7vyVP24wJMSO0=&pass_ticket=kMQ5zDy/0o1iowP5FPrUqgPgC3h8j+3Ryj96nBVogXk9LLpPOUvrCEltvAtPtKxp&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a6db0889-51a4-4f33-9a58-57ed1710a77c/a6db0889-51a4-4f33-9a58-57ed1710a77c/)