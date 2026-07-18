---
title: feedback_search_prefer_tavily
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


提取 URL 正文时，工具优先级：
1. `tavily-extract-zh` — 通过 AISA Tavily API，最适合 AI 的正文抽取
2. `WebFetch` / `defuddle` — 备选

**Why:** 用户明确说 tavily 才是最适合 AI 的搜索工具，要求排在第一优先级。

**How to apply:** 当用户提供 URL 需要提取内容时，先用 tavily-extract-zh skill，失败或不可用时再回退到 WebFetch / defuddle。
