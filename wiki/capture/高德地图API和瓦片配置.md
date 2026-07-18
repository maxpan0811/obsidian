---
title: 高德地图API和瓦片配置
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 高德地图API与瓦片配置经验

## 高德Geocoding API
- 注册：https://lbs.amap.com/（Web服务类型，免费5000次/天）
- 已有 `AMAP_KEY=2a5991fda0526a97e44180d711cb96eb`
- 运行：`python3 scripts/geocode_locations_amap.py --refresh`
- 合并：`python3 scripts/merge_geocoding_into_unified_kb.py`
- 全流程：`python3 scripts/build_data.py --geocode --publish-frontend`

## 地图瓦片源（中国可用）
- OSM `tile.openstreetmap.org` 被墙，地图空白
- 替换为高德瓦片：`https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}`
- 不需要API Key，渲染快

## Geocode替代方案
- Nominatim超时不可用
- DeepSeek API对古代中国地名坐标效果很好（70/70成功）

## Vite构建注意
- 修改`public/data/`后需 `npx vite build`，或手动复制到`dist/data/`
- 否则vite preview使用旧数据

## 本次产出
资治通鉴卷1：70地点/137角色/86事件/211关系
