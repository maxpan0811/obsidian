---
title: 真正能提升你日常工作效率的 Mac 设置，彻底改变使用体验
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/真正能提升你日常工作效率的 Mac 设置，彻底改变使用体验.html
tags: [其他]
---

# 真正能提升你日常工作效率的 Mac 设置，彻底改变使用体验

原文链接: https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=224749...

Original 点蓝色字关注👉  程序员echo 
说到 Mac 的设置，我第一年用 MacBook 的时候，总觉得别人都知道我不知道的秘密，好像他们都参加过一个叫“如何让你的 Mac 不烂”的培训班，而我当时还在喝咖啡。后来才发现，我其实有点对，真的有一些设置能彻底改变你的使用体验，只是大部分人根本懒得去碰它们，因为这些设置不是藏在三层菜单深处，就是需要打开终端敲几行看起来像在黑 Pentagon 的命令。

所以我整理了一些真正让我的 Mac 使用感提升的设置，不是什么换壁纸这种花里胡哨的操作，而是那种每天用起来会觉得快、顺手、不像在和电脑斗气的调整。
一、超级增强 Quick Actions（你不知道的右键菜单隐藏技能）Quick Actions 本质上就是 Automator 的工作流，藏在右键菜单里，大多数人忽略它是因为默认选项太无聊，但只要你自己加几个操作，就像给自己加了超能力

怎么创建呢：打开 Automator（应用程序里有），选择 Quick Action，然后按照自己的需求建工作流
举个例子，我经常写东西，截图多得跟海一样，每张截图都大得可怕，这个 Quick Action 就能让我右键任意图片（或一堆图片）就能统一缩放到我想要的尺寸
在 Automator 里操作步骤如下：
先选择文档类型 “Quick Action”，然后点 “Choose”设置“Workflow receives current”为 Image Files添加动作：选中 Copy Finder Items，拖到工作区（注意，如果想保留原文件，不要勾“Replace existing files”）再添加动作：Scale Images，设置你想要的宽度，比如 480px 或 800px按 Cmd + S 保存工作流，比如命名为 “Image Resize”现在，去文件夹里选中图片，右键 -> Quick Actions -> Image Resize 就搞定图片会按 Copy Finder Items 里的目标路径输出，比如我选的图片在 Downloads 文件夹，缩放后的会到 DesktopQuick Actions 功能太多了，我打算专门写一篇帖子聊 Automator 和 Quick Action 的高级玩法，比如批量重命名、自动加水印、文本处理等等，用起来你会怀疑自己以前为什么要手动做这些操作
二、Finder 高手操作Finder 本身用起来还行，但稍微调一调，就能从“凑合用”变成“真好用”

加入 “Recents” 到侧边栏：Finder → 设置（Cmd + ,）→ 侧边栏，把 “Recents” 勾上，这样就能一键看到最近打开的文件，不用再翻文件夹找昨天存的东西文件剪切粘贴（终于）：你可能一直用 Cmd + C 复制文件，再 Cmd + V 粘贴，但其实也能剪切文件，就像 Windows 一样，Cmd + C 复制，然后 Cmd + Option + V 就能移动到新位置，原位置文件就消失显示完整路径：Finder → 视图 → 显示路径栏，现在每个 Finder 窗口底下都有完整路径，可以直接点路径里的文件夹跳转，超级方便三、 Safari 阅读模式（因为现在的网站都太烦了）不知从什么时候起，网站全都爱弹窗、自动播放视频、新闻订阅铺满半屏，让你连第二段都没看到就烦死了

...Safari 的
