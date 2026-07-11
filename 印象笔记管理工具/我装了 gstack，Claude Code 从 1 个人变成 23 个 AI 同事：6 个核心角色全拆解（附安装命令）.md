# 我装了 gstack，Claude Code 从 1 个人变成 23 个 AI 同事：6 个核心角色全拆解（附安装命令）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484817&idx=1&sn=a8bceee3e195e1df0f0a449c8f1704e0&chksm=f16ca25afdba49d6f153c992d67bee69d4d21cdb8682f12c549b667bfe28383ab5e9680fc283&scene=90&xtrack=1&req_id=1778641985117985&sessionid=1778641957&subscene=93&clicktime=1778642008&enterid=1778642008&flutter_pos=8&biz_enter_id=4&ranksessionid=1778641985&jumppath=20020_1778641976584,1104_1778641978681,20020_1778641984653,1104_1778641990733&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004926&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQEhczISESoY2z5FSnSSkg9RLVAQIE97dBBAEAAAAAAFdYEqeoedsAAAAOpnltbLcz9gKNyK89dVj0aornZhCNmVXnxv9XcJpS1jiGNo2VHoDdbXIXuLZqzNy3NCEJrCyG4y0UnHVKKO60xQLuVVXoN98AOTwO2zkyIi9+NKej1/ZRoiZQdcezpqUnTrBCeoh7ufmsGvmqh40Ll9PE5MJvMDrY0g6510svoxDjBWn2lAdimODrl3uF3jJGNaA4pst7URhCg9EMeNGoYrLojNFUjVySKaF2NBGtXeB8AVbCSCJYDWTTnLIAow==&pass_ticket=Z16GN1zsr+d1bnuHW/mL3KL46reY/i5eTkufmyOfMGvlWwsVEmyDZ9YLK37NNdvK&wx_header=3)

Original莲花明 AI落地手记

上个月有个采访让我看了三遍。

Karpathy 在 No Priors 上说：我已经基本没敲过一行代码了。

这话从写过 micrograd、教过斯坦福 CS231n 的人嘴里说出来，挺扎心。

但更让我注意的是另一条线——YC 总裁 **Garry Tan** 在差不多时间晒了他 2026 年的 GitHub 贡献图，绿格子密到看不见间隙。

他说他做的是同一件事，只是工具不一样了。然后顺手把自己的工具包开源了。

这个工具包叫 **gstack**。两个月，GitHub **89.7K star**。

![](.evernote-content/1F6ECA2C-DAC2-490A-A8B1-9C1D9B9DD496/F4EEA869-35B2-483E-AEA4-4301DB11542B.jpg)

这篇把 gstack 的 **23 个 AI 同事 + 8 个底层工具** 拆开，每一个是什么、怎么工作、为什么对你有用。

---

先看全局：23 个 AI 同事，三层架构
--------------------

gstack 不是一堆松散命令，它把工程团队拆成三层：决策层、执行层、守门层。每层管的事不同，缺一不可。

![](.evernote-content/1F6ECA2C-DAC2-490A-A8B1-9C1D9B9DD496/09DB9AF0-4E22-479D-96C3-1D88EA5E3566.jpg)

一个需求从想法到上线，要逐层穿过这三层关卡。下面我先拆每层最值钱的几个角色，再给完整命令表。

---

一、决策层：先想清楚，再动手
--------------

这一层管"该不该做、按什么架构做"。普通用 Claude 的人最少触发的一层——因为大家进来就想让 AI 写代码，不想再聊需求。

但 gstack 把它做成了强制流程。

① /office-hours —— YC 办公时间

▎ 一句话：用 YC 经典的六个灵魂问题逼你重新看产品。

⚠ 铁律：回答不出这六个问题，禁止往下走架构设计。

Garry Tan 在 YC 做了十年合伙人，每周给创业者开 Office Hours，问的就是这六个问题：

| # | 问题 | 为什么扎心 |
| --- | --- | --- |
| 1 | 你的用户是谁？精确到一个人。 | "程序员"不算用户，"独立开发者，周末用 SaaS 副业的人"才算 |
| 2 | 你解决的痛点，他们今天用什么凑合？ | 没有竞品 = 没有市场，不是你发现了蓝海 |
| 3 | 你的产品比凑合方案好 10 倍在哪？ | 只好 2 倍用户懒得换 |
| 4 | 为什么是现在？ | 5 年前能不能做？不能 → 时机对。能 → 凭什么轮到你 |
| 5 | 一个月之后，你怎么知道这功能成功了？ | 说不出指标 = 不该做 |
| 6 | 砍掉 60% 的功能只留核心，能不能用？ | 答"不行" = 你没想清楚核心是啥 |

