# 一日一技 | 如何调整 Safari 新建标签页的位置 - 少数派

---

如何调整 Safari 新建标签页的位置
====================

![](.evernote-content/E955EA06-D730-451C-A4F0-72DE605D4BD7/583A89B9-8731-410C-A2A7-B3B4FB9DAF31)

一日一技 | 如何调整 Safari 新建标签页的位置

不知道你发现没有，Safari 新打开标签页的位置，默认是紧挨着当前标签页后面。意思是说当你的 Safari 已经显示了 ABC 三个标签页时，你在浏览 B 页面点击网页链接新打开了标签页 D，那么它会出现在 B 和 C 之间：ABDC。

![](.evernote-content/E955EA06-D730-451C-A4F0-72DE605D4BD7/056DD514-093B-4853-A110-BA2A230E8CFF.gif)

新打开的标签页会紧挨着当前标签页

新打开的页面紧挨着当前页面，这可能是为了提示用户这两个页面的关联度。不过一旦标签页太多，当你在多个标签页来回跳转时，这样的机制可能并不能帮你快速找到那些新打开的页面。

[TJ Luoma](https://twitter.com/tjluoma/status/1237533889104506880) 提供了一个解决方法，可以让 Safari 新打开的标签页「后开靠后」，即新打开的标签页永远在最后。同样是上面的案例，在 B 页面打开的标签页 D 位于所有标签页的后面：ABCD。

设置方法为：

1. 打开 **系统偏好设置 - 安全性与隐私 - 隐私 - 完全磁盘访问权限**，添加 「终端」应用，使其获得完全磁盘访问权限。
2. 打开终端，输入：

   ```
   defaults write com.apple.Safari IncludeInternalDebugMenu 1
   ```
3. 重启 Safari，可以看到 Safari 的菜单栏出现了「Debug」选项。我们选择 **Tab Ordering - Position of New Tabs - After Last Tab**，并勾选 **Apply Position to Spawned Tabs**。

![](.evernote-content/E955EA06-D730-451C-A4F0-72DE605D4BD7/9C904F12-D5E6-4F79-AF01-CF7EB2C970DF.png)

新出现的「Debug」选项

现在我们通过网页链接打开新的标签页，或者新建新的标签页都会默认位于所有标签页的最后。

![](.evernote-content/E955EA06-D730-451C-A4F0-72DE605D4BD7/53C3B9C1-BEDE-414D-A48A-905EEE8B310F.gif)

新打开的标签页位于最后

设置完成后，我们可以在终端中输入下面这条命令来隐藏 Debug 菜单：

```
defaults write com.apple.Safari IncludeInternalDebugMenu 0
```

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多实用小技巧 ⚙️

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/59551)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b4a1429b-9183-4e00-b42a-2e07dfae4b63/b4a1429b-9183-4e00-b42a-2e07dfae4b63/)