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

---

## 2026-07-08 会话记录：剪藏失败的 defuddle 回退方案

### 背景
通过 Yinxiang 网页剪藏 API（`clipAndSaveNote`）保存微信公众号文章时，部分文章返回 `code: 10116`（页面无法抓取）。
发现 defuddle CLI 可作为轻量级回退方案（无需 headless Chrome，比 CDP 方案更轻量）。

### 问题发现

| URL 类型 | 剪藏 API | 处理方式 |
|----------|----------|----------|
| 阿里云开发者文章（developer.aliyun.com） | ✅ code 8200 | 直接剪藏 |
| CSDN 文章（blog.csdn.net） | ✅ code 8200 | 直接剪藏 |
| 公众号文章 `NWA_9bJ...` | ❌ code 10116 | defuddle 回退 |
| 公众号文章 `UqQtGC1...` | ❌ code 10116 | defuddle 回退 |
| 百度资讯 JS 动态页（mbdlite.baidu.com） | ⚠️ 内容残缺（仅标题） | defuddle 重新提取 |

### defuddle 回退流程

```bash
# 1. 用 defuddle 提取标题 + 正文
defuddle parse "$URL" -p title                     # 提取标题
defuddle parse "$URL" --md -o /tmp/article.md      # 提取 Markdown 正文

# 2. 调用 createNoteFromMCP API
curl -s -X POST \
  "https://app.yinxiang.com/third/third-party-note-service/restful/v1/createNoteFromMCP" \
  -H "Content-Type: application/json" \
  -H "auth: \$YX_AUTH_TOKEN" \
  -d "$(python3 -c 'import json,sys; print(json.dumps({"title":open("/tmp/title.txt").read().strip(),"content":open("/tmp/article.md").read()},ensure_ascii=False))')"
```

### 与 CDP 方案的对比

| 维度 | CDP 方案 | defuddle 方案 |
|------|----------|---------------|
| 依赖 | Headless Chrome | defuddle CLI（npm） |
| 启动 | 需 `nohup chrome &` + 等待 | 无需启动 |
| 渲染 | 完整 JS 渲染 | 仅 HTML 解析 |
| 图片 | 完整下载并嵌入 Resource | 图片以 URL 形式保留 |
| 成功率（已验证） | 14/14 | 3/3 |
| 适用场景 | 需要完整渲染/图片下载 | 仅提取文本正文 |
| 启动耗时 | ~4s | 0s |

### 验证结果

| 方式 | 公众号 1 | 公众号 2 | 百度资讯 |
|------|----------|----------|----------|
| 剪藏 API | ❌ 10116 | ❌ 10116 | ⚠️ 内容残缺 |
| defuddle 回退 | ✅ 正文完整 | ✅ 正文完整 | ✅ 正文完整 |

### 使用建议

1. **优先使用剪藏 API**（clipAndSaveNote）— 最简单，能处理图片
2. **10116 时再降级到 defuddle** — 无需启动 Chrome
3. defuddle 后如需图片，可在印象笔记中手动上传
4. **百度等 SPA 页面**即使 code 8200 也建议用 defuddle 验证内容完整性

### 相关技能更新

- `yinxiang-skill` v1.0.3 → **v1.1.0**
- 新增 `references/defuddle-fallback.md` 参考文档
- 场景二新增 10116 错误处理 → defuddle 回退说明

### 经验持久化

memory 文件：`memory/20260708-yinxing-10116-defuddle-fallback.md`

### 完整保存记录

