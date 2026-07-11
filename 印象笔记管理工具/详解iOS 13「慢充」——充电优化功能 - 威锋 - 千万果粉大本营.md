# 详解iOS 13「慢充」——充电优化功能 - 威锋 - 千万果粉大本营

---

详解iOS 13「慢充」——充电优化功能
====================

Ruins0080
发表于: 2019-08-05 16:52

来自 威锋网页版

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' data-v-7d2a2a76='' aria-hidden='true' width='16px' height='16px' data-evernote-id='1658' class='js-evernote-checked'%3e%3ctitle data-evernote-id='2400' class='js-evernote-checked'%3esee copy 2%e5%a4%87%e4%bb%bd 19%3c/title%3e%3cdesc data-evernote-id='2401' class='js-evernote-checked'%3eCreated with Sketch.%3c/desc%3e%3cg id='icon-eye_%e9%a6%96%e9%a1%b5' stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' data-evernote-id='2402' class='js-evernote-checked'%3e %3cg id='icon-eye_%e7%a4%be%e5%8c%ba%e6%8e%a8%e8%8d%90%e5%a4%87%e4%bb%bd-2' transform='translate(-1024.000000%2c -704.000000)' stroke='%23AAAEB3' data-evernote-id='2403' class='js-evernote-checked'%3e %3cg id='icon-eye_%e7%bc%96%e7%bb%84-10' transform='translate(1024.000000%2c 702.000000)' data-evernote-id='2404' class='js-evernote-checked'%3e %3cg id='icon-eye_%e7%bc%96%e7%bb%84-7' data-evernote-id='2405' class='js-evernote-checked'%3e %3cg id='icon-eye_%e7%bc%96%e7%bb%84-4%e5%a4%87%e4%bb%bd-4' data-evernote-id='2406' class='js-evernote-checked'%3e %3cg id='icon-eye_%e5%88%86%e7%bb%84-12' transform='translate(0.000000%2c 1.000000)' data-evernote-id='2407' class='js-evernote-checked'%3e %3cg id='icon-eye_Group-10-Copy' transform='translate(0.000000%2c 1.000000)' data-evernote-id='2408' class='js-evernote-checked'%3e %3cg id='icon-eye_Group-11' transform='translate(0.500000%2c 2.500000)' data-evernote-id='2409' class='js-evernote-checked'%3e %3cpath d='M0.392752293%2c5.5 C1.42729415%2c2.48789379 4.2187504%2c0.329855942 7.5%2c0.329855942 C10.7812496%2c0.329855942 13.5727059%2c2.48789379 14.6072477%2c5.5 C13.5727059%2c8.51210621 10.7812496%2c10.6701441 7.5%2c10.6701441 C4.2187504%2c10.6701441 1.42729415%2c8.51210621 0.392752293%2c5.5 Z' id='icon-eye_Combined-Shape' data-evernote-id='2410' class='js-evernote-checked'%3e%3c/path%3e %3ccircle id='icon-eye_Oval-6' cx='7.5' cy='5.5' r='2.06711693' data-evernote-id='2411' class='js-evernote-checked'%3e%3c/circle%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e%3c/svg%3e) 2.2w

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' data-v-7d2a2a76='' aria-hidden='true' width='16px' height='16px' data-evernote-id='1659' class='js-evernote-checked'%3e%3ctitle data-evernote-id='2912' class='js-evernote-checked'%3emessage copy%e5%a4%87%e4%bb%bd 10%3c/title%3e%3cdesc data-evernote-id='2913' class='js-evernote-checked'%3eCreated with Sketch.%3c/desc%3e%3cg id='icon-message_%e9%a6%96%e9%a1%b5' stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' data-evernote-id='2914' class='js-evernote-checked'%3e %3cg id='icon-message_%e7%a4%be%e5%8c%ba%e6%8e%a8%e8%8d%90%e5%a4%87%e4%bb%bd-2' transform='translate(-1088.000000%2c -704.000000)' data-evernote-id='2915' class='js-evernote-checked'%3e %3cg id='icon-message_%e7%bc%96%e7%bb%84-10' transform='translate(1024.000000%2c 702.000000)' data-evernote-id='2916' class='js-evernote-checked'%3e %3cg id='icon-message_%e7%bc%96%e7%bb%84-7' data-evernote-id='2917' class='js-evernote-checked'%3e %3cg id='icon-message_%e7%bc%96%e7%bb%84-4%e5%a4%87%e4%bb%bd-4' data-evernote-id='2918' class='js-evernote-checked'%3e %3cg id='icon-message_%e7%bc%96%e7%bb%84-15' transform='translate(64.000000%2c 0.500000)' data-evernote-id='2919' class='js-evernote-checked'%3e %3cg id='icon-message_message-copy' transform='translate(0.000000%2c 1.500000)' data-evernote-id='2920' class='js-evernote-checked'%3e %3cpath d='M13.812533%2c5.55791801 C13.4946162%2c4.80250439 13.0388416%2c4.12446089 12.4578697%2c3.54207498 C11.8768978%2c2.96109579 11.1988628%2c2.50390878 10.442052%2c2.1873947 C9.66836064%2c1.86244024 8.84684107%2c1.69785292 8.00000069%2c1.69785292 L7.97186646%2c1.69785292 C7.11939923%2c1.70207311 6.29365953%2c1.87088062 5.51715473%2c2.20286872 C4.76737745%2c2.52360299 4.09496931%2c2.97938327 3.51962427%2c3.56036246 C2.94427923%2c4.14134164 2.4927248%2c4.81657169 2.18043483%2c5.56917184 C1.85689116%2c6.34849985 1.69371262%2c7.17706338 1.69785295%2c8.02954131 C1.70215289%2c9.00581142 1.93566701%2c9.97504788 2.37315432%2c10.8415931 L2.37315432%2c12.9798216 C2.37315432%2c13.3371308 2.66293691%2c13.626917 3.02024165%2c13.626917 L5.15984998%2c13.626917 C6.02638432%2c14.0644098 6.99560861%2c14.2979269 7.97186646%2c14.3021471 L8.0014074%2c14.3021471 C8.84402764%2c14.3021471 9.66132708%2c14.1389665 10.4307983%2c13.8196389 C11.183389%2c13.5059383 11.8600173%2c13.055785 12.4395825%2c12.4804327 C13.0205544%2c11.9050804 13.4777356%2c11.2326638 13.7970592%2c10.4828771 C14.1290431%2c9.70636259 14.2978485%2c8.88061252 14.3021471%2c8.02813459 C14.3062888%2c7.17143647 14.1402968%2c6.34005947 13.812533%2c5.55791801 L13.812533%2c5.55791801 Z M11.6869918%2c11.7193922 C10.7008869%2c12.6956623 9.39264516%2c13.2330328 8.00000069%2c13.2330328 L7.97608659%2c13.2330328 C7.1278395%2c13.2288127 6.28521926%2c13.0178033 5.54106882%2c12.6211056 L5.42290505%2c12.5578028 L3.44225513%2c12.5578028 L3.44225513%2c10.577128 L3.37895311%2c10.4589627 C2.98226044%2c9.71480297 2.7712537%2c8.87217214 2.76698971%2c8.0239144 C2.76140672%2c6.62140533 3.29736383%2c5.30470674 4.28065524%2c4.31296261 C5.26253993%2c3.32121848 6.57500184%2c2.77259407 7.9774933%2c2.76696716 L8.0014074%2c2.76696716 C8.7047632%2c2.76696716 9.38701832%2c2.90341989 10.0298855%2c3.17351191 C10.6572789%2c3.43657028 11.2199635%2c3.81498045 11.7038723%2c4.29889532 C12.1863744%2c4.78140345 12.5661865%2c5.34550189 12.8292416%2c5.97290314 C13.1021436%2c6.62281206 13.2385947%2c7.31210939 13.2358239%2c8.0239144 C13.227341%2c9.42501674 12.6773167%2c10.7374951 11.6869918%2c11.7193922 Z' id='icon-message_Shape' fill='%23AAAEB3' fill-rule='nonzero' data-evernote-id='2921' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M5.96359615%2c6.4688744 L10.1650275%2c6.4688744' id='icon-message_%e7%9b%b4%e7%ba%bf' stroke='%23AAAEB3' stroke-linecap='round' data-evernote-id='2922' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M5.96359615%2c9.61994794 L10.1650275%2c9.61994794' id='icon-message_%e7%9b%b4%e7%ba%bf' stroke='%23AAAEB3' stroke-linecap='round' data-evernote-id='2923' class='js-evernote-checked'%3e%3c/path%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e %3c/g%3e%3c/svg%3e) 50

