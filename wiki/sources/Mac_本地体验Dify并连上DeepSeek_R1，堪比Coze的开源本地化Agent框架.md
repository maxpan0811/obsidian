---
title: Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架.md
tags: [AI技术]
updated: 2026-06-27
---

---
title: "Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架"
source: evernote
type: note
export_date: 2026-06-25
guid: 86dbe22e-f4a9-4b41-80bf-5e299967c3ab
---

# Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwODYwMTE5Mw==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkwODYwMTE5Mw==&mid=2247483809&idx=1&sn=d470669215127ca77719a57a2e6019ad&chksm=c1b81f5361781d47c4aef8a33be4a9e7d53d87d8636d7d06be3ca25a20f175ca288d5495e8b6&scene=132&exptype=timeline_recommend_article_extendread_extendread_for_notrec&show_related_article=1&subscene=90&ascene=0&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQd8hCZaQFW8jDTbStlY0AwhLWAQIE97dBBAEAAAAAALtXMcJKm6gAAAAOpnltbLcz9gKNyK89dVj0mwQL8vfyYEur7NTakcTuHpShAJIvsL+Oqjw6S3LV31x3T7S+Y8pq9AQj15q6cJZALxj3eZbCAZ26S2ihnHZR6sogFbEh9ULw4H0kJ6ckOsRdKk4usg2NGltNaz9uKfAoYYFDk7KTI3agGefwd9aqJ4m0lKV+FOQM1L15kCU0jZ7A00KNFGbCDHfV+M045CwHjaZ8rduxBovitNCqPgWK3ZIbAVd9GKYFXalVkQkSLYc=&pass_ticket=4PkewGTPTmcfpQlE4zJq8Ofwbz+yH1o4IURw/vqkQSXWXZVzqYLhr1apY3HRV1Bd&wx_header=3)

# Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架

原创青塬科技小五青塬科技

前文讲过在本地布署DeepSeek R1推理模型。

这篇内容，主要讲一下Dify安装。更多好玩的应用，起码得先有个架子不是。

Dify可不光是Agent，还有很多好玩的东西在里面。工作流、知识库、大模型对话，一应俱全。

我将使用Docker进行Dify安装，后续的相关应用，有空再写点文章了。

为什么使用Docker呢，主要是随用随关，避免把系统整太多垃圾了。不光是Dify，安装好Docker能体验的好东西太多。

顺手分享一些简单的Mac经验技巧。

### 第一步：创建一个干净的目录，存放Dify的源码和文件。

比如我创建的目录是：  
/Users/xxxx/AITool/Agentic

题外话：

这里分享一下常用的设置，建好的目录，如果最快速打开iterm2并跳转到此目录下。

iTerm2是Mac上我感觉最好用的终端工具，Mac自带的终端当然是弱爆了。

下载安装地址：https://iterm2.com/

iterm2可以800个窗口tab，同时干活，不是很爽吗。

![](attachments/514f4d4e8b92913b.jpg)

如何来实现快捷键打开iterm2，并切换到当前目录呢。

打开Mac的系统设置：

找到键盘，键盘快捷键。如下图所示：  

![](attachments/fdf0e21f367f950b.jpg)

弹出窗口，找到服务，文件和文件夹，并展开它  

![](attachments/f924be5caafcffae.jpg)

选择在此处打开iTerm2并设置一个快捷键  

![](attachments/5ee688ee568825ac.jpg)

比如我的是Cmd+Shift+J。完工。

打开任何目录，按快捷键Cmd+Shift+J，将自动打开iTerm2并新建一个Tab,并自动跳转到这个目录下，想执行命令，是不是简单多了。

### 第二步，安装Docker

下载地址：https://www.docker.com/

下载苹果芯片版本，如果是老款Mac，下载Intel芯片版本，如果不清楚，看看系统设置里面，关于本机系统报告里，看看自己的CPU是什么芯片

![](attachments/4624bfb2e8af8c95.jpg)

双击安装，这个比较简单，安装之后，可以直接打开Docker使用。

比较重要的2个概念是Container容器，和Images镜像。可以先不用关注，我们跑起来再说。

镜像相当于模板，容器相当于在模板上，自定义配置搭建出来的实例。

![](attachments/ffc021ec88edeac5.jpg)

### 第三步：拉取Dify并安装

官方布署文档如下：  
https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose

大概流程我整理如下：

额外分享一个经验。使用ssh克隆仓库，比https稳定，https尤其是某些站点的代码比较大时，常常会拉取失败。

比如使用：git clone https://github.com/langgenius/dify.git  
常常会提示各种奇怪的git问题，比如：致命错误：fetch-pack：无效的 index-pack 输出。或者下载到一大半中断掉。原因很简单，  
一般是因为挂了代理IP造成的。换成ssh访问会稳定很多。

如果遇到试试：git clone git@github.com:langgenius/dify.git

大多数时候能解决问题。

1、安装

