---
title: "如何在ubuntu上搭建forge服务器_百度知道"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在ubuntu上搭建forge服务器_百度知道.md
tags: [印象笔记]
---


如何在ubuntu上搭建forge服务器
====================

1、安装必要组件，我很推荐装一个screen，因为这样你可以让服务器在后台跑

apt-get install screen default-jdk

在安装完java之后，用java -version看一下是否安装正确

2、创建一个MC服务器的目录并且切换过去

mkdir /yourpath/minecraft/

cd /yourpath/minecraft //yourpath改为自己想要的路径

3、下载MC服务器的压缩包

wget -O minecraft\_server.jar<https://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/minecraft_server.1.7.10.jar>（这是一行）

cp minecraft\_server.jar minecraft\_server.1.7.10.jar

4、启动服务器

java -Xmx2048M -Xms2048M -jar minecraft\_serve

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->