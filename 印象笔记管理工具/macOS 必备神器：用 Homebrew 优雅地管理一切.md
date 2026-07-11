# macOS 必备神器：用 Homebrew 优雅地管理一切

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c5880ac4f2ff83d2145f23e3da69a34...](https://mp.weixin.qq.com/s?chksm=c5880ac4f2ff83d2145f23e3da69a3405123dec335df8f66c63c147598fa1eab84ce37c2b382&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1764575937_1&req_id=1764565686199140&scene=169&mid=2247485095&sn=6a93d5b677ce553ddcee6f291c78e4cd&idx=1&__biz=Mzk4ODE3NTYyOA==&sessionid=1764576349&subscene=200&clicktime=1764577904&enterid=1764577904&flutter_pos=8&biz_enter_id=5&jumppath=20020_1764577683960,1104_1764577771956,20020_1764577806100,1104_1764577870460&jumppathdepth=4&ascene=56&devicetype=iOS26.1&version=18004225&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQCbkW9M93xFld1doNwtIYZBLTAQIE97dBBAEAAAAAAIecMAXMcXAAAAAOpnltbLcz9gKNyK89dVj0lAW75oISMW52O3/PqNXb4ln/JASnjniLiVEBWP01LQsZ+auO5UYPJsrCkis6FULn6wg+tiNwrqU8TzS0ewwaXW/ropAh334WrdJG9Zp+QCJ6pcwU6BUV2wGNImhpTnW0QQfpael/ZL3hdWkDCSC9uSVGZq+DMPLg8QyNzQ9gf/cDWSxs8H3qp00ZIk0+5PrzHNCBpAbXrTreUejiH4ssIByL1dT+NUIA20nb3uU=&pass_ticket=7nHqnw9az0wqxX33t47D80g3BPMKHZsSZTH2KtFGjnthawORhXFQtX95xlsYx1ES&wx_header=3)

macOS 必备神器：用 Homebrew 优雅地管理一切
=============================

Original荒野徒夫荒野徒夫

目录：

* 一、为什么需要 Homebrew？
* 二、安装与基础配置

+ 1. 安装 Command Line Tools (CLT) for Xcode
+ 2. 安装 Homebrew
+ 3. 修改 Homebrew 镜像源（可选）

* 三、常用命令
* 四、Homebrew 的高级技巧

+ 1. 环境迁移
+ 2. 管理后台服务
+ 3. 添加第三方仓库

* 五、相关推荐

> ❝
>
> 对于 macOS 用户来说，Homebrew 就像 apt 之于 Ubuntu、yum 之于 CentOS、yay 之于 Arch。它让你可以**一行命令安装、升级、管理一切软件**--从命令行工具到图形界面应用。如果你厌倦了手动下载 DMG 文件，这篇文章就是为你准备的。

一、为什么需要 Homebrew？
-----------------

macOS 自带的 App Store 并不适合开发者或者命令行用户。很多常用工具（如：wget、htop、curl、git 等）根本无法通过 App Store 安装。

Homebrew 解决了如下问题：

* 统一的软件管理入口；
* 自动解决依赖关系；
* 支持命令行与图形应用安装；
* 完美兼容 Intel 与 Apple Silicon。

一句话：

> ❝
>
> “Homebrew 让 macOS 拥有了 Linux 式的自由。”

二、安装与基础配置
---------

### 1. 安装  CLT for Xcode

```
xcode-select --install
```

安装常用开发工具，例如：git、make、gcc、g++ 等。

### 2. 安装 Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. 修改 Homebrew 镜像源（可选）

#### 建议：

* 中国大陆建议配置清华、USTC、阿里、华为等镜像源；
* 如果你使用 Proxy/VPN，可以保留官方源，避免镜像不同步造成的其他问题；
* 镜像源不影响 Homebrew 的使用逻辑，主要影响的是更新/下载速度。是否更换视你的网络环境而定。

以下为安装完成后替换为阿里源的命令：

```
# 确定 Homebrew 的安装路径  
❯ brew --prefix  
/opt/homebrew  
  
# 查看当前使用的镜像源地址  
❯ cd /opt/homebrew  
❯ git remote -v  
origin https://github.com/Homebrew/brew (fetch)  
origin https://github.com/Homebrew/brew (push)  
  
# 永久替换源为阿里源  
# bash 用户  
echo 'export HOMEBREW_API_DOMAIN="https://mirrors.aliyun.com/homebrew-bottles/api"' >> ~/.bash_profile  
echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.aliyun.com/homebrew/brew.git"' >> ~/.bash_profile  
echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.aliyun.com/homebrew/homebrew-core.git"' >> ~/.bash_profile  
echo 'export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.aliyun.com/homebrew/homebrew-bottles"' >> ~/.bash_profile  
source ~/.bash_profile  
brew update  
  
# zsh 用户  
echo 'export HOMEBREW_API_DOMAIN="https://mirrors.aliyun.com/homebrew-bottles/api"' >> ~/.zshrc  
echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.aliyun.com/homebrew/brew.git"' >> ~/.zshrc  
echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.aliyun.com/homebrew/homebrew-core.git"' >> ~/.zshrc  
echo 'export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.aliyun.com/homebrew/homebrew-bottles"' >> ~/.zshrc  
source ~/.zshrc  
brew update
```

三、常用命令
------

| 功能 | 命令 | 说明 |
| --- | --- | --- |
| 搜索软件 | brew search <pkg\_name> | 查找软件包 |
| 安装软件 | brew install <pkg\_name> | 安装软件包 |
| 升级软件 | brew upgrade -g | 升级所有软件包 |
| 查看已安装 | brew list | 显示当前安装的软件 |
| 卸载软件 | brew uninstall <pkg\_name> | 卸载软件包 |
| 清理旧版本 | brew cleanup | 释放空间 |

四、Homebrew 的高级技巧
----------------

### 1. 环境迁移

💻 我的 macOS 软件安装优先级：

brew > App Store > dmg

这是我长期使用 macOS 包管理的习惯。

* Brew 是我首选：一条命令能装好全部 CLI 和 GUI 应用，brew bundle 更是一站式恢复环境的利器。换机、重装系统时，只需要备份一个 Brewfile，所有工具和软件包都能精准、轻量、干净地还原。不依赖 Time Machine，也不需要“全盘搬家”。
* App Store 排第二：系统级别管理、支持自动更新、沙箱机制更安全，但恢复策略受限。虽然它也能自动更新大多数 App，但迁移时得靠 iCloud 或 App Store 的购买记录一个个点回来。
* DMG 安装包最后才用：无可替代不得不用的情况。

所以从可维护性、可恢复性、版本一致性角度来看，brew 是王道，App Store 可做备选。

```
# 生成 brewfile 迁移文件  
❯ brew bundle dump  
  
# 将 brewfile 同步到新系统或者新电脑执行迁移命令  
❯ brew bundle
```

### 2. 管理后台服务

很多服务（如：MySQL、Redis、HAProxy 等）都可以用 brew 来启动守护进程：

```
❯ brew services start mysql  
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)  
  
❯ brew services list  
Name          Status  User        File  
dnsmasq       none  
frpc          none  
haproxy       none  
mysql         started federicosun ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist  
nginx         none  
node_exporter started federicosun ~/Library/LaunchAgents/homebrew.mxcl.node_exporter.plist  
redis         none  
sing-box      started federicosun ~/Library/LaunchAgents/homebrew.mxcl.sing-box.plist  
unbound       none
```

### 3. 添加第三方仓库

例如：安装非官方包

```
❯ brew tap homebrew/cask-fonts  
❯ brew install --cask font-jetbrains-mono
```

五、相关推荐
------

[用好 option 键，效率翻倍：macOS 系统进阶](https://mp.weixin.qq.com/s?__biz=Mzk4ODE3NTYyOA==&mid=2247483861&idx=1&sn=0896f6fbd342ffcfa220fefa36c449a2&scene=21#wechat_redirect)

[macOS 高效使用指南：那些你可能错过的系统设置](https://mp.weixin.qq.com/s?__biz=Mzk4ODE3NTYyOA==&mid=2247483895&idx=1&sn=1eb692f9da19531ec967f85bfe7f865f&scene=21#wechat_redirect)

[把 Mac 玩出新花样：macOS 打造家庭服务器实战](https://mp.weixin.qq.com/s?__biz=Mzk4ODE3NTYyOA==&mid=2247484763&idx=1&sn=d7be15b836714be0485fc03d508d700a&scene=21#wechat_redirect)

[macOS 环境烧录启动盘：小白用工具，高手用命令](https://mp.weixin.qq.com/s?__biz=Mzk4ODE3NTYyOA==&mid=2247484979&idx=1&sn=8167c03ced7885ee7c0ea22820ba79b4&scene=21#wechat_redirect)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c5880ac4f2ff83d2145f23e3da69a3405123dec335df8f66c63c147598fa1eab84ce37c2b382&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1764575937_1&req_id=1764565686199140&scene=169&mid=2247485095&sn=6a93d5b677ce553ddcee6f291c78e4cd&idx=1&__biz=Mzk4ODE3NTYyOA==&sessionid=1764576349&subscene=200&clicktime=1764577904&enterid=1764577904&flutter_pos=8&biz_enter_id=5&jumppath=20020_1764577683960,1104_1764577771956,20020_1764577806100,1104_1764577870460&jumppathdepth=4&ascene=56&devicetype=iOS26.1&version=18004225&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQCbkW9M93xFld1doNwtIYZBLTAQIE97dBBAEAAAAAAIecMAXMcXAAAAAOpnltbLcz9gKNyK89dVj0lAW75oISMW52O3/PqNXb4ln/JASnjniLiVEBWP01LQsZ+auO5UYPJsrCkis6FULn6wg+tiNwrqU8TzS0ewwaXW/ropAh334WrdJG9Zp+QCJ6pcwU6BUV2wGNImhpTnW0QQfpael/ZL3hdWkDCSC9uSVGZq+DMPLg8QyNzQ9gf/cDWSxs8H3qp00ZIk0+5PrzHNCBpAbXrTreUejiH4ssIByL1dT+NUIA20nb3uU=&pass_ticket=7nHqnw9az0wqxX33t47D80g3BPMKHZsSZTH2KtFGjnthawORhXFQtX95xlsYx1ES&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5d74edcf-f170-4375-8b45-a9253156330d/5d74edcf-f170-4375-8b45-a9253156330d/)