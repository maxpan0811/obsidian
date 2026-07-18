---
title: evernote-rest-api-vs-thrift-export-20260701
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-01 对比了印象笔记两种 API 的批量导出性能：

## REST API（第三方服务网关）

| 指标 | 值 |
|------|-----|
| 端点 | `app.yinxiang.com/third/ai-chat-note/grpc-api/search/` |
| 同批次成功率 | 136/2682 (5%) |
| 失败原因 | 大多数笔记 `getNoteDetail` 返回空结果或解析失败 |
| 资源获取 | `resourceList` 条目的 `content(body)` 全为空，拿不到图片二进制 |
| 内容格式 | 纯文本，非 ENML，不含 `<en-media>` 标签 |
| Developer Token 兼容 | 可用（`auth` 头直接传） |
| **结论** | **不可用于批量导出**——大部分笔记拿不到内容 |

## Thrift API（evernote2 SDK）

| 指标 | 值 |
|------|-----|
| 协议 | `getNote(token, guid, withContent, withResourcesData, ...)` |
| 满速调用 | ~3/s（不带资源数据），~0.2/s（带资源数据） |
| 限流桶容量 | ~600-700 次调用 |
| 限流恢复 | errorCode=19, rateLimitDuration=800-1800s |
| 资源内容 | 完整 ENML + 图片二进制 |
| **结论** | **唯一可靠的批量导出方式** |

## 推荐策略（fast_export.py）

1. **扫描阶段**: `getNote(token, guid, True, False, False, False)` — 快（3/s），仅获取 ENML 文本，不下载资源
2. **文本导出**: 扫描同时完成，ENML→纯文本→.md 文件
3. **资源识别**: 根据 ENML 中的 `<en-media type="...">` 判断图片 vs 非图片附件
4. **图片下载**: 只有含图片的笔记才调用 `getNote(token, guid, True, True, False, False)` — 慢但次数有限
5. **附件处理**: 非图片附件 → 笔记移入 temp

**限流处理**: 无延迟满速调用，被限流后 sleep(rateLimitDuration+30)，重试

**Why：** 旧的 sync_favorites.py `step_export()` 对每篇笔记加了 4 秒间隔，导致 13,779 篇需要 ~20 小时。移除延迟后仅 ~5-6 小时（满速调用直到限流，睡眠恢复后继续）。