真实场景：你说"加个用户行为分析后台"。Claude 触发 `/office-hours`，问完六个问题后你发现——用户根本不会看后台，他们要的是每周一封邮件总结。你省了三周开发时间。

② /plan-ceo-review —— CEO 视角重写需求

▎ 一句话：从商业价值角度审需求，砍掉不必要的功能。

⚠ 铁律：每个功能必须能答出"它为公司赚钱/省钱/留人在哪一条"。

需求被技术化是大公司的通病：业务方说"做个表单"，工程师做的就是"一个能填的表单"。CEO 视角会问：

• 这个表单填完之后呢？数据流向哪？**没有下游处理 = 数据死库存。**

• 用户填完之后能得到什么反馈？**没反馈 = 用户填一次再也不来。**

• 我们用这数据做什么决策？**没决策 = 这个表单不该存在。**

装上 `/plan-ceo-review` 之后，Claude 会自动用这套问法挑刺，把"做个表单"翻译成完整产品逻辑。

---

二、执行层：真正动手，但有分工
---------------

六个角色，是真正在写代码、做设计、跑测试的人。决策层想清楚之后，工作流交给他们。

③ /review —— Staff 工程师挑刺

▎ 一句话：从生产环境视角找代码隐患，能修的自动修。

⚠ 铁律：普通 review 看代码风格，/review 只看会不会出生产事故。

它专门盯这几类问题：

| 类别 | 示例 | 普通 review 会发现吗 |
| --- | --- | --- |
| N+1 查询 | 在循环里调数据库 | 不会，看代码很正常 |
| 竞态条件 | 两个请求同时改同一行 | 不会，单线程跑测试看不出 |
| 事务漏写 | 更新状态忘记 BEGIN | 不会，正常路径都成功 |
| 信任边界 | 前端传 user\_id 后端直接用 | 看到才知道，新人写常踩 |
| 幂等漏洞 | 回调接口能重复触发 | 不会，QA 一般不重复点 |

真实场景：你写完一个"批量审批"功能，跑 `/review`。AI 输出：「第 47 行循环里查了 user 表，对每个审批项查一次，1000 项 = 1000 次查询。建议改成批量 IN 查询。已自动修复。」

这种问题，普通工程师跑测试发现不了（测试 5 条数据当然秒过），上线之后批量审批 1000 条直接超时。

④ /qa —— QA 主管开真浏览器

▎ 一句话：启动持久 Chromium 进程，真的去点你的页面。

⚠ 铁律：Claude 说"测试通过"不算数，必须有浏览器截图为证。

这是 gstack 里最反 AI 味的一个命令。

普通 AI 助手做"前端测试"是怎么做的？读你的代码，分析逻辑，然后告诉你"看起来没问题"。

结果你打开浏览器——白屏。

`/qa` 不一样。它启动一个真实的 Chromium 进程，按你描述的用户流程一步步点：

![](.evernote-content/1F6ECA2C-DAC2-490A-A8B1-9C1D9B9DD496/B10D5260-5E86-4B50-A146-564EAF8AF85E.jpg)

`/qa 测试登录流程`

`[AI 启动 Chromium]`

`→ 访问 localhost:3000`

`→ 截图：登录页面正常`

`→ 输入测试账号`

`→ 点登录按钮`

`→ 等待跳转`

`× 卡在白屏 3 秒`

`× 查 console：401 未授权`

`× 定位：JWT 校验失败 (auth.ts:45)`

`[AI 自动修复] auth.ts:45`

`→ 重跑测试`

`✓ 登录成功，跳转 dashboard`

`✓ console 零报错`

`✓ 顺手补一条回归测试`

⚡ 关键设计：它用无障碍树（accessibility tree）定位元素，不是 CSS selector。这意味着你换皮肤、改样式不会让测试挂掉。响应时间 100-200ms，比常见的 Chrome MCP 方案快 20 倍。

---

三、守门层：上线前最后一道关
--------------

上线相关的活全在这一层。个人开发者最容易省略的——因为你一个人开发，谁还跟自己做安全审计？

gstack 把这步装进流程，等于强制你过最后一道关。

⑤ /cso —— 首席安全官

▎ 一句话：上线前跑一遍 OWASP Top 10 + STRIDE 威胁建模。

⚠ 铁律：安全漏洞修起来不贵，被攻破之后修就晚了。

