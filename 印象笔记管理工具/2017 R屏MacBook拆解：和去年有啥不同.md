# 2017 R屏MacBook拆解：和去年有啥不同

---

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/426FCEF3-67FE-43D0-95D2-83CC91585B19.png)

今年 Retina MacBook 的更新来的要比往年晚一些，从 3 月份更新推迟到了 6 月份的 WWDC 大会上，今天就让我们通过 iFixit 的拆解来看看，这款迟到了的 2017 Retina MacBook 相比去年的机型是否有了什么新的变化。

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/A694C34A-3A08-4BD3-8849-5F188328BC9A.png)

本次拆解是深空灰 2017 Retina MacBook，规格如下：

－12 英寸 2304 × 1440 (226 ppi) IPS Retina 屏幕

－1.2 GHz 四核 Intel Core m3 处理器 (睿频加速至 3.0 GHz)

－8 GB 的1866 MHz LPDDR3 SDRAM

－256 GB PCIe SSD

－Intel HD Graphics 615 显卡

－802.11ac Wi-Fi 和 Bluetooth 4.2

－一个 USB-C 接口和 3.5 mm 耳机接口

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/2D145448-0E92-4E32-92B3-3DA12A4072A7.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/F386A629-6FB5-4A88-A6C9-7467946B4687.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/8CBBF119-43D4-43C1-A6E5-F80A027B2E5A.png)

超大触控板、USB 3 接口还有麦克风，这一切看起来怎么那么熟悉。2017 MacBook 型号是 A1534，好像 2016 Retina MacBook 也是这个型号。这么多相同的地方，是不是把去年的复制粘贴一遍就好了？

EMC 码是 3099，这个数字是不一样的，16 款的 EMC 码为 2991，15 款的是 2746。新设备里应该还有不一样的地方，让我们继续挖掘。

梅花型螺丝钉扭出来，外壳拿掉，看看 MacBook 里有什么天地。

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/A9E5174A-3B2C-49C4-8ABD-899F549A5DDA.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/550EDAA4-8B59-4FB1-B477-A0FF1129C795.png)

触控板下的东西看起来和去年的机型没什么区别，IC 和去年是一样的：

－红：博通 BCM5976 触控屏控制器

－橙：意法半导体 32F103 ARM Cortex-M3 微控制器

－黄：International Rectifier IRFH3702 、 N-Channel HEXFET 金氧半场效晶体管

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/8A0337D8-98B3-4FDF-91E6-EAB47EBDA257.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/3ED2E21E-79AA-4F78-A930-5580F464DF55.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/515E7C36-6374-47B4-9D06-E2C209C4EA43.png)

在这里，2017 款 MacBook 和 201 6款一样，将三翼螺丝换成了飞利浦螺丝，内部的其它螺丝都是常规的飞利浦梅花型螺丝。对于想要自己动手维修设备的用户来说，这可是个好消息。

坏消息就是，我们看到苹果将很多部件都焊接在了主板上，这些部件完全动弹不得。

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/3546FB12-BD24-455A-BAC7-9D648164ECE9.png)

芯片组中总算有点不同了：

－红：英特尔 SR346 Intel Core m3-7Y32 处理器(4M 缓存，可加频至 3.00 GHz)

－橙；东芝 TH58XGT0JFLLDVK 128 GB NAND 闪存 (另一边还有 128 GB，所以总共是 256 GB)

－黄：SK 海力士 H5TC4G63CFR 4Gb DDR3 SDRAM

－绿：环隆电气 339S0250 Wi-Fi 模块

－青：博通 BCM15700A2

－蓝：美国国家半导体公司 48B1-11

－紫：SK 海力士 H9CKNNN4GTATMR-NTH (SSD 控制器应该在它的下方)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/9CFE23B9-1E9F-46D5-99EB-A43A575A18E2.png)

另一面：

－红：东芝 TH58XGT0JFLLDVK 128 GB NAND闪存

－橙：镁光科技 7CB47D9TDZ 4 GB 1866 MHz LPDDR3 RAM (两个，一共 8GB )

－黄：苹果 338S00227-A0

－绿：德州仪器/Stellaris LM4FS1EH SMC 控制器

－青：德州仪器 TMP513A 热管理/电源管理

－蓝：德州仪器 SN650839, TPS51980A 和 CD3215C00

－紫：英特锡尔 95828

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/82BE712B-1D35-4D80-ADA1-E9DCAABA634A.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/632DB2AE-E8A9-4C8A-8942-49206372B134.png)

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/95B57B1A-639F-48DE-8B89-6A521A36ABFF.png)

消息称第二代蝴蝶式键盘让 MacBook 的键盘更难用，那么这款新产品的键盘里面到底是什么样的。

今年的深灰版键盘和去年的玫瑰金版键盘对比，我们可以看到检测键击的机械开关变成了简单的圆穹形，去年是 X 形。塑料蝴蝶机制也重新设计以更适应新的开关，变成新的更薄的框架。control 和 option 键也有了变化，它们现在是键盘快捷键的代表。

![](.evernote-content/8ED9FB7C-91FF-4514-858B-74E4B1B32B2B/A567AD3F-9943-426C-BA8F-BBCEA124AD23.png)

因为今年的 Retina MacBook 变化确实很少，所以拆解步骤也非常少。iFixit 的总结如下：

－可维修性得分 1 分（满分 10 分，最容易维修）

－苹果没有用回三翼螺丝，而是换成了飞利浦螺丝和梅花型螺丝

－处理器、RAM 和闪存仍然焊接在主板是上

－电池也用大量强力胶黏在机壳上

－Retina 屏幕和保护玻璃熔成一体。显示屏坏的话，整面屏幕都得更换，维修成本很高。

[阅读全文](http://www.feng.com/iPhone/news/2017-06-09/2017-R-screen-MacBook-apart-what-is-different-with-that-of-last-year_681999.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2017-06-09/2017-R-screen-MacBook-apart-what-is-different-with-that-of-last-year_681999.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e3f92346-ccf6-43a7-9560-f29dea0f6491/e3f92346-ccf6-43a7-9560-f29dea0f6491/)