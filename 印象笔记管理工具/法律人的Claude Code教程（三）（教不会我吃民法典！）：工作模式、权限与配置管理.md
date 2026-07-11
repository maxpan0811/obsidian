# 法律人的Claude Code教程（三）（教不会我吃民法典！）：工作模式、权限与配置管理

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485791&idx=1&sn=84ae504404b5663e0a1cb9f4ed62efbd&chksm=c2547a82f523f3944535790de2529ba38d6afb66a8b1fd6dd567be2cddafbc9fe4c79a6013db&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRlkyWn4EoAaLOpJi/O5IhBLVAQIE97dBBAEAAAAAAAUADFF2ai0AAAAOpnltbLcz9gKNyK89dVj0Yco7hpj5mP/eQWC3PxCUqWCxro6HcXiZvRAqWjR+Ly1uIhFf+yXA0R96tqzpa944/1ToPw24M9w2RIHsDNXMQEaxIISsVUHTGxQeNAIjYMNJZYnZ7aRUcwGTs04cDjZlpG1qppwExSO78fA+C859L5Na1McSooIFKYXNwv+vW0ix0uZ6wWSnmxZyHQVJ/RNmeF56EQI/wkxHsDit09oAvzZoKY1Sf1wYh75XQQlakQ==&pass_ticket=Ma4XVhS+mbw9gDbZLjW7qh1WB5n9UH5rtbU+pEgDXNd/O3eXo74Tty19CwRgqjWs&wx_header=3)

法律人的Claude Code教程（三）（教不会我吃民法典！）：工作模式、权限与配置管理
============================================

积成 智律积成

上一篇教程，我们一起学会了 Claude Code 的基本操作——在终端里跟它对话、让它读文件、帮你干活。

[法律人的Claude Code教程（一）（教不会我吃民法典！）：安装与配置](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485751&idx=1&sn=33d24ddf860b6bdfd0fb9211a4cb979c&scene=21#wechat_redirect)[法律人的Claude Code教程（二）（教不会我吃民法典！）：十分钟掌握核心操作](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485775&idx=1&sn=ed1138eb730f4dc22440ed8ec360ae95&scene=21#wechat_redirect)

但我猜，你现在大概遇到了这样的问题：

你让 Claude Code 帮你审查一份合同。

它需要读取合同文件——弹窗确认。

它要创建一个审查意见文档——弹窗确认。

它想搜索一下关联条款——弹窗确认。

它要把修改建议写入文件——弹窗确认。

你点了十多次"允许"，合同还没审完，手指先累了。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/D42B56A9-C104-4941-8B41-54B79E71737B.png)

然后你想，行，下次我直接让它自动执行算了。

结果它一口气改了五个文件，其中有一个改错了——把客户名字都替换错了。

你才后知后觉：有时候，还是应该让它先说说想法，再动手。

***我用 AI，不就是为了少干这些重复劳动吗？怎么反而更累了？***

**真正的问题不在于 Claude Code 不聪明，而在于你还不知道怎么给它"档位"和"规矩"。**

就像带团队一样——新来的实习生，你得盯着他每一步；信任的老助理，可以放手让他干。但不管是谁，有些红线是不能碰的。

这一篇，我们就来搞定这件事。

---

三种工作模式：给 Claude Code 选个合适的"档位"
------------------------------

Claude Code 有三种工作模式，你可以把它们理解成汽车的档位。

不同的路况，挂不同的档。

---

### Default 模式：带新来的实习生

这是 Claude Code 的出厂设置。

当 Claude Code **首次使用某类工具**时——比如第一次读文件、第一次写文件、第一次执行命令——会弹出确认，等你点头才继续。

注意，不是每一步都问你。

如果你第一次已经允许了"读取文件"，后续再读其他文件就不会再弹了。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/7A7FC9F3-2490-45DC-9DC9-4FF066339AB7.png)

***第一次做某类事情之前先请示你，得到授权后同类事情就放手去做了。***

什么时候用 Default 模式？

* 你刚开始用 Claude Code，还在摸索
* 处理的是敏感文件，比如客户合同、诉讼材料
* 任务比较复杂，你需要确认 Claude Code 会用到哪些工具

不用做任何设置，打开 Claude Code 就是这个模式。

对于法律人来说，Default 模式其实是最安全的起点。

尤其是第一次让 Claude Code 处理某类任务，先用这个模式看看它的"工作习惯"，心里有底再放手。

---

### Plan 模式：让助理先出方案

这个模式很有意思——Claude Code 只分析、只规划，不动手。

