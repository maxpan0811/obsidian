# Notion 小技巧 | Notion 如何快速记录？ - 少数派

---

Notion 如何快速记录？
==============

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

我每天都用 Notion，它是我最喜欢的任务管理和笔记软件。但 Notion 少了一个像 [Unclutter](https://sspai.com/post/28798) 一样的「快速记录」模式，后者可以节省了大量时间，帮助我快速记录新内容或是新想法。

另外 Unclutter 也有缺点，它只支持纯文本，不支持 Markdown 和图片，也没有自带的云同步功能（iCloud 可以实现同步）。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/E9D731E5-72C7-4324-8297-6E5141E7EB0B.gif)

Unclutter 的操作方式

好在通过最近的摸索，我发现在 Mac 上实现 Notion「快速记录」有两种方式：

**方法一**：使用软件 [Fluid](https://sspai.com/post/29160) 将 Notion 固定在 Mac 的**菜单栏**上，点击菜单栏 icon 即可记录。相比于方法二，好处是能简化页面样式，干净舒服。

**方法二**：使用软件 [Slidepad](https://sspai.com/post/55546) 或 Better and Better 将 Notion **吸附**到 Mac 的侧边，鼠标碰到侧面就会出现。相比于方法一，好处是操作更加方便快捷。

方法一：固定在 Mac 的菜单栏里
-----------------

Fluid 是一个将网站变成应用程序的 Mac 实用程序。因为 Notion 提供了 Web 版本，我可以将每个重要的 Notion 页面制作成 Fluid 应用程序，并将其固定在菜单栏上。通过使用浮动窗口来将这些网页悬停在我的其他窗口上，并结合自定义的 CSS，让界面更加简洁。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/737DDBC8-C8FB-42A8-8AC8-A229825A4934.gif)

来自 https://bensmith.uk/，在「Notion中文社区」得知

### 步骤

1. **安装** Fluid ，前往 http://osen.deisgn 搜索「Fluid」下载

2. 打开 Fluid，出现如下窗口，**填写**相关信息。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/F449CB2E-7DF7-4A41-9C39-CAC069BB48A6.png)

* 「URL」是 Notion 页面的分享链接 (位于「共享」菜单中)
* 「Name」 最后会显示在 「应用程序」 里的名称。
* 「Location」 是这个 App 的安装目录，推荐「Application」；「Icon」是最后显示在菜单栏上的 icon（后面也可以修改），可以自定或用下面这个。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/E24C0032-7E22-45C4-9F77-B02E9E00B539.png)

Notion\_logo

3. 首次打开需要先**登录**，在然后就能进去页面

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/33E96DF4-E544-4D42-9A33-573963497EAA.png)

4. 然后点击 App 右上角的菜单 - **Preferences** 进行配置

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/BA81CE16-FE1A-4381-A714-8B10B6ABDD92.png)

在这个屏幕上最重要的改变是设置 Window level 为「floating」，可以让窗口在最顶端。

### 固定在菜单栏

点击菜单上的 **Pin to Status Bar**，然后点击 OK，重新打开 APP 即可。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/B9D2CCAB-B581-4F9E-B8C0-7A4A5D81F00A.png)

### 简化界面

将 Notion 中的侧边目录、标题去掉，变成一个**干净、沉浸**的页面。

1. 右键菜单栏上的 icon，选择「Userstyles」

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/BEB890BA-A1A7-495A-A823-CD5050DD45A6.png)

2. **复制**下面的代码（注意不要用快键键 Cmd+A 全选），如下图操作，完成后关闭窗口并重新启动应用程序，大功告成。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/56E21183-8623-4B1C-8429-A0D4335C0FCC.gif)

代码如下：

