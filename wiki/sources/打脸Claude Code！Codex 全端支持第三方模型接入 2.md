---
title: 打脸Claude Code！Codex 全端支持第三方模型接入 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/打脸Claude Code！Codex 全端支持第三方模型接入 2.md
tags: [evernote, impression, yinxiang]
---

# 打脸Claude Code！Codex 全端支持第三方模型接入

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518219&idx=1&sn=636232f0d05c537c4f0bf7c182dba0b7&chksm=e9833676a69ce9627190c21c6f094efccd6017bde5a3d3d83241604d55d20f8143eba8f35d97&scene=90&xtrack=1&req_id=1781744558291443&sessionid=1781744767&subscene=93&clicktime=1781744774&enterid=1781744774&flutter_pos=0&biz_enter_id=4&ranksessionid=1781744558&jumppath=1001_1781744767270,1104_1781744768642,MMFlutterViewController_1781744769799,1104_1781744771150&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbipQmjMMmnTsVUlC/stZNRLTAQIE97dBBAEAAAAAALbqM/vfs2sAAAAOpnltbLcz9gKNyK89dVj0nI9UBnqggSvBH4CMwIDjZH9RhN0exkwTH+kljSyCvTG8t4t//YwGq6o1xJ34baooM2+ASLDad7nz2fQmO1LW9yipMgZLsNMrHmcZmXON6GVxQ5rgP4+8Zko+A8/RjQa0i7rnsfPV6BGUYBd4lLmw5tzMpsJHGEcqRyWMiDp9phon7ZUad4Kg2L3HE/VQHVcdESTzh7BhQh+GSlr5n7z8LWoW8GXKorxuQx4gV/M=&pass_ticket=8rt0XsIGDhw//Y1/DMVnWKIzMbpsr218qBl6J7CIVHenZGEyGJkci015uRCf6Dyf&wx_header=3)

打脸Claude Code！Codex 全端支持第三方模型接入
===============================

Original字节笔记本 字节笔记本

 

