---
title: evernote_python314_fixes
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Python 3.14 移除了 `distutils` 和 `inspect.getargspec`，影响 `save_article_playwright.py` 和 `dedup_evernote.py`。

**修复清单：**

### 1. inspect.getargspec monkey-patch
两个脚本都需在 imports 中添加：
```python
import inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
```
影响模块：thrift → evernote2 → oauth2 调用链

### 2. 移除 sys.path.insert(0, .../Python/3.9/...)
原来为了绕过旧版 thrift/evernote 添加了 Python 3.9 site-packages，但在 Python 3.14 下应直接用 pip3 安装的版本，避免 `distutils` 缺失问题。

### 3. Playwright 风控绕过
微信会检测 headless Chrome 的 `navigator.webdriver` 标志。需：
- launch args: `['--disable-blink-features=AutomationControlled']`
- context: 设置 `user_agent`（Mac Chrome）、`viewport`、`locale='zh-CN'`
- context.add_init_script: `Object.defineProperty(navigator, 'webdriver', {get: () => undefined})`
- 用 `wait_until="domcontentloaded"` + `page.wait_for_timeout(2000)` 替代 `networkidle`

### 4. 纯文本文章保存
已永久修复 0 图片时的强制退出逻辑。

### 5. updateNote 需要完整 Note 对象
Evernote `updateNote` API 要求传入的 Note 对象包含 title 字段。**不能只创建空 Types.Note() 再赋值 guid/notebookGuid**：
```python
# ❌ 错误：报 EDAMUserException(errorCode=2, parameter='Note.title')
note = Types.Note()
note.guid = guid
note.notebookGuid = TEMP
note_store.updateNote(TOKEN, note)

# ✅ 正确：先通过 getNote 获取完整对象
note = note_store.getNote(TOKEN, guid, True, False, False, False)
note.notebookGuid = TEMP
note_store.updateNote(TOKEN, note)
```

### 6. run_export.py exec() 缺失 __file__
`run_export.py` 用 `exec(f.read())` 运行 export_favorite_html.py，但 `exec()` 不传递 `__file__`。脚本中 `os.path.dirname(os.path.abspath(__file__))` 会因 __file__ 未定义而失败，且影响 processed.json 的路径定位。
```python
# ❌ 错误：FileNotFoundError（路径解析到错误位置）
exec(f.read())

# ✅ 正确：手动传入 __file__
exec(code, {'__file__': script, '__name__': '__main__'})
```

**Why:** 系统从 Python 3.9 升级到 3.14 后，多个库依赖的 deprecated API 被移除。
**How to apply:** 修改已在 `save_article_playwright.py` 和 `dedup_evernote.py` 中应用。新环境部署时参考此清单。
