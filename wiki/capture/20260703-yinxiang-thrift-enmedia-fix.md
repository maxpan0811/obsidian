---
title: 20260703-yinxiang-thrift-enmedia-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 印象笔记 Thrift API 嵌入图片修复

## 问题

把网页文章保存到印象笔记时：
- `clipAndSaveNote`：保存整页含广告，图片可能缺失
- `createNoteFromMCP`（REST API）：支持 Markdown/HTML 但**丢弃所有图片引用**
- **唯一方案**：Thrift API + `<en-media>` + `Resource` 对象

## 关键踩坑

### 1. Python 3.14 `inspect.getargspec` 已移除

```python
if not hasattr(inspect, 'getargspec'):
    # 实现兼容补丁
```

Thrift 委托使用 `inspect.getargspec`，Python 3.14 已删除。

### 2. `bodyHash` 必须是二进制16字节

```python
# ❌ 错误：ASCII hex 字符串（32 字节）
d.bodyHash = md5_hex.encode('ascii')
# ✅ 正确：二进制 MD5（16 字节）
d.bodyHash = hashlib.md5(img_data).digest()
```

服务器校验 `bodyHash` 格式，不对则丢弃整个 `<en-media>`。

### 3. img→en-media 替换必须早于属性清洗

`data-hash` 属性不在 ENML 允许列表中，先删属性会丢失 hash 值。

### 4. HTML5 标签需 unwrap

`<article>`、`<section>`、`<header>` 等不是有效 ENML 标签。

## 完整工作流

1. fetch 页面 → BeautifulSoup 解析
2. 下载图片 → 创建 `Resource`（md5_bin for bodyHash）
3. unwrap 非 ENML 标签 → img 替换为 en-media
4. 清洗属性 → 生成 ENML
5. Thrift `createNote(note, TOKEN)` 提交
