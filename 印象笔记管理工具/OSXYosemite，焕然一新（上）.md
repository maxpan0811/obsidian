# OSXYosemite，焕然一新（上）

---

![](.evernote-content/43880EED-56B8-4924-BBB5-473C0C4DC965/B01F20A6-D04F-4739-9FD6-87A75F04AA71.jpg)

9月20号，在一个月黑风高的夜晚，我在两个倒霉蛋的忽悠下，把 OS X Mavericks 升级到了 OS X Yosemite，当时的版本是 DP8。升级中和升级后，都发生了很多有趣的事情，在那段特殊的时期，我常常徘徊在杀人与忍住不杀间无法自拔，如果不是因为相距甚远，简直难以想象会发生什么事情……

在恢复了理智之后，我很快就把 Yosemite 收拾的服服贴贴了。山高路远坑深，大军纵横驰奔；谁敢横刀立马，惟我卖桃君。当然，那两个家伙也没得到什么好处，其中一个在 iPhone 6到手的第二天就把屏幕摔了个稀烂，另一个家伙买来的 Plus 还没焐热就被大领导据为已有了……出来混，总是要还的！

目前 OS X Yosemite（10.10）的最新版本是 GM Candidate 3.0，GM 即 Golden Master，最后的 GM 版本基本上就是正式版。如果预想的不错，苹果应该会在北京时间10月17日的产品发布会上正式发布 OS X 10.10，那么关于「Yosemite」的系列文章，也就可以开场了，正如苹果发布会的主题「It’s been way too long」，久违了，各位读者。

#### Yomesite 的命名

在上一个版本 Mavericks 之前，OS X 一直采用大型猫科动物命名，比如雪豹、山狮等等。从10.9开始，苹果采用旅游胜地为 OS X 命名，比如冲浪胜地 Mavericks，这次的 Yomesite 则取自「优胜美地国家公园」，这是一个原生态的公园，以壮观的花岗岩悬崖、瀑布、清澈的溪流、巨杉和丰富的生物多样性闻名于世。我的一位朋友刚刚从优胜美地骑行归来，转了一些照片给我，果然美得让人心醉。

![](.evernote-content/43880EED-56B8-4924-BBB5-473C0C4DC965/172D4CF7-E786-4D24-8171-5326930BD481.jpg)

![](.evernote-content/43880EED-56B8-4924-BBB5-473C0C4DC965/03FA64BC-C14C-4874-B0DC-DD642B76B597.jpg)

#### 安装

如果你是苹果的 iOS 开发者，进入开发者中心网站，找到OS X Yosemite GM Candidate 3下载项，点击「Get Free Download」，系统会自动生成Redeem Code（兑换码），并激活 App Store程序并弹出对话框，你输入自己的开发者账户和密码，就可以通过 App Store 下载了。如果是 OS X 开发者，可以直接下载。

如果你不是苹果的开发者，只是普通用户，那么可以申请加入「OS X Yosemite Beta 计划」获得兑换码下载，因为正式版推送在即，我就不在这里多费口舌了。

老生常谈，安装之前一定要用 Time Machine 进行系统备份，保证你可以随时恢复到现在的系统状态。不要有侥幸心理，一旦升级过程出现问题，您就是哭倒长城，那些数据也回不来了。现在的 Mac 硬盘都很大，全盘备份可能有几百 G，速度慢也没那必要，我建议只备份系统文件，数据文件可以直接拷贝到移动硬盘上，我的备份设置如下：

![](.evernote-content/43880EED-56B8-4924-BBB5-473C0C4DC965/96698BD5-F246-42A0-9F7B-0D81E9809FEF.jpg)

每一代 OS X 都是升级安装，向下兼容。那什么是升级安装呢，可以引用我之前写的一段文字来解释一下：

> 有一天你很累，早早就睡下了，这时候一个装修队趁着夜色的掩护偷偷进入你的豪宅进行了一次升级装修。等早晨的闹钟轻轻敲醒沉睡的心灵，你慢慢张开自己的眼睛，发现一切似乎都不一样了，但所有的东西都在，家具和电器换了新的，但衣物、摆设、位置都没变，甚至你上次打开的电视频道都保留下来了，总之系统已经不是那个系统，但你的个人设置（Profile）都保存下来了。OS X系统的每次升级都是如此，安装完成后几乎所有软件都不需要重新安装，甚至你打开文件的进度、Safari 的 Tab 页都会被作为状态保存下来。

有读者问我升级了 Yosemite 之后原来装的程序还在吗？大部分都在，甚至连状态都保存下来了，哪些不在了呢？大部分是服务程序或程序框架，这一部分我们会在下一节介绍。

我自己安装的过程中发生了一点小插曲。安装之前我问前文中提到的两个倒霉蛋安装过程需要多长时间，一个说二十多分钟，一个说半个多小时，于是我就信了。开始时一切都是顺利的，美好的，充满了感激之情的，直到系统安装进度条指到了最后，苹果告诉我，兄弟，恭喜你，只剩「大约」一分钟了。我立刻变得跃跃欲试，终于可以见到活的「Yosemite」的 UI 了，于是我去上了个厕所，回来一看，「还剩大约一分钟」，转了一圈又泡了杯茶，耐着性子读书，喝茶，两杯茶喝完了，「还剩大约一分钟」……

