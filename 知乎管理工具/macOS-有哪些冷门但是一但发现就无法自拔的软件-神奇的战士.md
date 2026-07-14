---
title: "macOS 有哪些冷门但是一但发现就无法自拔的软件？"
author: 神奇的战士
source: zhihu
date: 2026-07-14
url: https://www.zhihu.com/question/35050387/answer/645466357
type: zhihu-article
---

# macOS 有哪些冷门但是一但发现就无法自拔的软件？

> ✍️ 神奇的战士 · 📅 2026-07-14 · [原文](https://www.zhihu.com/question/35050387/answer/645466357)

---

让俺来推荐一个 MacOS 上用了就**完全无法自拔**的神器

**Hammerspoon**！

相较于其他 MacOS 上的效率工具，**它可以一个打十个**！

![](attachments/a78788cc6764d6c91db6cc0773410a7e.jpg)LogoHammerspoon 是 MacOS 上的自动化工具，许多介绍 Hammerspoon 的文章都主要介绍了它是一个窗口管理工具，但是 Hammerspoon 能做到的远远不仅如此。

Hammerspoon 开源、免费和支持插件，将大多数系统层面的接口封装成了 Lua API，这就让**这把小锤子在 MacOS 上近乎无所不能，可玩性极高**。

## 俺都用 Hammerspoon 做了些什么？
- **菜单栏显示最近几天天气情况**
- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/blob/master/weather/weather.lua)
- 请求免费的天气 API，在深圳这个多雨的城市里提醒我别忘记带伞。

显示天气- **剪切板历史记录**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/clipboard)
- 记录剪贴板历史，点击某一项再重新复制。
显示剪切板记录

- **音量调节快捷键**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/volume)
- 当我使用外接键盘时，自定义快捷键 cmd + up/down 调节系统音量

快捷键调节音量

- **窗口管理**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/window)
- 快捷键实现二分屏、三分屏和全屏
快速窗口分屏

- **Wi-Fi 自动脚本**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/wifi)
- 根据 Wi-Fi SSID 判断是否在公司还是在家，例如在家里自动挂载 NAS 服务器，如果在公司 sshfs 挂载服务器目录等。
![](attachments/8d8ece6fb1deb1f10368ac0f4513bb0d.jpg)检测 Wi-Fi 连接

- **蓝牙耳机自动连接**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/headphone)
- 电脑锁屏时，自动断开连接的蓝牙耳机，参考我的[另一篇介绍](https://zhuanlan.zhihu.com/p/59737941)。

- **输入法自动切换**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/ime)
- 在每个 App 界面自动切换成搜狗输入法，配合搜狗输入法自动中英文切换，再也不用在系统默认的英文输入法和搜狗输入法之间来回切换了。

- **定时自动提交代码**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/autoscript)
- 使用 hs.timer 定时器，定时启动脚本推送我的笔记、代码和收藏的电子书到 Github 仓库。

- **USB 设备连接记录**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/usb)
- 记录插上你电脑的每一个 USB 设备信息，凡插过必留痕迹。

- **消息推送**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/speaker)
- 推送任意消息提醒

- **TTS 发声**

- [参考示例](https://link.zhihu.com/?target=https%3A//github.com/wangshub/hammerspoon-config/tree/master/speaker)
- 调用 say hello world 合成 TTS，模拟真人发音，让 Mac 会说话。

- **更多... (完全停不下来啊)**

## 其他插件思路
- **番茄钟**
- **应用搜索**
- **桌面小部件**
- ...

## 快速使用入门
Hammerspoon 已经将与 MacOS 之间的系统交互封装成了 **Lua 的 API**，配置 ~/.hammerspoon/init.lua 脚本可以与系统进行交互，只需要了解一些基本的 Lua 语法，就可以 **Happy Hacking** 了，请查阅:

- [Lua 快速入门教程](https://link.zhihu.com/?target=https%3A//learnxinyminutes.com/docs/lua/)
- [Hammerspoon API 文档](https://link.zhihu.com/?target=https%3A//www.hammerspoon.org/go/)
如果你也像我一样第一次使用 Lua 代码，相信我入门会十分简单，而且 Hammerspoon 很值得一试。

## 我的参考配置
如果你懒得配置，可以参考我的配置，再根据自己的习惯修改，安装方法请见链接:

![](attachments/19b797b6a4ca63231d09597ad53c2443.jpg)init.lua

## 最后
已经完全停不下来了，Hammerspoon 每天至少为我省下了 30 分钟的时间。  ⏱