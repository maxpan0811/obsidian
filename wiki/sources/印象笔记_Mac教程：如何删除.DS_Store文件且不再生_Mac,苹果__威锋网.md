---
title: "Mac教程：如何删除.DS_Store文件且不再生 Mac,苹果 _威锋网"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Mac教程：如何删除.DS_Store文件且不再生 Mac,苹果 _威锋网.md
tags: [印象笔记]
---

# Mac教程：如何删除.DS_Store文件且不再生 Mac,苹果 _威锋网

# Mac教程：如何删除.DS_Store文件且不再生 Mac,苹果 _威锋网 --- Mac教程：如何删除.DS\_Store文件且不再生 ========================== 5小

---

# Mac教程：如何删除.DS_Store文件且不再生 Mac,苹果 _威锋网

---

Mac教程：如何删除.DS\_Store文件且不再生
==========================

5小时前

[叫我知心哥哥丶](http://bbs.feng.com/u.php?uid=8964037)

威锋网

[分享](http://www.feng.com/iPhone/news/2016-06-07/Mac-this-tutorial-how-to-delete.-DS-Store-file-without-regeneration_648701.shtml#shareBox)
[10](http://www.feng.com/iPhone/news/2016-06-07/Mac-this-tutorial-how-to-delete.-DS-Store-file-without-regeneration_648701.shtml#comments)

1586

[收藏](#)

.DS\_Store文件重新生成非常令人困扰，我们可以用终端命令简单的处理掉。

　　在 Mac OS X 系统下，几乎绝大部分文件夹中都包含 .DS\_Store 隐藏文件，这里保存着针对这个目录的特殊信息和设置配置，例如查看方式、图标大小以及这个目录的一些附属元数据。  
  
　　而在 OS X 系统中，这些文件是默认隐藏起来的，但是当我们将这些文件转移共享到 Windows 系统的时候，它们就会变成可见状态，并且看起来非常像是一些垃圾文件。

![](.evernote-content/16C725B9-BCDA-48D9-8928-140F7A184BB7/F74238AE-5B5F-4FB5-804F-E4289A342369.png)

  
　　许多用户会选择在 Windows 系统中将这些 .DS\_Store 文件删除，但是它们会重新生成，这一点非常令人困扰。对于这个问题，锋友“[诺记大婶](http://bbs.feng.com/forum.php?mod=viewthread&tid=10551343&extra=page=2&filter=author&orderby=dateline&orderby=dateline)”给出了自己的解决方案，他表示，我们可以用终端命令简单的处理掉，并且防止 DS\_Store 文件的再生。  
  
　　我们需要打开终端窗口，并输入删除命令：sudo find / -name ".DS\_Store" -depth -exec rm {} \;  
  
　　按下回车键盘之后，终端会提示用户名和密码，直接输入密码再按回车即可。  
  
　　删除后继续在终端输入：defaults write com.apple.desktopservices DSDontWriteNetworkStores true  
  
　　然后按下回车，就可以防止 .DS\_Store 文件的再生了。

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2016-06-07/Mac-this-tutorial-how-to-delete.-DS-Store-file-without-regeneration_648701.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f7c41528-f705-4e2d-ab7e-d2f767dc408a/f7c41528-f705-4e2d-ab7e-d2f767dc408a/)