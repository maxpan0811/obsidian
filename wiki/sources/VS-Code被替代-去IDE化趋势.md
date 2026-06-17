---
title: 这下，VS Code 也没有安装的必要了！
type: source
created: 2026-06-11
updated: 2026-06-11
source_path: 印象笔记管理工具/这下，VS Code 也没有安装的必要了！.html
tags: [ide, vscode, warp, zed, ai-agent, trend]
---

**摘要**: 探讨 AI 时代的去 IDE 化趋势。VS Code 的 Remote-SSH 功能已被 Warp（新增 SSH 文件树和 Agent 能力）+ Zed（SSH 远程项目）替代。Windsurf 改名 Devin Desktop 转型 Agent Command Center。"过去把所有能力塞进 IDE，现在 AI 把能力重新拆出来——编辑归编辑，远程归远程，执行归 CLI，复杂任务交给 Agent。"

## 核心观点

- VS Code Remote-SSH 的功能已被 Warp 和 Zed 的本地 SSH 替代
- Warp 支持通过 SSH 的文件树 + Agent 能力，无需另起 CLI
- Windsurf 改名 Devin Desktop，从编辑器转型 Agent Command Center
- 新工作流：CLI 里描述目标 → Agent 改代码 → 用户做方向判断+结果验收
- 去 IDE 化趋势明显：编辑、远程、执行、Agent 各司其职

## 关键细节

- **Warp**: SSH 文件树 + Warp Agent 远程控制，支持 DeepSeek 第三方模型
- **Zed**: Rust 跨平台，启动快，SSH 远程项目
- **Sublime**: 纯查看代码用
- **个人选择**: 卸载所有 Electron IDE（VS Code/Cursor），留 Zed + Sublime

## 相关页面

- [[concepts/去IDE化趋势]]
