---
title: "Keyboard Maestro 一键切换账户 _ 实用技巧"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Keyboard Maestro 一键切换账户 _ 实用技巧.md
tags: [印象笔记]
---

# Keyboard Maestro 一键切换账户 _ 实用技巧

# Keyboard Maestro 一键切换账户 | 实用技巧 --- Keyboard Maestro 一键切换账户 | 实用技巧 ============================== |

---

# Keyboard Maestro 一键切换账户 | 实用技巧

---

Keyboard Maestro 一键切换账户 | 实用技巧
==============================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

中区 Apple ID 其实存在很多问题，比如应用不全、Apple Music 曲库不全、没有电影 / 电视剧 / 书籍商店等等，因此很多人会选择注册一个其它地区的 Apple ID 作为备用。1 

多个 Apple ID 意味着我们时常会有切换账户的需求，然而传统切换账户的方法却很繁琐：先注销 → 重新点击登录 → 输入邮箱、密码 → 确认登录 → 确认换区 → 完成更新 / 购买等操作后，再重新走一遍流程切回原地区。

像这一套流程，偶尔执行一次尚可接受，但如果操作频繁了，比如 Spotify、Google、Tumblr 等美区应用会周期更新，我的主力账户在中区无法检测到它们的更新，多次切换下来，就会心生厌烦了。

iOS 切换账户
--------

在 iOS 上，我们可以通过 Workflow（[点此下载](https://workflow.is/workflows/7f9379467312453e9f839c17554c57ed)）或者 Launch Center Pro（[点此下载](https://launchcenterpro.com/2gwg25)）来进行换区更新，无需注销原有账户。原理是打开一个不属于本区的应用，那么商店页面就会自动切换至其它地区，从而检测到该区的应用更新，不需要输入账户密码。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/C4A66852-DFFE-4C0D-BE39-288CA1E0C630.gif)

用 Launch Center Pro 进行切换地区

Mac 切换账户
--------

在 Mac 上，roamlog 曾写过一篇[教程](http://readful.com/post/77044128470/%E5%88%A9%E7%94%A8-keyboard-maestro-%E5%88%87%E6%8D%A2-appstore-%E5%B8%90%E6%88%B7)，使用 Keyboard Maestro 来进行一键切换，将中间繁琐的注销登录等重复操作交给机器，能节省掉我们大量的时间。但随着 macOS 系统的升级，一些菜单栏选项的名称和操作顺序都发生了变化，因此这个 Keyboard Maestro 也需要进行一些修订。

Mac App Store 和 iTunes Store 切换账号的动作稍有不同，你可以先下载我做好的 Keyboard Maestro 动作，再接着看后面的动作讲解：

* [App Store 切换账号](https://cdn.sspai.com/App%20Store%20%E5%88%87%E6%8D%A2%E8%B4%A6%E5%8F%B7%20Macros.kmmacros.zip)
* [iTunes Store 切换账号](https://cdn.sspai.com/iTunes%20Store%20%E5%88%87%E6%8D%A2%E8%B4%A6%E5%8F%B7%20Macros.kmmacros.zip)

### 动作详解

这两个动作的使用方式是：

1. 按下快捷键，比如我设置的是 `⌥Option-A`；
2. 从弹出的菜单中选择地区，按下 `1` 或 `2`；  

   ![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/0CF43017-D9F7-43AC-AB32-F5002F34B0FA.png)

   选择地区
3. 等待换区完成就可以了，非常简单。

两个动作都是在 Keyboard Maestro 中建立动作组，只设置对本应用生效，并赋予一个快捷键（图中设置的是 `⌥Option-A`）。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/039D5DE1-6BAB-4F4A-BAE4-6D372209D274.jpg)

动作组

在动作组中创建两个动作（Keyboard Maestro 中叫做 Marcos），一个是切换到中区账号，另一个是切换到美区账号，并设置触发方式为 **Hot Key Trigger**，设置为 `1` 和 `2`。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/8F603392-BD29-4561-9890-CF365B7F36CE.jpg)

创建两个动作

我们再来看一下动作的具体设置：

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/2C663519-0A45-4918-805C-6DC63B49C4AB.jpg)

动作具体设置（点击查看大图）

我们一步一步来看，如下图，这部分的作用是：点击菜单栏中的「商店 - 退出登录」选项，然后等待「登录…」选项出现，再进行点击。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/4565A41F-5EEE-48A8-B341-9145D0A88096.jpg)

接着等待 0.3 秒，因为电脑和网络都需要一点响应时间，如果立即进行下一步操作的话，可能会让流程失败。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/7E586104-AAAB-4ED7-A8F3-34801B617AC1.jpg)

等待 0.3 秒

下一步则是用到了 Keyboard Maestro 的变量（Variable）功能，如果一个变量的名称以「Password、PW」开头或结尾，那么它们的内容将不会被储存在 Keyboard Maestro 中，而是直接访问 iCloud 钥匙串里的数据，并使用 **Insert Text** 粘贴进 App Store 中，避免应用和剪贴板知道你的密码，保护我们的隐私。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/7C5D3764-C3B3-4F61-8D12-3997BB143B87.jpg)

让变量读取 iCloud 钥匙串

我们需要到**钥匙串访问** App 中，创建一个名为「Apple\_ID\_CN」的密码。用户名称和密码则对应你的 Apple ID。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/4A6B74F5-813C-4DEA-9644-B8931329AAC6.png)

在 iCloud 钥匙串中创建密码

后面这部分很好理解，由于登录 App Store 时是先填密码再填邮箱，所以需要按下 `⇧Shift-Tab` 来聚焦到邮箱。最后一步则是等待「好」按钮出现并自动按下。

![](.evernote-content/3D22ED90-5130-4BD6-AB14-63C8AE5775C2/65B1BEC3-8EB9-4E67-8011-6C084869FB70.jpg)

填写邮箱和自动按下「好」

iTunes Store 和 App Store 不同的地方也在这里：App Store 是先输入密码，再输入邮箱；iTunes Store 则是反过来，先输入邮箱，再输入密码。

此外，iTunes 的菜单名称也和 App Store 有一些区别，比如「商店 → 帐户」和「退出登录 → 退出登录…」，前面下载两个动作里，我已经为你提前修改好了，你只需要将里面的邮箱修改成自己的 Apple ID 就行。

1. [通常大家会选择美区和港区，喜欢日语歌曲的人则会选择日区。↩](#)

---

[🌐 原始链接](https://sspai.com/post/43659)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ffded502-cb9a-4282-9307-a65c7d9d70bf/ffded502-cb9a-4282-9307-a65c7d9d70bf/)