---
title: "通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac.md
tags: [印象笔记]
---


![](.evernote-content/DE3423C6-ECED-49F0-B9CB-6A2D65E29792/56DEDA57-EF04-46FB-939E-D9C52B82D697.jpg)

出于美观或者最大化利用屏幕的原因，很多人在使用 Mac  时都习惯把 Dock 栏调成隐藏状态，但是当你需要打开或查看应用，用鼠标唤出 Dock 栏的时候，会发现 Dock 出现的速度较慢，不仅影响心情，多次操作下来，对效率的影响也很可观。

我们可以通过终端命令来调整 Dock 栏的出现速度。

解决方法
----

Dock 显示隐藏缓慢的原因，是因为 OS X 隐藏和显示 Dock 的动画持续时间被设置成了 1 秒，想要改变这一时间，只需要打开终端，选择以下代码的其中一项执行就可以实现：

* `defaults write com.apple.dock autohide-delay -int 0`（时间设为最短）
* `defaults write com.apple.dock autohide-delay -int 0.5`（时间设为 0.5s）

以上两个选项是比较推荐的设

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->