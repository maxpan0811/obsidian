---
title: Codex报重大 bug！SSD正在被加速磨损
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/Codex报重大 bug！SSD正在被加速磨损.md
tags: [evernote, impression]
---


title: "Codex报重大 bug！SSD正在被加速磨损"
source: evernote
type: note
export_date: 2026-06-23
guid: 872e5832-c983-43b4-96d9-f6ebc1af3df1
---

# Codex报重大 bug！SSD正在被加速磨损

来源：[打开原文](https://mp.weixin.qq.com/s/ffwickZMkrKoNgT1VQvcZQ)

## Codex报重大 bug！SSD正在被加速磨损

Codex 正在加速磨损你的 SSD，这个 bug 至今没有修复。

Codex 在运行时会把所有过程都记录进一个日志文件。

模型每输出一个字，就写一次，更严重的是日志的存储方式。

它用的是 SQLite，写入流程先进缓存，再刷盘，再写一份备份，等于每次写操作在底层被放大了好几倍，写入量就爆了。

硬盘静默损耗，基本感知不到，但多开几个窗口跑 Codex，界面会 freeze，键盘输入也有延迟。

Desktop 版更惨，跑长对话内存能超 1GB，CPU 常驻 60%。

GitHub 上已

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->