掀完桌子再打脸！[掀Claude Code的桌子！Codex 一键搬家功能](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518172&idx=1&sn=162d5962f093dd401375e4c623b970d8&scene=21#wechat_redirect)

OpenAI如今越来越 open 了，正式在全端 CLI 桌面客户端等支持第三方模型的接入使用，通过简单的配置就可以自由定制任何的供应商，不论闭源还是开源模型。

相比较自掘坟墓，闭源又处处做限制的 A\，OpenAI 如今的格局已经撑破了天花板！

---

哪些可以直接接？
--------

原生支持 Responses API 的供应商其实都可以，具体可以查看模型供应商的文档，config.toml 加几行就搞定，

**以 Ollama 为例**

Ollama 已经支持 Responses API（需要较新版本），直接接：

model = "qwen2.5-coder:32b"
model\_provider = "local\_ollama"
[model\_providers.local\_ollama]
name = "Ollama"
base\_url = "http://localhost:11434/v1"

不需要写 `env_key`，本地服务没有鉴权。用 `--oss` 参数可以更简单：

codex --oss

**LM Studio 也可以**

LM Studio 是 Codex 内置 ID，直接指：

model\_provider = "lmstudio"

或者配置默认本地供应商后用 `--oss` 启动：

oss\_provider = "lmstudio"

---

DeepSeek要走中间层
-------------

DeepSeek 目前还不行。

Codex 在 2026 年初彻底废弃了 Chat Completions 协议，现在只支持 OpenAI Responses API。 

而 DeepSeek 官方 API 目前还是 Chat Completions 格式，所以需要做一下转接，目前的方法很多，我推荐使用最简单的方法：

使用 OpenRouter，完全零配置。

OpenRouter 在自己这侧实现了 Responses API 的转换，对 Codex 暴露 Responses 格式，背后再去调 DeepSeek。

先在 OpenRouter 控制台绑定 DeepSeek API key（BYOK 功能），然后：

model = "deepseek/deepseek-v4-pro"
model\_provider = "openrouter"
[model\_providers.openrouter]
name = "OpenRouter"
base\_url = "https://openrouter.ai/api/v1"
env\_key = "OPENROUTER\_API\_KEY"

export OPENROUTER\_API\_KEY=sk-or-你的key

通过 OpenRouter 也可以接其他任何 OpenRouter 支持的模型，改 model 字段就行：

# 临时切换模型
codex --profile openrouter --model anthropic/claude-sonnet-4-6
codex --profile openrouter --model google/gemini-2.5-pro

上面定义第三方的模型供应商都是通过配置文件选项来完成的，随着 Codex的功能越来越强大，配置选项也越来越多，我大概统计了一下，有 98 个之多，如果要一个个的看下来再一个个的配置，实在是太麻烦了。

所以写了一个可视化的图形Codex配置网站。

![](.evernote-content/E0ABFE2A-E3D5-4A0C-9483-097E70C1FF9C/3278CEB1-F56A-41EA-9596-5729F50B9610.png)

实时同步官方最新的最全的 Codex 配置字段，每一条都增加了详细的注解和说明。

![](.evernote-content/E0ABFE2A-E3D5-4A0C-9483-097E70C1FF9C/488AD014-70F0-456E-8BF1-275DE058403A.png)

提供了最简化的配置，所有的配置完成之后，可以通过一键下载或者复制的方式在本地的.codex 目录中进行使用。

![](.evernote-content/E0ABFE2A-E3D5-4A0C-9483-097E70C1FF9C/8FE2E957-2179-4FBD-B989-28B0517E3F8D.png)

配置文件其实非常有，比如我们在规划的时候使用高级的模型，在执行的时候配置使用更廉价、更快速输出的开源模型，结合自己的实际工作场景，再通过这些配置选项，可以最大程度地发挥出 Codex 的所有潜能。

之前我已经在[AI编程高效开发指南](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIzMzQyMzUzNw==&action=getalbum&album_id=3955838883623043087&from_itemidx=1&from_msgid=2247518164#wechat_redirect)中的[2026最新 .codex 目录及配置详解](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516735&idx=1&sn=052ffdb69d2ba139933cf007763ea4dd&scene=21#wechat_redirect)有更详细的讲解，可以搭配理解和使用。

Codex可视化的图形配置地址，如有任何建议和意见，可以在留言区留言：

https://codexapp.cc

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518219&idx=1&sn=636232f0d05c537c4f0bf7c182dba0b7&chksm=e9833676a69ce9627190c21c6f094efccd6017bde5a3d3d83241604d55d20f8143eba8f35d97&scene=90&xtrack=1&req_id=1781744558291443&sessionid=1781744767&subscene=93&clicktime=1781744774&enterid=1781744774&flutter_pos=0&biz_enter_id=4&ranksessionid=1781744558&jumppath=1001_1781744767270,1104_1781744768642,MMFlutterViewController_1781744769799,1104_1781744771150&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b25&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbipQmjMMmnTsVUlC/stZNRLTAQIE97dBBAEAAAAAALbqM/vfs2sAAAAOpnltbLcz9gKNyK89dVj0nI9UBnqggSvBH4CMwIDjZH9RhN0exkwTH+kljSyCvTG8t4t//YwGq6o1xJ34baooM2+ASLDad7nz2fQmO1LW9yipMgZLsNMrHmcZmXON6GVxQ5rgP4+8Zko+A8/RjQa0i7rnsfPV6BGUYBd4lLmw5tzMpsJHGEcqRyWMiDp9phon7ZUad4Kg2L3HE/VQHVcdESTzh7BhQh+GSlr5n7z8LWoW8GXKorxuQx4gV/M=&pass_ticket=8rt0XsIGDhw//Y1/DMVnWKIzMbpsr218qBl6J7CIVHenZGEyGJkci015uRCf6Dyf&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6cd32a5d-3c5f-4f67-bb89-14490429137f/6cd32a5d-3c5f-4f67-bb89-14490429137f/)
