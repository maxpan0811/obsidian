---
title: "18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！.md
tags: [印象笔记]
---

# 18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！

# 18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！ --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2MTI4MjI

---

# 18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2MTI4MjI0MQ==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247544674&idx=1&sn=bdc8ea0e468ea7b29551b1375e3ff430&chksm=fdd0a74bc68260fd4352a00d7e5ab08a37c287d49f2a63a920d775f3350eac13982fd070e263&scene=90&xtrack=1&req_id=1783854116571164&sessionid=1783853967&subscene=93&clicktime=1783854202&enterid=1783854202&flutter_pos=40&biz_enter_id=4&ranksessionid=1783854116&jumppath=WAWebViewController_1783854149864,WAWebViewController_1783854150352,20020_1783854159458,1104_1783854160191&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b3a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSKp88T6mk1d2sjdR/CktwRLTAQIE97dBBAEAAAAAAArOGlCPCEwAAAAOpnltbLcz9gKNyK89dVj0yMBHUcJvU92uUIr4iNCSzwZ5xv6WMQhoFIH6n2TzY0hAhhBcAn26iC3yL3/RvzQmSo9IBbXi9mBUgBkDj/G9KopKUyrquV6UXaq1mjP6V5cgBLNJnJjjiyDZmgBolTbV/YnAnB+A1UclNnpcQynWDRmhEetZTfTfw1zBh3GVNW/vK/zBRUFFUjDVN+PcvzwbLRHDATnm/Q9fneqgyez1unHulSDY4iun5LFjTso=&pass_ticket=/Y6KazY8DwSj5+WuY8EXB8YCEzPSKiKJWkrB6OHMn1+2gGUsbqq3OS6MlJ9NjSkU&wx_header=3)

18k+ Star 暴涨！一款开源的匿名聊天软件，把手机号、账号、ID 全砍了！
========================================

Original小黑极客之家

刷 GitHub Trending 的时候看到这个项目，SimpleX Chat，Star 从 8k 飙到 18k+，日增一千多。我点进去看了眼，发现它连手机号、用户名、邮箱、公钥，甚至随机 ID 都不要，它自称是世界上第一个完全没有用户标识符的即时通讯平台。

说实话，我第一反应是：这能行吗？

创始人 Evgeny Poberezkin 2021 年在伦敦搞的这个项目，底层用 Haskell 写核心协议。Haskell 写协议，这门槛够高的，客户端覆盖 iOS、Android、Linux、macOS、Windows，AGPL v3 开源。

背书挺硬的，我对这个实现比较好奇，研究了一下。

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/A7D67902-A475-44CF-8298-CC684B6789C5.png)

这个项目连ID都不要
==========

Signal 要手机号，Telegram 要用户名，Matrix 要服务器地址，SimpleX Chat 把这些全砍了。

它的思路是单向消息队列，每个联系人对应一组独立的队列地址。消息从发送方队列出去，经过中继服务器，进入接收方队列。服务器只负责临时存储和转发，消息送达后立即删除，服务器都不知道谁在通信，因为入站和出站消息之间没有任何共同标识符。

每个联系人配的是专属通道，通道地址只用来收信，不暴露身份。

功能特性
====

### 加好友只能走一次性链接

没有用户名，搜索功能自然不存在，加联系人只能走一次性邀请链接或二维码。

我们打开 App，生成邀请链接，发给对方。对方点击后，双方建立连接，这个链接只能用一次，过期作废。当面不方便的话，可以视频通话时让对方扫码。

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/FFE3BD00-0523-4BB3-8357-5601121DDBC3.png)

这种设计把人际关系网的暴露面压到最小，没有中央服务器存好友关系，没有可搜索的用户目录，联系人列表只存在本地。

聊天界面看起来和常规 IM 差不多。文字、图片、文件、语音消息、视频通话都支持，群聊和频道功能也有，v6.5 版本还上线了公开频道。

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/6C6B4C5F-1EF0-41F4-930C-66F382CFA04A.png)

群聊

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/E5EFB130-C470-473F-A47C-B127774B83B1.png)

视频通话

### 双层加密，安全性很高

SimpleX 的加密分两层：

1. 1. 双棘轮算法，基于 Signal 协议改进。X3DH 密钥协商加上临时 Curve448 密钥，提供前向保密。每条消息使用独立的消息密钥，历史密钥泄露不影响后续通信。
2. 2. 队列加密。每条 SMP 队列消息额外用 NaCl crypto\_box 加密，基于 Curve25519 + Salsa20 + Poly1305，传输层再走 TLS 1.3。

服务器持有 Ed448 签名密钥，用于授权 SMP 命令，但服务器解不开消息内容，也关联不了通信双方。

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/92991AA5-A4BC-4CAA-9403-DBBE6E0E4482.png)

### 元数据保护这块够狠的

说实话，元数据保护这块把我惊到了。

所有消息填充到固定 16KB 大小。我们发一个"好"字还是一份 PDF，网络流量看起来一样，这防止了消息大小分析攻击。

发送方 IP 只对第一跳中继可见，接收方 IP 只对第二跳可见，两跳洋葱路由隐藏了双方的传输层身份。

没有共同标识符，没有全局命名空间，服务器之间不互联。即使有人攻破某个中继服务器，也拼不出完整的通信图谱。

### MITM防护做成默认

Signal 的安全码验证是可选的，很多用户嫌麻烦，直接跳过。

