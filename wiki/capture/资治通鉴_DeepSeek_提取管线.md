---
title: 资治通鉴 DeepSeek 提取管线
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 资治通鉴 DeepSeek 提取管线经验

## 管线流程

```
adapted_book.json
  → batch_extraction.py (DeepSeek API, CHUNK_SIZE=3, THREADS=8)
    → data/store/juan_N.json (原始提取 chunk)
      → entity_resolution.py (Union-Find 合并同名实体)
        → data/unified_knowledge.json
          → build_data.py --publish-frontend
            → visualization/public/data/unified_knowledge.json
```

## 关键参数

- `CHUNK_SIZE=3`: 每 API 调用处理 3 句，减少 2/3 调用量
- `CONTEXT_SIZE=5`: 前 5 句做上下文
- `max_workers=8`: 8 并发线程，用 `ThreadPoolExecutor`
- 全本 30,758 句 → `CHUNK_SIZE=3` → ~10,717 API 调用 → ~2h

## 卷1产出

137 角色 + 27 政权 + 17 组织 + 70 地点 + 86 事件 + 211 关系

## API 配置

- `langchain_deepseek.ChatDeepSeek`
- `model=deepseek-v4-flash` / `deepseek-v4-pro`
- `openai_api_base=https://api.deepseek.com`
- 需要网络访问权限（`require_escalated`）
- `disable_streaming=True`, `cache=False`

## 使用方式

```bash
# Smoke test (1句)
python3 scripts/smoke_deepseek_extraction.py --juan 1 --segment 1 --chunk-start 0

# 批量提取卷1-3
python3 scripts/batch_extraction.py --juan-start 1 --juan-end 3 --chunk-size 3 --max-workers 8

# 构建 + 发布前端
python3 scripts/build_data.py --publish-frontend
```
