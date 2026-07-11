# 官方 iCloud 云盘将 Windows 10 PC 融入 Apple 生态 - 少数派

---

官方 iCloud 云盘将 Windows 10 PC 融入 Apple 生态
=======================================

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/0FD2EE9D-4333-46CC-A018-AA6C2BFCC81B)

官方 iCloud 云盘将 Windows 10 PC 融入 Apple 生态

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

作为一名忠实多年的果粉， Apple 全家桶自然是不会少的。iCloud 则是将 Apple 全家桶中的各种设备结合在一起的粘合剂，通过 iCloud 无缝同步各类内容（文件、相册、通讯录、邮件等等）也一直是 Apple 设备诱人的功能之一。在 iCloud 的众多服务中，iCloud 云盘则是用来多设备同步文件的好帮手，没有广告、价格合适，并且（在当前的网络环境下）速度也很快。我目前开了 200G 的 iCloud 云盘容量，并且由于家中大部分设备是 iPhone 和 iPad，所以还启用了家庭共享，这样家人也可以利用较大的容量通过 iCloud 存储文件、备份手机。

Apple 的生态自然是好，可是当一台 Windows PC 加入我们的设备列表，麻烦的事情就多了起来。PC 和 Apple 设备间文件难以同步、应用不能通用，如果能够像 macOS 和 iOS 中的文件应用一样将 iCloud 云盘直接整合到 Windows 文件资源管理器，再加上能够读取其中文件的类似应用，就能够一定程度上解决文件互通的问题。而能够将 Windows 10 也纳入 Apple 的文件管理系统中的，不是别的，正是 Apple 官方提供的 [iCloud for Windows](https://support.apple.com/zh-cn/HT204301) 软件。iCloud for Windows 已经上架 [Microsoft Store](https://www.microsoft.com/store/apps/9PKTQ5699M62)，但是仅有 Windows 10 1903（Windows 10 版本 18362.145）及以上版本才能够正常下载安装1 。

登录 Apple ID、进行设置后，iCloud 会自行开始同步 iCloud 云盘中的内容，此时已经可以在文件资源管理器中找到 iCloud 云盘的内容。iCloud 云盘不仅会下载常用的文件和文件夹，同时还会将使用 iCloud 的 iOS 或者 macOS app 所建立的文件夹直接下载到本地硬盘上，并且根据文件最近是否被使用来动态保留在本地，从而可以实现快速的读取。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/C08E77EC-3EC5-49DE-B7BD-D0E57602D8B5)

我 iCloud 云盘中的根目录

文件管理
----

iCloud 在 Windows 上与系统的契合还是不错的，支持 Windows 的文件资源管理器直接浏览所有 iCloud 云盘上存储的文件，并且可以使用 Windows 资源管理器所能够提供的几乎所有操作，从复制粘贴到创建桌面快捷方式：

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/C29D8293-9108-469B-BC7B-DC1F4193A02A)

iCloud 文件可以像 Windows 文件一样管理

因此，你总是可以直接将 Windows 文件管理的习惯直接用在 iCloud 云盘中的文件管理上，而不用重回 Mac 上的文件管理方式以至于造成割裂感。当然，有一些 iCloud 的专属操作会让你觉得梦回 macOS，这些也是 iCloud 的核心功能。

### 文件上传与下载

如果想要把文件上传到 iCloud 云盘，只需要直接把文件或者文件夹拖入已经存在 iCloud 云盘的目录中，就会自动上传，并且在状态这一栏中显示上传进度与当前电脑上的可用状态。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/6D5E1D98-90DA-4678-85FE-F46238730FCF)

可以在 Windows 资源管理器随时查看文件可用状态

而如果要将文件强制保存在本地，或者将已经上传但是现在已经不用的文件从本地删除从而节省空间，只需要右键单击某个文件或者文件夹并且点击相应的选项就可以了。默认情况下，得益于 Windows 10 所具有的网盘文件自动下载功能和 iCloud 的支持，如果你在使用电脑的时候用到 iCloud 中的文件，它会自动下载到本地以供使用。如果应用是 UWP 应用并且支持微软的自动下载 API，甚至会有可管理的通知来提醒你文件正在自动下载。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/6879E19C-DC2C-403D-8B12-4BF9537E67C7)

