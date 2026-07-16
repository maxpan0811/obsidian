---
title: "这款在线工具也许是新手练习 Python 最好的选择：Google Colab"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/这款在线工具也许是新手练习 Python 最好的选择：Google Colab.md
tags: [印象笔记]
---

# 这款在线工具也许是新手练习 Python 最好的选择：Google Colab

# 这款在线工具也许是新手练习 Python 最好的选择：Google Colab --- [少数派](https://sspai.com/) [![](https://sspai.com/post/

---

# 这款在线工具也许是新手练习 Python 最好的选择：Google Colab

---

[少数派](https://sspai.com/)

[![](https://sspai.com/post/52980)](https://sspai.com/post/52980)

* [正版软件](https://sspai.com/mall)
* [付费栏目](https://sspai.com/series)
* [Matrix](https://sspai.com/matrix)
* [专题广场](https://sspai.com/topics)
* [热门文章](https://sspai.com/tag/%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0#home)
* [应用推荐](https://sspai.com/tag/%E5%BA%94%E7%94%A8%E6%8E%A8%E8%8D%90#home)
* [生活方式](https://sspai.com/tag/%E7%94%9F%E6%B4%BB%E6%96%B9%E5%BC%8F#home)
* [新玩意](https://sspai.com/tag/%E6%96%B0%E7%8E%A9%E6%84%8F#home)

![如何用 Google Colab 练 Python？](https://cdn.sspai.com/2019/02/19/802e19f08c1ce8c575377362893ee0e8.jpg)

如何用 Google Colab 练 Python？
==========================

02月19日

[![玉树芝兰](https://sspai.com/post/52980)](https://sspai.com/user/775063/updates) 

#### [玉树芝兰](https://sspai.com/user/775063/updates)

这个学期，我在北得克萨斯大学（University of North Texas）教「INFO 5731: Computational Methods for Information Systems」课程，主要内容包括： Python 基础、自然语言处理，以及机器学习。

授课的对象是信息科学、数据科学专业的硕士与博士研究生。跟在国内一样，我依然使用翻转教学（flipped instruction）方式。过去的几周，我们把「Python 基础」部分学完了。每周，我都会要求学生在课前阅读两本教材上的指定章节，然后把所有的代码自己重复一遍。在此基础上，对每一段代码，学生都要自己试着进行一些改动。出错也没有关系，尝试解决。

因为绝大部分学生，都是 Python 初学者。因此他们都会遇到以下的实际问题：

* 不知道如何安装和设置运行环境；
* 遇到问题会慌乱，不知如何有效寻找解决方法；
* 对于团队作业，不知该如何有效协作；
* 不懂得如何进行版本控制，代码越改越乱。

这些问题，也构成了学生的痛点。如果不能有效加以解决，学生会把每周宝贵的学习时间，浪费到许多琐碎的无用功上。更可能的情况，是他们的信心会被打击，导致丧失学习的**动力和兴趣**。

因此，我为他们找到了一款合适的 Python 练习工具。这里，我把这款工具也分享给你。

这款工具，就是 Google Colab 。我曾经在《[如何免费云端运行Python深度学习框架？](https://www.jianshu.com/p/eebf9a13c52a)》一文中为你介绍过它，在《[如何用 Python 和循环神经网络做中文文本分类？](https://www.jianshu.com/p/caee648f6a1f)》和《[如何用 Python 和循环神经网络预测严重交通拥堵？](https://www.jianshu.com/p/7af712ee173a)》里，我也曾用它给你做过代码的展示。

下面，我给你们介绍一下如何用 Google Colab 应对上述的 4 个痛点，为你的 Python 练习提供辅助。

环境
--

新手最常见的问题，就是好不容易累积了学习的兴趣，上手不久便遇到报错。而 Python 新手遇到的许多错误，实际上都和环境的配置有关。例如说，Anaconda 套件下载环节，你就不知道该选择哪个版本。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/80C083A3-B4EB-4164-9DED-FC42C83EE23F.jpg)

好不容易安装好了，因为路径设置问题，连 Jupyter Notebook 都呼叫不出来。终于能输入代码了。结果一输入就提示，你要调用的模块名称，没听说过！

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/F362B78C-5E35-4C55-A963-9798F24A73E7.png)

而这些，Google Colab 都帮你处理好了。只需要打开一个浏览器（推荐 Google Chrome 或者 Firefox），输入：`https://colab.research.google.com` 就可以看到以下页面。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/E5602236-28CA-43D5-8067-BEE47EF810AD.png)

选择新建 Python 3 笔记本，然后就能看到**完全配置好**的 Python 运行环境了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/639C7145-152D-48D0-9D37-378A9500CE7D.png)

对，就是这么简单。你可别小瞧这个运行环境，虽然你没有执行任何安装过程，但是它基本上涵盖了你做数据科学分析，要用到的各种工具，这些工具包括但不限于 Numpy、Scipy、Pandas 等，甚至连深度学习的框架，例如 Tensorflow、Keras 和 Pytorch，也是一应俱全。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/0FD760B7-8E90-40D5-A04D-60D68CFFBE74.png)

Google Colab 的深度学习环境支持，可不只是软件那么简单。Google 慷慨的提供了 GPU， 甚至是更专业化的 TPU， 供你**免费**使用。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/4027D05C-AD06-4D87-BF05-9A1C9220577C.jpg)

默认状态，这些云端硬件是**不开启**的。你需要在菜单栏中选择 runtime，然后选择 Change runtime type，就可以看到不同硬件支持的选项了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/5DAAF197-B066-447E-B434-86E2E15079BB.png)

有的书籍样例代码，甚至是 Python 组件，都需要 Python 2 环境才能运行，这也没关系。点击新建笔记本，你就能使用不同的 Python 版本了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/C33A581A-CC0B-451B-8A48-F722DA90EF0E.png)

细心的你会发现，在上面的「修改运行时设置」页面里，也可以随时调整 Python 版本。

求助
--

作为新手，你遇到错误和问题，是完全正常的。而 Python 具有强大的社区，可以给你提供很多帮助。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/92C6034F-696D-4515-A072-FFDB0DF4AB2C.jpg)

但如果你尝试过，便可能有一种错觉——这些 Python 高手很不友好。因为你贴了问题，却没人理你。其实，这很可能是你问问题的方式不对。想想看，你笼统地说一个报错信息，可能的原因或许有数十甚至上百种，谁能帮你一一排除？这倒也罢了。可是你明明贴了一段代码，还给出了错误信息的截图啊。为什么还是没有人伸出援手？因为这些信息，可能依然不够。

想想看，你本地安装了什么样的套件？其中的各种模块，都分别是什么版本？你执行当前代码有问题，那上下文是什么？会不会是因为之前某个代码段落，影响了你当前段落的执行？你的操作系统，是否完全支持你正在使用的组件功能……这些可能性，无穷无尽。同样，也没有人这样花时间帮你枚举。

但是有了 Google Colab ，你提问的效果却可以大大提升。因为，你可以用**最简单**的方法，让潜在的回答者复现你的问题。这就是，把你的笔记本**共享**出去。如下图，点击笔记本右上角的 Share 按钮。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/53484882-4939-49D7-B128-14886718739D.png)

在出现的对话框里，注意选择权限。选成**可以浏览**（view），就可以了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/0D0A7671-2B4D-4DD5-A64D-E9B4F49E38FD.png)

然后，选择「复制链接」，链接就到了你的剪切板里面了。把它连同你的文字描述，直接贴到 Python 的论坛或者课程讨论区里。别人只需要点击，就能查看你的全部代码、报错信息。而且，还能**运行**你的笔记副本。注意，虽然你俩可能用的是不同的操作系统、不同的浏览器，但因为都用了 Google Colab ，你们的 Python 环境是**完全一致**的。等到对方解决了问题，他还可以把完整的笔记本再用链接方式分享给你。你的问题于是迎刃而解。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/BBC96B8D-7ABE-4F53-A006-52F1F7230BCA.png)

问问题，只是寻求帮助的一个方面。在提问之前，你还是应该自己尝试一下解决的。毫不愿意思考，直接当**伸手党**，社区里的人很难喜欢跟你打交道。而 Google Colab 为你主动寻找问题答案提供了工具支持。每当你遇到报错的时候，你都会看到下方有个按钮。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/9251AC95-079D-4DA9-9D36-92ED9AD3EE2C.png)

点击这个按钮， Google Colab 就会用搜索引擎，在 Stackoverflow 这个 IT 问答站点上，帮你寻找相关报错的已有答案。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/1E04F345-DCC5-45A0-8597-3E8A27AAD70B.png)

一般来说，点击前几条信息，你就会有收获。例如这次，你就很幸运，因为答案明确说明，这是因为 Python 版本带来的差异。你只需要根据提示，进行代码的轻微调整，就能正常运行了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/A403DE8C-BE77-49AE-9195-72540926C2F1.png)

