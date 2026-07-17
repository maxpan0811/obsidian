---
title: Claude装太多，只会更废
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Claude装太多，只会更废.md
tags: [印象笔记]
---


Claude装太多，只会更废
==============

Originalde 大迁世界

上个月刚开始时，我的 Claude Code 里装了 31 个 skills。

一个月后，只剩下 8 个。

被我删掉的那 23 个，并不是坏了，也不是不能用。问题是：我根本没怎么用它们。很多 skill 都是六周前看到社交媒体帖子、Top 10 推荐清单后顺手装上的。装完之后，它们就安静地躺在那里。

可问题是，它们并不是“躺着不动就不消耗”。

每一个 skill 的 description，都会在每一轮对话里继续占据我的 context window。无论我有没有触发它，它都在消耗 token。Anthropic 自己的 playbook 里也提到过，skills 数量最好控制在 8 到 12 个以内。一旦超过这个范围，成本就开始显现。

超过之后，每一行多余描述，都是 context tax。

也就是说，这是模型必须支付的 token 成本，不管这个 skill 最后有没有真正帮上忙。

这次 audit 之后，我才看清一个差距：高级 Claude Code 配置，通常是 8 个

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->