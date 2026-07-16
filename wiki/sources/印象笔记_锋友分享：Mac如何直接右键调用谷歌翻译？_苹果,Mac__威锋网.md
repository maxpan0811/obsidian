---
title: "锋友分享：Mac如何直接右键调用谷歌翻译？ 苹果,Mac _威锋网"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/锋友分享：Mac如何直接右键调用谷歌翻译？ 苹果,Mac _威锋网.md
tags: [印象笔记]
---

# 锋友分享：Mac如何直接右键调用谷歌翻译？ 苹果,Mac _威锋网

# 锋友分享：Mac如何直接右键调用谷歌翻译？ 苹果,Mac _威锋网 --- 锋友分享：Mac如何直接右键调用谷歌翻译？ ===================== 1小时前 [叫我知心哥哥丶](h

---

# 锋友分享：Mac如何直接右键调用谷歌翻译？ 苹果,Mac _威锋网

---

锋友分享：Mac如何直接右键调用谷歌翻译？
=====================

1小时前

[叫我知心哥哥丶](http://bbs.feng.com/u.php?uid=8964037)

威锋网

[分享](http://www.feng.com/iPhone/news/2017-05-02/Feng-friends-sharing-Mac-right-how-to-directly-call-Google-translation_677074.shtml#shareBox)
[7](http://www.feng.com/iPhone/news/2017-05-02/Feng-friends-sharing-Mac-right-how-to-directly-call-Google-translation_677074.shtml#comments)

525

[收藏](#)

在处理文档的时候，如果可以右键直接调用翻译软件的话，将可以大大提升我们的工作效率。

　　在处理文档的时候，我们常常需要使用到一些翻译软件，如果可以右键直接调用的话，将可以大大提升我们的工作效率。日前，锋友 [z26jns2](http://bbs.feng.com/read-htm-tid-11245959.html) 分享了一个在 Mac 的任意位置选中文字都可以直接调用谷歌翻译的方法，一起来看看吧。

[![](.evernote-content/ADE05704-44C1-4690-81E7-F49EA457D8A9/9F89BBAE-8940-4BFD-AB5C-03BFDBBB6D39.jpg)](http://resource.feng.com/resource/h061/h72/img201705021622360.jpg "锋友分享：Mac如何直接右键调用谷歌翻译？")

  
　　首先进入 Launchpad – 其他，打开 Automator 并且点击新建文稿，文稿类型选择“服务”，在左上角的搜索框输入 apple，在搜索结果中双击“运行 AppleScript”这一项。  
  

[![](.evernote-content/ADE05704-44C1-4690-81E7-F49EA457D8A9/1FCA5703-CCBE-415F-99D9-AD19D777C4CA.png)](http://resource.feng.com/resource/h061/h72/img201705021622371.png "锋友分享：Mac如何直接右键调用谷歌翻译？")

  
　　在右侧的编辑区中删除默认添加的代码，并且粘贴以下代码：  
  
　　on run {input, parameters}   
　　set output to "https://translate.google.cn/#auto/zh-CN/" & urldecode(input as string)  
　　return output  
　　end run  
　　on urldecode(x)  
　　set cmd to "'require \"cgi\"; puts CGI.escape(STDIN.read.chomp)'"        do shell script "echo " & quoted form of x & " | ruby -e " & cmd  
　　end urldecode  
  

[![](.evernote-content/ADE05704-44C1-4690-81E7-F49EA457D8A9/28AD85F2-53CC-40F3-B06F-6CEEBA6CE531.png)](http://resource.feng.com/resource/h061/h72/img201705021622382.png "锋友分享：Mac如何直接右键调用谷歌翻译？")

  
　　上述代码中的“/#auto”表示自动检测语言，“/zh-CN/”表示翻译为简体中文，你可以根据你自己的需求，改为“中译英”、“日译繁中”、“德译法”等等，具体的语言代码可以在浏览器中打开谷歌翻译，选择语言后在地址栏获取。  
  
　　接下来，继续搜索“菜单”，找到“网站弹出式菜单”并双击，在右侧的编辑区可以修改部分设置，比如大小选择“自定”，个人建议大小设为 720×480，位置选择“鼠标指标”。  
  
　　最后保存，可以修改为自己想要的名字。  
  

[![](.evernote-content/ADE05704-44C1-4690-81E7-F49EA457D8A9/C7FB9EDF-FC68-46C8-9045-502300011CF6.png)](http://resource.feng.com/resource/h061/h72/img201705021622393.png "锋友分享：Mac如何直接右键调用谷歌翻译？")

  
　　这时候，在 Mac 的任何地方，只要选中文本，并且右键点击，即可在服务中找到谷歌翻译并快速翻译。

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2017-05-02/Feng-friends-sharing-Mac-right-how-to-directly-call-Google-translation_677074.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bfd38e6d-35a7-4d68-ae4c-e780e5b52315/bfd38e6d-35a7-4d68-ae4c-e780e5b52315/)