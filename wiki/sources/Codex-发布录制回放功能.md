---
title: Codex 发布录制回放功能
type: source
created: 2026-06-20
updated: 2026-06-20
source_path: 印象笔记管理工具/Codex 发布录制回放功能.html
tags: [教育, 管理, 职场]
---

Codex 发布录制回放功能
原文链接: https://mp.weixin.qq.com/s?__biz=MzI2NTI4MDczMA==&mid=224748...Codex 在 macOS 上线了 Record & Replay：在 Mac 上演示一遍操作流程，Codex 观察学习后生成可复用 Skill。很多重复性工作流（报销、请假、建Issue、下报表）步骤零碎、依赖个人偏好，用文字提示词很难写清楚。这个功能把"写指令"变成了"做一遍"，AI 直接从操作中学习。流程页简单，插件菜单发起录制 → 正常操作 → 停止后 AI 自动生成 Skill草案（含触发时机、输入、步骤、校验标准），可编辑细化。下次开新线程调用 Skill，换新的参数值直接跑。目前需启用 Computer Use，macOS 首发。团队分发、多 Skill 组合或接入 MCP 服务器的需求，走插件开发。#code…

---
### 截图OCR提取（{today}）
### 截图1
识别结果:
### 截图2
识别结果:
### 截图3
识别结果:
### 截图4
识别结果:
### 截图5
识别结果:

---
### 截图OCR提取（2026-06-20）
### 截图1
CODEX
2026.06.19
CODEX·产品更新
Codex 发布
录制回放功能
操作变技能，录一遍，下次再
用。在 Mac 上演示一遍工作流
程，Codex 观察学习后生成可
复用 Skill。
来源/OPENAI DOCS/2026.06

### 截图2
CODEX RECORD & REPLAY
机制
Codex Record & Replay
录一次
用无数次
01
开始录制
打开插件，选 Record a skill。给 Codex 一句上下文：
你要做什么、哪些输入会变。
02
演示工作流
D
在 Mac 上正常操作。Codex 观察每一步动作和窗口内
容，直到你停止录制。
03
生成Skill
<>
Codex 分析录制内容，生成可检查、可编辑的 Skill。
包含何时用、需要什么输入、每一步怎么做。
04
下次复用
开新线程，告诉 Codex 用这个 Skill。换新的输入值就
行，比如换一份报表、换一个日期范围。
演示时用真实数据，但避开密码和敏感信息

### 截图3
CODEX RECORD & REPLAY
场景
Codex Record & Replay
什么时候
用它最合适
工作流重复出现
每次步骤一样，只是输入值不同。比如报销、请假、建
Issue、下载报表。
依赖你的个人偏好
命名规范、字段默认值、决策点、隐藏习惯，这些写在
提示词里不如录一遍。
演示比描述更直观
发视频、填表单、操作内部工具，这些动作用文字描述
很啰嗦，做一遍就清楚。
1P
个人用，不需要分发
吕
这个 Skill 就你自己用。团队共享、多 Skill 打包、接入
MCP服务器的，走插件开发。
快速创建个人 SKILL → RECORD & REPLAY / 团队标准分发 → 插件开发

### 截图4
CODEX RECORD & REPLAY
须知
Codex Record & Replay
能用在哪
不能用在哪儿
√
macOS 首发，Computer Use 需启用
初始仅支持 macOS。需在设置中启用 Computer Use,
Record & Replay 共用同一开关。
录制后可继续编辑 Skill
√
生成的 Skill 不是黑盒。你可以让 Codex 进一步细化，补充隐
藏偏好和决策规则。
组织管理员可通过requirements.toml控制功能
开关
Computer Use 和 Record &Replay由
[features].computer_use统一管控。
多Skill打包、团队分发、MCP接入，走插件开发
Record & Replay 是创建个人 Skill 的快路径。团队级、可版
本管理、接入外部服务的，打成插件。
录制后立即停止/不要继续无关操作

### 截图5
CODEX RECORD & REPLAY
TIPS
Codex Record & Replay
录得越好
用得越稳
01
演示要短而完整
只录这个任务本身，完成后就停止。不要把后续无关操作也
录进去。
02
提前说明哪些输入会变
录制前告诉 Codex你的目标和可变输入。比如"报表日期每次
不同"Issue 标题会换"。
03
用真实数据，但避开敏感信息
日期、文件名、表单内容用真实的，这样 Codex 学得更准。
但不要录密码、密钥、个人信息。
04
录制后细化Skill
生成的 Skill 可以继续改。补充命名习惯、默认选项、决策点
这些录制没覆盖到的偏好。
步骤稳定+成功标准明确，录制更可靠