你让它做什么，它会告诉你"我打算这样做"，列出步骤和思路，但绝不会碰任何文件。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/29BC363B-9A5D-40B4-8339-E86D06A883D6.png)

***先出一份案件分析方案，你审批通过了，再让他去执行。***

怎么切换到 Plan 模式？

按 `Shift+Tab`，会弹出模式选择器，选择 **Plan** 就行。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/99E0AA06-324F-43ED-960E-E3B36A1B3CE2.png)

或者直接输入 `/plan` 命令。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/A85B41A0-D5F3-4F89-8B24-22CDBA73BE11.png)

什么时候用 Plan 模式？

* 拿到一个新案件，先让 Claude Code 摸底
* 要处理大量文件，先让它列个清单
* 复杂任务，你需要先看看它的思路对不对

**法律场景举例：**

你接了一个新案子，对方发来一整个文件夹的材料——合同、往来邮件、付款凭证、聊天记录截图。

先开 Plan 模式，跟 Claude Code 说：

*"阅读这个文件夹里的所有文件，帮我整理出：当事人信息、关键时间线、双方争议焦点。"*

Claude Code 会通读所有材料，给你一份结构化的分析。

但它不会创建任何文件、不会修改任何内容。

你看完它的分析觉得靠谱，再切换到别的模式让它动手。

这就是 Plan 模式的价值——**先想清楚，再动手**。

跟我们做案件一样，先分析事实和法律关系，再写文书。

---

### Auto Accept 模式：信任的老助理

Auto Accept 模式下，Claude Code 会**自动接受文件编辑操作**，不再逐步问你。

读文件、创建文件、修改文件——一气呵成。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/17413BD7-8EE8-46F7-9191-01075B0ABF13.png)

不过要注意，某些高风险操作（比如执行 Bash 命令）仍然可能需要你确认，除非你在白名单里放行了。

***文件相关的事他自己就办了，但要动用"公章"（执行命令）还是会跟你请示。***

怎么切换到 Auto Accept 模式？

同样按 `Shift+Tab`，选择 **Auto Accept**。

什么时候用 Auto 模式？

* 批量处理多份类似文件
* 模板化、标准化的任务
* 你就在旁边盯着，随时可以按 `Esc` 喊停

**法律场景举例：**

你手上有 20 份格式类似的采购合同，需要逐份审查、标注风险点、生成审查意见。

合同模板你已经熟悉了，审查要点也跟 Claude Code 说清楚了。

开 Auto 模式，让它一口气跑完。

你泡杯咖啡，回来检查结果就行。

***注意：Auto Accept 模式自动接受的是文件读写和编辑操作。Bash 命令（比如执行脚本）仍然可能弹出确认，除非你已经在白名单里放行了。处理重要客户文件时，请确保你在旁边，随时准备叫停。***

---

### 怎么选？记住一个快捷键

记住一个快捷键就够了：`Shift+Tab`。

每按一次，模式按这个顺序轮换：

**Default → Auto Accept → Plan → Default → ...**

随时按，随时切。

***推荐工作流：Plan 模式先摸底，确认方案没问题，再切 Auto Accept 模式执行。***

这个流程特别适合法律工作——先分析，后执行，有理有据。

---

权限管理：给 Claude Code 立规矩
----------------------

模式是"临时档位"，你随时能切。

但如果你想让某些规则固定下来呢？

比如——"永远不要删除我的客户文件"。

这就需要配置权限了。

---

### 权限确认时的三个选择

在 Default 模式下，每次 Claude Code 要做操作，都会弹出确认。

这时候你有三个选项：

* **Yes**（允许一次）：就这一次，下次还得问我
* **Yes, and don't ask again for \_\_\_**（永久允许）：以后这类操作不用再问了
* **No**（拒绝）：不行，不许做

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/60549F69-5FC3-433A-96C6-2684F00143EA.png)

这里有个关键点：**三类工具，三种确认机制**。

| 工具类型 | 是否需要确认 | "Yes, don't ask again" 有效期 |
| --- | --- | --- |
| **只读工具**（读取文件、搜索内容等） | 不需要 | 直接执行，无需你点头 |
| **Bash 命令**（执行脚本、系统命令） | 需要 | 永久生效（按项目目录+命令记录） |
| **文件修改**（创建、编辑、写入文件） | 需要 | 仅当次会话，下次重新确认 |

这个设计很合理——读文件不会有风险，直接放行；命令行操作一般是确定性的，记住就行；而文件编辑每次内容不同，多确认一下更安全。

**法律场景：**

读取合同、搜索条款这些操作，Claude Code 直接就做了，不会打断你。