| # | URL | 处理方式 | 结果 | 笔记 GUID |
|---|-----|---------|------|-----------|
| 1 | 阿里云开发者文章 | 剪藏 API | ✅ 8200 | `67db478a-8605-4848-a959-bbacf96a9469` |
| 2 | CSDN 文章 | 剪藏 API | ✅ 8200 | `d76e88ab-3d70-4ad8-a881-ca9781ef44bf` |
| 3 | 公众号 `gv3OfB...` | 剪藏 API | ✅ 8200 | `2c07064b-aa2e-4000-922a-1d5b7b81a1c7` |
| 4 | 公众号 `zFXVLA...` | 剪藏 API | ✅ 8200 | `73d1d80e-6469-48b1-9564-9908c0101ba1` |
| 5 | 公众号 `NWA_9bJ...` | 剪藏❌ → defuddle✅ | ✅ | `d5201725-c420-447e-ba40-ad7222df0c44` |
| 6 | 公众号 `AGoC19...` | 剪藏 API | ✅ 8200 | `78e5fad3-2431-42d8-99f9-eec96fa72d58` |
| 7 | 公众号 `JEiIa1...` | 剪藏 API | ✅ 8200 | `67c24831-2c81-4558-b42f-aab4b94b329c` |
| 8 | 公众号 `PJBi7K...` | 剪藏 API | ✅ 8200 | `d6d996d5-4e0b-496e-82e8-130780addef7` |
| 9 | 公众号 `UqQtGC1...` | 剪藏 API | ✅ 8200 | `da79a0ca-71b8-4b75-a88b-66abb079a543` |
| 10 | 百度资讯 JS 页 | 剪藏❌ → defuddle✅ | ✅ | `efed3151-25a0-468e-b57a-d2c63952f958` |

### 决策记录

| 决策 | 替代方案 | 理由 |
|------|----------|------|
| defuddle 作为回退方案 | CDP + Thrift API（更重，需 Chrome） | 轻量、无浏览器依赖、快 |
| 10116 时自动降级 defuddle | 始终用 CDP | 剪藏 API 大部分情况够用，只需兜底 |
| defuddle + createNoteFromMCP | 修改 defuddle 输出格式 | 直接复用现有 API，无需额外解析 |
| 先 try 剪藏 API | 直接 defuddle | 剪藏 API 能处理图片，优先用 |

## 2026-07-11: CDP 批量保存 bug 修复记录

### 背景
CDP 方式批量保存 8 篇微信公众号文章到印象笔记工作篮。脚本 `/tmp/save_articles_via_cdp.py`。

### 发现的 bug 及修复

| Bug | 表现 | 根因 | 修复 |
|-----|------|------|------|
| `<section>` 子节点不遍历 | walk() 检测到 0 张图片 | `if (tag === 'SECTION') { walk(el); return; }` — 递归同一元素，WeakSet 检查立即返回 | 改为 `for` 循环迭代 children |
| bodyHash 编码错误 | en-media hash 不匹配资源，图片不渲染 | `resource.data.bodyHash = hexdigest().encode()` (32 ASCII 字节) — 应为 16 字节 MD5 原始值 | 改为 `hashlib.md5(img_data).digest()` |
| en-media 含非法 style | 印象笔记拒绝渲染图片 | `<en-media style="max-width:100%;height:auto"/>` — ENML DTD 不允许 style | 移除 style 属性 |
| monkey-patch 缺 getresponse() | thrift HTTP response 为 None | `flush()` 发送请求后未读取响应 | 补充 `getresponse()` + code/message/headers |
| img_hash_map 映射错误 | en-media count=0 | `img_hash_map[src]` 存 URL hash，但 `resources_dict` 用 data hash | 改为 `img_hash_map[src] = data_hash` |
| cleanParagraph 跳过 BR/STRONG | 英文文档结构全乱 | `if(['BR','WBR','HR'].includes(tag)) return;` 丢弃所有换行和格式 | BR → `<br/>`；STRONG/B → `<strong>`；EM/I → `<em>`；SPAN → 保留 style；A → 保留 http href |
| A 标签 javascript:; 链接 | Evernote 拒绝：`Invalid a href attribute` | `href="javascript:;"` 未经过滤 | 仅在 href 以 http 开头时输出 `<a>` 标签 |
| 误判"没有图片"（人为失误） | 用户说"图片不显示"，我理解成"不需要图片" | 理解偏差 | 撤销图片过滤代码，正确修复 bodyHash + en-media style |

### 注意事项
- macOS 沙箱杀掉 Chrome 进程 → Chrome 启动 + Python 脚本必须在同一次 escalation 内
- 批量 URL 直接空格分隔传参
- 保存后建议后台运行 `dedup_evernote.py --date $(date +%Y-%m-%d)` 去重
- CDP 脚本需持续改进 walk() 的 DOM 覆盖率