协作
--

不知你有没有尝试过跟人协作编写代码？我的课上，是有小组作业的。要求学生 2 – 3 人一组，一起用 Python 解决问题。有的人，是这样协作的：自己写一段代码，用邮件传给对方；对方改完，发回来；自己在上面修改添加，再发回去……

这样显然**效率很低**。有没有高效的方法？当然有。依然利用我们刚才已经见到过的共享功能。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/B3D8EA0B-1D30-48AF-B3A6-3F6DFE73D9CE.png)

只是这一次，在选择权限的时候，给对方「可修改」权限。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/DC90ABA9-F449-47B0-9FAE-F59FB6643753.png)

例如还是刚才的 print 命令没有加括号的问题。只不过这次，对方除了能看到你的问题，还可以直接编辑。你的协作者，新建了一个代码块，并且输入了正确的信息。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/2116E63E-25B8-4046-B5B9-1B142C6FF173.png)

在你这里看起来，就是这个样子的。协作者的头像，会显示在对应的修改内容旁边。这样一目了然。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/CAE5C9DE-2A5E-4BCC-83BA-8381B6422C0F.png)

对方还可以在代码块旁，选择添加注释。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/7E62EBD8-7BD5-4362-B376-CB71BF4ABFA8.png)

例如输入以下内容。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/DD28D49D-0848-49DD-9755-042F31DFC2C2.png)

