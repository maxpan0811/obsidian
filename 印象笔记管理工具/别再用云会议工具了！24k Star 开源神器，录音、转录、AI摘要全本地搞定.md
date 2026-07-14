# 别再用云会议工具了！24k Star 开源神器，录音、转录、AI摘要全本地搞定

---

大家好，我是小黑，今天我们聊聊最近有点火的 Meetily，目前在 GitHub 24k Star，这个是 Zackriya Solutions 开源的 AI 会议助手，MIT 协议。

[🔗 原文链接](https://mp.weixin.qq.com/s/GldHdr7OJAmY2ZerVNPOrg)

它干的事很简单：录你电脑上的声音，本地转成文字，再用 AI 出摘要，所有东西都存在你自己机器上，不需要同意什么乱七八糟的隐私政策，数据不会跑到别人的服务器。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/4242062D-2877-4EC7-B0D4-AB810E9C3E15)

简介

Meetily 是一个桌面端应用，macOS 和 Windows 有安装包，Linux 需要源码编译。它直接抓取系统音频和麦克风，本地完成转录和摘要，转录引擎用 Whisper.cpp 或 NVIDIA Parakeet，摘要接 Ollama 本地模型。数据存在本地 SQLite，向量检索用 VectorDB。

市面上类似的工具不少，Otter.ai、Fireflies、Granola 都是成熟的 SaaS。但它们的共同点是：你的声音、会议内容、客户信息，全部要经过第三方服务器。Meetily 的区别就在这里，它把整条链路放在本地。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/F7F08B63-E431-4F91-9B7F-6FA45C342BFA)

功能详情

本地录音，不混进会议

Meetily 不会以机器人的身份加入你的 Zoom、Teams 或 Google Meet，它直接录你电脑的系统声音，混音后本地处理。IT 部门不会看到「未授权机器人加入会议」的提示，也不会因为平台限制机器人导致断线，线下面对面讨论也能录，因为它抓的是系统音频，不是会议流。

音频处理做了降噪、防削波、音量平衡，录出来的东西能听清，不是一团糊。

双引擎转录：Whisper 和 Parakeet

转录支持两个引擎，OpenAI Whisper 生态成熟，语种覆盖广，准确率稳定。NVIDIA Parakeet 速度快，官方说比 Whisper 快 4 倍，适合对速度有要求的场景。两个引擎都在本地跑，不需要联网，断网也能转。

转录结果实时显示在界面上，带时间戳，开会过程中瞄一眼，就能确认刚才那句话识别得对不对。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/96C8E646-5C8E-4D86-B03F-65ADA58F0FE9)

六种摘要模板

会议结束后，Meetily 把 transcript 丢给 LLM 生成结构化摘要。内置六种模板：议程、决策、行动项、关键讨论、会议纪要、自定义。我们可以选模板，也可以自己写 prompt 调格式。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/E31A9086-14F9-4478-864F-C31E505CBA5A)

模型选择很宽，Ollama 完全离线，适合隐私要求高的场景；Claude、Groq、OpenRouter、OpenAI 接 API，适合追求效果的情况。还有自定义 OpenAI-compatible 端点，公司内部有模型网关的可以直接接。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/67E29435-323B-49A0-B78C-6DC980595983)

导入旧录音重新处理

Meetily 支持导入已有的音频文件，重新生成 transcript 和摘要。我之前用 QuickTime 录了一堆旧会议，导入后换了个更大的 Whisper 模型重新跑，准确率比当初高了不少。语言也能切换，同一段录音用不同语种模型试，看哪个效果好。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/D3AF4383-2E61-4C25-85E4-454ABA9AF3B2)

本地数据库和语义搜索

所有 transcript、摘要、元数据都存在本地 SQLite。VectorDB 做语义搜索，我们直接搜「上周关于预算的讨论」，不用翻文件名。数据主权完全在自己手里，换电脑时把数据库文件拷走就行。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/061A6D5E-C8FC-4D09-B702-0F20F6EA676C)

跨平台与版本

macOS 和 Windows 有原生安装包，下载双击即用。Linux 目前需要源码构建或 Docker 部署。社区版免费，Pro 版 10 美元/月/用户，多了高精度转录、高级导出、自动会议检测、团队功能。企业版支持私有化部署，走 AWS、Azure、GCP 或本地机房。

快速开始

安装包安装（macOS / Windows）

去 GitHub Releases 下载对应系统的安装包：

* • macOS：.dmg 文件，拖到 Applications 里
* • Windows：.exe 安装程序，一路下一步

首次启动会引导下载转录引擎和摘要引擎的模型文件，几百 MB 到几个 GB，取决于你选的模型大小，下完点 Continue 就能用。

界面很干净，左侧会议列表，中间实时 transcript，右侧摘要面板。底部红色按钮开始录音，自动捕获系统音频和麦克风。会议结束点停止，选模板生成摘要，导出 Markdown。

![](.evernote-content/CD7394F7-5132-4BC7-A5C5-AFE6BCFA631A/47BAA71B-5AFB-4F8B-9861-9840C4F86617)

如果想用本地 Ollama，先装好 Ollama 并拉一个模型，比如 llama3，然后在 Meetily 设置里把摘要引擎切到 Ollama，填模型名，Claude 或 OpenAI 就填 API Key。

源码构建（Linux / 开发者）

Linux 目前没有现成安装包，需要源码构建，环境要求：Rust、Node.js 18+、pnpm。

# 克隆仓库

git clone https://github.com/Zackriya-Solutions/meetily.git

cd meetily

# 安装前端依赖并构建

cd frontend

pnpm install

pnpm build

# 回到根目录，构建 Tauri 应用

cd ..

pnpm tauri build

构建完成后，在 src-tauri/target/release/ 目录下找到可执行文件，具体依赖和构建细节看 README，不同 Linux 发行版可能需要额外装系统库。

我的看法

我用了几天，说实话，Meetily 的体验不如 Otter.ai 顺滑。转录准确率有差距，尤其是多人说话重叠的时候，另外日历集成、Obsidian 插件、移动应用，这些也都没发布。功能完整度上，它确实打不过付费 SaaS。

但是它免费、不需要联网。线下会议，会涉及一些敏感数据用 Meetily 非常合适，尤其是金融、银行行业等行业，如果你用联网的 SaaS 做自动化会议纪要，大概率是会被K的。

技术选型我也挺喜欢，Rust 做音频捕获和转录，性能够硬；Tauri 比 Electron 轻太多；Next.js 前端响应快。整个架构模块化，开发者想改哪里 fork 就行，MIT 协议，商用、二次开发、闭源修改，全不限制。

如果你只是偶尔开开会，Otter.ai 免费版够用了。但如果你处理敏感信息，或者在合规要求严格的行业，Meetily 是目前少有的能真正落地的开源方案。

GitHub地址：

https://github.com/Zackriya-Solutions/meetily

[📎 在印象笔记中打开](evernote:///view/207087/s1/228cdf94-c6b7-47c8-a77a-839690f46301/228cdf94-c6b7-47c8-a77a-839690f46301/)