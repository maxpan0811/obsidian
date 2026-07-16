---
title: "GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。.md
tags: [印象笔记]
---

# GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。

# GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。 --- 前段时间再看哈利波特的时候，看到一个剧情。 小哈利在汤姆里德尔的笔记上写字，停笔等一会儿，刚写下去的字会慢慢消失。 一行新的

---

# GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。

---

前段时间再看哈利波特的时候，看到一个剧情。

小哈利在汤姆里德尔的笔记上写字，停笔等一会儿，刚写下去的字会慢慢消失。

一行新的手写体从纸面上浮出来，像是另一头的汤姆里德尔给哈利的回信。

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/F8155568-90D2-4F43-BCC5-CFE8D23E9E8C)

今天推荐的这个开源项目就用 AI 复刻了这个效果。

项目叫 **Riddle**，作者是 Maxime Rivest。它把《哈利波特》里汤姆·里德尔的日记实现了。

目前这个项目在 GitHub 上已经拿到约 1.4k Star。

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/16B886C0-753F-4494-A987-2AF27F3B201C)

01

**会回信的日记**

现在大部分 AI 产品都长得差不多。

左边历史记录，中间聊天窗口，下面一个输入框。你打字它回复。再换一层皮，本质上还是那个聊天框。

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/A3ECC8D2-FA1D-4BE6-B612-E2531247806D)

Riddle 的有趣之处在于，你看到的就是一张空白纸。

拿笔写下一句话，比如问它今天该写点什么，或者让它回忆之前聊过的内容。

停笔大概几秒后，页面会把你的墨迹吞掉。接着，会用手写动画一点点写出来。

已关注  关注  重播  分享  赞 关闭**观看更多**更多*退出全屏**切换到竖屏全屏**退出全屏*逛逛GitHub已关注分享视频，时长00:250/000:00/00:25 切换到横屏模式 继续播放进度条，百分之0播放00:00/00:2500:25倍速*全屏* 倍速播放中 0.5倍 0.75倍 1.0倍 1.5倍 2.0倍 超清 流畅 您的浏览器不支持 video 标签 继续观看 GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。 观看更多转载,GitHub 上已开源，有人把《哈利·波特》中的笔记做出来了。逛逛GitHub已关注分享点赞在看已同步到看一看写下你的评论 视频详情

整个过程不追求快，也不追求信息密度。

它追求的是一种很完整的错觉：你不是在操作一个 AI 工具，你是在和一本奇怪的日记通信。

这也是它能出圈的原因。

AI 已经很会回答问题了，但 Riddle 让回答变得有氛围。

开源地址：https://github.com/MaximeRivest/Riddle

02

**它是怎么做到的**

Riddle 的核心流程其实很直观。

你写字的时候，项目会直接读取 reMarkable 的笔输入。停笔后，它把当前页面提交成一张小的灰度 PNG 图片，再交给视觉模型读取。

模型看懂你写了什么，生成回复。

然后 Riddle 把回复变成手写效果，在电子墨水屏上一笔一画播放出来。

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/1C99BCEF-4F34-4EF2-B7B0-D732581DB317)

开源项目会把回复用 Dancing Script 字体渲染出来，再做细化和路径追踪，把它变成单像素笔迹路径，最后按笔画动画写回屏幕。

所以你看到的不是一段普通文字突然出现，而是真的像有人在纸上写字。

流程大概是这样：

pen -> strokes -> page PNG -> vision LLM -> handwritten reply -> e-ink display

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/9857D1CD-428F-46BD-A677-6CC1C9C2BEEC)

它支持 OpenAI-compatible 的接口。只要服务兼容 /chat/completions，并且模型能看图，就可以接进去。

README 里提到了 OpenAI、OpenRouter、Groq，也支持本地服务。

03

**如何使用**

Riddle 不是网页应用，也不是下载安装到电脑上的软件。

它要跑在 reMarkable Paper Pro 上，所以你需要先有这台设备。

![](.evernote-content/3829D405-FEBF-4929-9ECA-1F39D6F289ED/FD7C7243-AA27-48BE-8F28-7E5837AAAA43)

作者推荐的最简单方式是用 remagic 安装。

remagic 会帮你处理 developer mode、launcher 和应用安装。

安装命令很短：

remagic install riddleremagic config riddle

第一条命令会把 Riddle 安装到设备里。第二条命令会打开配置页面，让你填模型服务和 API Key。

配置好之后，在 reMarkable 的 AppLoad 里点一下 **Reload**，再打开 **The Diary**。

接下来就很像电影里的那本日记了：你拿笔在屏幕上写字，停笔几秒，页面会把你的字吃掉，然后用手写体慢慢回信。

如果你没有 remagic，也可以下载 GitHub Release 里的安装包。

04点击下方卡片，关注逛逛 GitHub这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了：

[原文链接](https://mp.weixin.qq.com/s/sZBeiKhePKy1x73DiOA1_A)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f8015164-2b33-4a9d-9ca8-a9b84b99696b/f8015164-2b33-4a9d-9ca8-a9b84b99696b/)