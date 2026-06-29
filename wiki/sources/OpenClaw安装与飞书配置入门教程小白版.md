---
title: OpenClaw 安装与飞书配置入门教程（小白版）
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/OpenClaw 安装与飞书配置入门教程（小白版）.html
tags: [印象笔记, 其他]
updated: 2026-06-27
---

---
title: "OpenClaw 安装与飞书配置入门教程（小白版）"
source: evernote
type: note
export_date: 2026-06-26
guid: 1a239173-d384-477d-adf7-feded2f21d86
---

# OpenClaw 安装与飞书配置入门教程（小白版）

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5OTQ0MjU2Mw==&mid=265169...](https://mp.weixin.qq.com/s?__biz=MjM5OTQ0MjU2Mw==&mid=2651699615&idx=1&sn=8d5a3ebf2fabd6a5d9a59ab315051b2f&chksm=bd8bb6a9492e0aa1b5e0f438b2d4ed6c8718e0be4987562d3d38d7ec91c453e610f1d471feb3&mpshare=1&scene=24&srcid=0308JSBs0WS9uE9XAcsHJiha&sharer_shareinfo=00ecb6c2e6564d4ca0f4036eff0d261d&sharer_shareinfo_first=00ecb6c2e6564d4ca0f4036eff0d261d&clicktime=1773139974&enterid=1773139974&ascene=14&devicetype=iOS26.3.1&version=1800452e&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQEIhAP6Y39k441N022f7d5xLVAQIE97dBBAEAAAAAAI6/OWcOOZAAAAAOpnltbLcz9gKNyK89dVj0CnpRitRoDvv8lmjwsGjc6aPVCJ4nCn0mxTBY/U5B3MHoCP7DjF5NohJuHDyxOTPparMZXYlW7u/G//QTiMjaphh8VKR6iacY6hIkfuI3W/XbvSZh6xOhnid73OaW/os73bNy5odqm+8jkkk/VjwpvcSB+BMHzwcNg6yvEYGeJHGo9NffVANaLXpfIH5+2TMmuyOn1ikoQmi+LW1+v2gVHwByhNxuodkyProjptbMmg==&pass_ticket=G8Cy3ITLWdMnWnCUUVEzl6/1h3w4dQG5v4DIrKiQ0DoMLE6awMibF+djuE5YB6rU&wx_header=3)

# OpenClaw 安装与飞书配置入门教程（小白版）

OriginalKane 独立AI空间

![](attachments/e0ea56796ba1a8f0.png)

本教程适合完全没有接触过 OpenClaw 的新手，手把手带你完成安装和飞书接入，全程约 30 分钟。

---

## 一、OpenClaw 是什么？

OpenClaw 是一个 AI 智能体框架，能让你的 AI 模型（比如 GPT、Qwen、MiniMax 等）通过飞书、Telegram、Slack 等聊天工具直接与你对话，帮你自动完成各种任务。

**你能用它做什么？**

- • 在飞书里直接和 AI 聊天、下达任务
- • 让 AI 帮你自动处理文件、回复消息、执行代码
- • 通过手机随时随地调用 AI 能力

---

## 二、开始之前：准备好这三样东西

在安装 OpenClaw 之前，你需要先准备好以下环境。如果已经有了可以直接跳过对应步骤。

![](attachments/506046a81556183b.png)

### ✅ 第一步：安装 Node.js（v22 或更高版本）

Node.js 是运行 OpenClaw 必须的基础环境，就像手机 App 需要操作系统一样。

1. 打开官网：https://nodejs.org/zh-cn/download
2. 下载对应你系统的安装包（Windows / macOS / Linux）
3. 一路点击"下一步"完成安装

**验证是否安装成功：**

打开终端（macOS/Linux）或命令提示符（Windows），输入：

node -v

如果看到类似 `v22.x.x` 的版本号，说明安装成功了。

---

### ✅ 第二步：安装 Git

Git 是用来下载代码的工具，OpenClaw 的部分插件安装需要它。

- • 官方安装指南：https://git-scm.com/book/zh/v2/起步-安装-Git

**验证是否安装成功：**

git --version

看到版本号即为成功。

---

### ✅ 第三步：准备一个 AI 模型的 API Key

OpenClaw 需要连接一个 AI 模型才能工作。你需要至少一个 AI 服务商的 API Key（相当于"通行证"）。

**推荐新手使用以下任一平台（按需选择）：**

| 平台 | 特点 | 地址 |
| --- | --- | --- |
| **MiniMax** | 国产模型，新客有优惠 | platform.minimaxi.com |
| **阿里云百炼** | Qwen 系列，新客首月 7.9 元 | 阿里云 AI 优惠 |
| OpenAI / Anthropic | 需要国际支付方式 | 官网注册 |

💡 **建议新手选择 MiniMax 或阿里云百炼**，有中文支持且价格友好。注册后在控制台创建一个 API Key 并复制保存好。

---

## 三、安装 OpenClaw

![](attachments/db76f6aa80b81102.png)

准备工作完成后，开始正式安装。

**OpenClaw 官网：** https://openclaw.ai/

### macOS / Linux 用户

打开终端，复制粘贴以下命令并回车：

curl -fsSL https://openclaw.ai/install.sh | bash

### Windows 用户

以**管理员身份**打开 PowerShell（右键菜单选择"以管理员身份运行"），输入：

iwr -useb https://openclaw.ai/install.ps1 | iex

⚠️ **注意**：Windows 上必须用管理员权限运行，否则会安装失败。

安装过程中会有交互界面，操作方式：

- • **上下方向键**：移动选项
- • **回车**：确认选择
- • **空格**：勾选/取消选中

---

## 四、初始化配置（新手引导）

安装完成后，运行新手引导命令：

openclaw onboard

这个命令会一步步引导你完成基础配置，按提示操作即可：

1. **是否启动 QuickStart 向导？** → 选 `Yes`
2. **选择 AI 模型提供商** → 根据你准备的 API Key 选择对应平台（如 MiniMax、Qwen 等）

- • 选择后会自动跳转到对应平台的授权页面
- • 登录并获取 API Key，粘贴进去

3. **点击浏览器中的 "Confirm" 按钮** 完成 OAuth 授权
4. **配置通信渠道**（飞书 / Telegram / Slack）→ 可以先选 `Skip for now` 跳过，后面再配

---

## 五、健康检查（必做！）

安装完成后，**一定要运行这个命令**检查是否一切正常：

openclaw doctor

这个命令会帮你检查环境依赖、配置是否正确，并给出安全提醒。如果有报错，按照提示修复即可。

---

## 六、配置飞书（让 AI 在飞书里和你聊天）

这一部分稍微复杂一点，但按照步骤来不会出错。整体流程如下：

![](attachments/8c6b5b3fa148fe88.png)

### 第一步：在飞书开放平台创建应用

1. 打开飞书开放平台：https://open.feishu.cn/app
2. 登录你的飞书账号
3. 点击\*\*"创建企业自建应用"\*\*，填写应用名称（随便起，比如"我的AI助手"）

![](attachments/a14b1edc36d0b042.png)

### 第二步：添加机器人能力

1. 进入刚创建的应用
2. 在左侧菜单找到\*\*"机器人"**，点击**"添加"\*\*

![](attachments/f581311e47fd6e9a.png)

### 第三步：配置权限

1. 在左侧菜单点击\*\*"权限管理"\*\*
2. 开启机器人需要的权限（主要是消息相关权限）

![](attachments/f89de5f350ecbaac.png)![](attachments/709798dd1a3a03bf.png)

📌 详细权限配置说明可参考官方文档：GitHub - m1heng/clawdbot-feishu

### 第四步：安装飞书插件

回到终端，运行以下命令安装飞书插件：

openclaw plugins install @m1heng-clawd/feishu

![](attachments/f255087573d59c8e.png)

安装过程中会提示你输入飞书应用的 **App ID** 和 **App Secret**（在飞书开放平台应用的"凭证与基础信息"页面可以找到）。

### 第五步：配置事件与回调

1. 在飞书开放平台应用中，找到\*\*"事件与回调"\*\*菜单
2. 添加一个接收消息的事件（通常是 `im.message.receive_v1`）
3. 将插件安装时生成的回调 URL 填入

![](attachments/8e6a7f513eef572a.png)

### 第六步：完成配对授权

1. 在你的**手机飞书**上，找到刚创建的机器人，给它发一条消息
2. 机器人会回复一条包含授权码的消息（类似 `WLCZVUDA` 这样的代码）
3. 回到电脑终端，运行以下命令（把 `WLCZVUDA` 替换成你收到的实际授权码）：

openclaw pairing approve feishu WLCZVUDA

![](attachments/7a7d93d3b7c1d7c9.png)

1. 看到成功提示即完成配对！

---

## 七、开始使用

配置完成后，在飞书客户端里：

1. 打开**工作台**
2. 找到你创建的机器人
3. 直接发消息就可以和 AI 聊天了！

![](attachments/ad31cd2cddfc8497.png)

---

## 八、常用命令速查表

日常使用中可能用到的命令，遇到问题时参考：

| 命令 | 作用 |
| --- | --- |
| `openclaw doctor` | 健康检查（遇到问题先跑这个） |
| `openclaw status` | 查看运行状态 |
| `openclaw gateway status` | 查看网关状态 |
| `openclaw dashboard` | 打开浏览器控制面板 |
| `openclaw gateway start` | 启动后台服务 |
| `openclaw gateway stop` | 停止后台服务 |
| `openclaw channels add` | 添加新的社交平台 |
| `openclaw logs` | 查看实时日志（排查报错必看） |
| `openclaw skills list` | 列出已安装的技能 |

---

## 九、遇到问题怎么办？

1. **先运行** `openclaw doctor` 检查环境
2. **查看日志** `openclaw logs` 找具体报错信息
3. **参考官方文档**：https://openclaw.ai/
4. **飞书插件文档**：https://github.com/m1heng/clawdbot-feishu

---

## 十、卸载方法（不想用了）

如果需要彻底卸载 OpenClaw，依次运行以下两条命令：

openclaw uninstall --all --yes
npm uninstall -g openclaw

---

## 总结

整个流程回顾：

安装 Node.js + Git
    ↓
准备 AI API Key
    ↓
安装 OpenClaw（一条命令）
    ↓
运行 openclaw onboard 完成初始化
    ↓
运行 openclaw doctor 健康检查
    ↓
飞书开放平台创建应用
    ↓
安装飞书插件并完成配对
    ↓
在飞书工作台找到机器人开始聊天 🎉

到这里，你已经完成了 OpenClaw 的全部安装和飞书配置。有任何问题，优先通过 `openclaw doctor` 和 `openclaw logs` 排查。祝使用顺利！