但 Bash 命令（尤其是 `rm` 删除之类）需要谨慎放行。

这样用着用着，Claude Code 就被你"训练"成了符合你工作习惯的助理——该放的权放了，该管的管住了。

---

### Settings 配置文件

如果你不想一个个点，想一次性把规矩定好，就用配置文件。

Claude Code 的配置文件分为两个层面——**全局**和**项目**，每个层面又分"共享"和"本地"两种。

**全局层（适用于所有项目）**

| 文件 | 路径 | 用途 |
| --- | --- | --- |
| 全局设置 | `~/.claude/settings.json` | 你主动配置的全局规则——模型、语言、权限等 |
| 全局本地设置 | `~/.claude/settings.local.json` | 日常点 "don't ask again" **自动积累**的权限 |

全局设置是你自己手动写的，比如：

json

{
"model":"opus",
"language":"Chinese",
"permissions":{
"deny":["Bash(rm \*)"]
}
}

全局本地设置则是 Claude Code 帮你维护的——每次你在权限弹窗点 "Yes, don't ask again"，那条规则就会自动记录到这个文件里。

你不需要手动编辑它，用着用着它自己就越来越"懂你"了。

**项目层（只对当前项目生效）**

| 文件 | 路径 | 用途 |
| --- | --- | --- |
| 项目共享设置 | `.claude/settings.json` | 会被版本控制，**团队成员共享** |
| 项目本地设置 | `.claude/settings.local.json` | 不会被版本控制，**仅你个人** |

项目共享设置适合放团队统一规则（比如"禁止删除文件"），所有人都会受到约束。

项目本地设置适合放你个人的偏好（比如你想多放行几个 Bash 命令），不影响其他同事。

**优先级从高到低：**

***项目本地 > 项目共享 > 全局***

就像律所有统一的办案规范（全局），你个人日常也积累了些习惯做法（全局本地），但具体到某个案子有特殊要求（项目共享），而你个人在办这个案子时还有一些自己的偏好（项目本地）。

最简单的配置方式：在 Claude Code 里输入 `/config` 命令，它会引导你完成配置，不用手动去编辑 JSON 文件。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/75FB8B3F-883D-47CB-BE62-C9BD8BF25EB4.png)

---

### 白名单和黑名单

这是配置文件里最核心的部分。

看一个例子：

json

{
"permissions":{
"allow":[
"Read",
"Write",
"Grep",
"Glob"
],
"deny":[
"Bash(rm \*)",
"Bash(curl \*)"
]
}
}

逐行翻译一下：

* `"Read"` — 允许读取文件（不再弹确认）
* `"Write"` — 允许创建和写入文件
* `"Grep"` — 允许搜索文件内容
* `"Glob"` — 允许查找文件
* `"Bash(rm *)"` — **禁止**删除文件（直接拦截）
* `"Bash(curl *)"` — **禁止**发送网络请求（防止数据外泄）

***白名单里的操作，Claude Code 直接做，不弹确认。黑名单里的操作，Claude Code 碰都不能碰。***

对法律人来说，这个设计太合理了。

你想想，我们平时带助理不也是这样吗——"这些事你直接做就行，但那些事必须先跟我说"。

---

### 危险模式：别碰

Claude Code 有一个"核弹级"选项：启动时加上 `--dangerously-skip-permissions` 参数，可以跳过所有权限检查。

***就像给助理签了一份全权委托书。***

**处理真实客户文件时，绝对不要用这个选项。**

它只适合一种情况：你在测试环境里跑自动化脚本，文件夹里全是测试数据，弄坏了也无所谓。

记住，光看这个参数的名字——"dangerously"——Anthropic 自己都在提醒你：这很危险。

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/6380B2F4-3FAB-429B-9C89-992D9680DAF2.png)

---

实战：两个法律场景的权限配置
--------------

下面我们用两个真实场景，看看怎么把权限配置用到实处。

---

### 场景一：独立律师——保护客户隐私文件

**你的情况：**

你在处理一个并购项目，工作目录是这样的：

并购项目/
├── .env# 存着客户 API 密钥
├── 客户名单.xlsx# 所有客户信息
├── 内部备忘.md# 你的办案思路，不想外泄
├── 合同审查/
├── 法律检索/
└── 尽职调查/

你让 Claude Code 帮你处理合同和检索资料，但不想让它读到 `.env`、`客户名单.xlsx` 这些敏感文件。

**配置方案：**

在项目根目录创建 `.claude/settings.local.json`：

json

