---
title: feedback_excel_filename_date_range
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


导出 Excel 报表的文件名：
- 用日期范围格式：`6.1-6.7`（月.日-月.日），不要写"第23周"
- 不要带运行时间戳（如 `151108`），干净简洁
- 自动把旧版文件移入废纸篓（`shutil.move` 到 `~/.Trash`），不要 `os.remove` 彻底删除
- 旧文件如果有同名，加时间戳后缀避免覆盖

**Why:** 用户说周数不直观，时间戳意义不明。文件名应当一眼看出是哪个周期的数据。

**How to apply:** 新建或修改生成报表的脚本时，文件名按此规则输出。清理旧文件用废纸篓而非删除。
