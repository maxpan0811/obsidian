---
title: "技巧：利用 AppleDNS 项目加速 Apple 服务"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/技巧：利用 AppleDNS 项目加速 Apple 服务.md
tags: [印象笔记]
---

# 技巧：利用 AppleDNS 项目加速 Apple 服务

# 技巧：利用 AppleDNS 项目加速 Apple 服务 --- ![](.evernote-content/618C8018-53A9-4E61-9F4E-85FF2EA97168/296790

---

# 技巧：利用 AppleDNS 项目加速 Apple 服务

---

![](.evernote-content/618C8018-53A9-4E61-9F4E-85FF2EA97168/29679003-58E2-4156-A9B0-BFDFE1F84546.jpg)

[AppleDNS](https://github.com/gongjianhui/AppleDNS) 是 GitHub 上针对 Apple 服务进行加速的一个项目。具体来说，AppleDNS 项目通过收集 Apple 在全中国几乎所有省级行政区的 CDN IP 列表，能够解决以下 Apple 服务在国内部分地区速度缓慢的问题：

* App Store
* Mac App Store
* iTunes Store
* Apple Music
* iBooks Store
* TestFlight

出于隐私、安全以及系统稳定性方面的考虑，项目作者未在加入 iCloud 与 Apple ID 相关的域名。由于 iTunes 大规模启用了 HTTPS 的连接方式，你也大可不必担心作者会通过此项目获取个人敏感信息。

使用方法
----

### 1. 一些准备工作

由于 Apple DNS 项目提供了自动生成配置形式的 Python 脚本文件，运行脚本需要电脑中安装有 Python 软件。

Python 目前有 Python 2 以及 Python 3 两个版本，如果你正在使用 Mac，系统是 OS X 10.8 或者以上版本，系统已经自带了 Python 2.7。你可以在终端中运行下列命令查看当前系统默认的 Python 版本：

`python -V`

当然，如果你想安装并使用 Python 3，你可以前往 [Python 官网](https://www.python.org/downloads/mac-osx/)下载安装包安装。或者，你可以根据[《借助 Homebrew Cask，教你快速下载安装 Mac App 新姿势》](http://sspai.com/32857)一文中的方法搭建 Homebrew 环境，通过 Homebrew 安装 Python 3，命令如下：

`brew install python3`

### 2. 配置文件的配置方法

Apple DNS 支持通过运行项目文件夹内的 Python 脚本自动生成各种形式的配置（Surge、hosts、Merlin），只要将生成的配置加入相应配置文件内并放至对应位置即可生效。

在开始操作前，你需要在[项目首页](https://github.com/gongjianhui/AppleDNS)下载项目文件。这里假设你的项目文件夹存放于桌面，你只要在终端内依次运行下列命令即可完成配置的生成。

**在 Python 3 环境下：**

1. `cd ~/Desktop/AppleDNS-master` - 切换到 Apple DNS 项目文件夹
2. `python3 fetch-timeout.py --payload ChinaUnicom.json`- 多线程测速脚本，最后一项参数为对应运营商，示例代码以中国联通为例，电信 / 移动运营商对应参数为 ChinaNet/CMCC。**测速需要一定的时间，请耐心等待。**
3. `python3 export-configure.py --target hosts` - 示例代码表示生成需要的 hosts 配置，Surge/Merlin 配置对应参数为 Surge/Merlin。
4. 在终端内复制相应配置到对应的配置文件内即可。

**在 Python 2 环境下：**

1. `cd ~/Desktop/AppleDNS-master`
2. `python fetch-timeout-py2.py --payload ChinaUnicom.json`- 最后一项参数为对应运营商，示例代码以中国联通为例，电信 / 移动运营商对应参数为 ChinaNet/CMCC。**测速需要一定的时间，请耐心等待。**
3. `python export-configure.py --target hosts`
4. 在终端内复制相应配置到对应的配置文件内。

如果你是 Apple Music 重度用户，我建议完成上述操作后继续执行以下步骤，并将终端中的结果替换掉之前 `aod.itunes.apple.com`、`streamingaudio.itunes.apple.com`两个域名中的 IP：

* `python3 fetch-timeout.py --payload Music.json`
* `python3 export-configure.py --target surge`

Python 2 使用下面的命令：

* `python fetch-timeout.py --payload Music.json`
* `python export-configure.py --target surge`

### 3. 放置配置文件

这里以 hosts 的配置方式为例，介绍一下配置文件的使用方法：

* 输入以下命令并执行，根据提示输入密码：

  `sudo vi /etc/hosts`
* 粘贴刚才生成好的 hosts 配置
* 按下「ESC」按键并输入 `:wq` 然后回车，即可保存 hosts 的配置。

P.s.建议完成设置之后，清理一下 DNS 缓存，具体方法为：

* `sudo killall -HUP mDNSResponder` OS X 操作系统
* `ipconfig /flushdns` Windows 操作系统

### 4. ONE MORE THING

相信你也注意到了，AppleDNS 能够用于网络调试工具 Surge，Surge 用户可在配置文件 `[Rule]` 模块前新建 `[Host]` 模块，将生成的配置放入 `[Host]` 之后、`[Rule]` 模块之前即可。

如果你对于上述方法存在疑问，你也可以下载这份[示例文件](http://pan.baidu.com/s/1kVq3ID5)进行研究。

文章来源 [少数派](http://sspai.com) ，原作者 [waychane](http://sspai.com/author/703114) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33481)

[📎 在印象笔记中打开](evernote:///view/207087/s1/47f77c34-fad8-4537-a61d-c8d440a48346/47f77c34-fad8-4537-a61d-c8d440a48346/)