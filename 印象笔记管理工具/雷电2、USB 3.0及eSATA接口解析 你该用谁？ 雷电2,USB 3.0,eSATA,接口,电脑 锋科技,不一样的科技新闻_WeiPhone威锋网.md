# 雷电2、USB 3.0及eSATA接口解析 你该用谁？ 雷电2,USB 3.0,eSATA,接口,电脑 锋科技,不一样的科技新闻_WeiPhone威锋网

---

2015 Jul 06 21:28

[[PC和硬件](http://tech.feng.com/pchardware)]| Posted by [STAROUS](http://bbs.weiphone.com/u.php?uid=8806282)| Links *腾讯数码* | [*1* Comments](evernote-html-snippet://#comment)

目前市面上存在的主流传输接口标准有Thunderbolt、USB以及eSATA，本文试图理清这些令人眼花缭乱的名词，加深读者对数码知识的了解。  
　  
　　**Thunderbolt 2与Thunderbolt 1的差异何在？**  
  

[![](.evernote-content/12F50B20-4CA2-486A-B860-02F6C52AF127/456E7219-C88A-44E4-BFFE-431969BA08C1.jpg)](http://resource.feng.com/resource/h058/h23/img201507062130140.jpg "雷电2、USB 3.0及eSATA接口解析 你该用谁？")

  
　　第二代Thunderbolt标准结合了DisplayPort以及PCI Express规范，较第一代的Thunderbolt有着更快的数据传输速率。前者可以通过单一连接通道传输4K视频数据，两倍于第一代的速率，但它们的带宽都是40Gbps。  
  
　　两者的区别就在带宽的分配利用上。初代Thunderbolt标准支持4个单向通道，每个提供10Gbps带宽，两个用于传输上行数据，还有两个用于下行。  
  
　　而Thunderbolt 2提供了2个双向通道，每个分别拥有20Gbps的带宽，这意味着单一通道就可胜任4K视频或高速存储设备的传输要求。  
  
　**速度**  
  
　　全部三个标准在传输速率上都远胜于USB 2.0。USB 2.0的最高速率为480Mbps，eSATA最高支持6Gbps（老版本是1.5Gbps或3Gbps），USB 3.0是5Gbps（即将推出的USB 3.1将会支持10Gbps），而Thunderbolt则是20Gbps。  
  
　　**兼容性**  
  

[![](.evernote-content/12F50B20-4CA2-486A-B860-02F6C52AF127/32D9EB54-CA17-4987-82F0-D8BBA548EA5C.jpg)](http://resource.feng.com/resource/h058/h23/img201507062130141.jpg "雷电2、USB 3.0及eSATA接口解析 你该用谁？")

  
　　Thunderbolt结合了两项接口标准：PCI Express（PCIe）以及DisplayPort，这意味着用户可以连接显示器、外部驱动器、视频捕捉设备等等。DisplayPort提供后向兼容性，但用户需要一个连接线适配器才能使用现有的DisplayPort端口。同时，通过适配器，Thunderbolt也能够连接至DVI、HDMI以及VGA显示器。此外，如果用户使用OS X，则可以将两台Mac通过Thunderbolt而非传统的以太网端口进行组网。  
  
　　Thunderbolt 2的连接头与最初的Thunderbolt标准一致，因此，用户可以将Thunderbolt设备连接至Thunderbolt 2端口，反之亦然，连接线也可以通用。与其他标准类似，采用旧规格的连接方式将无法从新标准提升的性能中获益。  
  
　　需要特别指出的是，如果用户在同一链路（菊花链，daisy-chaining）中同时连接了Thunderbolt以及Thunderbolt 2设备，请确保老式Thunderbolt设备位于链路末端，否则全部设备都将降速至Thunderbolt标准运行。  
  
　　USB 3.0也提供后向兼容性，因此，用户可以将USB 2.0设备连接至USB 3.0端口，反之亦然。当然，USB 2.0设备或端口无法提供USB 3.0的速度。如果用户需要使用多重USB设备，则需要多重USB端口，或者购买USB集线器。USB设备针对独立使用而设计，没有采用Thunderbolt设备的菊花链方式。  
  
　　eSATA是串行ATA的外置式版本，后者通常作为内置式硬盘的高速接口标准使用。包括东芝在内的一些公司推出的笔记本采用了双模式端口设计，可以同时连接eSATA或USB设备。  
  
　　**可用性**  
  

[![](.evernote-content/12F50B20-4CA2-486A-B860-02F6C52AF127/D000BFDE-BBEE-42A7-ACE2-9112281255F2.jpg)](http://resource.feng.com/resource/h058/h23/img201507062130142.jpg "雷电2、USB 3.0及eSATA接口解析 你该用谁？")

  
　　目前，Thunderbolt 2在很大程度上局限于近期推出的苹果计算机上，例如MacBook Pro视网膜屏版本、Mac Pro、5K iMac以及2014款Mac Mini。在少数PC端口适配器上也能发现其踪影。同时也存在少数例外，例如戴尔的Precision M3800工作站就针对专业用户提供了Thunderbolt 2端口。  
  
　　相比较而言，USB 3.0就比较常见了，用户在大量的PC以及PC外设中都能发现其踪影，很大程度上是为了取代各种外设上的eSATA端口，例如外置式硬盘。然而，eSATA在企业客户中依然十分流行，主要原因是，在这类场合，USB端口通常出于安全原因被IT部门关闭。因此，各类外置设备需要eSATA端口作为连接手段。  
  
　　虽然Thunderbolt仍处于小众范围，但情况很可能发生改变。Thunderbolt 3将会与USB Type-C统一端口，且兼容USB 3.1标准，不仅支持DisplayPort、HDMI以及USB，同时还提供高达40Gbps的数据传输速率以及双向供电能力。  
  
　　英特尔方面表示，已有超过30种PC产品将会支持Thunderbolt 3，该接口有望一统江湖。  
  
　**哪一款最适合自己？**  
  
　　如果想要将PC连接至外置式存储设备，eSATA最为适合，对于企业IT部门来说尤为如此。然而，对于普通消费者而言，USB 3.0更常见，且价格更为便宜。  
  
　　Thunderbolt的价格还不算便宜，主要面向从事4K视频编辑、需要高速数据传输速率以及那些面对一根2米的连接线上高达500元的售价连眼睛都不会眨一下的人。

---

[🌐 原始链接](http://tech.feng.com/2015-07-06/Lightning-2-USB-3.0-and-hookup-to-parsing-Who-should-you-use_618088.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d0482ea8-ee63-4e73-9793-0b63ee819085/d0482ea8-ee63-4e73-9793-0b63ee819085/)