---
tags: [yinxiang, evernote, thrift, en-media, python-3.14, bugfix]
created: 2026-07-03
---

# 印象笔记 Thrift API 嵌入图片踩坑记录

## 背景

保存网页文章到印象笔记时，要求：
1. **只保存文章正文**，不保留导航/广告/页脚/关联文章
2. **图片必须嵌入**，不能仅存外链

## 尝试失败的方案

### ❌ clipAndSaveNote（服务器端剪藏）

```bash
curl -X POST "https://app.yinxiang.com/third/clipper-gateway/restful/v1/clipAndSaveNote" \
  -d '{"url":"URL"}'
```

- 保存整页含广告、导航、页脚
- 图片未正确保存为 Resource
- 无法控制只提取文章正文

### ❌ createNoteFromMCP（REST API，号称支持 Markdown）

```bash
curl -X POST "https://app.yinxiang.com/third/third-party-note-service/restful/v1/createNoteFromMCP" \
  -d '{"title":"T","content":"![](image.jpg)"}'
```

- **过滤所有图片引用**：`![](url)`、`<img src="">` 均被静默丢弃
- HTML `<img>` 同样被过滤
- 仅纯文本 Markdown（标题/列表/加粗等）保留

> 结论：该 REST API 只适合纯文本笔记，不支持图片嵌入。

## 最终方案：Thrift API + evernote2

选用 `evernote2` Python 库的 Thrift API 直接操作 EDAM：

### 核心流程

```
1. requests 抓取网页 HTML
2. BeautifulSoup 解析 → 提取 <div class="ar_ar_con"> 内 <article>
3. 下载 <img> 的图片数据
4. 创建 Resource 对象（bodyHash 必须是二进制16字节！）
5. 替换 <img> 为 <en-media type="..." hash="...">
6. 清洗非 ENML 属性和标签
7. 构建 ENML 包装（XML 声明 + DTD + <en-note>）
8. Thrift NoteStore.Client.createNote(token, note)
```

## 关键踩坑（按严重程度）

### 🔴 1. `Data.bodyHash` 格式错误

**问题**：传了 `hashlib.md5(data).hexdigest().encode('ascii')`（32字节 hex 字符串）
**服务器表现**：静默丢弃 `<en-media>` 标签，Resource 虽保留但无法关联
**修复**：传 `hashlib.md5(data).digest()`（16字节二进制 MD5）

```python
# ❌
d.bodyHash = md5_hex.encode('ascii')  # 32 bytes ascii text
# ✅
d.bodyHash = hashlib.md5(img_data).digest()  # 16 bytes binary
```

### 🔴 2. img→en-media 替换必须在属性清洗之前

**问题**：先清洗属性 → `data-hash` 被删（不在 ENML 允许列表）→ img 变空 → en-media 未生成
**修复**：先替换再清洗

```python
# 正确顺序
img['data-hash'] = md5_hex       # 1. 存hash
em = <en-media hash=md5_hex/>    # 2. 替换
img.replace_with(em)
# ...之后再 run 属性清洗
for tag in find_all(True):
    if attr not in ('href','src','type','hash'): del
```

### 🔴 3. HTML5 标签不是有效 ENML

**报错**：`Element type "article" must be declared.`
**修复**：`article_body.unwrap()` — 把 `<article>` 的子节点移出

ENML 只允许 XHTML 子集：
- ✅ `<p>` `<h1>`-`<h6>` `<ul>` `<ol>` `<li>` `<div>` `<span>` `<strong>` `<em>` `<en-media>` `<a>`
- ❌ `<article>` `<section>` `<header>` `<figure>` `<figcaption>` `<main>` `<nav>` `<aside>` `<footer>`
- ❌ `<br>`（需用 `<div>&nbsp;</div>` 代替换行）

### 🟡 4. Python 3.14 `inspect.getargspec` 已移除

evernote2 的 `Store.__getattr__` 委托使用 `inspect.getargspec`，Python 3.14 删除，需 monkey-patch：

```python
if not hasattr(inspect, 'getargspec'):
    from collections import namedtuple
    ArgSpec = namedtuple('ArgSpec', ['args', 'varargs', 'keywords', 'defaults'])
    def _getargspec(func):
        f = func.__func__ if hasattr(func, '__func__') else func
        sig = inspect.signature(f)
        # ... 兼容实现
    inspect.getargspec = _getargspec
```

## 完整可用脚本

```python
import requests, hashlib, os, re
from bs4 import BeautifulSoup
from evernote2.edam.type.ttypes import Note, Resource, Data, ResourceAttributes
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol
from evernote2.edam.notestore import NoteStore as NS

def create_note_with_image(token, page_url, note_title, article_selector):
    '''保存文章到印象笔记，正文无广告，图片内联嵌入'''
    # 1. 抓取页面
    resp = requests.get(page_url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    article = soup.select_one(article_selector)
    
    # 2. 下载图片 + 创建 Resource
    resources = []
    for img in article.find_all('img'):
        img_data = requests.get(make_abs_url(img['src'], page_url), ...).content
        md5_bin = hashlib.md5(img_data).digest()       # 16 bytes!
        d = Data(); d.body = img_data; d.bodyHash = md5_bin
        r = Resource(); r.mime = 'image/jpeg'; r.data = d
        resources.append(r)
        img['data-hash'] = hashlib.md5(img_data).hexdigest()
    
    # 3. 先替换 → 后清洗（顺序重要！）
    for img in article.find_all('img'):
        em = soup.new_tag('en-media')
        em['hash'] = img['data-hash']; em['type'] = 'image/jpeg'
        img.replace_with(em)
    
    for tag in article.find_all(True):
        for attr in list(tag.attrs):
            if attr not in ('href','src','type','hash'):
                del tag.attrs[attr]
    
    # 4. Thrift 创建
    enml = f'<en-note>{article}</en-note>'
    note = Note(); note.title = note_title; note.content = enml; note.resources = resources
    note_store.createNote(token, note)
```

## 最终成品

笔记 GUID：`73133fd5-b82a-4796-b9ee-118dd5e1997c`
- 正文纯净（无广告/导航/页脚）
- 图片嵌入为 Resource（131KB, JPEG）
- ENML 包含 `<en-media>` 标签
- 来源链接标注在文末
