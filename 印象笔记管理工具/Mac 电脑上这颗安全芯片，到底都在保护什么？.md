# Mac 电脑上这颗安全芯片，到底都在保护什么？

---

Mac 电脑上这颗安全芯片，到底都在保护什么？
=======================

[产品](https://www.ifanr.com/category/product)

14 小时前

0

评论

对苹果来说，自研芯片已经成为了一种寻求产品差异化的手段， 这不仅在 iPhone 上有所体现，你在 Mac 电脑、Apple Watch 手表和 AirPods 耳机中都能找到苹果芯片的身影。

从 2016 年起，苹果开始为新 MacBook 加入名为「T1」的自研芯片，当时主要是为了驱动 TouchBar 触控条的运行，同时也负责指纹识别的安全管理。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/6DEB62C6-FB60-4DF6-B716-113C2F7B4B63.jpg)

到了 2017 年，苹果在发布 iMac Pro 的同时也带来了新的 T2 芯片。

表面上看，苹果仍然把 T2 定义为一颗「[安全芯片](https://support.apple.com/zh-cn/HT208862)」，但这个「安全」具体包含哪些部分，我们在日常使用时往往很难感知得到。

最近，[Appleinsider](https://appleinsider.com/articles/19/07/29/what-apples-t2-chip-does-in-your-new-macbook-air-or-macbook-pro) 便为我们归纳整理了苹果 T2 芯片的使用场景和细节，他们认为在安全之外，T2 实则还掌管着 Mac 电脑中很多关键元器件的「使用权」。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/06680158-0009-4FAF-B116-E2C51B444CD9.jpg)

[根据苹果官方文档的介绍](https://www.apple.com/mac/docs/Apple_T2_Security_Chip_Overview.pdf)，凡是配备了 T2 芯片的 Mac 电脑，都可以在开机时启用「[安全启动](https://support.apple.com/zh-cn/HT208330)」功能。这个功能主要是确保 Mac「始终从合法、经过认证的系统中启动」，以防止恶意软件从系统最底层进行篡改。

这不仅包括苹果自家的 macOS 系统，也包含了从 BootCamp 安装的 Windows 系统，当然用户可以自由选择是打开还是关闭。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/1105A90B-8474-413E-B9FC-0F7D0984608A.png)

数据保护还涉及到硬件层面。T2 芯片内置了专用的 AES 加密引擎，主要用来保护 SSD 硬盘上的数据。就算你直接把硬盘拆下来插到另一台 Mac 上也不可用，因为当你一旦启用这块硬盘，机器内的 T2 芯片就已经和它牢牢绑定了。

此外，由于它是通过硬件层面实现的，所以也不会影响到硬盘本身的读写性能。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/BD08B4BE-C627-42E8-87FC-330737C537AD.jpg)

▲ 图片来自：[Wired](https://www.wired.com/story/apple-t2-security-chip-macbook-microphone/)

而在 Touch ID 方面，和以前的 T1 一致，T2 同样会负责将用户的指纹数据存储在本地，并交由一个名为「Secure Enclave」的独立区域进行管理。

据悉，这种经由 T2 存储的指纹数据，并非是指具体的图像，而是一种加密数字形式。

同时，这个区域不能被任何系统和软件所读取访问，只有当用户使用指纹识别验证时，T2 才会启用「Secure Enclave」区域进行匹配操作。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/DC10B6FE-80BD-4759-93E8-7D62180777D3.jpg)

Mac 电脑上的摄像头、麦克风等元件，如今也都归 T2 芯片管理。在过去，一些软件可能会尝试偷偷唤醒摄像头、麦克风元件，收集用户的隐私数据，就算是我们合上笔记本电脑后，也可能存在麦克风被调用然后被监听的情况。

而 T2 芯片所做的，就是借助内置的音频、图像控制器，直接从硬件层面断开软件与硬件之间的联系。

此时它类似于扮演一个中间人的角色，如果有软件想要获得硬件访问权限，就必须先获得 T2 芯片的许可。

同时，T2 芯片中这些控制器不仅用于安全防范，也会协助硬件实现更好的功能。比如说图像处理器就会在 Facetime 视频中优化曝光和白平衡；音频管理器则会全天候监测当前环境中「嘿，Siri」的语音指令，在不影响续航的情况下及时做出响应。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/30DE255B-7E44-43CB-BF3C-6E208CAD9000.jpg)

▲ 图片来自：[Appleinsider](https://appleinsider.com/articles/19/04/09/apples-t2-chip-makes-a-giant-difference-in-video-encoding-for-most-users)

最后一项改进和视频转换有关。[Appleinsider](https://appleinsider.com/articles/19/04/09/apples-t2-chip-makes-a-giant-difference-in-video-encoding-for-most-users) 在使用 Handbrake 这款开源视频转码软件时发现，在都使用英特尔 i3 处理器、相同转速硬盘的情况下，集成了 T2 芯片的 2018 款 Mac mini，会比没有 T2 芯片的 2019 款 4K iMac 获得更快的视频转码速度，这在随后的多款设备测试中也得到了验证。

这么来看的话，T2 芯片在目前 Mac 电脑中的地位，并不比 CPU/GPU 要低；如果从管理权限角度说，它甚至算得上是更核心的存在。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/7451BD84-A1D5-4257-B765-89E8515A2B2A.jpg)

这种芯片级硬件的加入，也让部分用户和维修商感到头疼。[MacRumors](https://www.macrumors.com/2018/10/04/t2-macs-must-pass-diagnostics-for-certain-repairs/) 在 2018 年曾报道称，由于 T2 芯片对 Mac 电脑硬件的掌控，如果用户或第三方官方维修商使用了未经官方验证的配件，或是私自进行拆修，会无法通过 T2 芯片的维修检测，之后系统也会自动锁定电脑。

从苹果的角度看，它可能希望借助 T2 芯片进一步把控售后维修的利益链，但对部分身处偏远地区，附近没有苹果官方维修点的用户来说，限制第三方维修只会给带来更多麻烦，也有损消费者的自主权益。

![](.evernote-content/06452F05-635E-4596-91E9-35A61D3EE9DA/1DA9F07C-0A86-4BA4-ABB0-6785C756F9DA.jpg)

不过，T 系列芯片仍然很重要，它意味着苹果已经开始在个人电脑设备中推行和智能手机一样的协处理器设计，这就和当年 NVIDIA 推行 GPU 概念一样，目的都是将某些特定场景下的任务需求，交给专用的芯片来执行，以减轻 CPU 的负担。

至于它的最终形态出炉之日，大概就是苹果推出自己的 Mac 电脑主处理器之时了。

题图来源：[Wired](https://www.wired.com/story/apple-t2-security-chip-macbook-microphone/)

Measure

Measure

---

[🌐 原始链接](https://www.ifanr.com/1241874?utm_source=rss&utm_medium=rss&utm_campaign=)

[📎 在印象笔记中打开](evernote:///view/207087/s1/45abb236-0ea0-432a-9759-d6e5e51b4679/45abb236-0ea0-432a-9759-d6e5e51b4679/)