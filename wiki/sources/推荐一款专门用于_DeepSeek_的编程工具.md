---
title: 推荐一款专门用于 DeepSeek 的编程工具
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/推荐一款专门用于 DeepSeek 的编程工具.html
tags: [网文推荐, AI技术, 教育]
---

# 推荐一款专门用于 DeepSeek 的编程工具

点击上方🔺公众号🔺关注我✅觉得不错，可以星标

你好啊，我是雨飞，见字如面。感谢阅读，期待我们下一次的相遇。

最近体验了一个不错的 AI 编程工具，专门为 DeepSeek 模型打造，从实际效果来说，体验不输 CC。接下来分享下这款开源项目。

本项目名为：DeepSeek TUI，专门为 DeepSeek V4 系列模型定制的编程智能体，可用于代码开发、执行 Shell 脚本、调用 MCP、Skills，并提供了沙箱环境保证代码安全。目前 github start 数量已经超过 30k，还在持续增长中。

安装也非常简单，第一种是使用 NPM 或者 cargo 安装，

npm install -g deepseek-tui
# 2. Cargo —— 无需 Node。
cargo install deepseek-tui-cli --locked   # `deepseek` 入口
cargo install deepseek-tui     --locked   # `deepseek-tui` TUI 二进制

第二种则是手动下载，地址：https://github.com/Hmbown/DeepSeek-TUI/releases

在上面的目录下，将 Dispatcher 以及 TUI 都下载下来，然后放置到本地目录下并配置环境变量。

Windows 参考地址：C:\Users\{你的用户名}\.local\bin

安装完成后，使用 deepseek 命令即可启动 TUI，根据步骤配置好 DeepSeek 的 API key 就可以使用了。

输入小键盘数字可以选择，默认情况下会自动检测语言，按回车键继续后面的步骤。

输入 DeepSeek 的 API key，然后继续。

成功配置完成后，可以看到如下的页面，就可以开始编程了。

该工具提供了 plan、agent、yolo 三种不同的模式，点击 Tab 键就可以切换不同的模式。

输入 / 则可以看到所有的快捷命令，还有不少汉语拼音特色的命令，更适配国人使用了。

另外，该项目还贴心的给大家展示了整个项目的架构和一些开发思路，有希望自己开发或者迭代编程工具的可供参考、学习。

地址：https://github.com/Hmbown/DeepSeek-TUI/

最后，AI编程、OpenClaw 交流群现在已经有很多空位，加我微信，私聊暗号：小龙虾，入群。#AI编程 #OpenClaw

来，这是雨飞的介绍（第9版，交个朋友，限时送福利）

2、更多AI编程、小龙虾 OpenClaw、副业相关知识，不定时福利，扫码加入 6300+ 人的免费星球

我是雨飞，AI算法工程师，职场努力升职，业余时间探索副业，寻找第二曲线，聚焦 AI 编程、智能体方向副业变现。
