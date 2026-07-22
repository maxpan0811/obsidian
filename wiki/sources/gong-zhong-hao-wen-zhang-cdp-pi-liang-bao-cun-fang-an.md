---
name: gong-zhong-hao-wen-zhang-cdp-pi-liang-bao-cun-fang-an
type: source
tags: [wechat, cdp, chrome-devtools-protocol, yinxiang, web-clipper]
source_path: /Users/panbo/Obsidian/程序开发/公众号文章CDP批量保存方案.md
---

[摘要]
本文记录了通过CDP（Chrome DevTools Protocol）方式批量抓取微信公众号文章并保存到印象笔记工作篮的完整方案，以及后续的defuddle回退方案和多次bug修复记录。

核心流程三步：启动Headless Chrome（--remote-debugging-port=9222 --headless=new）、执行CDP脚本批量保存多个URL、后台运行去重脚本清理旧版本。首批10篇100%成功，第二批4篇含click_id和scene参数也100%成功，总样本14/14。

关键技术决策与理由：使用CDP connect_over_cdp方式而非Playwright launch（绕过macOS sandbox MachPort权限错误）；一次性传全部URL而非分次执行（节省Chrome启动时间，sandbox会杀掉后台进程）；用http://127.0.0.1:9222而非localhost（避免macOS IPv6解析导致ECONNREFUSED）；后台nohup dedup（避免779s API限流阻塞工作流）；source .env加载token而非硬编码。

2026-07-08补充defuddle回退方案：当剪藏API返回code 10116（页面无法抓取）时，用defuddle CLI作为轻量级回退方案（无需headless Chrome，比CDP更轻量）。验证了公众号文章和百度资讯JS动态页的defuddle回退均正文完整。优先级策略是优先剪藏API，10116时降级defuddle。

2026-07-11修复CDP批量保存8个bug：section子节点不遍历、bodyHash编码错误（需16字节二进制MD5而非hex字符串）、en-media含非法style属性被拒绝、thrift缺getresponse()、img_hash_map映射错误、cleanParagraph跳过BR/STRONG导致英文文档结构乱、A标签javascript:;链接被拒绝、误判没有图片的人为失误。

2026-07-14修复图片抓取长期bug：walker和fallback都只查#js_content但图片可能分布在外层容器；fallback触发条件过严（只要walker找到文本块就跳过fallback导致0图）；懒加载data-src未注入。修复后测试文章从0图恢复到15图发现14图有效。

最后通过OpenClaw WeChat Connect插件（腾讯ilink API）实现微信到Codex的双向消息通道，弃用了iOS Shortcut+iCloud Drive的中间方案。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/公众号文章CDP批量保存方案.md