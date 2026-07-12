# 通过终端命令改变 Launchpad 中应用图标的大小丨一日一技 · Mac

---

![](.evernote-content/69DDEA0F-5669-433E-A344-6690622FC724/03F1C004-FF96-45AF-8FCD-9534BE51018B.jpg)

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

Launchpad 是 OSX 上用来查找和打开 App 的快捷启动界面。在调整系统分辨率后，Launchpad 中应用的图标会因为变得太大或太小而影响美观，如果你希望调整一下里面的图标大小，让显示效果看起来舒服一点，可以通过终端命令来执行。

操作方法
----

首先，你可以在 LaunchPad 或应用程序文件夹内打开终端，或者直接在 Spotlight 中搜索「终端」。

![](.evernote-content/69DDEA0F-5669-433E-A344-6690622FC724/3D66F2E3-D1D0-4ADB-B7F1-F94DA697A6AE.jpg)

![](.evernote-content/69DDEA0F-5669-433E-A344-6690622FC724/1E0188FB-F6D1-4FE3-8CD2-4D4556FF662B.jpg)

找到并打开终端后，按照下面的格式输入指令，把其中的「列数」和「行数」替换成你想要的数字：

1. 设置 Launchpad 的列数，对应于每一行 App 的个数

`defaults write com.apple.dock springboard-columns -int 列数`

2. 设置 Launchpad 的行数，对应于每一列 App 的个数

`defaults write com.apple.dock springboard-rows -int 行数`

3. 重置 Launchpad

`defaults write com.apple.dock ResetLaunchPad -bool TRUE`

4. 重置 Dock

`killall Dock`

你也可以将所有指令放到一句话中，每一个分句用「;」分隔，我们来看看将 Launchpad 从 7 x 5 布局调整为 9 x 7 布局的效果，在 terminal 中输入指令并按下回车：

`defaults write com.apple.dock springboard-columns -int 9;defaults write com.apple.dock springboard-rows -int 7;defaults write com.apple.dock ResetLaunchPad -bool TRUE;killall Dock`

调整前：

![](.evernote-content/69DDEA0F-5669-433E-A344-6690622FC724/D0598AFA-71C2-4F9F-A4E9-C95EAF8F8A84.jpg)

调整后：

![](.evernote-content/69DDEA0F-5669-433E-A344-6690622FC724/9A8302D0-E65C-4CC4-8DCB-120A407A7003.jpg)

可以看到，应用图标变小了，Launchpad 也不像调整前那么拥挤了。需要注意的是，由于重置了 Launchpad，之前在 Launchpad 中创建的文件夹会丢失，所有应用都会恢复到独立的状态。

好了，以上就是调整 Launchpad 布局的方法，如果你有任何疑问，或是有其他更好的方法，欢迎在下面的评论区与我们交流。

想要获得更多简单实用的小技巧？*[查看往期「一日一技」>](http://sspai.com/tag/%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)*

文章来源 [少数派](http://sspai.com) ，原作者 [luiyezheng](http://sspai.com/author/713414) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33299)

[📎 在印象笔记中打开](evernote:///view/207087/s1/756a9b1f-a99c-498f-8f65-2616e2507b69/756a9b1f-a99c-498f-8f65-2616e2507b69/)