---
name: sspai-wang-ye-jian-cang-tu-wen-bing-cun-fang-an
type: source
tags: [yinxiang, evernote, web-clipper, thrift-api, sspai]
source_path: /Users/panbo/Obsidian/程序开发/sspai网页剪藏-图文并存方案.md
---

[摘要]
本文记录了保存sspai.com付费专栏文章到印象笔记时，从6次失败到最终成功使用Thrift API+ENML+Resource嵌入图片的完整踩坑过程。

问题背景：sspai.com的付费专栏文章（Microsoft 365工具升值包）需要保存到印象笔记，要求正文纯净无广告、图片嵌入式保存。尝试了7种方案：clipAndSaveNote只能拿到SSR预览（200-400字）；createNoteFromMCP写Markdown图片URL被静默丢弃；直接base64 data URI嵌入导致payload太大被API截断；Thrift API传base64 hash图片存了但不显示；用hex编码hash测试终于显示出图片但文字是简略版。

最终方案是Thrift API+Chrome渲染后HTML自动解析：用户已在Chrome登录sspai有订阅权限，开启AppleScript JS执行权限后通过AppleScript提取完整渲染HTML，Python解析HTML提取段落/标题/列表/表格并替换figure为占位符，用curl加Referer头绕过CDN校验下载图片，创建Resource对象（注意Data.bodyHash必须是16字节二进制MD5而非32字节hex字符串），构建ENML内容使用hex编码的en-media标签，通过Thrift NoteStore.createNote一次性提交文字+资源。

关键教训：en-media的hash属性必须是hex编码（32字符小写）不是base64；sspai图片CDN需要Referer: https://sspai.com/头否则返回403；createNoteFromMCP API不保存图片且有内容长度限制；Thrift API在Python 3.14需要monkey-patch inspect.getargspec和getUserUrls(token)参数；Playwright无法在Chrome已运行时用同一profile启动，AppleScript是登录态场景下的实用选择。

通用剪藏方法论：用户发URL+保存时优先用clipAndSaveNote（最快适用大多数网页），如果URL在特殊名单或内容明显不完整（clip结果文本长度<500字/存在付费墙文字），回退到浏览器渲染+Thrift API。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/sspai网页剪藏-图文并存方案.md