「大约一分钟」最终持续了四十多分钟，期间我屡次按捺住自己关机重启并恢复系统的冲动，等待换来的结果是，Yosemite 安装成功了。其实我什么也没做，只是等待。有时候生活中处于「卡壳」状态的时候，再等等就好。

最终，我的安装用时应该接近一个半小时，而不是那两个家伙的二十分钟或半个小时。为此我问了度娘和谷歌，度娘什么也没说，默默的走开了。谷歌告诉我，苹果重新定义了一分钟。不得已我又翻了一些资料，最终的原因可能是由于我是用类似 Homebrew 这样的安装包安装了大量的服务器端程序和框架导致的。

为什么那两个家伙没事？因为他们一个是项目经理，一个是纯粹的 iOS 开发者，根本不碰服务器端的程序嘛。

#### 技术人员之殇

> 这一节主要面向服务器端的开发者，如果你是普通用户、项目经理或纯粹的 iOS 开发者，可以直接看下一节。

系统升级完成之后，如果你是个开发者，你会发现：Homebrew 不能用了因为 Ruby 的版本变成2.0了，Vim7.3-66 也不能用了因为 Perl 的版本也变了，原来用 iCloud 的第三方程序里的数据消失不见了，Java 再次被干掉了，Docker 也起不来了，CocoaPods 也罢工了，连视频播放器 MPlayer 也开始崩溃了。

「妈妈我该怎么办呀」，你发出了撕心裂肺的喊声，抹抹泪准备恢复到老版本 Mavericks……停！泡杯茶平复一下万念俱灰的心情，然后继续读 MacTalk。

1、首先处理 Homebrew 问题

执行如下命令：

cd `brew --prefix`

mv Cellar /tmp

brew prune

rm -r `git ls-files`

rm -r Library/Homebrew Library/Aliases Library/Formula Library/Contributions

rm -rf .git

rm -rf ~/Library/Caches/Homebrew

然后重新安装 Homebrew：

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew update

把备份的程序复制回来，更新所有程序：

mv /tmp/Cellar .

brew update

brew upgrade

打完这一套组合拳，你之前安装的大部分程序和库就可以恢复生机，重新进入你的编程序列。万能视频播放器 MPlayer 也可以播放你心爱的影片了。

2、Vim 和 YouCompleteMe

之前写过很多 Vim 相关的文章，这说明了我是 Vim 的重度使用者。Yomesite 的升级导致 Vim 和 YouCompleteMe 插件都出了问题。因为使用 YouCompleteMe 插件需要 Vim 的版本在 7.3.584 以上，所以我们需要重新安装 macvim：

brew install macvim ##最新版本是7.4-73\_1

然后在.zshrc 里重新设置别名：

alias vim='/usr/local/Cellar/macvim/7.4-73\_1/MacVim.app/Contents/MacOS/Vim'

更新插件 YouCompleteMe：

cd ~/.vim/bundle/YouCompleteMe

git pull

git submodule update --init --recursive

./install.sh --clang-completer

这些命令执行完，你就会发现 Vim 比你使用的上一个版本还要好用那么一点点。

3、Java 再次被干掉

Java 没了，所有 Java 相关的开发工具和中间件都不能用了，不过不用担心，这个问题最容易解决。

在命令行执行：

java -version

系统会弹出如下窗口：

![](.evernote-content/43880EED-56B8-4924-BBB5-473C0C4DC965/350FD27E-92E9-46D2-B71D-8F89BAC3B69E.png)

点击「更多信息」，或直接到以下网址下载：

http://support.apple.com/kb/DL1572?viewlocale=en\_US&locale=en\_US

下载的介质是「JavaForOSX2014-001.dmg 」，打开后点击「JavaForOSX.pkg」即可安装 Java 的SDK，版本是「1.6.0\_65」。如果你想安装更新的版本，去找 Oracle 就可以了。

做完这一步，你的 Eclipse、IDEA、PyCharm 等 IDE 和 Java 中间件就可以正常运行了。

还有 Docker 和 CocoaPods 没写呢就这么多了，待续吧。

后续章节：UI 的变革、炫彩功能、融合 - iOS 和 OS X等。

---

如果你觉得这篇文章对你有价值，请为我增加一个读者，点赞。

点击「阅读原文」，查看拉勾网为 MacTalk 定制的招聘职位。

阅读原文

阅读

举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=201068562&idx=1&sn=2ce214ddc5f403c621fa5a78f65fb27d#rd)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&amp;mid=201068562&amp;idx=1&amp;sn=2ce214ddc5f403c621fa5a78f65fb27d#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/336d5621-b5c6-4214-bc88-1714d4da88c5/336d5621-b5c6-4214-bc88-1714d4da88c5/)