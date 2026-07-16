---
title: "如何查看未越狱 iPhone 电池剩余最大容量丨Matrix 精选"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何查看未越狱 iPhone 电池剩余最大容量丨Matrix 精选.md
tags: [印象笔记]
---

# 如何查看未越狱 iPhone 电池剩余最大容量丨Matrix 精选

# 如何查看未越狱 iPhone 电池剩余最大容量丨Matrix 精选 --- ![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/5

---

# 如何查看未越狱 iPhone 电池剩余最大容量丨Matrix 精选

---

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/5D8FEC4D-4C79-4130-82A0-D31FCD1ED202.jpg)

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/1E7B6EE0-E5BB-46E8-865B-51CB72A3E2EC.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章内容仅代表作者本人观点，仅对排版有略作修改，[原文链接](http://matrix.sspai.com/p/d29b67c0)。

iPhone 6s 才买了大半年，最近总是觉得电池越来越不够用了，甚至一天要充电两次才够用。搜索后在苹果官网看到关于电池的 [保修条款](https://support.apple.com/zh-cn/iphone/repair/battery-power)：「如果您在保修或 AppleCare+ 的保障范围内，且您的电池蓄电量在其原始容量的 80% 以下，我们将免费对其进行更换。」

通过诊断与用量数据查看
-----------

那么如何查看剩余电量呢？根据搜索得知，在「设置 - 隐私 - 诊断与用量 - 诊断与用量数据」中的 `log-aggregated` 日志中包含了电池容量的相关信息。具体字段为：

```
com.apple.snapshot.battery.maxCapacity
```

对应的 value 值即为电池剩余最大容量，除以出厂设计容量，就能判断是否在原始容量 80% 以下了。

如果没有找到 `log-aggregated` 文件，请检查自动发送是否开启。开启后需要等两天才能看到。

虽然这样能从 `log-aggregated` 中找到电池容量的信息，但是这个文件的信息一般有数千行，凭肉眼很难找到这个键值对（我是找了一个小时都没找到……），所以最好还是将 log 全选复制，粘贴到备忘录中再搜索吧。

但是长按后并没有全选按钮，该如何全选呢？经过小编指点，我又 Get 到了一个新技能，如果在长按文本后没有全选按钮，我们可以用一只手按住后面的光标，然后另一只手快速下划，很快就可以全选所有内容，然后就可以复制了。

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/58CF9914-6F63-44A6-AC4E-101E03CC56EC.jpg)

通过 iBackupbot 查看
----------------

[iBackupbot](http://www.icopybot.com/itunes-backup-manager.htm) 是一款用于备份 iOS 设备的工具，自带一个系统信息查看功能，在左侧的 `Devices` 中选中设备，点击右侧的 `More Information` 按钮，就可以看见电池信息了。

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/5DD7E6B5-C36D-4D7F-A544-5EB6143E3B54.jpg)

电池信息中包括充电循环次数（CycleCount），设计容量（DesignCapacity），目前剩余电池容量（FullChargeCapacity）以及其他信息。

从这里可以看出来，我的电池目前实际容量为 1400 mAh，设计容量为 1690 mAh，比例为 1400/1690 = 82%，还没达到更换电池的要求。

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/DB9F33BD-3600-46C6-8066-3677B8E9ED41.jpg)

使用 Coconutbattery 也很方便
----------------------

如果你觉得上面这两种方法比较麻烦，还有一个更方便的 Mac 平台的小工具可以查看 iPhone 的剩余电池容量。那就是 [Coconutbattery](http://www.coconut-flavour.com/coconutbattery/#idDownload)，下载打开就能查看，使用非常方便。它不仅可以查看 iPhone，iPad 等 iOS 设备，还可以直接查看 Mac 电脑的电池情况。

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/04780814-DA90-47D6-8B6F-062D38BF8A16.jpg)

通过 Coconutbattery 查看电池容量得知，目前我的 iPhone 6s 剩余容量为 1426 mAh，和使用 iBackupbot 查看的结果略有差异，不过总体上应该还是比较准确的。

更简单的方法：AIDA64 & Battery Life
----------------------------

感谢 Matrix 读者[广陵止息](http://sspai.com/user/715597)推荐了 AIDA64 这款 App，[AIDA64](https://www.aida64.com/) 是一款 Windows 平台上非常出名的测试软硬件系统信息的工具，如今也有了对应的 [iOS 版本](https://itunes.apple.com/us/app/aida64/id979579523?mt=8&uo=4&at=10lJSw)，下载打开就能查看，无需连接 Mac。

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/0D485C14-2ECA-425D-8E87-1FFD853B72D9.jpg)

测出来目前容量为 1438 mAh，和上面两款工具测出来的结果有些偏差，不过总体上也比较准确。

感谢 Matrix 读者 [iamcaoyang](http://sspai.com/user/683540) 推荐了 [Battery Life](https://itunes.apple.com/us/app/battery-life-check-internal/id1080930585?mt=8&uo=4&at=10lJSw) 这款 App。Battery Life 支持中文，打开默认显示电池的损耗水平，哈哈，这不正是我想要的吗？你也可以点击左侧的菜单，切换到原始数据页面，查看更多信息。（注：此应用目前不支持 iOS 10）

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/34B08E5F-E994-4096-B380-747E1C4F7900.jpg)

![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/1B628CFB-4E3A-448A-BD96-12CBAB76507B.jpg)

文章来源 [少数派](http://sspai.com) ，原作者 [Slark](http://sspai.com/author/716389) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/5FEBEC79-7302-44AB-A3A3-BF023EDAB5F1/C603E026-642F-4E29-AC3C-C1DA9403683C.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:BASE/destination:http://www.apple.com/cn/shop/product/HK2R2ZM/A/%E9%85%8D%E5%A4%87-smart-connector-%E7%9A%84-logi-base-%E5%85%85%E7%94%B5%E6%94%AF%E6%9E%B6-%E9%80%82%E7%94%A8%E4%BA%8E-ipad-pro?fnode=85)

---

[🌐 原始链接](http://sspai.com/35373)

[📎 在印象笔记中打开](evernote:///view/207087/s1/03738f0b-052d-403b-ba77-813e73335dfe/03738f0b-052d-403b-ba77-813e73335dfe/)