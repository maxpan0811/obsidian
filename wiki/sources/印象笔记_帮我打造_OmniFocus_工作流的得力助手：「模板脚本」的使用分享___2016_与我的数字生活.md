---
title: "帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 _ 2016 与我的数字生活"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 _ 2016 与我的数字生活.md
tags: [印象笔记]
---

# 帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 _ 2016 与我的数字生活

# 帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 | 2016 与我的数字生活 --- ![](.evernote-content/0DE4C0FD-DB6D-4C1F-88

---

# 帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 | 2016 与我的数字生活

---

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/FA9C7CA6-2B78-46A3-BE15-3C29878E4B15.jpg)

### *「2016 与我的数字生活」年度征文入围作品*

今年，我们在 [2016 年度盘点](http://sspai.com/topic/2016/) 中举办了一次大型年度征文活动，鼓励大家围绕「数字生活」为主题，回顾刚刚过去的 2016 年。我们给予最开放的选题、最自由的投稿方式、有史以来最丰厚的 [奖品](http://cdn.sspai.com/attachment/thumbnail/2016/12/26/faeb3befe1e2d8c138a027f0b72d30675810b_mw_800_wm_1_wmp_3.jpg)，以及跨越春节的两个月充足时间，等你参与。你可以 [点此查看](http://sspai.com/36695) 活动规则和奖品清单。

本文是「2016 与我的数字生活」征文活动的**第 4 篇**入围作品，我们会在两个月的活动期内，不定期从收到的投稿中挑选发布优秀的文章。所有经此发布的文章，即为已入围征文活动。本文仅代表作者本人观点，少数派仅对标题和排版略作调整。

在[《喜欢效率工具的法官 JannerChang，用 GTD 来处理案件判决》](http://sspai.com/36575)一文中，我介绍了我的工作流整体运转情况。因为各环节的实现细节稍微繁琐，没有详细介绍，今后我会有针对性的介绍其中的实现方法，本文并非是教程，只是分享下自己的思路和经验，希望能对读者有些许的帮助。

对于 [OmniFocus](http://sspai.com/tag/OmniFocus) 的购买建议，我个人建议一定要购买 Mac 上的 Pro 版，Pro 版主要是提供了对 AppleScript 的支持，iOS 版则看个人需要，我是很少打开看的。

OmniFocus 体系的建立
---------------

OmniFocus 是最符合 GTD 理念的一个 App，但也不是说我们一定要按照 GTD 的理念去做事情，适合你的 App 才是最好的，实在没有适合的就需要去调教它，我曾经也一度打算使用 [The Hit List](https://itunes.apple.com/cn/app/hit-list-simply-powerful-tasks/id432764806?mt=12&uo=4&at=10lJSw) 去替换 OmniFocus，但是最终还是回到 了 OmniFocus。

OmniFocus 能建立「顺序执行」的项目是我倚重它的主要原因，因为我的工作就是具有固定执行顺序的，可以通过 Context 很方便的查询进度安排工作。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/9DCD4E7B-5A4F-4664-A4E1-4118356534C1.jpg)

### 项目分解

使用 GTD 管理自己的工作，就要对工作进行分解或者归集，我是根据案件审理流程对 Context 进行分解，每个阶段是一个 Context。

Context 官方翻译是「上下文」，我刚接触这个概念的时候很迷茫，其实翻译成「场景」更好，可以是人、地点、时间段等等，这就好理解了，我的 Context 就是工作阶段。

任务分解是个长期而持续的过程，经常会在使用的过程中进行调整，不要想一开始就能建立一个完美的体系。我也是经过多次分解再归集才形成如下的结构：

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/76A11368-14A5-4034-AD39-149F29D5EE60.jpg)

我把每个案件都当作一个项目来处理，对于每年收一百大几的案件的我来说，每次都需要不停的新建项目，添加任务，设置 Context，这是一个枯燥又繁琐的工程，OmniFocus 又不提供模板功能，一度想要放弃，直到看到[《工具控的福音》](https://www.douban.com/doulist/1999298/)（这绝对是国内绝无仅有的启蒙教程），里面介绍了一个「模板脚本」简直帮了我的大忙，立刻将所有案件录入 OmniFocus，这才正式进入 OmniFocus 的世界。

我使用中的脚本
-------

自从熟悉了 OmniFocus 的脚本后就一发不可收拾，开始寻求各种脚本和改编脚本的过程。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/6BD336CF-9A52-43F0-A87C-ABC486B873B4.jpg)

### Templates

这是一个很复杂和强大的脚本，可以设置很多变量，相当的灵活。被我搬到了 [Keyboard Maestro](http://sspai.com/tag/Keyboard%20Maestro) 后，可以实现批量的变量赋值。原始「模板脚本」[点此下载](https://github.com/lemonmade/templates)，模板使用办法及说明都讲述的很清楚，实在不懂的可以与我交流（新版本 [点此下载](https://github.com/FradSer/templates-for-omnifocus%E2%80%932)）。

直接使用该脚本的话需要一步一步逐一添加变量，有时候时间长了容易失败，而且一旦输入错误就没法返回修改，我就改编成 Keyboard Maestro 可操作的版本，主要是实现对变量的批量录入。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/FF7F7641-D1D7-4FA7-B999-63048DB7156C.jpg)

### Folder

项目建立好后，因为需要对文档进行管理，使用 Folder 脚本在 Finder 中建立与项目同名的文件夹。该脚本同样是 Templates 脚本作者所写，原脚本提供了更多的功能（[点此下载](https://github.com/lemonmade/support)）。

我是根据自己的需求对脚本做了个简化，只有建立文件夹和打开文件夹的功能。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/850C1001-97A8-462A-AB9E-3D475BB714F9.jpg)

### Calendar

有些任务会有固定的时间去完成，OmniFocus 的提醒较弱，所以结合日历来实现会更直观。

选择你要发布到日历里的任务，设置好推迟时间，运行该脚本，选择日历即可，可批量处理。该脚本我后续是整合到了 Done&StartNext&Publish 里，同时执行多个操作。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/552C081F-9289-4BAF-98D6-FCE61BA9048D.jpg)

### FollowUp

有时候在你的工作流程中会有中断事项出现，在中断事项完成后才能开始下一任务。

因为在工作过程中经常出现一个突发事件，导致工作流的中断，比如：调解等，在查看各阶段任务时会产生干扰，根据此需求编写一脚本如下：

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/C0891AA7-BF86-4F08-937C-F086BA018FAC.jpg)

