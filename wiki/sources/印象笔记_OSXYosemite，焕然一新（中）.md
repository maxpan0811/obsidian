---
title: "OSXYosemite，焕然一新（中）"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OSXYosemite，焕然一新（中）.md
tags: [印象笔记]
---


![](.evernote-content/3D0A440C-5E2D-4188-82D0-48DD70A5B4E7/DA7AF9E5-7C8C-4AB2-8D6A-D8D536595960.jpg)

明天凌晨最新的 OS X 就会发布了。

马不停蹄，继续优胜美地中篇。另外，历时一个月，我的 iPhone 6 Plus 终于先于国行到货了，我先体验下你，回头给大家写写。

#### 开发者之殇（接续）

4、Docker  
如果你在自己的 Mac 上使用了 Docker，那么需要重新安装 Boot2Docker：  
[https://github.com/boot2docker/osx-installer/releases]  
重新安装 VirtualBox：  
[https://www.virtualbox.org/wiki/Downloads]

如果你之前有做好的镜像，最好在 Yesomite 升级之前先导出备份：

备份Docker 的镜像：docker save f81bcd8c1acd > gap411.tar   
注：f81bcd8c1acd 是镜像的 ID

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->