OWASP Top 10 是全球公认的 Web 应用十大安全风险（注入、失效认证、敏感数据泄露……）。STRIDE 是微软的威胁建模框架，从六个角度看每个功能可能被怎么打。

`/cso` 会逐条扫你的代码，输出报告：

`[CSO 安全审查报告]`

`✓ A01: 访问控制 - 已用 RBAC`

`× A03: 注入漏洞 - 第 88 行 SQL 拼接未参数化`

`→ 建议改用 prepared statement`

`× A07: 身份认证 - JWT 未校验 issuer`

`→ 攻击者可伪造其他系统的 JWT`

`✓ A09: 日志告警 - 已接入 Sentry`

`[STRIDE 威胁建模]`

`× Tampering - 用户能改 user_id 提交`

`× Information Disclosure - /api/users 泄露邮箱`

`✓ Repudiation - 操作日志已审计`

独立开发者最容易跳过这步，但跳过之后被攻破的代价是项目直接关停。

⑥ /ship —— 发行工程师

▎ 一句话：一条命令完成：同步代码、跑测试、推远程、开 PR。

⚠ 铁律：每个 PR 必须自动跑通完整 CI，失败直接拦在 push 之前。

一个标准的发版流程，正常工程师要做 8 件事：

`1. git pull --rebase main`

`2. 解决 conflict`

`3. 跑 npm test`

`4. 跑 npm run build`

`5. git push`

`6. 在 GitHub 开 PR`

`7. 填 PR 描述（包括改了什么、怎么测的）`

`8. 加 reviewer、加 label`

装了 gstack 之后：跑 `/ship`，8 步全自动。PR 描述里还会自动列出本次改动的文件、新增的测试、潜在影响范围。

---

完整命令表：23 个 AI 同事
----------------

上面拆了 6 个明星角色，剩下的 17 个角色按层级列出来。你可以截图收藏。

![](.evernote-content/1F6ECA2C-DAC2-490A-A8B1-9C1D9B9DD496/3BD5B5AE-37CB-42DE-85B8-056E1AF3B926.jpg)

### 决策层（4个）

| 命令 | 角色 | 一句话 |
| --- | --- | --- |
| /office-hours | YC 办公时间 | 六个灵魂问题，逼你重新看产品 |
| /plan-ceo-review | CEO / 创始人 | 从商业价值角度重写需求 |
| /plan-eng-review | 工程经理 | 锁死架构和测试策略，不让方案漂 |
| /plan-design-review | 高级设计师 | 从设计维度打分 |

### 执行层（6个）

| 命令 | 角色 | 一句话 |
| --- | --- | --- |
| /review | Staff 工程师 | 挖生产 bug，能修的自动修 |
| /investigate | 调试工程师 | 系统化根因定位，不瞎猜 |
| /design-shotgun | 设计探索者 | 一次出 4-6 套设计稿让你选 |
| /design-html | 设计工程师 | 把设计稿真的变成 HTML |
| /qa | QA 负责人 | 开真浏览器跑测试，找 bug 顺手补回归用例 |
| /document-release | 技术文档官 | 改完代码自动更新文档 |

### 守门层（5个）

| 命令 | 角色 | 一句话 |
| --- | --- | --- |
| /cso | 首席安全官 | OWASP Top 10 + STRIDE 威胁建模 |
| /ship | 发布工程师 | 同步、测试、推送、开 PR 一条龙 |
| /canary | SRE | 上线后盯指标，发现回归就告警 |
| /benchmark | 性能工程师 | 页面加载基线对比，回归就拦 |
| /retro | 工程经理（复盘） | 每周回顾，按人拆数据 |

### 底层工具（8个）

还有 8 个不绑定角色的通用工具：浏览器自动化、文件批操作、依赖检查、性能监控、日志分析、配置生成、迁移脚本、模板渲染。这些被上面的角色按需调用。

---

一个完整的工作流长什么样
------------

用一个虚构场景串一遍。假设你要给一个内部系统加"审批流程"功能。

`1. /office-hours  —— 描述需求`

`AI：审批是给谁用？审批失败后能修改重提吗？`

`你：1 分钟回答 → 砍掉 30% 不必要功能`

`2. /plan-eng-review  —— 锁架构`

`AI：输出审批表结构 + 状态机图 + API 列表`

`你：1 分钟看完确认`

`3. （Claude 开始写代码，10 分钟）`

`4. /review  —— Staff 视角挑刺`

`AI：找到 1 个 N+1 + 1 个事务漏写，已修`

`5. /qa  —— 开真浏览器`

`AI：登录跑完整流程，3 处截图，零报错`

`6. /cso  —— 安全审一遍`

