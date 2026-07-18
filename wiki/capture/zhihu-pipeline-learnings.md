---
title: zhihu-pipeline-learnings
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 知乎知识库管线

## opencli zhihu download 注意事项

- **answer URL 标题丢失**：`opencli zhihu download --url` 对 answer 类型 URL 无法提取标题和作者，输出始终为 `untitled/untitled.md`，全部写入同一目录
- **必须每篇文章用独立输出目录**：否则后一次下载会覆盖前一次的 `untitled/untitled.md`，导致内容串错。用 `--output /tmp/zhihu_download/<url_hash>/` 解决
- **不要用 `--site-session persistent` 或 `--keep-tab true`**：持久化会话会导致浏览器状态混乱，所有下载返回同一篇文章的内容
- **首次下载需浏览器登录态**：opencli 打开 Chrome 窗口，需要用户已登录知乎才能获取完整内容；无登录态只能拿到 ~3407 字符的预览片段
- **zhuanlan 文章 URL 正常**：`zhuanlan.zhihu.com/p/xxx` 格式的 URL 可以正确提取标题和作者

## 用户偏好

- 不要 AI 摘要，不要类型/关键词分类
- 不要日期前缀（文件名直接用标题）
- 不要生成日报文件
- 每次只处理增量（按 URL 去重，processed.json 长期留存）