{
"permissions":{
"deny":[
"Read(.env)",
"Read(客户名单.\*)",
"Read(内部备忘.md)"
]
}
}

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/2A1FC822-527B-4263-B63C-DF9567196DFD.png)

**效果：**

![](.evernote-content/BDFA73E7-9ED9-49C8-A201-388A77DB75AE/2B8DF659-082B-458F-954F-2923E8F759B9.png)

***就像给档案柜上了锁——有些抽屉能随便开，有些抽屉只有你有钥匙。***

---

### 场景二：带助理模式——放手文件，管住命令

**你的情况：**

你有个助理，刚学会用 Claude Code。

你希望他/她能用 AI 处理文书、整理材料，但担心他/她不小心执行了危险命令——比如 `rm -rf` 删错了文件夹。

**配置方案：**

json

{
"permissions":{
"allow":[
"Read",
"Write",
"Edit",
"Grep",
"Glob"
],
"ask":[
"Bash"
]
}
}

逐行解释：

* `allow` 里的工具 — 直接放行，不用确认（读文件、写文件、搜索内容等）
* `"Bash"` 放在 `ask` 里 — 每次要执行命令时，都弹窗让你确认一下

**效果：**

1️⃣ 助理让 Claude Code 写文书、改文件——不会弹确认，工作流畅

2️⃣ 但如果 Claude Code 要执行 `rm`、`curl`、`pip` 之类命令——必须助理确认

3️⃣ 你既给了助理自由度，又保留了一道安全阀

（此处可复用场景一的权限弹窗截图）

***就像给助理配了张门禁卡——办公室随便进，但要进财务室还得你签字。***

---

### 两种场景对比

| 场景 | 核心诉求 | 配置重点 |
| --- | --- | --- |
| 保护隐私 | 不让 AI 读敏感文件 | `Read(./文件路径)` 禁止读取 |
| 带助理 | 放手文件，管住命令 | `allow` 放行文件，`ask` 管住 Bash |

它们的共同点是：**从实际工作痛点出发，用最少的配置解决最担心的问题。**

***权限配置不是越多越好，而是越精准越好。解决你真正担心的问题就够了。***

---

小结
--

今天我们学了两件事。

**第一，三种工作模式。**

* Default：首次使用每类工具时确认，安全稳妥
* Plan：只读分析不动手，适合复杂任务的前期规划
* Auto Accept：自动接受文件编辑，适合批量处理
* `Shift+Tab` 随时切换

**第二，权限管理。**

* 三类工具有不同的确认机制：只读免确认、Bash 永久记忆、文件修改仅当次会话
* 用 settings.json 配置白名单和黑名单
* 全局 + 全局本地 + 项目共享 + 项目本地，四级管理
* 危险模式别碰

你现在已经能根据不同的任务，给 Claude Code 挂上合适的档位了。

也能给它立好规矩，让它在你划定的范围内干活。

这感觉是不是有点像……终于知道怎么管实习生了？

---

下一篇，我们要聊一个更有意思的东西：**CLAUDE.md 与上下文管理**。

简单说，就是给 Claude Code 写一份"岗位说明书"——告诉它你是谁、你做什么业务、你有什么偏好、你的工作流程是什么。

写好这份说明书，Claude Code 就不再是一个通用 AI，而是**你的专属法律助手**。

这大概是整个系列里最值得花时间的一篇。

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485791&idx=1&sn=84ae504404b5663e0a1cb9f4ed62efbd&chksm=c2547a82f523f3944535790de2529ba38d6afb66a8b1fd6dd567be2cddafbc9fe4c79a6013db&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRlkyWn4EoAaLOpJi/O5IhBLVAQIE97dBBAEAAAAAAAUADFF2ai0AAAAOpnltbLcz9gKNyK89dVj0Yco7hpj5mP/eQWC3PxCUqWCxro6HcXiZvRAqWjR+Ly1uIhFf+yXA0R96tqzpa944/1ToPw24M9w2RIHsDNXMQEaxIISsVUHTGxQeNAIjYMNJZYnZ7aRUcwGTs04cDjZlpG1qppwExSO78fA+C859L5Na1McSooIFKYXNwv+vW0ix0uZ6wWSnmxZyHQVJ/RNmeF56EQI/wkxHsDit09oAvzZoKY1Sf1wYh75XQQlakQ==&pass_ticket=Ma4XVhS+mbw9gDbZLjW7qh1WB5n9UH5rtbU+pEgDXNd/O3eXo74Tty19CwRgqjWs&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/80de2ec0-bcc4-4c69-a300-389088a76ee2/80de2ec0-bcc4-4c69-a300-389088a76ee2/)