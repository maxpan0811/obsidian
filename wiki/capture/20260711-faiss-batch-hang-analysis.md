---
title: 20260711-faiss-batch-hang-analysis
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# FAISS 批量索引卡死根因

## 症状

`wiki_faiss_build.py --limit 500` 在会话早期能跑完（400 篇/3.5 分钟），
会话后期连 `import sentence_transformers` 都卡住。

## 排查过程

### 尝试的措施（均无效）

- `model._pool = None` → sentence_transformers 3.x 无 `_pool` 属性。
  `Pool` 只在 `start_multi_process_pool()` 调用时创建，`__init__` 中不创建。
- `device='cpu'` → 本来就在 CPU 上运行，无 CUDA。

### 真正的根因

**系统状态退化**。多次 Python 进程启动/崩溃后：
1. 内存碎片化（bge-m3 模型 ~2GB 残留）
2. POSIX 信号量泄漏（loky 遗留）
3. 子进程卡死（之前 crash 的孤儿进程）

晚期会话新进程启动时系统无法分配足够资源，直接挂起。

### 唯一有效的预防措施

**在新会话中运行**——干净的系统环境 + 正确的 env 变量：

```bash
OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 wiki_faiss_build.py --limit 500
```

### 有效且已落实的措施

1. `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` — 防止离线环境联网超时
2. `sentence_transformers` 延迟导入 — 不在模块顶部 import
3. 脚本内 `os.environ.setdefault` 设 env 变量 — 双保险

## 数据

- 今日进度：1,205 → 1,805（+600 篇）
- FAISS 索引累计：1,805 篇
- 单批速度：~100 篇/2-3 分钟（CPU 编码）
