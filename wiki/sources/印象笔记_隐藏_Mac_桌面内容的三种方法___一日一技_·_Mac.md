---
title: "隐藏 Mac 桌面内容的三种方法 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/隐藏 Mac 桌面内容的三种方法 _ 一日一技 · Mac.md
tags: [印象笔记]
---


![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/562273BF-1186-4117-B47B-21CD25562D3E.gif)

通过隐藏桌面内容，一方面可以让我们在工作时保持一个整洁而漂亮的桌面，「眼不见，心不烦」，减少不必要的干扰；另一方面也能够避免在截取 / 录制屏幕，或向他人展示内容时个人隐私信息的暴露，避免一些不必要的麻烦。

虽然我们并不总是有此需求，但知道几种方法，以备「不时之需」也总好的 :-D

方法一：利用终端命令
----------

在「终端」中输入如下命令，回车确认，即可隐藏所有桌面内容（包括文件、文件夹以及设备图标等）：

```
defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder
```

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/5556598B-1481-4FF0-B750-ADBF750E286E.jpg)

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->