---
title: 2019 年末，我们能采用什么方式改善 Windows 的字体渲染？ - 少数派
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/2019 年末，我们能采用什么方式改善 Windows 的字体渲染？ - 少数派.md
tags: [印象笔记]
---

# 2019 年末，我们能采用什么方式改善 Windows 的字体渲染？ - 少数派

---

2019 年末，我们能采用什么方式改善 Windows 的字体渲染？
==================================

![](.evernote-content/A8A0EAB0-3956-4D4A-9482-27FC6CB20629/ABBF30CF-4337-4257-B0AE-C0211AAEBF14)

2019 年末，我们能采用什么方式改善 Windows 的字体渲染？

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

「9102 年」就要结束了，最新版 Windows 10（v1909）的字体渲染在 150% 以下缩放时的表现依然十分糟糕；开启 150% 缩放后字体渲染才会迎来大幅改善。

**这是因为微软雅黑内置的 gasp 表中对不同字号启用了不同的渲染方式定义**。在最新的 1909 上，这个阈值是 21px，即 21px 以上的文字才启用平滑渲染。很巧的是，21px 对应的缩放百分比正好是 130%。

这就意味着 125% 的缩放可能导致大部分字体渲染「崩坏」。对此，我们可以通过两个方法来「hack」。

注：

* 所有操作在最新版本系统 Windows 10（v1909）下操作，更早的版本可能效果有所不同。
* 本文所使用方法 2 来自知乎用户 @[洛晓晓晓晓](https://www.zhihu.com/people/luo-xiao-wu-17)，[原文地址](https://zhuanlan.zhihu.com/p/26046562) 及 [原理](https://www.zhihu.com/question/31865687/answer/153668179) 可跳转阅读。本文对工具进行了整合并系统化操作步骤。
* 本文所提及所有方法仅为临时解决方案，根治该问题的办法包括但不限于：虔诚地祈愿微软能找人把字体渲染的汇编重新写一次、等待新微软雅黑（一说新微软雅黑即小米兰亭 Pro）被部署到系统中、购买 4K 显示器并启用至少 150% 的缩放、破釜沉舟改用 Linux （针对计算机专业学生）、购买一台 Mac 等等。

方法 1：MacType
------------

可喜可贺的是，早前很多人所熟悉的 MacType 现在完全支持 Windows 10 且无需打补丁了，同时也不太可能会出现大的 bug。使用 MacType 可以看做一个「AOE 技能」，默认情况下对全部字体有效，且可以进行字体热替换、调整阴影、微调笔划等。

但缺点也很明显：

* 严重影响性能，包括 dwm 和用户程序如：Fences 3
* 无法在安全策略高的软件中加载，如：WPS
* 部分程序的渲染很奇怪，如宋体在 IE 或 Edge 下的渲染效果
* 效果调试起来比较麻烦，达到完美需要折腾一段时间

MacType 的配置方法倒也简单：从 Github 下载最新的 [Release](https://github.com/snowie2000/mactype/releases) ，安装后启用即可。在初始配置中建议遵循以下顺序：

* 第一次使用 MacType Wizard 时，选择「独立加载」模式
* 选择配置文件，观察 Explorer.exe (资源管理器) 内与 Word / Edge Beta 中的渲染效果
* 重新运行 MacType Wizard。若满意效果，将加载模式改为「注册表加载」或「服务加载」以获得更好的使用体验；若不满意，关闭所有应用程序，更改配置文件后重新观察渲染效果。

关于更详细的介绍与效果 demo，可参考《[用 MacType 拯救你的 Windows 字体 | 一日一技](https://sspai.com/post/35133)》。需要注意的是，此文写作于 2016 年，**部分配置方法已过时**。

方法 2：干掉微软雅黑的 hinting
--------------------

具体到本文开头提到的平滑渲染问题，我们也可以使用硬替换的方法，将系统中微软雅黑、Segoe UI、Arial、宋体等字体的 hinting 干掉来得到更好的渲染效果。

注意，这个方法也有一定的危险性且可能在操作系统更新后失效。**请在完全了解过程与其危险性的前提下进行此操作**。

工具包下载：[Link](https://2-ccna-1258671515.cos.ap-shanghai.myqcloud.com/sspai/remove_hinting_sspai.zip)。该链接仅供本站使用。

### 步骤

1. 解压缩工具包，并按照 instruction.txt 配置好环境。
2. 启动 Powershell，将目录切换到工具包目录下。
3. 执行 cd simsun 、 .\GaspHack\_v2.bat 与 cd ..
4. 执行 cd general 与 .\GaspHack\_v2.bat
5. 双击运行 backup 目录下的 back.bat
6. 如果一切都正常运行，backup 下应有一堆字体，包括 simsun.ttc, msyh.ttc, segoeui.ttf 等；general\workingDir\output 与 simsun\workingDir\output 下也有对应的字体。
7. 尽可能地退出其他无关软件，特别是杀毒软件等安全工具，运行「字体替换工具」，将 general\workingDir\output 与 simsun\workingDir\output 下的文件拖入，点击「开始执行任务」即可。
8. 重启电脑，打开设置并搜索「ClearType」，选择「调整 ClearType 文本」并按照提示操作。
9. 注销用户并重新登录，完成。

### Credit

总结
--

平心而论，通过干掉 hinting 的方式来改善渲染在效果上可能不如 MacType 好，但这种方法的优势很明显：兼容性好、性能高（没有动态加载其他 dll）。

出于性能及安全性考虑，本文不再介绍 WinFont 对此方法的一个小修复。如果想覆盖更多字体，可通过增删 general 目录下的 bat 文件中的 copy C:\Windows\Fonts\segoe\*.ttf .\ 段来达到目的。

同时，本方法主要面对使用 125% 缩放的设备，150% 与 175% 缩放的设备也可以通过该方法提升观感。200% 以上缩放的设备无需改动。对于低 PPI 屏幕（简单判断方法：Windows 推荐缩放比例为 100%，且 100% 下字体大小可接受）的用户，原作者建议不用折腾了。

如果在干掉 hinting 后想要恢复原来的字体，打开字体替换工具执行「还原」操作即可。

最后放上方法二操作前后的效果预览：

![](.evernote-content/A8A0EAB0-3956-4D4A-9482-27FC6CB20629/81F13596-2368-43AA-A390-1476F107449F.png)

Word 中的渲染示例

请查看原图观察效果。

由于每个显示器的像素排列方式等不同，效果也有可能不同，**这也是需要执行「调整 ClearType 文本」的原因**。宋体由于在小字号下使用平滑渲染看着比较难受，本文中给出的配置未进行处理。

**关联阅读：**[不输 MacType，这些优化思路也能让 Windows 字体细腻清晰](https://sspai.com/post/52815)

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，发现更多实用 Windows 技巧

> 特惠、好用的硬件产品，尽在[少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57729)

[📎 在印象笔记中打开](evernote:///view/207087/s1/078e913c-f9f2-4101-a209-118845e8bfac/078e913c-f9f2-4101-a209-118845e8bfac/)
