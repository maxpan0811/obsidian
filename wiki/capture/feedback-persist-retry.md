---
title: feedback-persist-retry
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


遇到问题时，不要向用户报告"不行了"或"做不到"，而是想办法解决后自动重试。用户会说"以后没做好就继续想办法做，不要跟我说不行"。

**Why:** 用户是问题解决型，讨厌被通知问题，希望直接看到结果。

**How to apply:** 保存失败→查原因→修代码→重试。图片下载失败→加重试、换 headers。链接打不开→换 URL 格式。Token 过期→让用户重新生成。所有问题都有方案，先试再说。
