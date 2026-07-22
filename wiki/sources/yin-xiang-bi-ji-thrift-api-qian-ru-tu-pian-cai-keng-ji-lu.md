---
name: yin-xiang-bi-ji-thrift-api-qian-ru-tu-pian-cai-keng-ji-lu
type: source
tags: [yinxiang, evernote, thrift, en-media, python-3.14, bugfix]
source_path: /Users/panbo/Obsidian/程序开发/印象笔记-Thrift-API-嵌入图片-踩坑记录.md
---

[摘要]
本文记录了通过印象笔记Thrift API（evernote2库）嵌入图片的详细踩坑过程和技术要点。

任务要求：保存网页文章到印象笔记时只保存文章正文（不保留导航/广告/页脚/关联文章），且图片必须嵌入不能仅存外链。

两个尝试失败的方案：clipAndSaveNote（服务器端剪藏）保存整页含广告导航页脚，图片未正确保存为Resource；createNoteFromMCP（REST API号称支持Markdown）过滤所有图片引用（![]()、img src均被静默丢弃），只适合纯文本笔记不支持图片嵌入。

最终方案选用evernote2 Python库的Thrift API直接操作EDAM协议。核心流程：requests抓取网页HTML、BeautifulSoup解析提取正文容器内article、下载img图片数据、创建Resource对象、替换img为en-media标签、清洗非ENML属性和标签、构建ENML包装（XML声明+DTD+en-note）、Thrift NoteStore.Client.createNote创建笔记。

关键踩坑4个。最严重是Data.bodyHash格式错误：传了hashlib.md5(data).hexdigest().encode('ascii')（32字节hex字符串），服务器静默丢弃en-media标签；正确做法是传hashlib.md5(data).digest()（16字节二进制MD5）。其次是img→en-media替换顺序必须在属性清洗之前，否则data-hash被删后en-media找不到hash。第三是HTML5标签（article/section/figure等）不是有效ENML，需unwrap或替换为en-note允许的XHTML子集（ph1-h6/ul/ol/li/div/span/strong/em/en-media/a）。第四是Python 3.14移除inspect.getargspec，evernote2的Store.__getattr__委托依赖该函数，需monkey-patch（用collections.namedtuple和inspect.signature做兼容实现）。

完整可用脚本附在文末，包含从抓取页面到Thrift创建笔记的完整Python代码，最终笔记GUID 73133fd5-b82a-4796-b9ee-118dd5e1997c，正文纯净无广告，图片嵌入为Resource（131KB JPEG），ENML包含en-media标签，来源链接标注在文末。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/印象笔记-Thrift-API-嵌入图片-踩坑记录.md