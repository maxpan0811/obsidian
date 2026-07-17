---
title: Claude Code 七层约束（2）：任务开始前的准备_Hook+Skill+CLAUDE 分层设计全拆解
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Claude Code 七层约束（2）：任务开始前的准备_Hook+Skill+CLAUDE.md 分层设计全拆解.md
tags: [evernote, impression, yinxiang]
---


Claude Code 七层约束（2）：任务开始前的准备/Hook+Skill+CLAUDE.md 分层设计全拆解
=========================================================

Original墨染zzz ZEROFLOWER

|  |
| --- |
| 摘要  本文是七层约束系列的第 2 篇，聚焦输入端三层——Hook、Skill 和 CLAUDE.md。这三层的核心逻辑是 Harness Engineering：不改变模型本身，而是在模型接收任务之前设定行为边界。文中完整拆解了 Hook 事件注入的配置方式与源码、Skill 的安装机制与三类使用场景、CLAUDE.md 三级加载体系及每级的写作原则。读完可直接复制配置落地。项目 GitHub 地址请见文章结尾。  关联阅读，7层约束系列第一篇：[让 Claude Code 成为稳定协作者：7 层约束系统设计与实践（已开源）](https://mp.weixin.qq.com/s?__biz=MzIwMDcwMjYwNg==&mid=2247484264&idx=1&sn=

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->