自动文件下载通知

### 可以选择将文件永远保存在 Windows 本地，或者删除以释放空间

### Windows 10 存储感知

macOS 上的 iCloud 云盘存储会根据上次使用文件内容的日期来自动将文件从本地磁盘清除从而节省空间，而 Windows 上的 iCloud 云盘也提供了相似的功能，因为它接入了 Windows 10 的存储感知 API。因此，可以直接在 Windows 10 的系统设置中选择自动删除本地文件副本的时间，从 1 天到 60 天。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/81657AB0-7104-4730-968F-1B09734C580A)

Windows 10 存储感知设置中的 iCloud 云盘

### 与 Mac 和 iOS 上一致的 iCloud 共享

右键菜单中可以看到 iCloud 共享的选项，点击它就会打开 iCloud 共享对话框，其中可以直接文件或是文件夹的共享方式与各位用户的权限，当然也可以随时复制共享链接或者直接停止共享。这些都与 Mac 和 iOS 上的 iCloud 共享是一致的。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/DC0271C6-CC5B-4825-89EA-06A7F92E1BF5)

Windows 下 iCloud 共享文件和文件夹

一些活用
----

文件读写是计算机软件系统的基本操作。从这一点出发，其实只要自己的文件处于 iCloud 云盘的同步范围内，就可以被各类 app 读取和编辑，从而能够实现 Windows PC 和 Apple 设备的互联互通。以下是我日常生活中很常用的一些方法，仅供参考。

### 工作文件夹上云

我目前是文科研究生在读，云上的文档大多是一些文字稿、论文、笔记，这些文件的共同点是：大小比较小，即使不通过较为快速的方法也可以在短时间内同步。因此，我将工作文件夹放在了 Mac 的桌面上，并且将 iCloud 云盘设置为同步桌面和文稿两个文件夹，这样就可以将工作文件夹也同步到 Windows 10 电脑上。为了体验一致，我同样把 Work 这个文件夹创建了桌面快捷方式，并且放进了 Windows 资源管理器的快捷访问中。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/DFB659D6-895F-402A-9351-E2723A5FBA10)

保持在云端的工作文件夹，点击即得到

因此，大多数时候，我要访问我工作使用的大部分文件时，只需要在 Windows 10 上打开桌面上的工作文件夹快捷方式即可。更改都会随时保存在 iCloud 中，我就可以从各个其他位置访问：iPhone、iPad 或是 MacBook。例如，我经常需要在电脑上编辑 Excel 和 Word 文档，并且利用手机或者平板电脑查看这些文档，并且做一些小的调整修改。iCloud 则能够帮助我将文件保持在所有设备上都有最新的版本随时可用，这大大提高了效率，不用微信或者其他方式来回在电脑和手机之间传送文件。

文件大小较小时，iCloud 可以在数秒内将文件上传，并在另一端实时下载。

### Typora 与 Ulysses 联动编辑文稿

Markdown 文稿在我的全平台设备上难以同步编辑也一直是困扰我的问题：Typora 很好用，然而没有 iOS 版本；Ulysses 也很好用，然而没有 Windows 版本。利用 iCloud 云盘的功能，至少可以实现在 Windows 上使用 Typora 来编辑 Markdown 文稿后使用 iPad 或者 Mac 上的 Ulysses 继续的功能。二者对于 Markdown 的支持类似，甚至都是基于文件夹的文档编辑工具，因此用来联动编辑 Markdown 文稿也是十分合适的。

Ulysses 在默认的 iCloud 文件夹之外，还支持从 iCloud 云盘中导入外部文件夹，并将其归类在最后的「外部文件夹」部分列表中。文件夹作为分类来显示，并且可以给分类指定标签和图标。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/5FDE0A12-2F88-4561-9B29-751521BF74B9)

Ulysses 利用外部文件夹功能导入 iCloud 云盘中的文档

像这种 Windows 和 Apple 设备不能共用的相似问题还有不少，如果是涉及通用格式的文件编辑（比如这里的 Markdown），我想 iCloud 云盘是解决问题的一种思路。

