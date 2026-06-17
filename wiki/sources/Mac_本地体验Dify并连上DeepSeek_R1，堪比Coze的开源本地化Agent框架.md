---
title: Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架.html
tags: [AI技术]
---

# Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架

原文链接: https://mp.weixin.qq.com/s?__biz=MzkwODYwMTE5Mw==&mid=224748...

Mac 本地体验Dify并连上DeepSeek R1，堪比Coze的开源本地化Agent框架 原创青塬科技小五 青塬科技

&#xa0;前文讲过在本地布署DeepSeek R1推理模型。
这篇内容，主要讲一下Dify安装。更多好玩的应用，起码得先有个架子不是。
Dify可不光是Agent，还有很多好玩的东西在里面。工作流、知识库、大模型对话，一应俱全。
我将使用Docker进行Dify安装，后续的相关应用，有空再写点文章了。
为什么使用Docker呢，主要是随用随关，避免把系统整太多垃圾了。不光是Dify，安装好Docker能体验的好东西太多。
顺手分享一些简单的Mac经验技巧。
第一步：创建一个干净的目录，存放Dify的源码和文件。比如我创建的目录是：/Users/xxxx/AITool/Agentic
题外话：
这里分享一下常用的设置，建好的目录，如果最快速打开iterm2并跳转到此目录下。
iTerm2是Mac上我感觉最好用的终端工具，Mac自带的终端当然是弱爆了。
下载安装地址：https://iterm2.com/
iterm2可以800个窗口tab，同时干活，不是很爽吗。

如何来实现快捷键打开iterm2，并切换到当前目录呢。
打开Mac的系统设置：
找到键盘，键盘快捷键。如下图所示：
弹出窗口，找到服务，文件和文件夹，并展开它
选择在此处打开iTerm2并设置一个快捷键
比如我的是Cmd+Shift+J。完工。
打开任何目录，按快捷键Cmd+Shift+J，将自动打开iTerm2并新建一个Tab,并自动跳转到这个目录下，想执行命令，是不是简单多了。
第二步，安装Docker下载地址：https://www.docker.com/
下载苹果芯片版本，如果是老款Mac，下载Intel芯片版本，如果不清楚，看看系统设置里面，关于本机系统报告里，看看自己的CPU是什么芯片

双击安装，这个比较简单，安装之后，可以直接打开Docker使用。
比较重要的2个概念是Container容器，和Images镜像。可以先不用关注，我们跑起来再说。
镜像相当于模板，容器相当于在模板上，自定义配置搭建出来的实例。

...第三步：拉取Dify并安装官方布署文档如下：https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose
大概流程我整理如下：
额外分享一个经验。使用ssh克隆仓库，比https稳定，https尤其是某些站点的代码比较大时，常常会拉取失败。
比如使用：git clone https://github.com/langgenius/dify.git常常会提示各种奇怪的git问题，比如：致命错误：fetch-pack：无效的 index-pack 输出。或者下载到一大半中断掉。原因很简单，一般是因为挂了代理IP造成的。换成ssh访问会稳定很多。
如果遇到试试：git clone git@github.com:langgenius/dify.git
大多数时候能解决问题。
1、安装
git&#xa0;clone&#xa0;git@github.com:langgenius/dify.git&#xa0;#&#xa0;拉取主仓库代码cd&#xa0;dify/dockercp .env.example .env 