只看作者

![](.evernote-content/B8356CCA-5E63-4254-ACB7-E1833E4BAE8A/E8E8C54E-77C0-4CC6-8D96-9E908CFFCF99.png)

保护电池了解一下。

[![](.evernote-content/B8356CCA-5E63-4254-ACB7-E1833E4BAE8A/B06E946B-8F48-45C7-9B3E-832795D633B3)](https://resource.feng.com/resource/h066/h48/img201908091654580.jpg)  
  
iPhone 的电池健康曾在 2018 年成为一个热门话题，此前苹果被发现悄悄地限制降低电池寿命的 iOS 设备的运行性能，尽可能延长电池的使用寿命。  
  
苹果通过发布 iOS 11 的软件更新回应用户对设备运行状况的担忧，引入了电池健康功能，提供了有关设备电池状态的更多信息。而在 iOS 13 中，苹果为电池健康功能添加了「优化电池充电」的新功能，旨在从充电方式上延长 iOS 13 设备的寿命，具体来说，iOS 13 会记录学习用户的充电习惯（随着使用时间的增长，准确度会不断提升），直到使用 iPhone 前进行完全充电，保证锂电池更长时间处于健康状态。  
  
「优化电池充电」的工作方式在实际使用中对于锂电池的保养非常有帮助，夜晚睡觉时设备可能将充电限制在 80%，在用户醒来前的一个小时左右充满剩下的 20%，通过减少电池长时间处在满点状态的时间，使 iPhone 保持最佳电池健康状态，从而缩短电池寿命。  
  
前往「设置」-「电池」，轻触「电池健康」，开启「优化电池充电」即可。  
  
启用该功能后，你会发现当 iPhone 闲置充电时，充电到 80% 便会进入缓慢充电状态，感觉就像是不再充电一样，实际上此时已经切换了涓流模式。如果出现高温问题，系统有机会在 80% 电量时停止充电。  
  
[![](.evernote-content/B8356CCA-5E63-4254-ACB7-E1833E4BAE8A/2AA7D3B1-E4BE-4273-8AFA-8821634B9742)](https://resource.feng.com/resource/h066/h48/img201908091655180.jpg)  
  
根据用户习惯，假如你平常是晚上 12 点开始充电，早上 8 点停止充电，开始使用手机。那么系统一开始会开始快充，电量冲到 80% 的时候便进入缓慢充电状态，并根据你使用手机的时间（上午 8 点），实时调节充电功率，以在此之前完成充电。  
  
在此前的 iOS 13 测试版中，优化后的电池充电功能在默认情况下是禁用的。这说明苹果对于这项功能还并未足够自信，当然，等过一段时间如果测试进展顺利，苹果将其设定为默认设置也不足为奇了——前提是 iOS 13 能清楚地掌握用户的使用习惯。  
  
在此之外，其实 iPhone 内部做有充分设计来保护电池健康，所以正常使用的情况下无需刻意做太多。不过，这里有一些其他的建议，可能会帮助你的 iPhone 电池尽可能长时间地保持最佳状态。  
  
1. 避免温度过高：例如，在温度很高的车内给手机充电是个坏主意。2. 尽量不要让你的电池完全放电：如果可能的话，将其保持在 20% 电量左右，有助于延长寿命。如果你打算让你的手机闲置一个星期或更长时间，最好将电池用完，然后完全关机。3. 不要让电池一直处在充电状态，即使你开启了电池充电优化功能。

本文著作权归
@Ruins0080
所有，经授权发布，不代表威锋立场。
  
如需转载请联系 hezuo@office.feng.com

---

[🌐 原始链接](https://www.feng.com/post/12808565)

[📎 在印象笔记中打开](evernote:///view/207087/s1/de0deebb-8bb2-41d3-9e77-f32632c5ac9d/de0deebb-8bb2-41d3-9e77-f32632c5ac9d/)