SimpleX 把这个步骤嵌入连接流程，变成非可选的强制步骤，密钥指纹直接嵌在邀请链接里。我们点击链接建立连接时，MITM 防护已经生效，用户无法跳过，也没有开关可以关闭。

这设计挺硬的，它假设用户会偷懒，所以直接把安全验证做成默认。

### 量子抗性加密

从 v5.6 开始，SimpleX 支持可选的量子抗性双棘轮算法。它用 Streamlined NTRU Prime（sntrup761）集成到双棘轮内部。

这里的技术细节挺有意思，传统 DH 是对称的，双方可以互相推导共享密钥。NTRU 是非对称 KEM，封装和解封装是单向的。SimpleX 的解决方案是双 KEM 并行：**每个棘轮步骤同时进行两个方向的密钥协商，再把结果混合到棘轮状态里。**

这保护了初始密钥交换，也保护了 break-in recovery 特性，后量子安全不是贴个补丁，而是重构了棘轮的核心逻辑。

### 去中心化架构

SimpleX 没有中央服务器，用户可以用官方预设的中继，也可以自己搭。服务器之间不通信，不共享状态，没有全网单一命名空间。

不存在网络级攻击面，无法像攻击 Telegram 服务器那样一锅端。用户随时切换服务器，不会丢失联系人和消息，没有 DNS 依赖，没有单点故障。

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/18882594-26E6-4402-913C-34A3A9B76148.png)

数据存哪里，自己选

这样的设计代价也有，消息走异步队列，延迟比中心化平台高。没有中央服务器存储数据，多设备同步变得复杂。目前同一个配置文件不能同时在多设备上在线，数据可以从手机导出到桌面端，但不能同时登录。

这些限制就是故意这么设计的，隐私和便利二选一，它选了隐私。

### 全平台覆盖

客户端已经覆盖主流平台，iOS 和 Android 有原生 App，桌面端支持 Linux、macOS、Windows，Linux 和 macOS 还可以用命令行版本。

装一个试试
=====

移动端最简单，iOS 去 App Store，Android 去 Google Play 或 F-Droid，直接下载安装。

桌面端可以用官方安装脚本：

```
curl -o- https://raw.githubusercontent.com/simplex-chat/simplex-chat/stable/install.sh | bash
```

或者从源码编译，需要 GHC 9.6.3 和 Cabal 3.10.1.0。Haskell 的工具链配置对新手不太友好，建议直接用安装脚本。

Docker 也可以：

```
DOCKER_BUILDKIT=1 docker build --output ~/.local/bin .
```

装完后，我们生成邀请链接，发给朋友，开始聊天，整个过程不需要注册账号、不需要输入手机号，同意什么隐私政策，任何有你个人标识的信息都不需要输入。

我的看法
====

SimpleX Chat 的隐私设计是我见过最激进的，它把"无标识符"这个理念执行到底，没有妥协。

但这种极端设计也有代价，添加联系人必须走带外通道，不能搜索用户名。换设备或丢失本地数据需要重新建立所有连接，多设备同时在线目前不支持，用户基数小，网络效应有限。

这个项目让我看清了一点：去中心化通讯完全可以没有全局用户 ID，这对隐私计算、去中心化身份等领域有很强的参考价值。它不适合日常闲聊，全部押注隐私的架构会牺牲很多功能体验上的便利，但对于需要强隐私保护的场景，这个项目算做到极致了。

---

**GitHub 仓库：**

> https://github.com/simplex-chat/simplex-chat

 

*****点击下方卡片，关注极客之家*****

这个公众号曾分享过许多有趣的开源项目。如果你不想逐篇翻阅历史文章，也可以直接关注微信公众号“极客之家”，通过后台留言与我们互动交流

![](.evernote-content/07DACF62-A27C-4261-A18C-A1363B04048A/554A0888-05AC-4122-9E48-6ABF807C65DF.jpg)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247544674&idx=1&sn=bdc8ea0e468ea7b29551b1375e3ff430&chksm=fdd0a74bc68260fd4352a00d7e5ab08a37c287d49f2a63a920d775f3350eac13982fd070e263&scene=90&xtrack=1&req_id=1783854116571164&sessionid=1783853967&subscene=93&clicktime=1783854202&enterid=1783854202&flutter_pos=40&biz_enter_id=4&ranksessionid=1783854116&jumppath=WAWebViewController_1783854149864,WAWebViewController_1783854150352,20020_1783854159458,1104_1783854160191&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b3a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSKp88T6mk1d2sjdR/CktwRLTAQIE97dBBAEAAAAAAArOGlCPCEwAAAAOpnltbLcz9gKNyK89dVj0yMBHUcJvU92uUIr4iNCSzwZ5xv6WMQhoFIH6n2TzY0hAhhBcAn26iC3yL3/RvzQmSo9IBbXi9mBUgBkDj/G9KopKUyrquV6UXaq1mjP6V5cgBLNJnJjjiyDZmgBolTbV/YnAnB+A1UclNnpcQynWDRmhEetZTfTfw1zBh3GVNW/vK/zBRUFFUjDVN+PcvzwbLRHDATnm/Q9fneqgyez1unHulSDY4iun5LFjTso=&pass_ticket=/Y6KazY8DwSj5+WuY8EXB8YCEzPSKiKJWkrB6OHMn1+2gGUsbqq3OS6MlJ9NjSkU&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b2b9ebc2-34fb-4db0-a86a-b254cd2d2de4/b2b9ebc2-34fb-4db0-a86a-b254cd2d2de4/)