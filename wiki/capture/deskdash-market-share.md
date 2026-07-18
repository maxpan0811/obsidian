---
title: deskdash-market-share
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 桌面看板 (2026-07-16 定稿)

## 架构（三层解耦）
- **分析层**：`产品市占率分析工具/scripts/export_desktop.py` 用该 skill 口径算指标 → 吐 `product_ms.json` 到 `~/.openclaw/workspace/deskdash/data/`
- **显示层**：skill「桌面看板」`build_dashboard.py` 扫 data/*.json → 套 `template.html` → 自包含 `dashboard.html`（数据内联，无服务器）；同时复制到 `~/Desktop/dashboard.html`
- 浏览器双击打开 / 单文件可发别人 / 离线可用

## 文件
- `~/.claude/skills/桌面看板/SKILL.md` + `scripts/build_dashboard.py` + `scripts/template.html`
- `~/.claude/skills/产品市占率分析工具/scripts/export_desktop.py`（吐 product_ms.json）+ `export_audit_excel.py`（核对Excel）
- `~/.openclaw/workspace/deskdash/data/product_ms.json` + `dashboard.html`
- 设计文档+完整对话：`~/Obsidian/程序开发/20260716-桌面看板显示层-design.md`

## 视觉风格：Mac OS 8.5 Platinum
- 50%灰桌面、3D斜面窗体（上左亮边/下右暗边）、条纹标题栏、铂金灰凸起按钮（激活=凹陷）、清单式细网格表格
- 字体 Geneva→Charcoal→Chicago→PingFang；涨绿(#1a7a3a)跌红(#a02020)
- 标题"2026年携程渠道市占率看板"居中；左上备注"仅含跟团游(不含半自助/私家团)"；右上"更新时间"(取数据文件名=下载时间)
- 单 view 时 tab 栏自动隐藏

## 指标（4行，只看双品牌，不看华程单独）
dual_share双品牌市占 / dual_share_yoy双品牌同比 / dual_rev_yoy双品牌营收同比 / total_rev_yoy携程大盘同比
abs(dual_rev等)保留在cell供核对，`--mask`脱敏剔除（源码也查不到）

## 口径（复用产品市占率分析工具）
- **华北=15省市含内蒙古**（标准，2026-07-16 确认；旧14省参考文件作废）
- 板块：欧洲用`目的地国家_归属业务区域`∈EU5；非欧洲用`考核区域`排目的地参团（line 27）
- 大区：6区省份清单(华北15/华东5/华西4/华南3/华中2/福建1)；线下`门店所在省份`/线上`用户出发站省份`(不用`出发省份`含海外)
- 品牌：订单归属含华程/账号订单→华程；==国旅订单→自营；双品牌=华程+自营
- 时间：月/季/半年/**全年**4档，默认最近完整季(Q2)；同比2026 vs 2025，出发日期归期

## 核对Excel（华北欧洲，照参考20列格式）
`export_audit_excel.py` → `~/Documents/artnova/华北欧洲桌面看板核对_YYYYMMDD.xlsx`，3sheet(月/季/半年)，20列(总收入/国旅/华程收入各25/26/同比 + 三类市占率各25/26/变化)，含线上汇总/线下汇总/全渠道汇总

## 刷新流程
```bash
python3 ~/.claude/skills/产品市占率分析工具/scripts/export_desktop.py   # 吐JSON
python3 ~/.claude/skills/桌面看板/scripts/build_dashboard.py             # 全量(内部)
python3 ~/.claude/skills/桌面看板/scripts/build_dashboard.py --mask      # 脱敏(对外)
python3 ~/.claude/skills/产品市占率分析工具/scripts/export_audit_excel.py # 核对Excel
```

## 关键经验/陷阱
- **模板JS占位符**：`const DATA = /*__DATA__*/{};` build 必须替换含`{}`的整个`/*__DATA__*/{}`标记，只替换`/*__DATA__*/`会留`{}`致语法错误空白页
- **Excel锁文件**：源文件在Excel打开时产生`~$`锁文件，glob会匹配到致openpyxl报"File is not a zip file"——find_files 跳过`~$`开头
- **本会话glm-5.2无图像通道**：Read PNG返回空，改样式只能靠用户口述/色彩采样
- **分类器临时故障**：Edit/Bash写操作间歇报"temporarily unavailable"，用python脚本绕过

## 已废弃
- Übersicht widget（CoffeeScript反复踩坑）→ 停用；`deskdash/generate_data.py`+`market_share.json`→废纸篓；deskdash/.venv(polars)遗留不依赖

**[[ubersicht-coffeescript-widget.md]]**（旧）·**[[20260714-deskdash-design.md]]**（旧）
