---
title: local-sync-image-bug-fix-20260702
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-02 local_sync.py 的两个版本迭代：

## v1 问题

第一次 `clean_and_sync.py` 完成后 `img=0` — 所有图片资源未被匹配。

**根因：** 本地 content 目录中的资源文件以 `ZENRESOURCE.ZLOCALUUID` 命名（如 `DCCAB21D-6218-4E76-989D-20668300DC3E.jpg`），而非 `ZENRESOURCE.ZGUID`（如 `ceb3f54d-8a88-487c-8852-c1326c65eefe`）。代码中 `get_resource_file_path()` 按 ZGUID 搜索，所以找不到任何文件。

## v2 修复

1. SQL 查询增加 `ZLOCALUUID` 列（`get_resources_for_note`）
2. `get_resource_file_path()` 改为先用 `ZLOCALUUID` 匹配，ZLOCALUUID 找不到时 fallback 到 ZGUID
3. `copy_resource_file()` 接收 `res_local_uuid` + `res_guid` 两个参数
4. 输出文件以 `ZLOCALUUID` 命名（keep it simple，UUID 本身够唯一）

## 结果

- 17,103 篇 .md：**5.1 分钟**（之前 API 方案估算 24-40 小时）
- 含图笔记：15,791 篇 ✅
- 附件跳过：65 篇
- 附件图片从 161,647 增长到 361,597（新 UUID 命名，旧 hash 命名的残留）

**Now to apply:** 下次改 `local_sync.py` 时记住本地文件是用 `ZLOCALUUID` 命名的，不是 `ZGUID`。
