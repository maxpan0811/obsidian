---
title: "视频：5 个命令放大 Dock 生产力"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/视频：5 个命令放大 Dock 生产力.md
tags: [印象笔记]
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
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'; killal

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->