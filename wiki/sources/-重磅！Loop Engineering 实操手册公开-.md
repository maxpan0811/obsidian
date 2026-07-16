---
title: "重磅！Loop Engineering 实操手册公开"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/重磅！Loop Engineering 实操手册公开.md
tags: [evernote, impression]
---

---
title: "重磅！Loop Engineering 实操手册公开"
source: evernote
type: note
export_date: 2026-06-23
guid: b91365eb-bca4-404c-a024-68072e9f4144
---

# 重磅！Loop Engineering 实操手册公开

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIyNjM2MzQyNg==&mid=224772...](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723610&idx=1&sn=d5ba333d61fa85da41ce6078be801bd8&chksm=e9080fb73936582fb22b566ba36566d8c3d941db473617dea814fc58b7d41cb50281c6c7ad78&scene=90&xtrack=1&req_id=1782085476509671&sessionid=1782085036&subscene=93&clicktime=1782085864&enterid=1782085864&flutter_pos=7&biz_enter_id=4&ranksessionid=1782085476&jumppath=20020_1782085606115,1104_1782085743340,20020_1782085751655,1104_1782085854224&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQsu80n3sUKtaCNt7gD6Q0aBLTAQIE97dBBAEAAAAAALOqBDrAMakAAAAOpnltbLcz9gKNyK89dVj0+5787s3jWMdYvQ/k4AAb1QdBD/lXQmROpBOX9YP0aIUPpdpnil5WrfIVYvml1u0HgVg84qSwR6oYjf8zJzo64abJY8IoZ8Nbjc+9PzTVMr+ijvHfA9fJ/WQpdVIbPm+iXwdlE/HEIpVJe6mWVMoLqCIifmkJCQol2I9e5G40LdlCmXVhmsG6tCBJMZ4EIjoHC75DXulL48SjuLjF/TWGoVK7PKNjzO2+uQAoPpo=&pass_ticket=FZ5+CRyR0K7LMljejTjKBQWNKup5ja4UpM8dZDw7Qws0rW8t0xqs/HRE5JozWszg&wx_header=3)

OriginalDatawhaleDatawhale

# Datawhale干货  ******作者：Codez，X博主******