```
-- 在一个项目中插入一个跟踪任务 
-- Context 为“FollowUp”，没有可以新建 
-- 在右侧内容窗口中，选中一个 task 或者 project 后运行脚本，会在该 task 任务所在的项目里创建一个 task 并移动到首位
 
 
 
tell front document of application "OmniFocus"  
    set contextName to first context whose name is "FollowUp"  
    tell content of document window 1  
        try  
            set OmnifocusItem to value of selected trees  
            set projectName to name of containing project of item 1 of OmnifocusItem  
        on error errText number errNum  
            if (errNum is equal to -1728) then  
                -- User cancelled. 
                display dialog "请选择一个任务或者项目后再运行"  
            end if  
        end try  
    end tell  
    tell containing project of item 1 of OmnifocusItem  
        set taskName to text returned of (display dialog "输入任务名称" default answer "输入任务名称")  
        set insertTask to make new task with properties {name:taskName, context:contextName}  
        move insertTask to beginning of tasks of containing project of item 1 of OmnifocusItem  
    end tell  
end tell
```

### Done&StartNext&Publish

该脚本是个流操作，以前我是在发完传票后挨个设置开庭时间，然后使用 Calendar 脚本发布到日历，使用中觉得还是比较麻烦，就编写该脚本。

**操作流程：**

1. 「阅卷」后，定下开庭时间；
2. 将该时间设置为「发传票」任务的截止时间；
3. 然后运行该脚本。

**脚本工作流程:**

1. 将「发传票」的截止时间设置为下一个任务「开庭」的开始时间；
2. 设置「发传票」任务完成；
3. 将「开庭」的开始时间发布到日历。

