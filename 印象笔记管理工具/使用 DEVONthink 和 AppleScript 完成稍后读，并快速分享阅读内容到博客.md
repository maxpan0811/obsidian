# 使用 DEVONthink 和 AppleScript 完成稍后读，并快速分享阅读内容到博客

---

使用 DEVONthink 和 AppleScript 完成稍后读，并快速分享阅读内容到博客
==============================================

06 月 02 日

[![](.evernote-content/A0EAD7DE-FB43-47CA-A3AE-7F59EE4C8A65/2D48F50F-CFDB-4E47-85D6-FAC773FEF713)](https://sspai.com/user/870817/updates) 

#### [Blanboom](https://sspai.com/user/870817/updates)

### Matrix 精选

Matrix 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

本文将介绍我使用 DEVONthink 做为稍后读工具，完成稍后读的流程；以及如何使用 AppleScript 将阅读到的内容自动整理为 Markdown 文档，以便于在博客中分享。

从 2019 年 2 月份起，我开始在我的博客中，通过「[每月收藏与分享](https://blanboom.org/tag/%E6%AF%8F%E6%9C%88%E5%88%86%E4%BA%AB/)」，分享自己阅读到的有趣内容，同时也是对自己每个月阅读的内容、观看的视频做一个简单的整理和回顾。但每次完成这样的博文，总会花费不少时间和精力......

在 5 月份，我开始尝试使用 [DEVONthink](https://www.devontechnologies.com/apps/devonthink) 做为自己的稍后读工具。在完成文章的阅读之外，还通过编写一个 AppleScript, 利用 DEVONthink 的强大功能，自动将要分享的文章生成为一份 Markdown 文件，稍加修改后，即可分享到博客。

收集
--

对我来说，我已经将 DEVONthink 用做自己的笔记软件和文档管理工具；所以，我也很自然地开始尝试用 DEVONthink 做为自己的稍后读工具，而不是使用 [Pocket](https://getpocket.com/)、[Instapaper](https://www.instapaper.com/) 这样的在线服务。

对于我常用来阅读文章的 App，例如 Safari 浏览器、[Fiery Feeds](http://cocoacake.net/apps/fiery/)、[奇点](https://itunes.apple.com/us/app/%E5%A5%87%E7%82%B9-%E8%BD%BB%E8%BD%BB%E6%9D%BE%E6%9D%BE%E5%88%B7%E5%BE%AE%E5%8D%9A/id947792507)、[Tweetbot](https://tapbots.com/teetbot/) 等，都支持通过 Share Sheet 将当前文章添加到 DEVONthink，供稍后阅读。

![](.evernote-content/A0EAD7DE-FB43-47CA-A3AE-7F59EE4C8A65/C79482FA-DA1D-47D8-80F1-FAB34F68AAAF.png)

将 Fiery Feeds 中待阅读的文章添加到 DEVONthink

如果想进一步了解做为稍后读工具，DEVONthink 有哪些优缺点，推荐阅读这篇文章：[Using DEVONthink as a Read-it-later Service -- The Sweet Setup](https://thesweetsetup.com/using-devonthink-as-a-read-it-later-service/)

阅读与整理
-----

在我开始在博客中进行「每月收藏与分享」后，最大的一个收获，就是能够使自己每个月抽出一段固定的时间，读完所有的待阅读文章，避免「稍后阅读」变成「永远不读」。

对于每篇稍后读文章，根据文章内容的不同，处理方式也有区别：

* 部分文章可能已经没有了继续阅读的价值，直接删除即可；
* 对于知识类文章，如果需要保存和整理，则会使用 DEVONthink 中的「Duplicate to」选项，复制一份到对应的目录下；
* 对于待办性质的文章，会转换为待办事项添加到 [Things](https://culturedcode.com/things/) 中（例如 [每月收藏与分享（201902）](https://blanboom.org/2019/201902/) 中提到的 [中关村创业博物馆](http://www.xinhuanet.com/local/2018-09/16/c_1123438091.htm)，就是我打算去的地方，所以将其做为待办事项处理。顺便提一下，这个博物馆内最近新开了 [品果时光电脑博物馆](https://mp.weixin.qq.com/s/dl7_nuiKnb6pmZPH-clcQQ)，如果对老电脑感兴趣，值得来参观）;
* 对于值得分享到博客中的文章，则会添加上「好奇心」、「生活」、「观点」、「技术」等 Tag，并添加注释，方便后续通过 AppleScript 生成分类整理并生成 Markdown 文件。而不需要分享的文章，则在阅读后直接删除。

下图是我使用 DEVONthink 阅读稍后读文章的整个流程：

![](.evernote-content/A0EAD7DE-FB43-47CA-A3AE-7F59EE4C8A65/71CAAAB2-2630-4141-9FAB-61BEED524FF8.png)

使用 DEVONthink 进行稍后读的流程

分享到博客
-----

经历了上面的步骤，在阅读完稍后读文章的过程中，同时也对文章进行了初步的分类和整理，只留下了需要分享的文章。

这时候，选中所有要分享的文章，运行下面的 AppleScript，就能自动生成包含所有要分享文章的 Markdown 文档。然后可根据需要进行进一步修改，并发布到博客。

```
# 用于从 DEVONthink 中生成我的博客中的《每周收藏与分享》文章，例如：https://blanboom.org/2019/201904/

# 参考了如下脚本：http://forum.eastgate.com/t/script-to-export-certain-devonthink-metadata-in-a-tsv-for-tinderbox-import/1105

# 用于匹配 DEVONthink 中文章的 tag，将文章放在合适的分类下，可根据实际需求修改

# 最后一个空字符串用于匹配未加 tag 的文章，不要删除

property tagList : {"好奇心", "生活", "Making", "观点", "工具", "游戏", "技术", ""}

tell *application* *id* "DNtp"

  try

    set theSelection to the selection

    if theSelection is {} then error "请选中需要生成的文档"

    set theFile to choose file name default name "每月收藏与分享.markdown"

    set theMarkdown to my createMarkdown(theSelection)

    set thePath to POSIX path of theFile

    if thePath does not end with ".markdown" then set thePath to thePath & ".markdown"

    do shell script "echo " & quoted form of theMarkdown & ">" & quoted form of thePath

    hide progress indicator

  on error error_message number error_number

    hide progress indicator

    if the error_number is not -128 then display alert "DEVONthink Pro" message error_message as *warning*

  end try

end tell

on createMarkdown(theseRecords)

  local these_records_before, these_records_after

  local current_tag

  local this_record, this_markdown, this_tags, this_name, this_URL, this_comment

  tell *application* *id* "DNtp"

    set this_markdown to ""

    set these_records_before to {}

    set these_records_after to theseRecords

    repeat with current_tag in tagList

      -- 下一轮循环，只处理未处理过的 record

      set these_records_before to these_records_after

      set these_records_after to {}

      -- 设置一级标题

      set current_tag to current_tag as *string*

      if current_tag is equal to "" then

        set this_markdown to this_markdown & "# 其他" & return & return

      else

        set this_markdown to this_markdown & "# " & current_tag & return & return

      end if

      repeat with this_record in these_records_before

        set this_tags to (tags of this_record) as *string*

        if (this_tags contains current_tag) or (current_tag is equal to "") then

          -- 文章标题

          set this_name to name of this_record as *string*

          -- 为文章标题添加链接

          set this_URL to URL of this_record as *string*

          if this_URL begins with "http" then

            set this_name to "[" & this_name & "](" & this_URL & ")"

          end if

          -- 为文章标题添加对应的格式

          set this_markdown to this_markdown & "- **" & this_name & "**" & return & return

          -- 添加注释

          set this_comment to comment of this_record as *string*

          if this_comment is not equal to "" then

            set this_markdown to this_markdown & this_comment & return & return

          end if

        else

          set end of these_records_after to this_record

        end if

      end repeat

    end repeat

  end tell

  return this_markdown

end createMarkdown
```

下图就是使用这段脚本直接生成的 Markdown 文档，包含了文章标题、文章链接、批注等信息：

![](.evernote-content/A0EAD7DE-FB43-47CA-A3AE-7F59EE4C8A65/76BE6020-5DE6-4CC0-BB2F-5BBC9772C5E1.png)

使用 AppleScript 生成的待分享 Markdown 草稿

归档
--

分享到博客后，DEVONthink 中保存的稍后读文章，就可以直接删除了。

但对我说，我不想马上删除这些文章，而是想将这些文章保存一段时间，便于后续搜索和查找。所以，我在 DEVONthink 中新建了一个名为「归档」的数据库，用于保存已阅读的文章。以后等「归档」数据库超过一定大小后，计划再写一个脚本，通过程序自动清理旧的文章。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，让你的工作更有效率 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://sspai.com/post/https-//shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

---

[🌐 原始链接](https://sspai.com/post/55041)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1b93089f-bf4b-4aa6-9c09-5785239ab1f8/1b93089f-bf4b-4aa6-9c09-5785239ab1f8/)