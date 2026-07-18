---
title: cdp-batch-10-articles
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 场景

一次保存 10 篇公众号文章到印象笔记工作篮（2026-07-01）。

## 采用方案

**CDP 连接 + 链式 escalation 启动**（Chrome headless=new + CDP 脚本在同一命令内）。

### 关键操作

```bash
nohup "$CHROME_BIN" --remote-debugging-port=9222 --no-sandbox --headless=new --disable-gpu &>/tmp/chrome.log &
sleep 4
python3 /tmp/save_articles_via_cdp.py <URL1> <URL2> ... <URL10>
```

## 验证结果

- **10/10 保存成功，0 失败**
- 文章类型覆盖：AI 资讯、教育、科技、家庭教育、历史、职场
- 图片保存验证：1 篇文章 0 图，9 篇含图文章全部下载成功（2~14 张）

### click_id 追踪参数兼容性

第 2 篇文章 URL 含 `?click_id=889145101`，CDP 保存完全无碍。改写了之前"短链接是唯一可靠格式"的判断——追踪参数不影响 CDP 路线。

## 坑记录

### Dedup API 限流

批量保存后运行 `dedup_evernote.py --date`，印象笔记 API 报 `⏳ 限流 779s`。10 篇文章在同一天保存，触发较严重的限流。

**解决方案**：批量保存后用 `nohup` 在后台跑 dedup：
```bash
nohup python3 scripts/dedup_evernote.py --date $(date +%Y-%m-%d) &>/tmp/dedup_$(date +%Y%m%d).log &
```

### 链式启动有效性

Chrome 启动和 CDP 脚本必须在同一 escalation 调用内执行。sandbox 在两次调用之间会杀掉后台 Chrome 进程，导致 CDP 连接失败（`ECONNREFUSED`）。


## 2026-07-02 补充：notebook GUID 不一致修复

**发现**：所有 2025-05 之后保存的公众号文章实际写入 **favorite** 笔记本（`d8e78929-d5b1-474a-b691-566df4d511ca`），但：

| 组件 | 原 GUID | 正确 GUID | 状态 |
|------|---------|-----------|------|
| `scripts/dedup_evernote.py` | `5a87b643` (工作篮) | `d8e78929` (favorite) | ✅ 已修复 |
| `scripts/save_article_playwright.py` main() | `5a87b643` (工作篮) | `d8e78929` (favorite) | ✅ 已修复 |
| `scripts/save_article_playwright.py` save_to_evernote() | `5a87b643` (工作篮) | `d8e78929` (favorite) | 保留默认值，加注释说明 |
| `/tmp/save_articles_via_cdp.py` | 调用 save_to_evernote() | 无参数，用默认值 | ❓ 与函数默认值绑定 |

**影响**：
- 去重脚本之前查不到笔记：因为查的是工作篮，笔记在 favorite
- 正确去重结果：2026-07-01 共 25 篇笔记，0 重复组


## 2026-07-02 修正：notebook GUID 是正常的

**用户反馈**：笔记是手动从 temp 移到 favorites 的，并非保存脚本写错了笔记本。

**实际流程**：
1. 保存脚本 → 写入 **工作篮**（GUID: `5a87b643`）← 正确
2. 用户移动作业 → temp → favorites
3. 我误判为"脚本写错笔记本"——回退了所有 GUID 修改

**教训**：不要仅凭笔记当前所在 notebook 推断写入目标。应先确认使用流程。
