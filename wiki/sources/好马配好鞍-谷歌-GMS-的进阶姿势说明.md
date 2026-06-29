---
title: 好马配好鞍，谷歌 GMS 的进阶姿势说明
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/好马配好鞍，谷歌 GMS 的进阶姿势说明.html
tags: [印象笔记]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "好马配好鞍，谷歌 GMS 的进阶姿势说明"
source: evernote
type: note
export_date: 2026-06-27
guid: dd08069c-9251-4d04-9244-a54d554445e4
---

# 好马配好鞍，谷歌 GMS 的进阶姿势说明

![](attachments/c0c9bedae2b87cfe.jpg)

对于广大刷机界的原生爱好者，躲开了果粉的炮火，也绕开了墙的围攻，好不容易干掉官方丑陋的 UI，刷上了 CM 或者是魔趣，难免就想再深入了解一下远在天边的 GMS（Google Mobile Service 谷歌移动服务）。

翻开各大手机论坛、应用市场评，都能见到许多热心群众默默贡献的 Gapps 包，有的甚至是上古流传下来的的陈年老包，一看编译日期还居然是 2014。或者图省心用个 Google 应用安装器，刷好一打开全家都蹦出来你更新。所以不少人就有这样的疑问：

- 怎么找到最新最适合ROM的包？
- 怎么了解各个包之间的区别？
- 怎么配置一个适合自己的包？

本文就来安利给大家一个配置 Gapps 的正确姿势。

新入坑的看官请等一下，在前段时间派家的 [好马配好鞍，安装谷歌服务框架的正确姿势](http://sspai.com/30499) 一文中，已经简要地介绍了 GMS 安装的教程，许多内容在此就不重复，有需要的可以先通读一下此文。

## 下载地址的选择

随着 PA Gapps 的停止维护，现阶段 opengapps 成为了 Android 手机想体验谷歌服务的几乎唯一且是最佳的选择。

[点击前往 opengapp 官方网站](http://www.example.com/)

如图，opengapps 会根据你的 CPU 指令集、Android 内核、应用套件，分别提供最新从Nexus 设备上采集大小不一的包，在刷机时，也会根据你屏幕 DPI 、Android 版本的不同刷入所适配的的应用。稳定、方便、自由都有了，不能更良心。

![](attachments/0c51866f2e3bf93c.jpg)

有同学可能会问了：前面的 ARM、X86、4.4、5.0 道理我都懂，后面的 stock、full、mni、micro、nano、pico 是什么鬼？那我就来图文并茂的说明一下，进一步提高姿势水平。

## 不同包间的比较

- **aroma**：图形化安装版本，可以自定义所需刷入的应用。（但某些机型会由于 recovery 的原因无法使用，谁能保证你的机型不是其中之一呢，不作为第一推荐）。
- **super**：最为完备的版本，该有的和不该有的，都给有了（比如日语输入法、注音输入法、安卓支付等大陆用户基本上不会需要的应用）
- **stock**：包括 Nexus 出厂所具备的所有应用，在安装好系统后，刷入该包会自动替换掉 Aosp 的应用，比如 Google 相机、Gmail、Google Now 桌面、Google 相册分别替换掉 Aosp 所带的 相机、邮件、桌面、相册等，当然 Google 全家桶的其他软件如 Gooele Play、Youtube、地图、Gooele keep 等也会随之刷入你手机。【认真严肃推荐该版本】
- **full** **：**与 stock 唯一区别就在于不会替换掉 Aosp 应用，也就是说你就有两个相机、两个邮件、两个桌面……（不嫌挤的可以试试这个）
- **mini****、****micro****、****nano****、****pico** **：**依次减少应用，但都具备 Google service 和 Play 。（想这俩都不要的你还刷它干嘛）

有详细需求的可以上 Github上查看 [opengapps 套件详细对比](https://github.com/opengapps/opengapps/wiki/Package-Comparison) 。

我把翻译后长长的说明贴下，方便大家选择（真的很长，所以叫长长）。不过**简单的说就是**：带 X 的被安装，带 O 的替代掉 Aosp 应用并安装，带 6.0 的只有 6.0 以上会被安装。

![](attachments/4ca37d656a4f76d8.jpg)

## **Gapps** **的进阶安装**

如果看了前文对各种包灵活性还不太满意，喜欢像风一样自由地安装自己想要的 App 的主儿可以试试这个，去除污渍，自定义一切安装。

[官网上有许多高级安装的方法](https://github.com/opengapps/opengapps/wiki/Advanced-Features-and-Options)，这里介绍一种相对比较简单的。

1. 首先推荐下载大而全的 stock 包（不想要替换应用的可以选择 full 包）。
2. 其次你需要在手机存储里新建一个名为 gapps-config.txt 的文件，并和 Gapps 包放在同一文件夹中（比如根目录）。
3. 在文件中写入选择不需要安装应用的 **关键字（**上图应用名右侧 keyword 栏**）**写成「**Exclude** +**keyword**」的形式 （如下图）。
4. 然后进入第三方 recovery 选择刷入 Gapps 包刷入，此时会自动跳过清单中被排除的应用。

### **示例姿势说明：**

**![](attachments/b42e84a2ff2dd1b7.jpg)**

### **你有可能不知道的知识：**

- 当需要清除 Gapps 中的内容，在 recovery 界面中仅仅双清是不够的，还需要手动清空 System分区。
- 当 GMS 中的应用被更新时，更新包不会被安装在 System 分区，而是安装在 Data 分区，因为系统需要保留最原始的版本以便回退。
- 当然你们是了解的，GMS 应用在「国内正常网络条件」下是不能使用的，你需要自备一把梯子。
- 你可能纳闷为什么时不时打开 Play 显示的都是不同语言的版本，这没有可能，肯定是你使用了不同的梯子，你需要学会锁区。
- Play 上下载的应用和国内市场上下载的应用有可能是不同的，比如 Play 上的微信就带 GCM 推送，但你在官网下的肯定就没有。
- 喜欢强行使用Google Now 的朋友，这里有一个你肯定喜欢的开启工具。[启用Google Now:Google Now Enabler](http://www.coolapk.com/apk/com.czbix.nowenabler)。
- Google相册真的很好用。

文章来源 [少数派](http://sspai.com) ，原作者 [我的隔壁是呆逼](http://sspai.com/author/693306) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](attachments/ec655a06413d2071.jpg)](http://sspai.com/topic/best-apps-2015)
