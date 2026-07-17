---
title: "不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用 - 少数派.md
tags: [印象笔记]
---


不用手动输密码，用 Apple Watch 也可以解锁 Mac 应用
==================================

如果你使用过带 Touch ID 的 MacBook Air 或者 MacBook Pro，那么一定会被指纹解锁的便捷性所深深打动。除了解锁 Mac，Touch ID 现在还被 1Password、Day One、MoneyWiz 等第三方 App 用来登录解锁，真的是属于用过就回不去的一个功能。特别是对于 1Password 这类密码管理类应用，主密码一般会设置地又长又复杂，如果每次都要手动输入，可谓是「苦不堪言」。

可是，如果你的 MacBook 没有配备 Touch ID 或者你将 MacBook 合盖外接显示器使用，就难免要手动输入主密码来解锁 1Password。为了解决这个问题，我最初采用的方法是通过 Keyboard Maestro 来获取预先储存在钥匙串访问 App 中的 1Password 主密码，然后再自动完成「输入文本（密码）- 按下回车键」等操作。但是，这个方案最大的问题是你必须让 Keyboard Maestro 获得

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->