---
name: cdp-browser-sheng-ji-agent-browser-qian-yi-ji-lu
type: source
tags: [browser-automation, agent-browser, cdp-browser, skill-upgrade, mcp]
source_path: /Users/panbo/Obsidian/程序开发/cdp-browser升级-agent-browser迁移记录.md
---

[摘要]
本文记录了cdp-browser skill从原始CDP+curl方案迁移到agent-browser CLI的完整过程。

原方案走原始CDP路线：手动启动Chrome（--remote-debugging-port=9222），然后curl+Chrome DevTools Protocol做浏览器操作。缺点是没有无障碍树和元素定位、没有read命令（HTTP级读页也得开浏览器）、需要手动管理Chrome进程和remote debugging端口、没有登录态持久化方案。

审计发现机器上已有agent-browser v0.26.0、Playwright v1.60.0和Playwright MCP，但coding agent不会用agent-browser，因为skill里写的是curl用法不是agent-browser用法。升级方案是完全重写SKILL.md，从1374行缩减到290行。

核心能力变化：开页面从先查tabId再goto简化为agent-browser open <url>；读页面新增HTTP级read命令（不启动浏览器）；元素定位新增@ref无障碍树/find语义定位/CSS选择器；截图新增--full全页和--annotate标注ref；浏览器管理实现自动化；登录态新增--session-name自动保存/--auto-connect/--profile；新增wait命令支持@ref/--text/--url/--load networkidle；新增eval --stdin支持复杂JS脚本。

新增工作流包括：会话管理（--session-name自动保存cookies+localStorage跨重启保持登录）、read命令（不发动浏览器直接HTTP取页面转干净Markdown，支持--outline/--filter/--llms）、并行会话（--session a和--session b独立浏览器独立cookies）、自然语言操控（agent-browser chat搜索并点击）。

文章还对比了不安装的组件：Playwright CLI（已有Playwright MCP+agent-browser不重复）和Puppeteer MCP（仅Playwright MCP遇到Chromium兼容性问题时按需安装）。最后列出原有cdp-browser全部命令与agent-browser等价命令的对照表。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/cdp-browser升级-agent-browser迁移记录.md