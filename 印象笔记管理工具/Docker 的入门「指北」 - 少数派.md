# Docker 的入门「指北」 - 少数派

---

Docker 的入门「指北」
==============

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

如果你购买过 VPS 云主机，那么或多或少，你都可能听说过 Docker。如果你从未听说过 Docker，那么本文可能能够为你开启新世界。

利用 Docker，你能够非常轻松地部署各类服务，无论是个人云盘（[Nextcloud：打造属于自己的网盘服务 Docker 版 (附带视频](https://sspai.com/post/55217)）、个人的 RSS 服务（[利用 Docker 搭建 Tiny Tiny RSS 服务](https://sspai.com/post/53072)）、HomeKit 桥接（[利用 Docker 搭建 HomeKit 智能家居](https://sspai.com/post/53071)），亦或者搭建一个个人博客（[使用 Docker 部署 Ghost 教程](https://sspai.com/post/36751)），甚至是做一个自己的维基百科、自己的社交软件，都能够轻松地实现。

是的，Docker 就好像是 服务器端的「应用商店」，你能够通过 Docker，轻松的部署各种属于个人、团队的服务。而现如今，无论是利用各个平台的云主机，还是树莓派、群晖、威联通等这类物理的服务器主机，甚至是自己废旧的老电脑，都能够很容易的使用上 Docker。

![](.evernote-content/D5D8360E-F178-4869-BDE6-FF5D2CB8EEF1/8F28BCB1-D207-4707-AF2C-1841A47920DE.png)

在正式开启前，本文默认读者了解基本的命令行操作，以及了解基本的 Linux 相关知识，如果您还不了解这些，可以通过 B 站 这个 UP 主的 [视频](https://www.bilibili.com/video/av56233347) 有所了解。

那么开启 Docker 之旅吧！
----------------

Docker 可以理解为寄存在主机上的特殊的虚拟机。它利用特殊的虚拟化技术，比一般的虚拟化技术能够更加高效合理的利用资源。一台主机上可以创建众多的容器，这些容器通过特定的方式与主机共享硬件资源，并且访问特定的文件，使用特定的端口。通过 Docker ，一台主机能够运行多种不同的服务。

![](.evernote-content/D5D8360E-F178-4869-BDE6-FF5D2CB8EEF1/AFD4086A-5D7C-480A-8FF3-3836DF0A4CDB.png)

### 第一步：安装或者启用 Docker

一般来说，Docker 会运行在 Linux 服务器上，无论是哪种发行版本，你都可以非常容易的在搜索引擎中找到其安装方法。这里我以 Ubuntu 为例：

```
$ sudo apt update # 先更行一下软件包缓存
$ sudo apt install docker-ce # ce 代表社区版
```

接着启动 Docker 服务：

```
$ sudo systemctl enable docker
$ sudo systemctl start docker
```

这样，你就可以尝试一下运行 `docker` 命令了：

```
$ sudo docker run hello-world
```

默认情况下，docker 命令需要使用 root 用户或者在 docker 组下的用户才能使用（docker 命令会使用 Unix socket 与 Docker 引擎通讯）。也就是说，如果不设置，默认情况下，所有的 docker 命令都需要加 sudo。一般情况下，你可以创建一个名为 docker 的用户组，再将当前用户加入到 docker 组中，使得操作更为安全。

```
$ sudo groupadd docker #创建 Docker 组。
$ sudo usermod -aG docker $USER #添加当前用户到 docker 用户组中，也可将 $USER 替换为你想加入到 docker 组中的用户。
```

### 第二步：拉取你的第一个 Image

其实你可以这么理解 Docker，你可以在一个名为 [Docker Hub](https://hub.docker.com/) 的网站中，查找 Docker 镜像（image）。

![](.evernote-content/D5D8360E-F178-4869-BDE6-FF5D2CB8EEF1/94B2CAB1-6284-4379-94F2-4B1501B41882.png)

这个过程就好像是在 App Store 中搜索自己需要下载的应用一样。查找完想要下载的镜像后，在终端中输入：

```
$ docker pull [镜像名称]
```

可以拉取镜像的到本地。是的，你就下载了这个应用，只不过是在服务端。当然，一般来说这个过程会比较缓慢，你可以 [替换国内源](https://yeasy.gitbooks.io/docker_practice/content/install/mirror.html) 加速这一过程。

### 第三步：启动你的服务

与一般应用下载打开不同，Docker 的镜像可以重复的被打开成不同的容器。你可以简单的理解为这是「应用双开」，或者说是「应用多开」。我们使用 `docker run` 命令来启动容器。

这个启动的过程可以是一次性的启动，即直接使用 `docker run` + 一些列参数的方式启动服务，也可以通过 `docker compose` 来编排你的项目。由于 compose 会相对专业，本文就不做过多的介绍了，这里只以 `docker run` 为例作为讲解，以下是常见的参数：

* `-d`：正常情况下，启动一个服务区，我们都会让其在后台运行，所以使用参数 -d 来告诉 Docker，在后台默默奉献即可；
* `--name=`：前面已经提到了，你可以对一个 Docker 镜像进行多开操作，所以通过 `dockr run -d --name=[你的名字]` 的方式，可以指定开启的这个容器的名称，这样在多开的情况下，能够更为方便的进行管理；
* `-p`: 指定端口的映射。

这里简单讲解一下端口的含义：以用户输入在浏览器中输入 `www.sspai.com` 为例，首先浏览器会通过 DNS 服务器把这个 Url 翻译为 IP 地址，再通过 IP 地址，找到少数派的服务器，最后通过端口号确定服务，例如如果你输入的是：`https:\\www.sspai.com`，那么对应的端口就是 443。端口号就相当于服务器的柜台，同个服务区会有多个柜台提供服务。诸如 `http` 服务，默认是 `80` 端口， `https` （上面的例子）默认是 `443` 端口，类似的 `FTP` 服务是 `21` 等等。 并且一个端口只能支持一个服务，就是说一个柜台只支持办理一项服务。

回到 `-p` 这个参数，`-p 8080:80` 就是指将 docker 中开启的端口，映射到主机的 `8080` 端口中。也就是说通过主机的 IP 地址的 `8080` 端口，可以访问到 docker 容器的 `80` 端口服务。 服务器的 `8080` 柜台接收到的服务，会发送到容器的 `80` 柜台中。是的，容器也相当于是一个服务器，在 Docker 内部，他们之间也是有 IP 地址的说法的，所以容器也是需要开「柜台」来管理服务的。

理解这一步非常重要，和一般的使用应用不同，服务器上的应用就是一直在运行，然后让你去访问的，所以 `-p` 参数设置不对，可就找不到柜台办理正确的服务器了。例如运行：

```
$ docker run -d --name=nextcloud_demo -p 8080:80 nextcloud
```

那么你可以通过 `http://localhost:8080` 访问到你的 nextcloud 服务。这里的 `loaclhost` 指的是在 Docker 服务器上访问。如果你想通过自己的电脑，访问 Docker 服务器上的服务，把 `loaclhost` 替换为服务器的 IP 地址即可。

* `-v`：建立主机于 docker 容器内的文件关联。通过 - v 能够 主机的文件映射到 docker 容器中，例如：

```
$ docker run -d\
-v nextcloud:/var/www/html\
nextcloud
```

就是将本地本地文件夹 `nextcloud` 映射到容器中的 `/var/www/html` 目录。

这 4 个参数就是 docker 最基础也是最常用的参数了。了解了这四个参数，再参照 Docker Hub 下每一个镜像的使用说明，你就可以尽情的拥抱和享受开源社区的各种服务了。

推荐一些好用的 Docker 镜像
-----------------

除了开篇提到的 NextCloud、Tiny Tiny RSS、Ghost 等服务外，还有一些镜像值得尝试：

* [MediaWiki](https://hub.docker.com/_/mediawiki)： 和维基百科一样的属于个人或者团队的维基服务。
* [Wekan](https://hub.docker.com/r/wekanteam/wekan)：属于个人或者团队的开源看板应用。参考 Trello 等服务。
* [WordPress](https://hub.docker.com/_/wordpress)：为人所知的、被广泛使用的、收购了 tumblr 的博客服务，可以用来搭建个人博客，甚至商用网站。
* gitlab、gitea 等 Git 服务：如果有团队代码管理需求，可以使用 Docker 快速部署一个私用的 Git 服务。

部署一时爽，运维「火葬厂」
-------------

Docker 让服务的安装变得异常容易，但是选择一项服务后，后面的运维才是真正折腾人的地方。

首先是管理容器中，最常使用到：

```
$ docker ps #查看运行中的容器。
$ docker ps -a #查看所有容器，包括停止的。
$ docker images #查看安裝的镜像
```

然后是停止、启动已有的容器：

```
$ docker stop <容器名称 / ID> # 正常停止容器
$ docker start <容器名称 / ID> # 启动已有容器
$ docker kill <容器名称 / ID> # 强制停止容器
```

一般容器运行后，会有一个 ID，用以区分容器，这个 ID 一般都是乱序的，所以之前的 `--name` 参数，能够使你更加方便对容器进行管理。

除此之外，还有就是进入 Docker 容器中，修改一些配置文件：

```
$ sudo docker exec -it <容器名称 / ID> /bin/bash
```

就是说你可以通过这个命令，进入到 容器的 `bash` 中，对容器内进行一些修改。

尾巴
--

最后 Docker 还有许多其他的命令和方法可供学习。本文只是作为入门，希望为各位读者提供帮助，更加轻松，便捷的使用上这项服务。

作为当今最受欢迎的容器化解决方案，docker 在业界发光发亮的同时，也为一般用户，「一键」启用某些服务提供了契机。利用开源社区，你可以比以往任何时候都更为容易的实现许多互联网服务的「自给自足」。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，了解更多硬核技巧 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://beta.sspai.com/post/56893)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2bca369f-9113-48d3-9cc4-9531ac0ddeac/2bca369f-9113-48d3-9cc4-9531ac0ddeac/)