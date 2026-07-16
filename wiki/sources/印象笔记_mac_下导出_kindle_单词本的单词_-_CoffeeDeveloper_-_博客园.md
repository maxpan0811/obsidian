---
title: "mac 下导出 kindle 单词本的单词 - CoffeeDeveloper - 博客园"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/mac 下导出 kindle 单词本的单词 - CoffeeDeveloper - 博客园.md
tags: [印象笔记]
---

# mac 下导出 kindle 单词本的单词 - CoffeeDeveloper - 博客园

# mac 下导出 kindle 单词本的单词 - CoffeeDeveloper - 博客园 --- mac 下导出 kindle 单词本的单词 ===================== 平常都是

---

# mac 下导出 kindle 单词本的单词 - CoffeeDeveloper - 博客园

---

mac 下导出 kindle 单词本的单词
=====================

平常都是用 kindle 来看电子书，偶尔也会看上一些英文书籍，不可避免的会遇到不少陌生的单词，而 kindle 专门针对这种需求，做了不少优化，可以直接在 kindle 上面查阅单词，甚至可以背单词。但是毕竟不是专门的英语学习工具，在复习陌生单词方面还是不够专业 (例如不能发音是个硬伤)，就想着导出单词到别的软件上复习。

而在 mac 下苦于不能直接用 [kindle mate](http://kmate.me/cn/) 这款软件 (我一次都没有用过这个软件，只是看到网上评论和使用比较多)，我也懒得去在 windows 虚拟机上面间接使用。一顿搜索之下，发现在 mac 下并没有直接导出 kindle 单词本的软件可提供使用。

经过一番思考，既然有第三方软件能够支持读取单词本这种功能，必然是存在方法在 kindle 上去获取单词本的数据。

直接将 kindle 通过 usb 链接到手机上，你会发现挂载了一个 `documents` 的文件夹，我在这个文件夹找了一圈，愣是没有找到。想着会不会有什么隐藏文件夹呢？  
![](http://oap12gnk8.bkt.clouddn.com/kindle-words-mount.png)

通过 `cd` 进入 kindle 的挂载盘，我发现除了 `documents` 文件夹外，还有一个叫做 `system` 的文件夹。顿时感觉有戏。层层递进，不负众望，在 `/Volumes/Kindle/system/vocabulary` 目录下，找到了 `vocab.db` 这个文件。

![](http://oap12gnk8.bkt.clouddn.com/kindle-words-ls.png)

`vocab.db` 是一个 `sqlite` 文件，如果你没有打开 `sqlite` 文件的软件可以下载一个 [SqliteBrowser](http://sqlitebrowser.org/)。

> SqliteBrowser 是开源免费的 Sqlite 数据库文件查看软件

通过 `SqliteBrowser` 可以直接看到到 `vocab.db` 的数据库下面的表  
![](http://oap12gnk8.bkt.clouddn.com/kindle-words-table.png)

在 `SqliteBrowser` 软件的 `Browse Data` 栏下，通过查看数据发现了两个有实际意义的数据表  
![](http://oap12gnk8.bkt.clouddn.com/kindle-words-table-words.png)

![](http://oap12gnk8.bkt.clouddn.com/kindle-words-table-lookups.png)

其中 `LOOKUPS` 表里面就是对应的你在那本书那块地方查询的这个单词的相关记录 (在 kindle 里面背单词可以看得到相关的数据)。  
`WORDS` 表就是我们单词本里面的所有单词数据了。

到这里，也宣告正式找到了 kindle 单词本的数据所在了。既然知道了数据在哪里了，剩下的导出就简单的多了，我只需要单词的 txt 文本，以便导入别的背单词软件，虽然可以通过软件直接导出，不过这种方式的复用性不够强。(考虑到导出单词是一个周期性的工作)

平时软件开发过程中，其实都已经安装好了 `sqlite3` 这个库，可以直接考虑用命令行来实现这个工作流程。

```
cp /Volumes/Kindle/system/vocabulary/vocab.db ~/
sqlite3 ~/vocab.db  "select word from words;" >> kindlewords.txt
```

将这两行 shell 命令保存成 `sh` 文件，这样我将 kindle 插入电脑的时候直接运行一下命令就可以直接得到我所需要的 txt 文件了，既简单又优雅。

> 后续考虑将整个流程自动化，从拷贝单词本到导入单词到相关的软件中。

Measure

Measure

---

[🌐 原始链接](https://www.cnblogs.com/coffeedeveloper/archive/2017/02/04/6366584.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ef9d6773-e3cf-4771-b294-14826b173a72/ef9d6773-e3cf-4771-b294-14826b173a72/)