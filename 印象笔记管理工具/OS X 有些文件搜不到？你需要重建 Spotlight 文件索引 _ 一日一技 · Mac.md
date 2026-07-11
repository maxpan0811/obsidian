# OS X 有些文件搜不到？你需要重建 Spotlight 文件索引 | 一日一技 · Mac

---

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

需求
--

作为一名 [Alfred](http://sspai.com/tag/Alfred) 用户，我最近发现利用 `find + 关键字`或 `Space 空格键 + 关键字` 只能够检索到部分文件。通常 OS X 系统的 [Spotlight](http://sspai.com/tag/Spotlight) 文件检索也存在同样的问题，而且这并非个例。

怎么会这样？如何解决文件索引问题？

方法
--

考虑到 Alfred 的文件检索所利用的是和 Spotligt 相同的 OS X 元数据索引（metadata index），所以为了让其恢复正常，我们需要重建文件夹或卷宗的索引。

根据 Apple 支持页面的 [Spotlight：如何重建文件夹或卷宗的索引](https://support.apple.com/zh-cn/HT201716) 词条描述，步骤如下：

1. 从 Apple () 菜单中，选取系统偏好设置。
2. 点按「 Spotlight 」。
3. 点按「隐私」标签。
4. 将一个文件夹或整个宗卷（硬盘驱动器）拖移至列表。
5. 如果系统提示确认，请点按「好」。
6. 点按刚添加至列表的项目或宗卷，然后点按减号「 - 」按钮来将其删除。
7. 关闭 Spotlight 偏好设置。

随后，系统将如「最终效果」截图页面所示，重建索引。索引完成后，Alfred 和 Spotlight 的文件检索功将恢复正常。

Bonus：让部分文件不被 Spotlight 搜到
--------------------------

Spotlight 的文件检索很厉害，但为了避免他人利用你的个人电脑检索到隐私文件，你可以通过下面两种方式让其不出现在检索结果中：

1. 在系统偏好设置的「Spotlight」面板中，你可以取消勾选部分「搜索结果」类型，比如「PDF 文档」「书签与历史记录」等；也可以在「隐私」中添加「防止 Spotlight 搜索这些位置」的文件夹或磁盘。

   ![](.evernote-content/17EA91C0-2E7A-41DD-827D-EB64C40CEDD6/2F2CD172-F870-4DC5-BBE3-B9856F8E6E8F.jpg)

   ![](.evernote-content/17EA91C0-2E7A-41DD-827D-EB64C40CEDD6/CF6A3DFB-9444-4F63-8810-B33BF004E6B5.jpg)
2. 但上述方式的缺点是，别人可以直接在上述面板中删去不被检索的文件夹。这时，你可以通过给文件夹添加后缀「.noindex 」的方式达到同样的效果（**注意：添加此后缀后，你仍然可以正常查看文件夹中的内容**）。这样一来，除非有人手动查看 Finder 中的文件夹，不然是无法获知到「.noindex」文件夹中的内容的。

   ![](.evernote-content/17EA91C0-2E7A-41DD-827D-EB64C40CEDD6/E27CF1E5-CB64-41F1-8ECF-E8B2CFAE4505.jpg)

最终效果
----

![](.evernote-content/17EA91C0-2E7A-41DD-827D-EB64C40CEDD6/959CC7CE-9C55-4775-8CBF-CF073614E2FD.jpg)

参考链接：

* [Can Alfred work without Spotlight enabled?](https://www.alfredapp.com/help/troubleshooting/indexing/spotlight/)
* [Spotlight：如何重建文件夹或宗卷的索引及更多](https://support.apple.com/zh-cn/HT201716)

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/17EA91C0-2E7A-41DD-827D-EB64C40CEDD6/16720E71-EDDB-457D-B8F4-9AC8463ECC1F.jpg)](http://matrix.sspai.com/p/c4780540)

---

[🌐 原始链接](http://sspai.com/33089)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1bb19d47-a9fe-49b7-80af-8d386d67d649/1bb19d47-a9fe-49b7-80af-8d386d67d649/)