上周，我们分享了一篇《[提示词工程已死，Loop Engineering来了！》](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723482&idx=1&sn=52522523fc778c878f71c1d9061535e3&scene=21#wechat_redirect)带大家了解了Loop enigeering是什么。

今天我们分享由Codez总结的 14 步，全网220w人看过，讲的就是如何构建Loop Enigneering。

![](attachments/1122e0a209b47d9e.png)

内容综合自 Anthropic 的工程文档、Addy Osmani 关于 loop 工程的长文，以及最近几篇有实测数据的研究。

![](attachments/46a271374159ec92.png)

全文分为三个层次：先判断你到底需不需要循环，再学会五块积木，最后搭一个最小的、不会坑你的循环。

### 一、动手前：四个问题，决定你要不要 Loop Engineering

Loop 不是免费的。它烧 token、要花时间搭、出了问题你还得去 debug 一个你没亲眼看它跑的系统。所以先问自己四个问题，都想清楚之后，再动手。

**一、这个任务是重复的吗？Loop 的搭建成本靠多次运行摊回来。一次性的活，一个好 prompt 更快更省。**

**二、有没有东西能自动判定"这活干砸了"？测试、类型检查、linter、构建脚本，随便哪个都行。没有自动检查，你就得自己逐行读 diff，那 loop 就并没有帮你节省时间。**

**三、你的 token 预算扛得住浪费吗？**Loop 会反复读上下文、重试、试探，不管有没有产出都在烧 token。

**四、Agent 能跑自己写的代码吗？Agent需要有日志、能复现、看得到哪里崩。**

还有个附加题，比上面四个都重要：**你打算 review 它产出的代码吗?**不打算，就别建Loop。

谁适合上手

有强测试套件的团队，干 CI 失败分类、依赖升级、lint-and-fix、把 issue 转成 PR 草稿这类任务（重复、能机器校验、出事范围小）。

谁不适合上手

消费级套餐上的个人开发者、测试覆盖不够的代码库、瓶颈在 review 而不在打字速度的团队。

所以，loop engineering 真有用，但大部分人现在还用不上。

![](attachments/fa70d36d2cc425fd.png)

## 二、Loop Engineering 的五个核心构件

@0xCodez 把 loop 拆成五个构件。这个拆法好在每个都能单独用、单独试。

![](attachments/02924394d221c756.png)

**Automations——loop 的心跳。**按节奏触发（定时，或某个事件），跑完一轮，停下，等下一次。Codex 在 Automations 里配，Claude Code 用命令配。关键是停止条件要写死，别让它无限跑。

![](attachments/2f1bb6c408b74116.jpg)

**Worktrees——并行不打架。**多个 Agent 同时干活，最怕它们改同一个文件。Git worktree 给每个 Agent 一份独立工作区，互不干扰，最后再合。

**Skills——把背景写下来。**项目用什么框架、有什么约定、踩过什么坑，写成一个 skill 存着，Agent 每轮直接读，省得你每次从零解释。

**Connectors——连上真实工具链。**只能看文件系统的 loop 干不了几件事。通过 MCP 接上 GitHub（开 PR）、Linear/Jira（更新 ticket）、Slack（发汇总）、Sentry（查告警），loop 才算真正接入你的工作流。

**Sub-agents——写的和验的分开。**这可能是最有用的一个改造。写代码的模型给自己打分太宽容。换一个带不同指令的第二个 Agent 来验收，能抓到第一个自我说服过去的问题。loop 是在你不看的时候跑的，一个你信得过的验证器，是你能放心走开的唯一理由。

## 三、构建一个最小的 Loop

当我们确定要构建 Loop了，也别上来就建"全能系统"，先建能用的最小版：

![](attachments/3e0eb6b3ae52c4d8.png)

1. **一个 automation：**按节奏触发，按明确条件停。

2. **一个 skill**：存下项目背景，省得每轮重讲。

3. **一个状态文件**：记下做完了什么、下一步干啥，明天续上。

```
# Loop state · ci-triage  
## 上次运行  
2026-06-09 03:30 UTC · 7 个失败已分类，3 个草拟修复，4 个上报  
## 进行中  
- claude/fix-auth-token-refresh — 本地测试通过，等 CI  
## 今日完成  
- claude/bump-axios-1.7.4 → 已合并（CI 绿，依赖 loop 已验证）  
## 上报给人  
- src/billing/refund.ts — 测试三种崩法，根因不明  
## 经验教训（写这里，别写在聊天里）  
- 2026-06-08: 这台 Windows runner 上 PowerShell 撞 TLS 1.2 问题，改用 bash。
```

4. **一个闸门：**自动拒绝坏活的测试 / 类型检查 / 构建。

此时，顺序是十分重要的。先让一次手动运行稳定 → 做成 skill → 包成 loop → 再去调度。

搭好之后盯一个指标：**每个被接受的改动的成本**。如果接受率低于 50%，这 loop 就在亏本。

## 四、Loop 跑起来之后，会存在三种翻车和一个安全问题

loop 跑起来后，容易以三种方式翻车。

**一是假装干完了。**工程师 Geoffrey Huntley 管这叫 Ralph Wiggum 循环：Agent 提前发"完成"信号，活干一半就退。原因只有一个：没有硬闸门，缺少了测试和验收。

![](attachments/757ce75103654642.png)

**二是理解债务。**loop 越快交付你没写过的代码，"仓库里有什么"和"你理解什么"的差距就越大。有一天，你得 debug 一个团队里没人读过的系统。

**三是认知投降。** 你慢慢不再自己判断，loop 返回啥就收啥。所以，即使有了Loop，也要读 diff、抽查闸门、不让 loop 碰架构。

安全上还有一条红线：**无人值守的 loop，就是无人值守的攻击面。**

- 生成代码未审就上线：闸门里得加 SAST、依赖审计、密钥扫描。
- Skill 是注入入口：社区 17022 个 skill 里有 520 个会泄露凭证，自动安装前先读源码。
- 凭证泄露进日志：生产 loop 关掉 verbose 日志。
- 权限蔓延：今天加一个写权限，明天再加一个，每 30 天复审一次。

## 写在最后：构建Loop Engineering的 14 步路线图

最后，我们把上面整条路径压缩成一张清单：

**第一段 · 先想清楚要不要做（5 步）**

1. 确认这活是重复的：一次性的活，好 prompt 更划算

2. 确认有东西能自动判定"干砸了"：测试、类型检查、linter，至少一个

3. 确认 token 预算扛得住浪费：loop 不产出也照样烧钱

4. 确认 Agent 跑得了自己写的代码：有日志、能复现、看得到哪崩了

5. 确认你真打算 review 产出：不打算，就别建

**第二段 · 搭一个最小能跑的 Loop（8 步）**

6. 先让一次手动运行稳定下来：顺序别跳

7. 把项目背景沉淀成一个 Skill：省得每轮从零解释

8. 加一个状态文件：记下做完了什么、下一步干啥

9. 设一道硬闸门：测试 / 构建过不了就自动拒

10. 配一个 Automation：按节奏触发，用 `/goal` 设停止条件

11. 多个 Agent 并行就上 Worktree：别让它们改同一个文件打架

12. 接上 Connectors：让 loop 能开 PR、更新 ticket、发 Slack

13. 拆出 Sub-agents：写代码的和验收的分开

**第三段 · 上线之后守住（1 步，但最难）**

14. 盯住每个被接受的改动成本，定期复审权限、读 diff、别让 loop 碰架构

两年来，与编码 Agent 协作的杠杆一直在提示词上。更好的提示词、更好的上下文、更好的一次性输出。

而现在，工作流成了真正的护城河。

![](attachments/30dd10ec00f2ec8a.png)

**一起“**点****赞”****三连**↓**


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723610&idx=1&sn=d5ba333d61fa85da41ce6078be801bd8&chksm=e9080fb73936582fb22b566ba36566d8c3d941db473617dea814fc58b7d41cb50281c6c7ad78&scene=90&xtrack=1&req_id=1782085476509671&sessionid=1782085036&subscene=93&clicktime=1782085864&enterid=1782085864&flutter_pos=7&biz_enter_id=4&ranksessionid=1782085476&jumppath=20020_1782085606115,1104_1782085743340,20020_1782085751655,1104_1782085854224&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQsu80n3sUKtaCNt7gD6Q0aBLTAQIE97dBBAEAAAAAALOqBDrAMakAAAAOpnltbLcz9gKNyK89dVj0+5787s3jWMdYvQ/k4AAb1QdBD/lXQmROpBOX9YP0aIUPpdpnil5WrfIVYvml1u0HgVg84qSwR6oYjf8zJzo64abJY8IoZ8Nbjc+9PzTVMr+ijvHfA9fJ/WQpdVIbPm+iXwdlE/HEIpVJe6mWVMoLqCIifmkJCQol2I9e5G40LdlCmXVhmsG6tCBJMZ4EIjoHC75DXulL48SjuLjF/TWGoVK7PKNjzO2+uQAoPpo=&pass_ticket=FZ5+CRyR0K7LMljejTjKBQWNKup5ja4UpM8dZDw7Qws0rW8t0xqs/HRE5JozWszg&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/b91365eb-bca4-404c-a024-68072e9f4144/b91365eb-bca4-404c-a024-68072e9f4144/)
