---
title: "技巧：利用 AppleDNS 项目加速 Apple 服务"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/技巧：利用 AppleDNS 项目加速 Apple 服务.md
tags: [印象笔记]
---


![](.evernote-content/618C8018-53A9-4E61-9F4E-85FF2EA97168/29679003-58E2-4156-A9B0-BFDFE1F84546.jpg)

[AppleDNS](https://github.com/gongjianhui/AppleDNS) 是 GitHub 上针对 Apple 服务进行加速的一个项目。具体来说，AppleDNS 项目通过收集 Apple 在全中国几乎所有省级行政区的 CDN IP 列表，能够解决以下 Apple 服务在国内部分地区速度缓慢的问题：

* App Store
* Mac App Store
* iTunes Store
* Apple Music
* iBooks Store
* TestFlight

出于隐私、安全以及系统稳定性方面的考虑，项目作者未在加入 iCloud 与 Apple ID 相关的域名。由于 iTunes 大规模启用了 HTTPS 的连接方式，你也大可不必担心作者会通过此项目获取个人敏感信息。

使用方法
----

### 1. 一些准备工作

由于 Apple D

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->