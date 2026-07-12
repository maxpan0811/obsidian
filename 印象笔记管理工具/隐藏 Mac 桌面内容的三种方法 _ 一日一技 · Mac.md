# 隐藏 Mac 桌面内容的三种方法 | 一日一技 · Mac

---

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/562273BF-1186-4117-B47B-21CD25562D3E.gif)

通过隐藏桌面内容，一方面可以让我们在工作时保持一个整洁而漂亮的桌面，「眼不见，心不烦」，减少不必要的干扰；另一方面也能够避免在截取 / 录制屏幕，或向他人展示内容时个人隐私信息的暴露，避免一些不必要的麻烦。

虽然我们并不总是有此需求，但知道几种方法，以备「不时之需」也总好的 :-D

方法一：利用终端命令
----------

在「终端」中输入如下命令，回车确认，即可隐藏所有桌面内容（包括文件、文件夹以及设备图标等）：

```
defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder
```

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/5556598B-1481-4FF0-B750-ADBF750E286E.jpg)

如果希望恢复桌面内容显示，只需再次执行如下命令即可：

```
defaults write com.apple.finder CreateDesktop -bool true; killall Finder
```

方法二：使用 Alfred Workflow
----------------------

如果你使用 Alfred with PowerPack 的话，则可以通过 [Hide Desktop](http://www.packal.org/workflow/hide-desktop) 这个 Workflow 来隐藏（或恢复）桌面内容的显示。

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/219C71A0-978E-4E02-987E-99DFF846EED8.jpg)

默认情况下，键入关键词「dhide」即可隐藏桌面内容；键入「dunhide」即可恢复桌面内容的显示，十分方便。当然，你也可以在 Alfred 中自行更改相应的关键词。

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/2DE36F6F-F8F8-4030-8565-F6D86B3CB78F.jpg)

方法三：使用 HiddenMe Free
--------------------

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/8BD4A845-AEB5-4ECC-A25D-0821B7F62078.jpg)

[HiddenMe Free](http://sspai.com/tag/HiddenMe%20Free)

Mac/

* 下载
* [Mac](http://sspai.com/dl/a10291?url=0 "<img src=\"http://sspai.com/qrimage?size=128&url=http://sspai.com/dl/a10291?url=0\" width=\"128\" height=\"128\" /><p class=\"qr\">扫码下载</p>")

[相关文章](http://sspai.com/tag/HiddenMe%20Free)

比起容易出错的命令行和有着不低使用成本的 Alfred Workflow 来说，免费的 HiddenMe Free 实现起来要更为方便。一般来说，HiddenMe Free 就可以满足大多数人的需求，如果你需要在多块屏幕上隐藏桌面内容的话，则可以考虑购买 HiddenMe Pro（￥18）。

安装完成后，即可在 Menu Bar 中看到 HiddenMe 的小圆点图标。点击「Hide Desktop Icons」，即可隐藏桌面内容；再次点击「Show Desktop Icons」即可恢复桌面内容的显示，一键操作，十分方便。

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/6E9FF020-914E-4D6D-BC69-AA9AC0A70D35.jpg)

除此之外，你还可以为其设定一个全局热键，进一步提高操作效率。

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/298DBE9F-F4C8-4B63-845B-1E8A8A22EA67.jpg)

其它
--

如果你只是希望隐藏设备图标在桌面的显示的话，只需前往 Finder -「偏好设置」，取消勾选「在桌面上显示这些项目」中的所有项目即可 —— 硬盘（即内置磁盘）、外置磁盘（如移动硬盘等）、CD、DVD 和 iPod 及已连接的服务器。

![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/DDBFE4B1-DB8D-43FA-81C8-6F66954B8919.jpg)

**参考链接：**

* [OS X Daily: Hide All Desktop Icons in Mac OS X](http://osxdaily.com/2009/09/23/hide-all-desktop-icons-in-mac-os-x/)
* [Pinapps：六款提升操作效率的 Alfred Workflow](http://zhuanlan.zhihu.com/p/20600933?refer=pinapps)

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/73FB9C94-8A61-4E75-983D-21CE903226AB/88B1E076-90AF-45E1-8BE0-0162A0FA3E1B.jpg)](http://sspai.com/33730)

---

[🌐 原始链接](http://sspai.com/33732)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2e1161f1-6821-4150-b28c-a3f949f0542d/2e1161f1-6821-4150-b28c-a3f949f0542d/)