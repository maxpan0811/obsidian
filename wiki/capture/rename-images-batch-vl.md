---
title: rename-images-batch-vl
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# rename_images.py — 批量图片重命名

在 `文件命名工具` skill 下新增 `rename_images.py`，用本地 qwen3-vl:30b 逐张分析图片内容，按"日期_人物_事件"规则自动命名。实测三批 180 张，100% 成功率。

## 关键设计

- **ThreadPoolExecutor 并发 4**：Ollama 共享权重，单张从 31s→14s
- **大图自动缩小**：1MB+ 用 `sips -Z 2248` 缩到短边 2248px，省 ~30%
- **Checkpoint + old→new mapping**：`--resume --execute` 直接用 mapping rename，不用重跑模型
- **已命名文件跳过**：文件名匹配 `^\d{4}年\d{2}月\d{2}日_中文` 格式自动跳过
- **Dry-run 默认**：加 `--execute` 才实际改名
- **重名自动加 (2)(3)**：视觉模型对相似内容易生成同名，自动去重

## 实测三批数据

| 批次 | 数量 | 耗时 | 平均 | 成功率 |
|------|:---:|:----:|:----:|:-----:|
| 第 1 批 JPG（cold） | 71 | 16m55s | 14.3s | 100% |
| 第 2 批 PNG（warm） | 67 | 10m36s | 9.5s | 100% |
| 第 3 批 mixed | 42+43skip | 7m7s | 10.2s | 100% |

## 实战踩坑记录

### 坑 1：两个 batch 同时跑撞车
两个 4-worker batch 同时提交，8 线程抢同一 Ollama 模型，单张从 15s 拖到 180s。
✅ **教训：** 只跑一个 batch，不重复提交。

### 坑 2：后台任务输出被缓冲
`run_in_background` 无 TTY，Python print 不 flush。
✅ **修复：** `PYTHONUNBUFFERED=1` 或 `python3 -u`。

### 坑 3：已命名文件被重复改名
已有 `YYYY年MM月DD日_中文` 格式的文件又被分析一遍，产生同名冲突加 `(2)` 后缀。
✅ **修复：** 正则匹配 `^\d{4}年.*[一-鿿]` 格式的文件跳过不改。
⚠️ **待改进：** 当前只匹配完整格式，`YYYY年_` 短格式漏掉了。

### 坑 4：Checkpoint mapping 存反
旧的 `old_to_new` 存反了方向，续跑时空跑不干活。
✅ **修复：** 统一 `old→new`，续跑 `--resume --execute` 直接 os.rename。

### 坑 5：文件列表锁定后源文件消失
启动时锁死文件列表，等排到执行时源文件已被前一轮 rename 改了名。
✅ **修复：** `try/except FileNotFoundError` 容错跳过。

### 坑 6：qwen3-vl:14b 不存在
Ollama registry 上 `qwen3-vl` 系列只有 `:30b` 一个 MoE 版本，其他 tag 全 404。
✅ **结论：** Qwen3-VL 只出了 MoE 单一大尺寸，不需要副驾模型。

## 模型模型发现

`qwen3-vl:30b` 是 MoE 架构（`qwen3vlmoe`），激活仅 ~3B 但总参 31.1B，M4 Max 上 88.5 tok/s。DeepSeek 按稠密 30B 估的 15-20s 太悲观——MoE 本身就是甜点。

## 落盘位置

- `~/.claude/skills/文件命名工具/scripts/rename_images.py`
- `~/.claude/skills/文件命名工具/SKILL.md`
- `/Users/panbo/Obsidian/20260520/程序开发/批量图片重命名工具优化记录.md`

## 与 rename_by_content.py 的关系

图片重命名独立脚本，不和文档公用逻辑。独立脚本减少相互影响。

**Why:** 视觉推理是 qwen3-vl 的事，不需要改文档命名那条线。
**How to apply:** 用户说"批量图片改名"时调 `rename_images.py`，说"批量文档改名"时调 `rename_by_content.py`。图片脚本默认 dry-run。
