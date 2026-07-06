# 公众号文章 CDP 批量保存到印象笔记方案

**日期**：2026-07-04
**工具**：印象笔记文章保存 Skill（印象笔记文章保存）

---

## 背景

通过 CDP（Chrome DevTools Protocol）方式连接 headless Chrome 浏览器，批量抓取微信公众号文章并保存到印象笔记工作篮。

---

## 核心流程

### 1. 启动 Headless Chrome（remote debugging port 9222）

```bash
nohup "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 --no-sandbox --headless=new --disable-gpu \
  &>/tmp/chrome.log &
sleep 4
```

### 2. 执行 CDP 脚本批量保存

```bash
cd ~/.claude/skills/印象笔记管理工具 && source .env
python3 /tmp/save_articles_via_cdp.py <URL1> <URL2> ... <URLN> 2>&1
```

### 3. 去重（清理旧版本）

```bash
cd ~/.claude/skills/印象笔记管理工具 && source .env
nohup python3 scripts/dedup_evernote.py --date $(date +%Y-%m-%d) \
  &>/tmp/dedup_$(date +%Y%m%d).log &
```

---

## 验证记录

| 批次 | 日期 | 数量 | 成功率 | URL 类型 |
|------|------|------|--------|----------|
| 首批 | 2026-07-01 | 10 篇 | ✅ 10/10 | 纯短链接 |
| 第二批 | 2026-07-04 | 4 篇 | ✅ 4/4 | 含 click_id、scene 参数 |

**总样本**：14/14 成功率 100%

---

## 2026-07-04 会话记录

### 保存文章列表

| # | 标题 | 内容块 | 图片 | 状态 |
|---|------|--------|------|------|
| 1 | 本地小模型的Claude Code来了，拆解它的完整 Harness！ | 94 | 13/13 | ✅ |
| 2 | 按照教科书学习初中理化，只能顺利毕业 | 49 | 5/5 | ✅ |
| 3 | 不抢抖音和小红书搜索，GEO就是残的 | 222 | 14/14 | ✅ |
| 4 | 美国记者拍摄的八路军 | 39 | 8/8 | ✅ |

### 保存结果

- **4/4 成功，0 失败** — 总耗时约 3 分钟
- 77KB 的完整对话已存入经验系统

### 关键技术决策

| 决策 | 替代方案 | 理由 |
|------|----------|------|
| CDP 方式（connect_over_cdp） | Playwright launch | 绕过 macOS sandbox MachPort 权限错误 |
| 一次性传全部 URL | 分次执行 | 节省 Chrome 启动时间，sandbox 杀不掉后台进程 |
| http://127.0.0.1:9222 | localhost | 避免 macOS IPv6 解析导致 ECONNREFUSED |
| 后台 nohup dedup | 前台执行 | 避免 779s API 限流阻塞工作流 |
| source .env 加载 token | 硬编码 | 避免提交密钥，印象笔记 token 有效期约 12 个月 |

### 知识点

1. **Chrome 启动 + CDP 必须在同一次 escalation 调用内** — sandbox 在两次调用之间会杀掉后台 Chrome 进程
2. **click_id / scene 追踪参数**不影响 CDP 保存，不会触发验证码
3. **walk() 处理长内容**验证正常 — 内容块最多 222 个（第 3 篇），无截断
4. **CDP 脚本路径**：`/tmp/save_articles_via_cdp.py`
5. **env 文件位置**：`~/.claude/skills/印象笔记管理工具/.env`
6. **笔记本 GUID**：`5a87b643-d40a-4d96-8999-e9d2aaf94b4f`（工作篮）
7. **dedup API 限流**：779s，需后台运行

### 技能文档更新

对应的 skill 文档 `~/.claude/skills/印象笔记文章保存/SKILL.md` 已更新：
- 新增 `/scene` 参数兼容说明
- 新增第二批验证记录表格
- 新增長內容（222 内容块）walk() 处理验证

### 经验持久化

memory 文件已保存到 `~/.local/share/codex-memory/20260704-evernote-batch-save-4.md`

---

## 常见问题

### Q: CDP 报 `ECONNREFUSED ::1:9222`
用 `http://127.0.0.1:9222` 替代 `localhost`。

### Q: dedup 跑了很久没响应
印象笔记 API 有后台处理延迟（最长 779s），建议 nohup 后台运行并检查日志。

### Q: 文章里的代码块格式乱了
少数科技号用嵌套 `<section>` 替代 `<pre>` 呈现代码块，walk() 有 allSectionChildren + padding 检测路径处理。

### Q: 保存后怎样验证
登录 https://app.yinxiang.com 检查"工作篮"笔记本。
