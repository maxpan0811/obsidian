---

name: claude-code-ch7-hooks
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（七）（教不会我吃民法典！）：Hooks — 给AI立铁律.html

---

# 法律人的 Claude Code 教程（七）：Hooks — 给 AI 立铁律

> 来源：智律积成（微信公众号）

## 核心思想

- CLAUDE.md 是"嘱咐"（可能忘），Skill 是"教招式"（可能跳步）
- **Hook 是"立铁律"**：触发了就自动执行，没有商量余地
- 从"希望 AI 做对"到"确保 AI 做对"

## 四种动作类型

| 类型 | 法律场景举例 |
|------|-------------|
| 执行命令 | 播放提示音、写日志、拦截危险操作 |
| 发送请求 | 任务完成后通知协作平台 |
| 让 AI 判断 | "这次审核是否覆盖了所有必查项？" |
| 派出子代理 | "检查输出的审核意见格式是否规范" |

## 配置方式

直接跟 Claude Code 说需求：
- "配置一个全局 hook：完成任务时自动播放 macOS 系统提示音"
- "给这个项目配置审计 hook：记录每次文件修改的前后内容"

## 武侠线

Skills = 招式（主动调用），Hooks = 护体真气（自动防御）。

[Related: [[features/Hooks]]]
