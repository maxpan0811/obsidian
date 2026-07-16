---
title: "如何替换 El Capitan 的 Finder 图标 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何替换 El Capitan 的 Finder 图标 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# 如何替换 El Capitan 的 Finder 图标 _ 一日一技 · Mac

# 如何替换 El Capitan 的 Finder 图标 | 一日一技 · Mac --- ![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F207

---

# 如何替换 El Capitan 的 Finder 图标 | 一日一技 · Mac

---

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/F63DB91C-322E-413D-B0EE-DF6249B68ED6.jpg)

在少数派最近的一篇[装了啥](http://sspai.com/search/?q=%E8%A3%85%E4%BA%86%E5%95%A5)文章里，分享者 24Says 的 OS X Dock 上的红色 Finder 引起了不少读者注意，在[文章](http://sspai.com/34885)后面的评论区求分享的呼声不小。作者给出了红色 Finder 图标的[素材下载](http://t.cn/Rtt6hR1)，但具体如何替换还是有很多人不清楚。

这篇教程将手把手教你替换图标，不同于之前[替换 OS X 应用程序图标的文章](http://sspai.com/26274/)，本次我们需要进行图标替换的 Finder 属于系统应用程序，所以方法有些不同。

由于 El Capitan 默认启用了[系统完整性保护](https://support.apple.com/zh-cn/HT204899)（System Integrity Protection）机制，在开始替换源文件之前，我们需要先手动禁用这一机制。在替换图标完毕之后，还需要手动清空图标缓存，才能看到系统应用图标替换后的最终效果。

第一步：关闭系统完整性保护机制
---------------

1. 将你的 Mac 电脑关机，按下开机键后同时按住 *Command+R*，进入恢复模式。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/EF0BAD3D-B118-47DB-A068-95936695622D.jpg)2. 点击菜单栏的「工具」，然后再下拉菜单中选择「终端」打开。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/FAFB2F48-C6E5-452B-B792-576315B3E782.jpg)3. 在终端中输入 `csrutil disable` 命令，并按下回车确认。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/E056B17F-B993-4274-81E4-4637B12827A1.jpg)4. 重启 Mac，即完成了禁用系统完整性保护机制。

第二步：替换 Finder 图标
----------------

1. 打开 Finder 窗口，按下 *Command+Shift+G* 快捷键，呼出「前往」对话框。

2. 输入路径 `/System/Library/CoreServices/Dock.app/Contents/Resources/` 后，按回车键。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/BD55FA54-78E4-491A-98DF-1700D855FEC6.jpg)3. 找到并备份 *finder.png* 与 *finder@2x.png* 两个文件（重要）。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/0F9059D2-0F6B-4E37-A564-69AF44EF7FB0.jpg)4. 将提前下载好的两张 Finder 图标素材图片拖入此窗口进行替换，输入管理员密码来「授权」确认即可。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/5C9D8A85-9D58-4822-9548-D3CFA0B93C4F.jpg)

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/5A05DBA0-3A9D-48DC-9A68-D5B5F27846D4.jpg)

第三步：清空图标缓存
----------

1. 在「前往」对话内输入路径 `/private/var/folders/` 并按下回车键（参考上一阶段的步骤 1 和步骤 2）。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/EFB6B23F-587C-49B0-9940-B5BA816E0FFA.jpg)2. 在 Finder 右上角搜索框内搜索 `com.apple.dock.iconcache`（注意需在「folders」范围内进行）。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/0AB06A86-6A4A-4EF8-8E87-558EC73D2A9C.jpg)3. 选中它并删除。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/D4E2D97F-01AF-4782-9D80-D2431B48BE5A.jpg)4. 打开「终端」应用程序，在终端窗口内输入 `killall Dock` 后，按下回车确认即可。

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/B0F12A80-645A-4E7D-B409-50F75DC875F3.jpg)现在你就可以看到替换好的新的 Finder 图标啦！

![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/465CB0A9-D5EE-4DC7-BA40-9A1BA75D5DAD.jpg)

* 注 1：红色 Finder 图标素材来自 [UEDetail.com](http://uedetail.com/)
* 注 2：更改完毕后，你可以在第一阶段的第 4 步中输入 `csrutil disable` 命令来重新启用系统完整性保护机制。
* 注 3：其他的系统级别图标替换，均可以参考此教程，注意备份。

文章来源 [少数派](http://sspai.com) ，原作者 [iTumbledSea](http://sspai.com/author/642336) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/E3C35113-F52B-4800-95FD-4F1F2073EF32/1943492A-A503-4E3F-856D-787DAE50D9F4.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:BASE/destination:http://www.apple.com/cn/shop/product/HK2R2ZM/A/%E9%85%8D%E5%A4%87-smart-connector-%E7%9A%84-logi-base-%E5%85%85%E7%94%B5%E6%94%AF%E6%9E%B6-%E9%80%82%E7%94%A8%E4%BA%8E-ipad-pro?fnode=85)

---

[🌐 原始链接](http://sspai.com/34971)

[📎 在印象笔记中打开](evernote:///view/207087/s1/150da3e9-3a19-45d7-9951-67753095157d/150da3e9-3a19-45d7-9951-67753095157d/)