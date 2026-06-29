---
title: "刚刚，Codex负责人官方发声：Codex原生支持其他模型！"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/刚刚，Codex负责人官方发声：Codex原生支持其他模型！.md
tags: [evernote, impression]
---
---
title: "刚刚，Codex负责人官方发声：Codex原生支持其他模型！"
source: evernote
type: note
export_date: 2026-06-22
guid: 83ace6a2-d878-4c97-a06c-5e53eaf76e80
---

# 刚刚，Codex负责人官方发声：Codex原生支持其他模型！

来源：[打开原文](https://mp.weixin.qq.com/s/-CTnFJWNARL_sSYitg1f_g)

Datawhale干货

作者：筱可，Datawhale成员

OpenAI 的 Codex CLI 是最近最好用的编程 Agent 之一，但默认连的是 OpenAI 自家模型。

就在刚刚，OpenAI Codex 负责人 Tibo 在 X 上首次官方强调：Codex App、CLI 和 SDK 可以搭配任何开源模型使用，不限于 OpenAI 模型。

![](attachments/31d03f56627c8ddb.png)

但这个方法有个前提：Codex 从 2026 年 2 月起强制使用 Responses API（wire\_api = "responses"），不再支持 Chat Completions。所以模型提供商的平台必须原生支持 OpenAI Responses API，Codex 才能直接对接。

阶跃星辰在这个月为平台上线了 Responses API 支持，并把 step-3.7-flash 作为首个接入 Codex 的模型。这篇文章直接教你把 step-3.7-flash 配进 Codex，再用它 review 一段代码。

一、前置准备：找到配置文件

Codex 的配置分两个文件，都在 ~/.codex/ 目录下（Windows 是 C:\Users\<用户名>\.codex\）：

~/.codex/  
├── config.toml    # 主配置：模型、提供商、功能开关  
└── auth.json      # 认证：API Key

## 二、保姆教程：三步接入模型

## 第 1 步：写入 API Key

把阶跃的 API Key 写入 auth.json。API Key 在阶跃星辰开放平台获取。

{  
  "OPENAI\_API\_KEY":"你的阶跃API Key"  
}

字段名仍然是 OPENAI\_API\_KEY，Codex 会通过 config.toml 里的 model\_provider 路由到阶跃。

## 第 2 步：配置 config.toml

model\_provider = "stepfun"  
model = "step-3.7-flash"  
model\_reasoning\_effort = "high"  
model\_context\_window = 256000  
model\_auto\_compact\_token\_limit = 200000  
model\_reasoning\_summary = "none"  
model\_supports\_reasoning\_summaries = false  
preferred\_auth\_method = "apikey"  
  
[model\_providers.stepfun]  
name = "StepFun"  
base\_url = "https://api.stepfun.com/v1"  
wire\_api = "responses"

几点注意：

• model\_reasoning\_effort只支持 low / medium/ high三档，不要写 xhigh。

• model\_reasoning\_summary 和 model\_supports\_reasoning\_summaries必须显式关掉，阶跃不支持 reasoning summary 参数，否则会报 Unsupported parameter 错误。

• base\_url 必须用标准 API 通道 https://api.stepfun.com/v1，阶跃的 Responses API 目前只支持这个通道。

• 不要加 env\_key = "OPENAI\_API\_KEY"，否则 Codex 会去找系统环境变量而不是 auth.json。

第 3 步：验证

codex exec"说一句话证明你能正常工作"

如果运行后 Codex 正常返回内容，且顶部信息里显示 model: step-3.7-flash、provider: stepfun，就说明接通了。

![](attachments/bf8ac4930dac9804.png)

如果 codex 命令找不到，说明 Codex 安装目录没进 PATH。Codex 桌面版装在 C:\Users\ke\AppData\Local\OpenAI\Codex\bin\，手动加进用户 PATH 后重开终端即可：

$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User')  
$codexPath = 'C:\Users\ke\AppData\Local\OpenAI\Codex\bin'  
[Environment]::SetEnvironmentVariable('Path', $currentPath + ';' + $codexPath, 'User')

## 三、实战案例：用 Codex review 代码

配置好之后，直接让 Codex 帮你 review 未提交的改动：

codex review --uncommitted

Codex 会读取当前仓库的 diff，用 step-3.7-flash 分析改动，给出 review 意见。如果你想针对某个具体文件，可以加上文件路径：

codex review --uncommitted src/utils.ts

或者用非交互模式快速拿到结果：

codex exec -o review.md "review 当前未提交的代码改动，列出潜在 bug、可读性问题和改进建议"

输出会写到 review.md 里，方便你之后逐条确认。

写在最后

把阶跃 step-3.7-flash 接入 Codex CLI，核心就三件事：确认平台支持 Responses API，config.toml 里配对 provider 和模型参数，auth.json 里填对 key。配置完成后，像 codex review --uncommitted 这类日常命令就能直接跑起来。

参考文献  
1. OpenAI Codex, Custom chat completion API not working after upgrade to codex >=0.59, GitHub issue #7051, 2025-11-20. https://github.com/openai/codex/issues/7051  
2. OpenAI Codex, Deprecating chat/completions support in Codex, GitHub discussion #7782, 2025-12-09. https://github.com/openai/codex/discussions/7782  
3. 阶跃星辰开放平台, API Key 管理. https://platform.stepfun.com/interface-key  
4. Tibo (@thsottiaux), Reminder that you can use the Codex App, CLI and SDK with any open source model, not just with OpenAI models, X/Twitter, 2026. https://x.com/thsottiaux

![](attachments/4d01a37e72f43a1b.png)

## 一起“点赞”三连↓