```
tell front document of application "OmniFocus"  
    tell content of document window 1  
        try  
            set OmnifocusItem to value of selected trees  
            repeat with thisItem in OmnifocusItem  
                set projectObject to containing project of item 1 of thisItem  
                set dueDate to due date of item 1 of thisItem  
                set completed of item 1 of thisItem to true  
                set nextTask to next task of projectObject  
                set defer date of nextTask to dueDate  
                set deferDate to defer date of nextTask  
                if estimated minutes of nextTask is not missing value then  
                    set estimatedTime to estimated minutes of nextTask  
                else  
                    set estimatedTime to 60  
                end if  
                set dueDate to due date of nextTask  
                if note of nextTask is not "" then  
                    set eventName to note of nextTask  
                else  
                    set eventName to name of nextTask  
                end if  
                set eventStartDate to deferDate  
                set eventEndDate to eventStartDate + estimatedTime  
                set eventURL to "omnifocus:///task/" & (id of nextTask) as string  
                if dueDate is missing value then  
                    set dueDate to eventStartDate + (estimatedTime / 60) * hours  
                end if  
                tell application "Calendar"  
                    activate  
                    set theCalendars to title of every calendar  
                    try  
                        set calendarName to item 1 of (choose from list theCalendars with prompt "选择日历" without multiple selections allowed)  
                        if calendarName is not false then  
                            tell calendar calendarName  
                                make new event with properties {start date:eventStartDate, end date:dueDate, summary:eventName, url:eventURL}  
                            end tell  
                        end if  
                    end try  
                end tell

            end repeat  
        on error errText number errNum  
            if (errNum is equal to -1728) then  
                -- User cancelled. 
                display dialog "请选择一个任务或者项目后在运行"  
            end if  
        end try  
    end tell  
end tell
```

### Shell 脚本

该脚本需要通过 brew 安装 brew fswatch 和 brew tag 来配合使用。

[原始脚本](https://github.com/RobTrew/tree-tools/tree/master/OmniFocus%20scripts/Shell%20scripts%20for%20Geektool%20or%20logging) 是通过 Hazel 监视 OmniFocus 的数据库，将完成的任务发布到 Day One 中，我这样的级别自然驾驭不了 Shell 脚本，故拜托群内 A 哥帮忙修改了一下。

该脚本流程：

1. 通过 fswatch 监视 OmniFocus 的数据库文件；
2. 发现有任务完成，根据条件判断，我是判断 Context；
3. 符合条件的执行相应的操作，这里用 tag 设置 Finder 文件夹 的 tag。

![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/A29228CE-83C5-4BD0-A577-DCE8CA20D059.jpg)

总结
--

很多人使用 OmniFocus 都是因为业界的广泛宣传，刚接触 GTD 的朋友在搜索教程时看见最多的肯定是 OmniFocus，但是 OmniFocus 上手并不容易，虽然其自身提供了完整的 GTD 流程，但是让能真正为自己服务好，就需要使用系统级脚本语言 AppleScript 对其进行扩展。

OmniFocus 提供了丰富的 AppleScript 接口，你可以提取和修改你需要的绝大部分数据，这就为你提取 OmniFocus 数据给其他 App 用，或提取其他 App 数据给 OmniFocus 提供了坚实的基础。

以上大部分脚本都在 [wiki](http://codesucker.com/doku.php) 中有详细介绍。如有其他疑问，可加入 [wiki](http://codesucker.com/doku.php) 中的 Telegram 群，也可微博与我交流。

（如果你喜欢这篇文章，我们鼓励你在文末点赞和评论，这会成为 [征文活动](http://sspai.com/36695) 最后评奖的参考之一）

文章来源 [少数派](http://sspai.com) ，原作者 [Janner Chang](http://sspai.com/author/735387) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/0DE4C0FD-DB6D-4C1F-88EE-9C95FD635B41/AEA93720-37C5-452D-9D62-DC614D218066.jpg)](http://sspai.com/topic/2016/)

---

[🌐 原始链接](http://sspai.com/36927)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4dac9590-4bcc-4c57-82f9-984bb5d6c48b/4dac9590-4bcc-4c57-82f9-984bb5d6c48b/)