```
	/* CSS version 4 - updated 8th May 2019 */  
/* This version adds support for pop-ups on database screens and hides commenting */  
  
div.notion-topbar>div>div:first-child,  
div.notion-topbar>div>div:last-child,  
div.notion-help-button,  
div.notion-sidebar-container,  
div.notion-frame div.notion-scroller.vertical.horizontal>div:first-child,  
div.notion-frame div.notion-scroller.vertical:not(.horizontal)>div:first-child,  
div.notion-frame div.notion-scroller.vertical.horizontal>div>div>div.notion-selectable,  
div.notion-frame div.notion-scroller.vertical:not(.horizontal)>div>div>div:not(.notion-selectable)>div>div:nth-child(1),  
div.notion-frame div.notion-scroller.vertical:not(.horizontal)>div>div>div:not(.notion-selectable)>div>div:nth-child(2),  
div.notion-frame div.notion-scroller.vertical:not(.horizontal)>div>div>div:not(.notion-selectable)>div>div:nth-child(3),  
div.notion-peek-renderer>div:nth-child(2)>div:first-child,  
div.notion-peek-renderer> div:nth-child(2)>div.notion-scroller.vertical>div:nth-child(3)>div {  
    display:none !important;  
}  
  
div.notion-topbar,  
div.notion-topbar>div {  
    height: 30px !important;  
}  
  
div.notion-page-controls {  
    visibility:hidden !important;  
    margin-top: 0px !important;  
}  
  
div.notion-page-content {  
    padding-left: 20px !important;  
    padding-right: 8px !important;  
}  
  
div.notion-selectable {  
    max-width: none !important;  
}  
  
div.notion-topbar,  
div.notion-cursor-listener,  
div.notion-frame,  
div.notion-frame>div:nth-child(1),  
div.notion-frame > div.notion-scroller.vertical > div:nth-child(1) {  
    width: 100% !important;  
    max-width: 100% !important;  
}  
  
div.notion-frame>div.notion-scroller.vertical:not(div.notion-scroller.horizontal)>div:nth-child(2),  
div.notion-frame>div.notion-scroller.vertical>div.notion-scroller.horizontal>div {  
    padding-left: 12px !important;  
    padding-right: 12px !important;  
}  
  
div.notion-peek-renderer>div:nth-child(2) {  
    top: 5% !important;  
    left: 8% !important;  
    right: 8% !important;  
}  
  
div.notion-peek-renderer>div:nth-child(2)>div.notion-scroller.vertical>div:nth-child(1)>div,  
div.notion-peek-renderer>div:nth-child(2)>div.notion-scroller.vertical>div:nth-child(2)>div {  
    padding-left: 20px !important;  
    padding-right: 20px !important;  
}
```

### 多个标签页

按 Cmd 键点击另一个页面，就会在顶部新建一个标签页。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/4293EE9C-335E-432A-AFF9-68DB00507A14.png)

方法二：固定在侧边
---------

Slidepad 和 Better and Better 这两个软件都可以吸附在侧边，区别是 Slidepad 借助第三方登录 Web 版 Notion，可以使用置顶功能；Better and Better 可以直接针对 Notion 官方客户端进行吸附，但不能置顶。

这里只详细说了软件 Slidepad 的使用，Better and Better 安装后在设置中开启吸附，然后点击窗口 `Ctrl+Cmd+Option+→` 即可吸附。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/4B911570-350A-4BE7-BF38-78A58161D7DD.gif)

### 步骤

1. **安装** Slidepad ，前往 http://osen.deisgn 搜索「Slidepad」下载

2. 打开 Slidepad，**点击 「+」**，选择 Notion，登录即可享用。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/9779D919-A4A4-467A-9DB6-5EB47CF36EE9.png)

### 固定窗口

将窗口固定并置顶，方便将图片拖到窗口中。

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/6B36FB6D-5273-40A8-91CF-AC04433B51CB.png)

总结
--

两种方式记录起来都挺方便的，能做到最快速度记录灵感和想法。

而适当延展一下，Fluid 和 Slidepad 还能对其他 Web 应用做快速访问，如 Evernote、Email、Slack 等等。有一点需要注意的是，网络不好的情况下，不要去刷新 Fluid 的页面，不然会丢失数据（测试 Slidepad 无网是无法刷新的），等待网络恢复后自动同步。

附：测试同步速度

![](.evernote-content/E6667B31-53DC-4012-BB71-7E2524C2144A/725C909C-9351-47A2-A036-9C5D0CCAAE24.gif)

感谢你的阅读，下周再见

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57340)

[📎 在印象笔记中打开](evernote:///view/207087/s1/04a35a13-5d5f-4803-810e-3923fbdf9e94/04a35a13-5d5f-4803-810e-3923fbdf9e94/)