```
git clone git@github.com:langgenius/dify.git # 拉取主仓库代码  
cd dify/docker  
cp .env.example .env  # 复制配置文件，然后要改配置就改.env了。  
docker compose up -d # 直接安装运行Dify
```

然后会根据配置拉取镜像，创建容器并启动项目。

http://localhost 即可进行访问。记得把语言改为中文。  

![](attachments/5dec5d6e2246a959.jpg)

再添加管理员：  

![](attachments/7beb90fabb31ea52.jpg)

2、更新 Dify  
进入 dify 源代码的 docker 目录，按顺序执行以下命令：

```
cd dify/docker  
  
// 备份自定义docker，可选  
cp docker-compose.yaml docker-compose.yaml.$(date +%s).bak  
  
// 拉取最新代码  
git checkout main  
git pull origin main  
  
// 停止现有的项目  
docker compose down  
  
// 备份资料，可选   
tar -cvf volumes-$(date +%s).tgz volumes  
  
// 拉取最新的镜像  
docker compose pull  
  
// 重新运行  
docker compose up -d
```

3、自定义配置，按下面的流程修改配置文件，然后重启即可。  
编辑 .env 文件中的环境变量值。然后，重新启动 Dify：

```
docker compose down  
docker compose up -d
```

除了mac系统，在Linux系统也是这套流程，只是需要注意一点。有些老的docker不是内置的compose模块。  
需要使用docker-compose。这玩意需要安装，也是一行命令的事，请自行搜索查阅安装文档。

### 第四步：配置DeepSeek R1

登陆Dify。点击右上角设置。

![](attachments/57494cb57441d5b2.jpg)

找到模型供应商  

![](attachments/b4e0f29648506d56.jpg)

点击Ollama，添加

设置模型名称和地址：  
本机一般为：http://127.0.0.1:11434  
但是直接连是不通的，因为docker内部和外部的ollama是不能访问的。  
需要使用地址：http://host.docker.internal:11434  
模型名称 通过:ollama list查看

如下：  

![](attachments/b6712d43303e9a71.jpg)

保存即可

### 第五步：在Dify中使用DeepSeek R1

首先创建一个空白应用  

![](attachments/b148e93cb0d2cb3f.jpg)

创建一个普通的聊天助手  

![](attachments/c42cfa54c89cf019.jpg)

创建之后就可以进行对话了。这时候你会发现，大概率还是用不了的。。。。

![](attachments/9d881ae573a70551.jpg)

一直会卡在提示这里。原因也是网络问题，Ollama默认是不允许非本机IP访问的。改动也很简单。

先关闭Ollama。

再执行下面的命令修改全局环境变量：

```
launchctl setenv OLLAMA_HOST "0.0.0.0"
```

再重新启动：ollama serve

当看到日志提示：listening on 所有地址时，就OK了。原来是on 127.0.0.1。  

![](attachments/a53df77e056c4b7c.jpg)

再回到Dify，试试聊天。

![](attachments/a18d3e8eaec1b8db.jpg)

小样，还治服不了你。

玩过之后要干正事。一行代码关闭，干净利落。

```
docker compose down
```

下次再up一下继续起飞。

### 后记

不知道Dify能干嘛？coze扣子能干的，很多它能干。

我看好它自由可控。Agent可是无比好玩的东西。通过整合我们可以让不同的AI帮助我们完成不同的事。

比如用DeepSeek R1做规划，用别的免费AI做执行，这就是工作流。

做翻译，做语音转录，一切都可以。

我是不会告诉你Dify后台模型管理里面，一大半的大模型提供商，都可以白嫖的。

个人观点，仅供参考


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkwODYwMTE5Mw==&mid=2247483809&idx=1&sn=d470669215127ca77719a57a2e6019ad&chksm=c1b81f5361781d47c4aef8a33be4a9e7d53d87d8636d7d06be3ca25a20f175ca288d5495e8b6&scene=132&exptype=timeline_recommend_article_extendread_extendread_for_notrec&show_related_article=1&subscene=90&ascene=0&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQd8hCZaQFW8jDTbStlY0AwhLWAQIE97dBBAEAAAAAALtXMcJKm6gAAAAOpnltbLcz9gKNyK89dVj0mwQL8vfyYEur7NTakcTuHpShAJIvsL+Oqjw6S3LV31x3T7S+Y8pq9AQj15q6cJZALxj3eZbCAZ26S2ihnHZR6sogFbEh9ULw4H0kJ6ckOsRdKk4usg2NGltNaz9uKfAoYYFDk7KTI3agGefwd9aqJ4m0lKV+FOQM1L15kCU0jZ7A00KNFGbCDHfV+M045CwHjaZ8rduxBovitNCqPgWK3ZIbAVd9GKYFXalVkQkSLYc=&pass_ticket=4PkewGTPTmcfpQlE4zJq8Ofwbz+yH1o4IURw/vqkQSXWXZVzqYLhr1apY3HRV1Bd&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/86dbe22e-f4a9-4b41-80bf-5e299967c3ab/86dbe22e-f4a9-4b41-80bf-5e299967c3ab/)
