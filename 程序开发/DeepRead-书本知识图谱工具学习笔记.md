---
title: DeepRead 书本知识图谱工具学习笔记
date: 2026-07-09
tags: [DeepRead, 知识图谱, AI结构化, booktools, Claude-Code]
---

# DeepRead：用 AI 把书变成可交互知识图谱

## 项目概览

**DeepRead**（[GitHub](https://github.com/liujuntao123/DeepRead)）是一个开源项目，用 AI 将书籍拆解成知识节点（人物、事件、概念、地点、组织），通过双向链接串成可交互的知识网络，最终可部署为静态网站或导入 Obsidian 使用。

已覆盖 26 本书（四大名著、百年孤独、资本论三卷、孙子兵法、做哲学等），共 1800+ 知识节点。

## 技术架构

### 四步管线

| 步骤 | 工具 | 说明 |
|------|------|------|
| 1. 格式转换 | BookTools / MinerU | EPUB → Markdown（booktools），PDF → MD（MinerU） |
| 2. 宏观分析 | AI Agent（Claude Code） | 识别全书结构，划分维度，生成任务清单 |
| 3. 批量填充 | AI Agent（Claude Code） | 按任务清单逐个生成节点，自动建立双向链接 |
| 4. 发布 | Obsidian / Quartz | 本地使用或部署 GitHub Pages |

### 发现：DeepReadTools（npm: booktools）

配套工具库 [DeepReadTools](https://github.com/liujuntao123/DeepReadTools) 已发布为 npm 包 `booktools`：

```bash
npm install -g booktools
booktools    # 交互式 CLI：扫描 epub → 转换 → 整理
```

核心功能：
- 封装 `epub2md` 做 EPUB → Markdown 转换
- 清理引用格式（去除脚注标记等）
- 创建 `books/` 目录结构
- **复制 `.claude/` 模板**（Agent + Command 定义）

### Claude Code Agent 工作流（关键发现）

`booktools` 会在输出目录中写入 `.claude/` 模板，用 Claude Code 的 Agent 系统完成 AI 分析：

| 文件 | 类型 | 职责 |
|------|------|------|
| `agents/Architect.md` | Agent | 通读全书 → 输出宏观蓝图（分类节点列表）+ `todo.md` |
| `agents/Generator.md` | Agent | 每批 10 个节点 → 从原文提取信息 → 生成结构化 Markdown |
| `commands/Initial_construction.md` | Command | 启动 Architect |
| `commands/node_generation.md` | Command | 循环读 todo.md，每批 10 个委派给 Generator |

**工作流**：
1. `booktools` 处理 epub → 生成 books/ + .claude/ 模板
2. 在输出目录中启动 Claude Code
3. 运行 `Initial_construction` → Architect 生成蓝图 + todo
4. 运行 `node_generation` → 循环处理直到 todo 清空

### 节点格式示例

每个知识节点是一个独立 Markdown 文件，含 5 部分：

```yaml
---
tags: [城乡中国, 核心概念]
---
城乡二元结构是指...

> 原文引述（1-3条）

## 展开阐述
结构化解释背景、内涵、作用及影响

## 关联节点
- [[017-制度安排-户籍制度]]
- [[018-制度安排-城乡分割制度]]
```

## 关键经验

### 可迁移的设计思路

1. **先规划再填充** — 宏观分析 → 任务清单 → 批量生成，比一锅炖可控
2. **Markdown 存储** — 人类可读、可手动编辑、可版本控制
3. **双向链接自动建立** — 生成节点时同步关联，而非事后手动链接
4. **人机分工清晰** — AI 做提取和结构化，人做校验和补充
5. **每本书自定义维度** — 不限固定模板（西游记分 7 维，三国演义分 4 维）

### 对 LLM Wiki 知识库的启发

- 自动双向链接可在 wiki ingest 管线中复用
- "先规划再填充"比当前 ingest 的一锅炖更可控
- Query 管线可增加知识图谱视图，不限于文本搜索

### 局限

- 技术门槛：需装 CLI 工具和大模型
- AI 准确率：复杂关系可能漏掉，但 Markdown 可手动修正
- 覆盖面 26 本，离"任何一本书"有距离

## 相关链接

- GitHub: https://github.com/liujuntao123/DeepRead
- 网站: https://deepread.aizhi.site
- BookTools: https://github.com/liujuntao123/DeepReadTools
- npm: `npm install -g booktools`
