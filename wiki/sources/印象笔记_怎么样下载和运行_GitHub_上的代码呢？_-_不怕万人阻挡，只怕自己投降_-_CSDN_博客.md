---
title: "怎么样下载和运行 GitHub 上的代码呢？ - 不怕万人阻挡，只怕自己投降 - CSDN 博客"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/怎么样下载和运行 GitHub 上的代码呢？ - 不怕万人阻挡，只怕自己投降 - CSDN 博客.md
tags: [印象笔记]
---

# 怎么样下载和运行 GitHub 上的代码呢？ - 不怕万人阻挡，只怕自己投降 - CSDN 博客

# 怎么样下载和运行 GitHub 上的代码呢？ - 不怕万人阻挡，只怕自己投降 - CSDN 博客 --- 怎么样下载和运行 GitHub 上的代码呢？ ======================

---

# 怎么样下载和运行 GitHub 上的代码呢？ - 不怕万人阻挡，只怕自己投降 - CSDN 博客

---

怎么样下载和运行 GitHub 上的代码呢？
======================

2018 年 06 月 16 日 19:27:35 
[寻找伯乐](https://me.csdn.net/qq_37606901)
阅读数 82197

从昨天开始就想着从 GitHub 上下载一个开源的 Vue 的实战项目，希望能从中学习更多的 Vue 的实用内容，结果搞了半天好不容易下载了，不知道怎么弄。然而，今天终于成功了，激动地我赶紧来记录一下。

如何从 GitHub 上下载自己需要的项目：

1. 首先，你要有一个自己的 GitHub（https://github.com/）的账号。关于如何注册 GitHub 的账号以及如何获取你的 SSH 密钥这个问题，请大家参考 https://blog.csdn.net/p10010/article/details/51336332。当然，最好是自己去网上搜索一下。

2. 你需要安装 Git。关于这个问题，我想，廖老师的 https://www.liaoxuefeng.com/ 里面的 Git 教程，讲的就再详细不过了，这里我就不再赘述了。

3. 下载你所需要的项目：

    3.1. 登录你的 GitHub 账号：

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/C7AA83A9-A9D2-435D-89C8-DBE3FC1C6149)

    3.2. 通过关键字，搜索你需要的项目

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/C6EDAA00-2C2A-45D9-854E-866A357F4507)

   3.3. 下载项目：

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/86075BDD-1194-4858-BBE6-8DD247B35246)

  这里可以看到 clone or download，如果你安装了 GitHub 的客户端的话，那么你直接点左下角的 Open in Desktop, 就可以在你本地的客户端直接打开。如果你想直接下载的话，那么就点击右下角的 Download Zip，可以直接下载项目的压缩包到你的电脑上。这两种方式基本上属于一看就能明白的，我这里也就提一嘴。

值得注意的是，如果你这两种方式都不想用，而是想要通过 git clone ... 的方式下载项目的话。那么请注意看接下来的操作。

3.3.1. 通过 HTTP 的方式克隆项目：

    如果你的账号没有添加 SSH 密钥，那么你可以用 HTTP 的方式克隆项目。

   3.3.1.1. 点击红色框圈住的位置，复制项目地址

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/69D3E4A4-2199-4998-B4D1-F108DE9ABE25)

   3.3.1.2. 打开你想要存储的该项目的位置（如 E:\Project），鼠标右键，点击 Git Bash Hear，弹出 Git 命令窗口，输入

   git clone 你复制的项目地址，如下所示，然后回车

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/C6938D2D-F618-460F-8151-7E7B4E428ED8)

当弹出如下所示的时候，表示你已经下载成功了。

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/F2A7B952-853A-4817-8822-471EBC92FD5C)

这个时候，你再进入你保存文件的位置，就会发现已经有一个文件夹了。

3.3.2. 通过 SSH 的方式下载项目。

如果你是登录的状态，并且已经添加过 SSH 密钥，那么你在点击 Clone orDownload 的时候，就会出现：

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/A65558AC-BCD4-4BFB-83AF-1EB9BF39F7FD)

那么就如同上面通过 HTTP 的方式下载项目一样，复制 ssh 的克隆地址。然后在 Git Bash 的命令窗口输入 git clone 你复制的地址，回车，然后直到出现下一个 $ 的时候，表示下载成功。

![](.evernote-content/0266AAC2-7B63-48AF-8A9C-3F50ADB2B069/7519B929-42CE-4B2C-BA51-37AE3CC524F9)

4. 如何运行你下载的项目。

    一般在你下载的项目文件里会有 README.md 文件，里面会提供你启动项目的方法，但需要注意的是：

    如果你没有安装 node.js 和 npm 的话，建议你先安装这个，这里我就不具体讲怎么安装了

    下载下来的项目，需要进入这个项目文件夹，然后右键 ->Git Bash Here，安装依赖环境 :npm install   // 安装完成之后，会在你的项目文件夹里看到 node\_modules 文件，然后按照 README.md 的提示启动就好啦～

以上内容，如有问题，欢迎指教！

---

[🌐 原始链接](https://blog.csdn.net/qq_37606901/article/details/80714732)

[📎 在印象笔记中打开](evernote:///view/207087/s1/90156fc1-055a-4af3-8aa7-1a4d67bdb33e/90156fc1-055a-4af3-8aa7-1a4d67bdb33e/)