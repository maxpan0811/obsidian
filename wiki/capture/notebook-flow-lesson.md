---
title: notebook-flow-lesson
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 场景

2026-07-02 跑 `dedup_evernote.py --date 2026-07-01` 报找到 0 篇。检查笔记库发现 7/1 的 25 篇笔记全部在 **favorite** 笔记本，而非 **工作篮**。

## 第一反应（错误）

"保存脚本写错了 notebook GUID" → 修改了 `save_article_playwright.py`、`dedup_evernote.py`、`save-to-evernote.md` 中的 GUID。

## 真相

用户把笔记从 temp 手动移到了 favorites。保存脚本的 工作篮 GUID 是正确的。

## 教训

- 笔记迁移（手工或自动化管线）是正常操作，不是 bug
- 确认操作流程后再做技术推断
- 跨 notebook 的去重在当前场景下不是刚需——笔记都在一个 notebook 内，去重只查同一个 notebook

## 修正动作

| 文件 | 操作 |
|------|------|
| `scripts/save_article_playwright.py` | 回退 GUID + 删除错误注释 |
| `scripts/dedup_evernote.py` | 回退 GUID |
| Memory `20260701-cdp-batch-10-articles.md` | 追加修正说明 |
