---
title: "通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac.md
tags: [印象笔记]
---

# 通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac

# 通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac --- ![](.evernote-content/DE3423C6-ECED-49F0-B9CB-6A2D65E29792/56D

---

# 通过终端命令调整 Dock 栏的隐藏速度｜一日一技 · Mac

---

![](.evernote-content/DE3423C6-ECED-49F0-B9CB-6A2D65E29792/56DEDA57-EF04-46FB-939E-D9C52B82D697.jpg)

出于美观或者最大化利用屏幕的原因，很多人在使用 Mac  时都习惯把 Dock 栏调成隐藏状态，但是当你需要打开或查看应用，用鼠标唤出 Dock 栏的时候，会发现 Dock 出现的速度较慢，不仅影响心情，多次操作下来，对效率的影响也很可观。

我们可以通过终端命令来调整 Dock 栏的出现速度。

解决方法
----

Dock 显示隐藏缓慢的原因，是因为 OS X 隐藏和显示 Dock 的动画持续时间被设置成了 1 秒，想要改变这一时间，只需要打开终端，选择以下代码的其中一项执行就可以实现：

* `defaults write com.apple.dock autohide-delay -int 0`（时间设为最短）
* `defaults write com.apple.dock autohide-delay -int 0.5`（时间设为 0.5s）

以上两个选项是比较推荐的设置，设置好了，就快看看效果吧。

想要获得更多简单实用的小技巧？*[查看往期「一日一技」>](http://sspai.com/tag/%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)*

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

文章来源 [少数派](http://sspai.com) ，原作者 [waychane](http://sspai.com/author/703114) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33366)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c723a0fc-3e60-4dc0-9938-11510298dc71/c723a0fc-3e60-4dc0-9938-11510298dc71/)