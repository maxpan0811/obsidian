# OS X小技巧：如何去除窗口截图产生的阴影

---

[![](.evernote-content/B04F5A8D-3F27-44D6-A61C-BBF23131A7F7/53E9746C-0273-440D-B090-BC92253B41E2.jpg)](http://www.feng.com/iPhone/news/2015-11-25/OS-X-tip-how-to-remove-the-shadow-cast-by-window-screenshot_631211.shtml)

　威锋网讯，使用 Mac 的朋友应该都知道，同时按下 Command + Shift + 3，你就可以对屏幕进行快速截屏，而同时按下 Command + Shift + 4，则可以拖动光标，选择希望截图的区域。如果你在截图之前按下空格键的话，则可以快速对某个窗口进行截图。

![](.evernote-content/B04F5A8D-3F27-44D6-A61C-BBF23131A7F7/53E9746C-0273-440D-B090-BC92253B41E2.jpg)

对于上述的技巧你可能已经驾轻就熟，但不知道大家有没有注意到，当你对一个窗口进行截图的时候，截图总是会伴随着阴影（drop shadow）出现，那么今天我们就来一起学习如何去除这些阴影。

首先打开终端窗口，然后输入下列指令

defaults write com.apple.screencapture disable-shadow -bool TRUE

点击确认后，输入下列指令

Killall SystemUIServer

这样当你对某个窗口进行截屏的时候，就不会出现阴影了。如果你想重新拥有“阴影”的话，只需在重复上述操作的时候，将第一行指令中的“TRUE”替换为“FALSE”即可。

![](.evernote-content/B04F5A8D-3F27-44D6-A61C-BBF23131A7F7/DF7E7622-77BC-42A5-94D0-FEBBAAED5A76.jpg)

**（▲ 去除阴影后）**

[阅读全文](http://www.feng.com/iPhone/news/2015-11-25/OS-X-tip-how-to-remove-the-shadow-cast-by-window-screenshot_631211.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2015-11-25/OS-X-tip-how-to-remove-the-shadow-cast-by-window-screenshot_631211.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7860ad86-6e47-4be7-b241-d9a4c3e61b77/7860ad86-6e47-4be7-b241-d9a4c3e61b77/)