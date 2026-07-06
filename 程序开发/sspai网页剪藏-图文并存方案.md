# sspai 网页剪藏方案 — 图文并存（Thrift API + Resource 嵌入）

## 背景

2026-07-03，保存 sspai.com 两篇付费专栏文章（Microsoft 365 工具升值包）到印象笔记。clipper gateway 的 `clipAndSaveNote` 只能拿到 SSR 预览（200-400 字），需要完整浏览器渲染 + 图片嵌入式保存。

## 问题链

| 尝试 | 结果 | 原因 |
|------|------|------|
| `clipAndSaveNote` | 只有 SSR 预览 | 服务端渲染，无登录态 |
| `createNoteFromMCP`（Markdown + 图片 URL） | 文字被截断，图片不显示 | API 有内容长度限制，不自动下载外部图片 |
| `createNoteFromMCP`（base64 data URI 嵌入） | payload 太大被截断 | 1.4MB+ payload 超 API 限制 |
| Thrift API + base64 hash | 资源存进去了但不显示 | `<en-media>` hash 格式错误（应为 hex 非 base64） |
| Thrift API + hex hash + 简略版文字 | 图片显示了但文字不全 | 手动缩略了原文 |
| Thrift API + Chrome 原始 HTML 自动解析 | **完整文字+10张图+表格** ✅ | 自动解析不遗漏 |

## 最终方案

### 流程

1. **Chrome 已登录** → 用户在 sspai 有订阅权限
2. **开启 AppleScript JS** → View > Developer > Allow JavaScript from Apple Events
3. **AppleScript 提取渲染后 HTML** → `execute tab javascript "document.querySelector('article.paid-article .article-body').innerHTML"`
4. **Python 解析 HTML** → 提取段落/标题/列表/表格，替换 `<figure>` 为 `<!--IMG_N-->` 占位符
5. **下载图片** → curl 加 `-H "Referer: https://sspai.com/"` 绕过 CDN 校验
6. **创建 Resource** → `types.Resource(data=types.Data(bodyHash=md5, size=len, body=data), mime=...)`
7. **ENML 内容** → hex 编码的 `<en-media alt="" type="..." hash="hex_md5"/>`
8. **Thrift API 创建** → `note_store.createNote(token, note)` 一次性提交文字 + 资源

### 关键教训

- `<en-media>` 的 `hash` 属性必须是 **hex** 编码（32 字符小写），不是 base64
- sspsai 图片 CDN 需要 `Referer: https://sspai.com/` 头，否则返回 403
- `createNoteFromMCP` API 不保存图片、有内容长度限制
- Thrift API (`evernote2` 库) 在 Python 3.14 需要 monkey-patch: `inspect.getargspec` + `getUserUrls(token)`
- `getUserUrls()` 在新版 API 需要 `authenticationToken` 参数

### 方法自动选择逻辑

```
用户发 URL + "保存" → 通用剪藏流程：
  1. clipAndSaveNote（最快，适用大多数普通网页）
  2. 如果 URL 域名在特殊名单 / 内容明显不完整 → 回退到浏览器渲染 + Thrift API

特殊处理名单：sspai.com（付费专栏）
检测指标：clip 结果中的文本长度 < 500 字 / 存在付费墙文字
```


---

## 完整对话记录

### 目标
保存 sspai.com 两篇付费专栏文章（Word 教程系列 "Microsoft 365 工具升值包"）到印象笔记。

### 第一轮：clipper gateway 失败
- 尝试：`clipAndSaveNote` API
- 结果：文字残缺、图片全无
- 原因：服务端 SSR 渲染，只拿到 200-400 字预览段

### 第二轮：Markdown + `createNoteFromMCP`
- 尝试：用 defuddle 提取 Markdown 后通过 createNoteFromMCP API 保存
- 结果：CDN 域名 DNS 沙箱内解析失败，需要 escalate
- 死胡同：API 会把 Markdown 存为纯文本，`![alt](url)` 图片不渲染

### 第三轮：clipper gateway 重试 + 登录态
- 用户登录 sspai 后重新尝试
- 但还是失败——clipper 服务端抓取的仍然是 SSR 预览

### 第四轮：CDP/Playwright + JS 提取
- 尝试启动 Chrome CDP（`--remote-debugging-port=9222`），一直无法启动
- Playwright `channel="chrome"` 超时 30 秒
- 根源：Chrome 已在运行，无法用同一 profile 启动第二个实例
- 用户开启 AppleScript JS 执行权限后，AppleScript 成功提取全内容

### 第五轮：base64 data URI 嵌入
- 下载 16 张图片 → base64 → 嵌入 Markdown
- `createNoteFromMCP` 返回成功，但内容被截断到 732 字节
- 原因：payload 太大（1.4MB + 8.3MB），API 静默截断

### 第六轮：Evernote Thrift API（base64 hash）
- 改用 evernote2 库 + `service_host='app.yinxiang.com'`
- Python 3.14 需要 monkey-patch `inspect.getargspec` + `getUserUrls(token)`
- 笔记创建成功，资源存进去了
- 但图片不显示——预览能看到缩略图，正文里空白

### 第七轮：hex hash 修补
- 对比已有笔记的 ENML，发现 hash 格式应为 **hex**（32 小写字符）而非 base64
- 修正后测试，图片可以显示了！
- 但文字是简略版（手动缩略了原文）

### 第八轮：完整原文重制
- 从 Chrome AppleScript 提取完整 HTML
- Python 自动解析 → 清理 ENML 不合规标签 → 提取图片/表格
- `<!--IMG_N-->` 占位符替换为 `<en-media>` 标签
- hex 编码 hash
- 最终：两篇文章图文完整、表格保留

### 第九轮：Playwright 统一方案讨论
- 想用 Playwright 替代 AppleScript 做统一方案
- 测试确认：Playwright 无法在 Chrome 已运行时用同一 profile 启动
- 结论：AppleScript 是登录态场景下的实用选择

### 最终结论
两条路，根据场景选择：
1. **简单网页** → `clipAndSaveNote` 最快
2. **付费/SPA 网页** → AppleScript + Chrome（复用登录态）→ Thrift API + ENML + Resource
