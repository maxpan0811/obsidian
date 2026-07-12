# 视频：5 个命令放大 Dock 生产力

---

视频：5 个命令放大 Dock 生产力
===================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

Dock 是 macOS 的标志性工具，想提高工作的效率，把它调教到顺手是很有必要的。除了在系统的偏好设置里能看到的那些选项之外，我们对 Dock 还有非常多可以做的事。以下是 5 个我认为最有实用价值的修改：

### 1. 用鼠标移动也能显示背景框

```
defaults write com.apple.dock mouse-over-hilite-stack -bool true
```

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/02B50AC6-41B5-4838-B97F-E19143867610.gif)

### 2. 用空白占位图标分割 Dock 区域

左：

```
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'; killall Dock
```

右：

```
defaults write com.apple.dock persistent-others -array-add '{tile-data={}; tile-type="spacer-tile";}' ;killall Dock
```

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/F6E135F5-8644-4BE0-9655-70ED25D3CFF8.png)

Dock 分组之后的效果

### 3. 滚轮/手势上划显示某个软件的所有窗口

开：

```
defaults write com.apple.dock scroll-to-open -bool TRUE; killall Dock
```

关：

```
defaults write com.apple.dock scroll-to-open -bool FALSE; killall Dock
```

注：区别在于 `TRUE/FALSE`

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/28014567-9287-49EE-8074-8FAD0FCC89FE.gif)

### 4. 使不活动的图标进入半透明状态

开：

```
defaults write com.apple.dock showhidden -bool TRUE; killall Dock
```

关：

```
defaults write com.apple.dock showhidden -bool FALSE; killall Dock
```

注：区别在于 `TRUE/FALSE`

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/976AC629-F2C6-4F63-8A6A-9EC3513A22B1.gif)

### 5. Dock 的瞬间隐藏和出现，以及切换用的快捷键

取消隐藏/出现动画：

```
defaults write com.apple.dock autohide-time-modifier -int 0;killall Dock
```

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/4A1B153A-362F-4EBF-8C30-03FE9DB75579.gif)

完全隐藏动画

将隐藏/出现动画变为 0.1 秒，区别在于有过渡效果和无过渡效果：

```
defaults write com.apple.dock autohide-time-modifier -float 0.1;killall Dock
```

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/15B046D6-99AB-4FAD-BF63-55FE0B5F0CC8.gif)

动画设置为 0.1 秒

恢复正常的隐藏/出现动画：

```
defaults delete com.apple.dock autohide-time-modifier;killall Dock
```

![](.evernote-content/55908A10-A5BD-480A-AB26-4C7BA174C4D3/9992599C-F01F-40DA-A277-4DA4C87C2F4A.gif)

macOS 默认的动画速度

---

如果你用不惯命令行的话，可以下载免费应用 [**TinkerTool**](https://www.bresink.com/osx/TinkerTool.html)。

**最后，乱搞搞坏了，可以用恢复 Dock 的命令：**

```
defaults delete com.apple.dock; killall Dock
```

这个命令会让你的 Dock 恢复出厂状态。

[#macOS](https://sspai.com/tag/macOS)

---

[🌐 原始链接](https://sspai.com/post/41333)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b46928df-ad29-4b64-80b0-ccfde73d678d/b46928df-ad29-4b64-80b0-ccfde73d678d/)