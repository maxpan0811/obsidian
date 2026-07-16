---
title: "自动开关电量百分比，你的 Mac 也可以拥有电量智能显示"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/自动开关电量百分比，你的 Mac 也可以拥有电量智能显示.md
tags: [印象笔记]
---

# 自动开关电量百分比，你的 Mac 也可以拥有电量智能显示

# 自动开关电量百分比，你的 Mac 也可以拥有电量智能显示 --- macOS 系统菜单栏中的任务菜单区域，空间有限，常驻有需要快捷查看或使用的信息与工具。一般在接通外接电源时，我们不用在意电池电量

---

# 自动开关电量百分比，你的 Mac 也可以拥有电量智能显示

---

macOS 系统菜单栏中的任务菜单区域，空间有限，常驻有需要快捷查看或使用的信息与工具。一般在接通外接电源时，我们不用在意电池电量，经常去瞥它反倒会分散注意力、令人感到焦虑；但是，在使用电池时却是要关注电量的，此时又需要手动开启百分比的显示。另外，偶尔也会有意外断电或者忘记插电源的情况，可能注意到时已经电量较低，影响正常的使用了。

![](.evernote-content/6BB0AF6C-C070-4589-A0AE-E9AA6F2CB532/48FCE3CC-45D3-409B-B53A-9FCD58A102CF.png)

为了免去手动开关电量显示的麻烦，我做了一个 [Keyboard Maestro](https://www.keyboardmaestro.com/main/ "Keyboard Maestro") 的自动化动作，它可以实现**「智能电量百分比显示」**，具体的功能为：

* 使用电池时，保持电量百分比显示；
* 接通电源后，电池电量达到 75% 以上时，关闭百分比显示。

使用方法很简单，下载 [电量百分比智能显示.kmmacros](https://cl.ly/403Z2E190A2J "电量百分比智能显示.kmmacros")，双击导入 Keyboard Maestro，然后启用该 Macro 即可。

它的原理如下图所示，使用周期触发器每五分钟执行一次情况判断：如果此刻在使用电池且没有显示百分比，则使用 AppleScript 脚本开启显示；如果在使用外接电源，电池电量达到 75% 以上，并显示百分比，则关闭显示。当然，你也可以根据自己的具体情况，修改 75% 这一数字。

![](.evernote-content/6BB0AF6C-C070-4589-A0AE-E9AA6F2CB532/6EAC7EFE-EF40-42ED-93BA-6C80471372BA.png)

此外，当电源切换至电池供电，自动开启电量百分比的显示时，其动作效果如下图。这也算是对于用户的一个简易提示，避免用户一直没有察觉到外接电源的断开。而且，这种使用 AppleScript 对系统界面的操作不会对用户同时进行的点击、输入产生影响。

![](.evernote-content/6BB0AF6C-C070-4589-A0AE-E9AA6F2CB532/DCE8238B-AFE9-46CF-A39B-DDF60CBFC6C8.gif)

上面所提供的 Macro 中用来开关百分比显示的 AppleScript 脚本如下，在 macOS High Sierra 中文版里运行正常。英文系统的用户则需要用下面第二段脚本替换 Macro 中的脚本。其它系统版本及语言情况未作测试，可能需要调整 AppleScript 后才能正常运行。

中文系统：

```
tell application "System Events"
    tell application process "SystemUIServer"
        set bettaryIcon to first menu bar item of menu bar 1 whose description starts with "电池"
        click bettaryIcon
        click (the first menu item of menu 1 of bettaryIcon whose name = "显示百分比")
    end tell
end tell
```

英文系统：

```
tell application "System Events"
    tell application process "SystemUIServer"
        set bettaryIcon to first menu bar item of menu bar 1 whose description starts with "Battery"
        click bettaryIcon
        click (the first menu item of menu 1 of bettaryIcon whose name = "Show Percentage")
    end tell
end tell
```

本文所使用的 [Keyboard Maestro](https://www.keyboardmaestro.com/main/ "Keyboard Maestro") 软件与 AppleScript 脚本，都是 macOS 平台上的自动化利器。如果想要进一步了解它们，可以看这两篇文章：

* [Keyboard Maestro 入门指南](https://sspai.com/post/36442 "Keyboard Maestro 入门指南")
* [手把手教你用 AppleScript 模拟鼠标键盘操作，实现 macOS 系统的自动化操作](https://sspai.com/post/43758 "手把手教你用 AppleScript 模拟鼠标键盘操作，实现 macOS 系统的自动化操作")

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk "少数派 iOS 客户端")、关注 [少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，让智能设备更好用 ⚡️

---

[🌐 原始链接](http://sspai.com/post/44714)

[📎 在印象笔记中打开](evernote:///view/207087/s1/69c3ef28-3658-4781-908e-c3e3db7a60ec/69c3ef28-3658-4781-908e-c3e3db7a60ec/)