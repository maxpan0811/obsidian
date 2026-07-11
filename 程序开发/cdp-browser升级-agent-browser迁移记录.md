---
date: 2026-07-09
tags: [browser-automation, agent-browser, cdp-browser, skill-upgrade, MCP]
---

# cdp-browser skill 升级：从 CDP+curl 迁移到 agent-browser CLI

## 背景

原 `cdp-browser` skill 走的是原始 CDP 路线——手动启动 Chrome (`--remote-debugging-port=9222`)，然后 `curl + Chrome DevTools Protocol` 做浏览器操作。缺点：

- 没有无障碍树和元素定位，每次操作必须先查 tabId
- 没有 `read` 命令（HTTP 级读页），读页面也得开浏览器
- 需要手动管理 Chrome 进程和 remote debugging 端口
- 没有登录态持久化方案

## 审计结果

机器上已有工具：
- **agent-browser** v0.26.0 ✅ (`~/.npm-global/bin/agent-browser`，Chrome for Testing v147 已安装)
- **Playwright** v1.60.0 ✅ (Homebrew 安装)
- **Playwright MCP** ✅ (已在 `~/.claude/.mcp.json` 配置)

但 coding agent 不会用 agent-browser——因为 skill 里写的是 curl 用法，不是 agent-browser 用法。只要把 cdp-browser skill 改写成 agent-browser wrapper 就够用了。

## 升级内容

完全重写 `~/.claude/skills/cdp-browser/SKILL.md`：1374 → 290 行，能力大幅提升。

### 能力变化

| 能力 | 之前（CDP+curl） | 之后（agent-browser） |
|------|------------------|---------------------|
| 开页面 | `goto <tabId> <url>` — 先查 tabId | `agent-browser open <url>` |
| 读页面 | 手动查 tabId + CDP DOM API | `agent-browser read <url>`（HTTP 级，不启动浏览器） |
| 定位元素 | 无 | `@ref` 无障碍树 / `find` 语义定位 / CSS 选择器 |
| 截图 | `snapshot <tabId>`（仅截图） | `screenshot --full` / `--annotate` 标注 ref |
| 浏览器管理 | 手动 `--remote-debugging-port=9222` | 自动管理 |
| 登录态 | 无 | `--session-name` 自动保存 / `--auto-connect` / `--profile` |
| 等待 | 无 | `wait @ref` / `--text` / `--url` / `--load networkidle` |
| JS 执行 | 无 | `eval --stdin` 支持复杂脚本 |

### 新增的工作流

1. **会话管理**：`--session-name` 自动保存 cookies + localStorage，跨重启保持登录
2. **`read` 命令**：不发请求启动浏览器，直接 HTTP 拿页面后转干净 Markdown（--outline / --filter / --llms）
3. **并行会话**：`--session a / --session b` 独立浏览器、独立 cookies
4. **自然语言操控**：`agent-browser chat "搜索xx并点击第一个结果"`

## 不装的东西

- **Playwright CLI**（`@playwright/cli`）：已有 Playwright MCP + agent-browser，两条路线都覆盖了，不重复安装
- **Puppeteer MCP**：和 Playwright MCP 竞品，仅在 Playwright MCP 遇到 Chromium 兼容性问题时按需补装

  安装方式：
  ```json
  {
    "mcpServers": {
      "puppeteer": {
        "command": "npx",
        "args": ["-y", "@puppeteer/mcp"]
      }
    }
  }
  ```

## 文章审阅要点

此前用户分享了一篇对比 agent-browser / Playwright CLI / Playwright MCP 的文章，审阅发现的缺口：

1. **Puppeteer MCP 完全被忽略**（Google 官方出品，与 Playwright MCP 直接竞品）
2. **`read` 命令的局限没讲**——对 SPA 页面（掘金等）只能拿到骨架 HTML，不是渲染后的正文
3. **缺少反检测维度**——Chrome for Testing vs 标准 Chrome 的指纹差异，Cloudflare 存活率
4. **中文场景没涉及**——npm registry 访问速度、snapshot 中文提取准确度、代理配置
5. **缺少 benchmark 数据**——CLI vs MCP 的实际 token 消耗差异没有量化
6. **缺少生态全景图**——Puppeteer MCP + Browserbase/Stagehand + Cline built-in browser + Browserless 不在视野内

## 原有 cdp-browser 命令对照

| 旧命令 | 新等价命令 |
|--------|-----------|
| `status` / `tabs` | `agent-browser tab` |
| `new <url>` | `agent-browser tab new <url>` |
| `goto <tabId> <url>` | `agent-browser open <url>`（自动管理） |
| `snapshot <tabId>` | `agent-browser screenshot [path]` |
| `query <tabId> getText [sel]` | `agent-browser get text [ref]` |
| `query <tabId> getHtml [sel]` | `agent-browser get html [ref]` |
| 手动 Chrome 启动 | agent-browser 自动管理 |
