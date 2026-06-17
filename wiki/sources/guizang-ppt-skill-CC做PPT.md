---
title: Claude Code 做 PPT：guizang-ppt-skill
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://github.com/op7418/guizang-ppt-skill]
source_path: 印象笔记管理工具/Claude Code 做 PPT 也太猛了：一句话生成高颜值网页PPT.html
tags: [claude-code, ppt, skill, tool-recommendation, guizang]
---

## 一句话摘要

歸藏老师的 `guizang-ppt-skill`（7K+ Star），让 Claude Code 一句话生成高颜值网页 PPT——核心策略是**先收窄自由度，再提高完成度**。

## 项目信息

- **GitHub**: [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)
- **作者**: 歸藏 (op7418)
- **Star**: 7K+
- **输出**: 单文件 HTML（不需要构建，浏览器直接打开）

## 两套视觉系统

### Style A：电子杂志 × 电子墨水

| 主题 | 适合场景 |
|------|---------|
| 🖋 墨水经典 | 通用默认、商业发布 |
| 🌊 靛蓝瓷 | 科技/研究/AI/技术发布会 |
| 🌿 森林墨 | 自然/可持续/文化/非虚构 |
| 🍂 牛皮纸 | 怀旧/人文/文学/独立杂志 |
| 🌙 沙丘 | 艺术/设计/创意/画廊 |

内置 10 种常用页面布局：封面、章节页、数据大字报、图文页、图片网格、流程页、对比页。

### Style B：瑞士国际主义

| 主题 | 适合场景 |
|------|---------|
| 克莱因蓝 IKB | 通用默认、商业发布、AI 产品 |
| 柠檬黄 | 年轻、运动、零售 |
| 柠檬绿 | 生态、可持续、Z 世代品牌 |
| 安全橙 | 警示、新闻、活力主题 |

内置 22 种锁定版式，强调 16 列网格、直角色块、1px 发丝线——无阴影、无渐变、无圆角。

## 配图与封面

- **配图推荐**: GPT Image 2.0 生成纪实照片、信息图、流程图
- **封面规格**: 公众号头图(21:9)、分享卡(1:1)、小红书封面(3:4)、视频号封面(16:9)
- **核心原则**: 只用少量关键词，视觉重心落在大标题上

## 安装方法

```bash
# CLI 安装
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill

# Agent 安装（给 Claude Code 指令）
帮我安装 guizang-ppt-skill skill，github地址：https://github.com/op7418/guizang-ppt-skill

# 手动安装
下载到 ~/.claude/skills/guizang-ppt-skill/
```

## 核心观点

> AI 做设计最容易出现的问题，就是每一页都想「发挥一下」，最后页面看起来很热闹但整体不统一。先收窄自由度，再提高完成度。

## 相关页面

- [[products/Claude Code]]
- [[features/Skills]]
- [[sources/claude-code-best-practice-工作流指南]]
- [[sources/Everything Claude Code完整上手攻略]]