你可以同步在自己的笔记本上，看到对方的注释。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/7924D525-A912-4EDE-9E8B-C39108B6FF95.png)

这样一来，团队协作 Python 练习沟通的效率，自然就高了许多。

注意，为了安全起见，一定只能把该权限，限定在你**信任**的协作者中。

如果是打算把你的成果展示出来，你可以使用 Google Colab 与 Github 的集成功能。如下图，选择保存副本到 Github 。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/3F93B87B-0908-4060-B66F-0B548D38B933.png)

然后，选择你希望保存到的 Github 项目。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/3EE50C40-E80F-4242-8E46-C34E0F42D26D.png)

保存完毕后，对应的 Github 页面会自动打开，供你预览。其中可以包含全部的文字、图片、代码和输出信息。注意笔记本的顶部，有一个「在 Colab 打开」的链接。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/9A0BC21F-67AF-4510-8F0A-C7D717B0B6D9.png)

点击它，你就能迅速开启 Google Colab 环境，并且直接运行这个 Github 上的笔记副本。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/FF226D97-77C1-4BA7-AED2-323FA72B6D2D.png)

版本
--

当你不停地尝试和改动代码的时候，很有可能会把问题改得更加糟糕。这时候，你恨不得有一个时光机，可以让你回到错误少一点的时候。这个时光机，Google Colab 是提供了的。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/F8F955A1-88B0-45E0-8082-AC1F70DF1F45.png)

