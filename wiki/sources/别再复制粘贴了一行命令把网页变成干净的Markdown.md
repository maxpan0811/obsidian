---
title: 别再复制粘贴了！一行命令把网页变成干净的Markdown
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/别再复制粘贴了！一行命令把网页变成干净的Markdown.html
tags: [印象笔记, 其他]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "别再复制粘贴了！一行命令把网页变成干净的Markdown"
source: evernote
type: note
export_date: 2026-06-26
guid: 6bfcff69-9cf6-4ee0-83bb-ba4277232d4f
---

# 别再复制粘贴了！一行命令把网页变成干净的Markdown

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA4NzY0MTk1Ng==&mid=265022...](https://mp.weixin.qq.com/s?__biz=MzA4NzY0MTk1Ng==&mid=2650229301&idx=1&sn=a79376cfed685768aaf41c340f6b7332&chksm=8905ece27ceff65c11e8afe9f9f179950e17b606eb6a9f4dc4a1357b4074db7c41099fe7afb6&scene=90&xtrack=1&req_id=1779286821060079&sessionid=1779286675&subscene=93&clicktime=1779286852&enterid=1779286852&flutter_pos=3&biz_enter_id=4&ranksessionid=1779286821&jumppath=20020_1779286679377,1104_1779286817282,20020_1779286820518,1104_1779286848839&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQTIWmSuFMsxfEeHfkjKWuPBLTAQIE97dBBAEAAAAAAFxuElGUfFkAAAAOpnltbLcz9gKNyK89dVj0FtA9W6v27QepY/oPecX+7WWQndXhYuPVU7VbxzG2/PkHlyGoJDtKs7gV6jmTCXA+FomVnhzkB9I2toSam4y3TboLHVsBeI3yz31c9ZRUH7CYyIjK+PdlsDSyNxdth6HvJS8uZtMeUzIzjZdSe6R/shE1xJcFX/b3SVf910HLwNbqgdBh/lIOhsSrvA2WPc0JT8Ctk8nJlrG+ha1WiBrP6D7SrPDeoYOrFlafk7s=&pass_ticket=+7TYfUV7SfnXpz9lXfLR7Ez3RZTfAJ2GVLJVWMNh5SXBBqlBgQP5w3z85V8/lJ2e&wx_header=3)

# 别再复制粘贴了！一行命令把网页变成干净的Markdown

Original海潮 我们爱学习

你有没有遇到过这种情况：

看到一篇好文章，想保存到笔记软件，复制粘贴后格式全乱——图片丢失、代码块变形、多余样式干扰。

或者想用 AI 分析一篇技术文章，结果网页里一堆广告、侧边栏、评论区，AI 读了一堆噪音，分析结果一塌糊涂。

我之前也是这样，直到今天发现了一个神器：**playwright-to-md**。

一行命令，把网页变成干净的 Markdown。

话不多说，直接上干货。

---

## 1. 这玩意儿能干嘛？

先看效果：

npx playwright-to-md https://juejin.cn/post/7605416964510810139 -o article.md

一条命令，掘金文章变成干干净净的 Markdown 文件。

**核心能力：**

• 自动过滤广告、导航、评论等噪音

• 代码块、表格、图片链接完整保留

• 支持懒加载图片（`data-src`、`data-original` 都能识别）

• 能绕过反爬机制，抓取需要登录的内容

说白了，它就是一个"网页净化器"。

---

## 2. 为什么不用浏览器插件？

市面上确实有浏览器插件能做到类似的事情，比如 SimpRead（简悦）。

但问题是：**没有 CLI**。

这意味着什么？

• 你没法在脚本里批量处理

• 你没法让 AI 自动读取网页内容

• 你没法集成到工作流里

playwright-to-md 的核心价值，就是把这个能力搬到了命令行。

**你可以：**

• 写个脚本，批量抓取某个站点的所有文章

• 让 AI 直接读取干净的 Markdown，而不是一堆 HTML 噪音

• 在 CI/CD 里自动抓取网页内容

这就像是把"手动挡"升级成了"自动挡"。

---

## 3. 核心技术拆解

这个项目的技术实现相当扎实，我看了源码，拆解一下核心亮点：

### 3.1 真实浏览器，不是无头爬虫

这是最关键的一点：**playwright-to-md 用的是真实的 Chrome 浏览器**，不是那种简单的 HTTP 请求 + HTML 解析。

这意味着什么？

• **JavaScript 动态渲染的内容能拿到** — SPA 页面、懒加载内容、异步请求的数据，都能抓到

• **反爬检测能绕过** — 因为它就是"真的"浏览器，不是模拟的

• **登录态能复用** — 用 `--profile` 参数直接用你 Chrome 的 cookies

很多爬虫工具抓 SPA 页面是一抓一个空，因为内容是 JS 渲染的。

playwright-to-md 没有这个问题。

### 3.2 三级降级策略

规则匹配 → Readability → 通用选择器

• **Tier 1：规则匹配** — 内置 SimpRead 的数百条站点规则，精准提取

• **Tier 2：Readability** — 注入 Mozilla 的通用文章提取算法

• **Tier 3：通用选择器** — 兜底方案，尝试 `article`、`main`、`.content` 等

这个设计很聪明：对主流站点用精准规则，对未知站点用通用算法，确保"总能提取到内容"。

### 3.3 反检测机制

// 移除 webdriver 标志
Object.defineProperty(navigator, 'webdriver', {
  get: () => undefined,
});
// 自定义 UserAgent
userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/136.0.0.0'

很多网站会检测 `navigator.webdriver` 来判断是不是自动化工具。

playwright-to-md 直接把这些标志干掉了，模拟真实浏览器行为。

不过有个例外：**知乎**。

知乎会检测 CDP（Chrome DevTools Protocol），这个目前还没法绕过。

### 3.4 SimpRead 选择器语法

这个项目直接复用了 SimpRead 的规则库，支持的选择器语法非常丰富：

| 语法 | 说明 | 示例 |
| --- | --- | --- |
| `<tag class='x'>` | CSS 选择器 | `<div class='article'>` |
| `[[{ code }]]` | jQuery 表达式 | `[[{ $('article').text() }]]` |
| `[['text']]` | 文本移除 | `[['广告']]` |
| `[[/regexp/]]` | 正则移除 | `[[/\d{4}-\d{2}/]]` |
| `` [[`xpath`]] `` | XPath | `` [[`//article`]] `` |
| `a \|\| b` | 管道回退 | `<article> \|\| <main>` |

这些规则覆盖了掘金、知乎、CSDN、简书等主流中文技术社区。

---

## 4. 实战使用指南

### 4.1 安装

# 方式一：npx 直接运行（推荐尝鲜）
npx playwright-to-md https://juejin.cn/post/xxx
# 方式二：全局安装（推荐常用）
npm install -g playwright-to-md
to-md https://juejin.cn/post/xxx

**前置要求：** Node.js >= 18，系统已安装 Chrome 浏览器。

### 4.2 基本用法

# 输出到终端
to-md https://juejin.cn/post/xxx
# 输出到文件
to-md https://juejin.cn/post/xxx -o article.md

### 4.3 抓取需要登录的页面

使用 `--profile` 参数，复用 Chrome 的登录状态：

# macOS
to-md https://example.com/member-only -o article.md --profile "~/Library/Application Support/Google/Chrome"
# Windows
to-md https://example.com/member-only -o article.md --profile "C:\Users\你的用户名\AppData\Local\Google\Chrome\User Data"

注意：`--profile` 模式会启动可见的 Chrome 窗口，别关掉它。

### 4.4 处理动态加载的页面

有些 SPA 页面内容是 JS 动态渲染的，需要等一下：

# 手动指定等待时间
to-md https://example.com/spa-page -o article.md --wait 3000
# 加大超时
to-md https://example.com/slow-page -o article.md --timeout 60000

### 4.5 自定义选择器

当内置规则匹配不到时，可以用 `-i` 指定内容区域：

to-md https://example.com/article -i ".post-content"
to-md https://example.com/article -t "h1.title" -i ".article-body"

---

## 5. 我最常用的场景

### 5.1 让 AI 读干净的文章

这是最核心的用法。

以前想让 Claude 分析一篇技术文章，直接贴链接进去，AI 读到的是一堆 HTML 噪音。

现在：

to-md https://juejin.cn/post/xxx -o article.md

然后把 `article.md` 的内容丢给 AI，它就能专注分析正文了。

**效果提升非常明显。**

### 5.2 批量保存技术文档

写个简单的脚本：

#!/bin/bash
urls=(
  "https://juejin.cn/post/xxx1"
  "https://juejin.cn/post/xxx2"
  "https://juejin.cn/post/xxx3"
)
for url in "${urls[@]}"; do
  to-md "$url" -o "articles/$(basename $url).md"
  sleep 2  # 别太快，避免被封
done

一键把某个系列的所有文章保存成本地 Markdown。

### 5.3 搭配爬虫工具，效果翻倍

playwright-to-md 的定位是"内容提取器"，不是"爬虫"。

**它和爬虫工具是互补关系：**

• **爬虫工具**（比如 Scrapy、Puppeteer）：负责发现链接、遍历页面、处理分页

• **playwright-to-md**：负责把每个页面的内容提取成干净的 Markdown

举个例子：

# 用 Scrapy 发现文章链接
# 用 playwright-to-md 提取文章内容
import subprocess
def extract\_article(url):
    result = subprocess.run(
        ['to-md', url, '-o', f'articles/{hash(url)}.md'],
        capture\_output=True, text=True
    )
    return result.returncode == 0

**爬虫负责"找到"，playwright-to-md 负责"提取"。**

这种组合特别适合：

• 建立行业知识库（爬取整个站点的文章）

• 竞品分析（批量抓取竞品的技术文档）

• 舆情监控（抓取评论区、论坛帖子）

### 5.4 建立个人知识库

配合 Obsidian 这类笔记软件，把抓取的文章直接存进知识库。

以后想查什么技术点，直接在本地搜索，比去网上找快多了。

---

## 6. 避坑指南

### 6.1 知乎抓不了

前面说了，知乎会检测 CDP，目前没法绕过。

如果需要抓知乎内容，还是老老实实用浏览器插件吧。

### 6.2 动态页面要加 `--wait`

有些页面内容是 JS 动态渲染的，不加 `--wait` 可能抓到空白。

如果发现抓取内容很短，试试加 `--wait 3000`。

### 6.3 `--profile` 模式会弹浏览器窗口

这是正常现象，因为要复用 Chrome 的登录态。

运行期间别关掉浏览器窗口，不然会中断。

### 6.4 太快会被封

批量抓取时记得加延迟，不然容易被目标站点封 IP。

---

## 7. 总结一下

**playwright-to-md 的核心价值：**

• 用真实浏览器抓取，JS 动态渲染的内容也能拿到

• 三级降级策略，确保总能提取到内容

• 反检测机制，能绕过大部分反爬

• 支持复用登录态，抓取需要登录的内容

• 搭配爬虫工具使用，效果翻倍

**适合谁用：**

• 需要用 AI 处理网页内容的开发者

• 需要批量保存技术文档的人

• 想建立本地知识库的技术博主

• 需要做竞品分析、舆情监控的人

**一句话总结：** 这是一个让网页内容"为我所用"的利器。

---

我是海潮，专注全栈技术分享，深耕效率工具，关注我，一起成长、少踩坑 ✨
