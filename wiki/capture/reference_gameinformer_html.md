---
title: reference_gameinformer_html
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Game Informer RSS -> Obsidian 随笔 HTML 工作流

## 命令

Game Informer 四个 RSS 频道（news/reviews/previews/features）各对应独立 XML 地址：

- `https://www.gameinformer.com/news.xml`
- `https://www.gameinformer.com/reviews.xml`
- `https://www.gameinformer.com/previews.xml`
- `https://www.gameinformer.com/features.xml`

需要 `require_escalated` 权限（网络访问）。用 `curl -sL` 拉取，Python 解析 XML 提取 title/link/pubDate/creator。

## 输出

生成中英双语的 HTML 页面，使用 theme-factory 的 Sunset Boulevard 主题（暖橙色调），包含四个板块的结构化卡片式布局。

## 保存路径

"/Users/panbo/Library/Mobile Documents/iCloud~md~obsidian/Documents/20260520/随笔/"

文件名格式：Game-Informer-游戏资讯-YYYY-MM-DD.html

## 注意事项

- 默认展示每板块 5-7 条，标题+链接+中文概览+日期+作者
- 不要 dump 原始 HTML 描述内容，只提供安全的短 teaser
- 如果某频道无内容，直接跳过该板块（不输出空标题）
- 四频道抓取可并行执行以节省时间
- 主题颜色映射：body bg #fdf8f0, text #264653, h2 #e76f51, border #e9c46a, meta #f4a261, fonts DejaVu Serif/Sans