点击菜单里面的 Revision history 功能，你就能看到当前笔记本已保存的全部历史版本，包括修改时间、谁改的、文件大小等各种信息，一应俱全，想回到哪个版本，点一下「恢复」按钮就可以了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/CBD2547C-8BD1-46BD-A584-E2CE76583FAD.png)

另外，你也可以把 Google Colab 笔记本，直接下载成为 ipynb 文件，在本地保存副本。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/8E1C79FF-F8E9-4443-8EB5-ACF31FFD1C31.png)

一定要注意选择需要的存储路径，避免不知存到哪里去了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/7DA1D548-B0BA-4037-9CB2-E230D43D1F32.png)

我一般让学生交作业的时候，都需要同时提交 Google Colab 链接，以及一个 ipynb 文件。二者的内容，应该是一样的。既然如此，为什么还需要提交两样东西呢？这个问题，作为思考题，留给你。请注意联系本节标题，加以分析。

有了 ipynb 文件，你可以用本地的 Jupyter Notebook 开启。但是如果你只是想查看内容的话，这里给你推荐一个更好的工具，叫做 [nteract](https://nteract.io/) 。它可以帮你直接开启 ipynb 文件，用于查看。这样，你就没必要每次都用 Jupyter Notebook 命令开启后台服务，然后再到浏览器中点开对应的 ipynb 了。

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/EF979E4A-64FB-45A2-A246-0DD4F7530662.png)

小结
--

还记得在《[如何高效学 Python ？](https://www.jianshu.com/p/3678e3dd29f5)》一文中，我给你推荐过的经典教材《笨办法学 Python》吧？

《笨办法学 Python》指出了一条看似笨拙，却非常有效的学习路径。我上课的时候，也一直在跟学生们强调——Python 这样的实践类技能，只能**练中学**（Learn by doing）。

本文给你推荐的 Google Colab ，可以帮你解决 Python 初学者练习实践 Python 编程时，最常遇到的几大痛点。包括：

* 自动配置
* 有效求助
* 协作编程
* 版本控制

这样一来，你可以把宝贵的时间，聚焦在技能的掌握和应用；而不是久病成医，成为「环境配置专家」了。

祝 Python 编程学习愉快！

[应用推荐](https://sspai.com/tag/%E5%BA%94%E7%94%A8%E6%8E%A8%E8%8D%90)[效率工具](https://sspai.com/tag/%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7)[Google](https://sspai.com/tag/Google)

---

0

---

[![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/66FCCF77-B640-4D5A-BE47-F8E450D57FBE.jpg)](https://sspai.com/user/775063)

#### 

#### [玉树芝兰](https://sspai.com/user/775063)

王树义。大学教师，终身学习者。稍微懂一点儿写作、演讲、Pyt...

关注

[![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/A244FA67-D8A5-40BF-9099-444C493D3A78.jpg)](https://sspai.com/column/104)

#### [提升效率之路](https://sspai.com/column/104)

一个优秀的工具，能让你在提升效率之路事半功倍。你是如何通过这些工具，技巧提高生产力，改善自己的效率？

关注

[![](https://sspai.com/post/52980)](https://sspai.com/post/52980)

![](.evernote-content/2AD12AC7-1F1C-4323-B9A2-9553686B140D/F72038C3-7E9B-4DD6-BFF6-DF951D73D398.png)

发送

### 评论（7） 最热 最新

[关注公众号 sspaime](https://sspai.com/post/52980)

* [支持我们](https://sspai.com/page/support)
* [作者招募](https://sspai.com/apply/writing)
* [用户协议](https://sspai.com/post/37739)
* [FAQ](https://sspai.com/post/37793)
* [Contact Us](https://sspai.com/post/52980)

© 2013-2019 [少数派](https://sspai.com/post/52980) | [粤ICP备09128966号-4](http://www.miitbeian.gov.cn/) | CC BY-NC 4.0

App 打开

---

[🌐 原始链接](http://sspai.com/post/52980)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b16bc433-9ac8-4560-8459-469d13ac75bd/b16bc433-9ac8-4560-8459-469d13ac75bd/)