### 从 Windows 直接打开保存到文件 app 的任意文档

iOS 上的分享功能十分强大，可以将几乎所有类型的文件直接保存到 iCloud 云盘中的文件夹。在 iPadOS 13 中，更是支持直接在文件保存页面新建文件夹并且重命名当前分享出来的文件。这可以看作是 AirDrop 的一个 iCloud 版本，因为任何保存到文件 app 中 iCloud 云盘的文件都会即时上传并且在 Windows 10 上可用，因此可以在 Windows 中直接打开保存的文档。

![](.evernote-content/FBCD2C7E-0B76-4B99-B7DA-23BDD5ABDAC5/07B47D77-AD13-47D4-859F-3301AA6C5CFC)

从 iPad 向 iCloud 云盘保存文件

### 与其他云服务的整合

我同时还在使用的云服务有 Microsoft OneDrive、Google Drive 和 Adobe Creative Cloud。

OneDrive 是购买 Microsoft 365 服务中的一个部分，我很少用，一方面是因为 OneDrive 在 macOS 和 iOS 上的体验完全不如 iCloud 在 Windows 上的体验。某些 Word 和 Excel 文档我会存在 OneDrive 中，但是主要目的是备份比较重要的文件。而另一方面，OneDrive 也不好直接利用网页访问，因此 Office Online 这一杀手级功能实际上处于不可用的状态，这一点让人很难真正爱上 OneDrive。

Google Drive 用来和外国友人沟通的时候使用。这个学期是一门留学生阅读课的助教，我会把材料放在 Google Drive 上，以方便因为疫情滞留在国外的留学生们下载。除此之外，Google Drive 是这几家云服务中唯一支持流化视频的，因此某些教学材料的视频我也会放在 Google Drive 上以便学生查看。这些文件在 iCloud 也可用，因为我需要备份。

Adobe Creative Cloud 里面的文档，我也放在了 iCloud 中。实际上，Adobe 云上的文件在 Mac 上的文件夹就在文稿文件夹中，因此十分方便就已经将所有文档都同步到了 iCloud 中。因此一般来说，我管理 Adobe 套件编辑的文件的方式就和普通文件一样，不会特意去使用 Creative Cloud —— 尽管它似乎也很方便，但是仅仅支持 Adobe 套件的这些文档是不够的，它们并非我的工作流中所要处理的全部，甚至可能不是最重要的文档。这时，iCloud 可以确保所有文档都能够保存为最新版本。

写在最后
----

iCloud for Windows 已经是国内网络环境下在 Windows 中我个人感觉最为纯净、功能也最全的同步盘了。它完全可以满足我想要将 Windows 10 PC 融入个人其他 Apple 设备生态中的大部分要求。但是，总还是有些次元壁难以打破，比如可离线使用的 AirDrop、iCloud 剪贴板、同步我 Mac 和 Windows 电脑上的其他文件夹等等。

然而，仅仅作为文件同步的工具来说，iCloud for Windows 不仅仅能够将 iCloud 云盘上的内容完整、实时呈现在 Windows 10 PC 上，更是能够整合 Windows 10 的一些 API 来提供更好的用户体验。尽管 Microsoft Store 中 iCloud 面临大量一星评价，证明它可能仍然不是最好的 Apple 软件，但是它能够在 Windows 的框架内符合我这样一个长期使用 Apple 设备的用户的使用习惯。

因此，如果你也有一台孤立的 Windows 10 电脑和许多 Apple 设备，不妨也试试利用 iCloud 云盘来同步自己的文件、创建适合自己的工作流。

> 下载少数派  [客户端](https://sspai.com/page/client) 、关注  [少数派公众号](https://sspai.com/s/J71e) ，了解更妙的数字生活

> 想申请成为少数派作者？[冲！](https://sspai.com/apply/writing)

* 1Windows 7 和 Windows 8 可以到 Apple 官网下载可执行文件 exe 进行安装。

12589

---

[🌐 原始链接](https://sspai.com/post/61430)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3dcb29b5-e139-49c2-8123-7816b2fd51d6/3dcb29b5-e139-49c2-8123-7816b2fd51d6/)