---
name: superpowers-v6-sheng-ji-fable5-zhong-gou-ji-lu
type: source
tags: [superpowers, fable5, codex-plugin, skill-framework, upgrade]
source_path: /Users/panbo/Obsidian/程序开发/Superpowers-v6升级-Fable5重构记录.md
---

[摘要]
本文记录了Superpowers从v5.x升级到v6.1.1的过程。Superpowers v6使用Fable 5完全重构，核心优化包括构建耗时降低约50%、token消耗降低约60%。

原文引用的关键改进：Fable 5内置autoresearch loop，用Opus当协调者，批量跑25组以上实验持续36小时，烧掉约650美元算力。发现反直觉结论：精简reviewer指令让输出压缩41%且判断质量不受影响；去掉流程步骤旁白再省54%且零方差。按任务复杂度动态分配模型（简单任务用haiku，复杂自动拒绝降级）。去Claude Code方言化，技能描述使用通用表达。新增Kimi Code、Pi、Antigravity三个harness。brainstorming可视化功能换了更安全的实现方式。

升级前组件版本：Codex官方市场版v5.1.3、git repo v5.1.0、旧Claude CLI插件v5.1.0。升级步骤：cd ~/.superpowers && git pull拉取最新代码、codex plugin remove superpowers@openai-api-curated移除旧版、codex plugin marketplace add ~/.superpowers添加本地repo为marketplace源、codex plugin add superpowers@superpowers-dev安装v6.1.1。

关键补记：Codex插件安装仅装到~/.codex/plugins/插件缓存，但CLI agent读取的技能来自~/.codex/skills/，该目录下全是到~/.claude/skills/的软链接。因此需要手动遍历替换14个技能目录的软链接，最终形成.codex/skills/xxx -> .claude/skills/xxx -> .superpowers/skills/xxx的三级链路。验证清单包括task-reviewer-prompt.md合并、参考文件修剪、using-superpowers引导压缩至3063字节、14个技能软链接两端就位、本地marketplace来源~/.superpowers。
[摘要]

原文链接: /Users/panbo/Obsidian/程序开发/Superpowers-v6升级-Fable5重构记录.md