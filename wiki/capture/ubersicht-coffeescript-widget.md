---
title: ubersicht-coffeescript-widget
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Übersicht CoffeeScript Widget 调试经验

## 编译失败根因
1. **目录名过长/含特殊字符**：`market-share.widget` 编译失败，改用短名 `ms.widget` 成功。原因是 CoffeeScript 编译器或 browserify 对长目录名处理有问题
2. **自定义方法不可用**：Widget 内部不能定义额外方法（`_render: () ->`），所有逻辑必须在 `render` 函数内。Custom methods via `@_render()` 不被 Übersicht 的 widget 生命周期识别
3. **try/catch 语法**：不能 inline 写 `try ... catch return`，必须用多行块
   ```coffeescript
   # ❌ 错误
   render: (output) -> try d = JSON.parse(output) catch return 'error'
   # ✅ 正确
   render: (output) ->
     d = null
     try
       d = JSON.parse(output)
     catch
       return '<div id="ms">Error</div>'
   ```
4. **afterRender 的交互**：在 afterRender 中用 `domEl.innerHTML = @render(JSON.stringify(@_data))` 可以重新渲染，但 @render() 会重新解析 output 字符串。正确做法是用实例变量存 `@_data` 然后调用渲染逻辑

## Widget 显示配置
- 配置文件：`~/Library/Application Support/tracesOf.Uebersicht/WidgetSettings.json`
- 必须同时设置：`showOnMainScreen: true, screens: [0], showOnSelectedScreens: false`
- Übersicht 启动后会覆盖配置文件（对未成功编译的 widget 重置设置），所以先确认编译成功再设置
- 重启 Übersicht 的正确方式：`ps aux | grep bersicht | awk '{print $2}' | xargs kill -9`
- `killall Übersicht` 因 `Ü` 特殊字符可能失败

## 数据口径注意
- 参考文件用 `目的地国家_归属业务区域` 定义欧洲（东欧+巴尔干/北欧/南欧/英爱/西欧），非 `考核区域`
- 渠道市占率分析现存脚本使用 CSV 文件（路径 `/Users/panbo/Documents/业务数据/artnova/`），目前数据已改为 XLSX（路径 `~/Documents/artnova/`）

**Why:** 多次调试 Übersicht widget 编译失败，需要记录已知陷阱避免重复踩坑

**How to apply:** 新建 Übersicht widget 时：用短目录名、不用自定义方法、用多行 try/catch、物理重启用 kill -9