`AI：JWT 漏校 issuer，已补`

`7. /ship  —— 发版`

`AI：自动 push + 开 PR + 写描述`

你全程做了什么：**回答需求 1 分钟，看架构 1 分钟，看修复 1 分钟，批 PR 10 秒。**

Claude 做了什么：其他所有事。

---

谁不该装
----

老实讲，不是所有人都需要 23 个 AI 同事。

**如果你只是偶尔写点脚本**，gstack 太重了，杀鸡用牛刀。装个 Claude Code 自己用就够。

**如果你在有完整流程的团队里**，你们公司已经有 PR review、有 QA、有 SRE，gstack 的角色你大部分用不到——除非你想偷偷多干点活。

**真正适合的是个人开发者、独立创业者、小团队 Tech Lead**——一个人要顶五个岗位的那种。gstack 不是让你更快，是让你不漏关键流程。

---

它和 superpowers 不一样在哪
--------------------

看到这里你可能想到另一个东西——superpowers。Jesse Vincent 做的，150K star，6 个月。两个项目都是给 Claude Code 装"工作方法"，但思路完全不同。

|  | superpowers | gstack |
| --- | --- | --- |
| 核心隐喻 | 一套方法论 + 14 个技能 | 一支团队 + 23 个岗位 |
| 核心动作 | 强制 TDD + 强制需求确认 | 强制角色切换 + 强制完整流程 |
| 适合谁 | 想让 AI 写代码更严谨的人 | 想让 AI 替你管一个项目的人 |
| 学习成本 | 低（14 个技能名） | 中（23 个 slash 命令） |
| 触发方式 | SessionStart 自动注入 | 手动 slash 命令 |

**简单说：superpowers 教 AI 怎么把单个任务做对，gstack 教 AI 怎么把整个项目跑完。**

两个不冲突，可以同时装。明天那篇专门讲组合用法。

---

安装：两条命令
-------

`# 1. 装 Bun（gstack 依赖）`

`curl -fsSL https://bun.sh/install | bash`

`# 2. 装 gstack`

`git clone https://github.com/garrytan/gstack ~/.claude/skills/gstack`

`cd ~/.claude/skills/gstack && bun install`

`# 重启 Claude Code，所有命令生效`

装到 ~/.claude/skills/gstack/，不污染 PATH，不开后台进程，纯本地。

---

真实局限
----

一、它绑死 Claude Code。其他 IDE 用不了。

二、23 个角色需要时间消化。第一次装上你会面对一长串命令不知道先用哪个，建议从 /office-hours 和 /review 开始。

三、Tan 自己说他 60 天写了 60 万行代码——这个数据有争议，他在 README 里专门写了一段叫《关于 LOC 争议》解释方法论。看的时候带点理性，工具是工具，不是魔法。

**Repo 地址：**`github.com/garrytan/gstack`

**License：**MIT，完全开源

明天发组合用法：Superpowers + gstack 双剑合璧。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484817&idx=1&sn=a8bceee3e195e1df0f0a449c8f1704e0&chksm=f16ca25afdba49d6f153c992d67bee69d4d21cdb8682f12c549b667bfe28383ab5e9680fc283&scene=90&xtrack=1&req_id=1778641985117985&sessionid=1778641957&subscene=93&clicktime=1778642008&enterid=1778642008&flutter_pos=8&biz_enter_id=4&ranksessionid=1778641985&jumppath=20020_1778641976584,1104_1778641978681,20020_1778641984653,1104_1778641990733&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004926&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQEhczISESoY2z5FSnSSkg9RLVAQIE97dBBAEAAAAAAFdYEqeoedsAAAAOpnltbLcz9gKNyK89dVj0aornZhCNmVXnxv9XcJpS1jiGNo2VHoDdbXIXuLZqzNy3NCEJrCyG4y0UnHVKKO60xQLuVVXoN98AOTwO2zkyIi9+NKej1/ZRoiZQdcezpqUnTrBCeoh7ufmsGvmqh40Ll9PE5MJvMDrY0g6510svoxDjBWn2lAdimODrl3uF3jJGNaA4pst7URhCg9EMeNGoYrLojNFUjVySKaF2NBGtXeB8AVbCSCJYDWTTnLIAow==&pass_ticket=Z16GN1zsr+d1bnuHW/mL3KL46reY/i5eTkufmyOfMGvlWwsVEmyDZ9YLK37NNdvK&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/03d17a8e-cab0-4f5f-9593-306458fbea8f/03d17a8e-cab0-4f5f-9593-306458fbea8f/)