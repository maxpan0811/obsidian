---
title: 将 EPUB 电子书直接丢给大模型处理时，最常 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/将 EPUB 电子书直接丢给大模型处理时，最常 2.md
tags: [evernote, impression, yinxiang]
---

# 将 EPUB 电子书直接丢给大模型处理时，最常

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0MTEyODEzMA==&mid=264866...](https://mp.weixin.qq.com/s?__biz=MzI0MTEyODEzMA==&mid=2648666301&idx=1&sn=1afbb9552911a1fb3d41bc4caf12ccbf&chksm=f13b9710c64c1e06bce4f179b92bc176b358553e7825bd1e45e08ce67bf038fe332f3fc9bbbb&exptype=servicebox_7449741252527284224&subscene=0&scene=288&clicktime=1776156729&enterid=1776156729&flutter_pos=2&biz_enter_id=5&ascene=56&devicetype=iOS26.4.1&version=18004637&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQkZ1WCnM68Zo56wm5mXLloBLVAQIE97dBBAEAAAAAADC0ALEPWqgAAAAOpnltbLcz9gKNyK89dVj0jptKdrRDFktzyIeaKFQ2IrxgQ0e82BAblme53ZG0jDWY6a3gyLW/DaTjFzu5X5seZVi9ZuIijULBYF57IPh5QcHqBP+jlDsTeWos256iyrPQTh7MK5jQdUON+G8pR6QekeFHbvGwSnLdGG/OoUUIWvgliW6J2QoiwWXWO50NEIPgiZW0yQJo1p+dlhO2yk6BkRoEH9YO83ZhN+S8WBGweqxD7RKWg2ZOZtIc425FoA==&pass_ticket=aNMAc4rczKIwpFcrX5pR6bWQUnsUfPO86SG4NdSSTD5OWs5yL4cT8t83cFk3/22t&wx_header=3)

![](.evernote-content/481733AD-398F-4AE6-ABC9-F49CB7AE3F93/7D14253D-725A-456E-9C0D-D36B99DEDFE3.png)![](.evernote-content/481733AD-398F-4AE6-ABC9-F49CB7AE3F93/1D0DE8DE-A445-4A22-9B3E-494D3DE6E8BE.png)

将 EPUB 电子书直接丢给大模型处理时，最常见的问题是：完整转换后形成单一巨型 Markdown 文件，导致上下文窗口迅速耗尽、翻译质量不稳定、后续知识管理几乎不可能。

我制作的 leoyang1984/ebookSkill 这个项目，专门针对这个痛点设计。

它使用 Pandoc 完成 EPUB 到 GFM 的初始转换，同时提取全部图片到独立文件夹并保持相对路径。

核心是通过两级切分逻辑实现可控输出：首先按 # 和 ## 标题进行章节级分割，然后对超长段落（>200 行）在 200–300 行区间寻找自然断点（次级标题或段落结束）进行二次拆分。

额外提供 clean\_markdown.py 脚本，用于彻底清除 Pandoc 转换后残留的 、

等 HTML 标签，输出真正干净的 Markdown。

最有价值的部分是为 AI Agent 标准化了翻译 SOP：删除 full\_content.md 防止误操作、先生成领域术语 translation\_prompt.txt 并人工确认、再逐文件顺序翻译到 Translated/ 目录，天然适配 Claude / Gemini 等模型的长文本处理习惯。

特别适合 Obsidian 用户构建个人知识库，或需要高质量逐章翻译的技术/专业类书籍处理场景。

直接运行 python epub\_to\_md\_splitter.py 即可得到结构化拆分结果。

GitHub：https://github.com/leoyang1984/ebookSkill

#ContextEngineering#AIAgent

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI0MTEyODEzMA==&mid=2648666301&idx=1&sn=1afbb9552911a1fb3d41bc4caf12ccbf&chksm=f13b9710c64c1e06bce4f179b92bc176b358553e7825bd1e45e08ce67bf038fe332f3fc9bbbb&exptype=servicebox_7449741252527284224&subscene=0&scene=288&clicktime=1776156729&enterid=1776156729&flutter_pos=2&biz_enter_id=5&ascene=56&devicetype=iOS26.4.1&version=18004637&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQkZ1WCnM68Zo56wm5mXLloBLVAQIE97dBBAEAAAAAADC0ALEPWqgAAAAOpnltbLcz9gKNyK89dVj0jptKdrRDFktzyIeaKFQ2IrxgQ0e82BAblme53ZG0jDWY6a3gyLW/DaTjFzu5X5seZVi9ZuIijULBYF57IPh5QcHqBP+jlDsTeWos256iyrPQTh7MK5jQdUON+G8pR6QekeFHbvGwSnLdGG/OoUUIWvgliW6J2QoiwWXWO50NEIPgiZW0yQJo1p+dlhO2yk6BkRoEH9YO83ZhN+S8WBGweqxD7RKWg2ZOZtIc425FoA==&pass_ticket=aNMAc4rczKIwpFcrX5pR6bWQUnsUfPO86SG4NdSSTD5OWs5yL4cT8t83cFk3/22t&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/23788674-7b3e-426f-aa89-dbad6be4c428/23788674-7b3e-426f-aa89-dbad6be4c428/)
