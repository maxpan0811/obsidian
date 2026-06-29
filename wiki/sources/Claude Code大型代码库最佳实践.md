---
title: Claude Code 在大型代码库里的最佳实践
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=224751...]
source_path: 印象笔记管理工具/Claude Code 在大型代码库里的最佳实践.html
tags: [claude-code, best-practice, monorepo, large-codebase, architecture]
updated: 2026-06-27
---

---
title: "Claude Code 在大型代码库里的最佳实践"
source: evernote
type: note
export_date: 2026-06-27
guid: 9675177d-01a0-43d8-bbe6-137c64afc7e7
---

# Claude Code 在大型代码库里的最佳实践

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516785&idx=1&sn=d4e0c05fd5b0019f76e1c6306c89f9b5&chksm=e97b761b536758c37757b91703531e44c9c6c39f3d91bb3195088f21a3a5e377f39e9ad2fbdc&scene=90&xtrack=1&req_id=1779149128941840&sessionid=1779149155&subscene=93&clicktime=1779149173&enterid=1779149173&flutter_pos=1&biz_enter_id=4&ranksessionid=1779149129&jumppath=1001_1779149144667,1104_1779149156767,20020_1779149158817,1104_1779149164737&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ7zHwF6Q1R2vurPImm+YoBhK/AQIE97dBBAEAAAAAACZXDqHp1eoAAAAOpnltbLcz9gKNyK89dVj0cgNP9MN89zi2qr5792d1zpw983azY2Pn/sliUcZ5gUxWkE2IJvb2Py/9o99ndpC1QaJqSJGk1ScNsXi3IWxnkqvf2q2OxA4dZEnEAC/bUiE6iskPWJ8giw0qILxmlM18ss8e5zonWmJ28U7Y/x8BDdJMhJ4wCl/4Hx/x041kAaiqYrlRd15OdvT1o+CXIIBtENiuGirpfKkE&pass_ticket=O6BpemKus+PDz1JhPI3HqIc/XXUDnnb9vqAYyWEyVA1cgNbaCGtiLzFawAV0G71v&wx_header=3)

# Claude Code 在大型代码库里的最佳实践

Original字节笔记本字节笔记本

![](attachments/ec4a6158c80616bf.png)

Anthropic 上周发了一篇文章,讲 Claude Code 在企业级代码库里的最佳实践。

文中覆盖的场景包括百万行级别的 monorepo、跑了几十年的遗留系统、几十个微服务分散在不同仓库。

内容中包含了非常多针对于大型项目的精细化管理，非常值得学习和借鉴。

---

## CLAUDE.md的最佳实践

CLAUDE.md 分层写，不要全堆根目录。

Claude 在启动时自动加载CLAUDE.md,沿目录树向上查找，逐层叠加。

你可以这样组织:

```
repo/  
├── CLAUDE.md               # 全局约定:代码风格、提交规范、关键路径  
├── services/  
│   └── payments/  
│       └── CLAUDE.md       # 支付服务专属:测试命令、部署流程、特殊约束  
└── infra/  
    └── CLAUDE.md           # 基础设施专属:terraform 规范、云账号信息
```

根目录 CLAUDE.md 只放真正全局的内容:

```
# Repo 全局约定  
  
## 提交规范  
使用 conventional commits。feat/fix/chore,不要缩写。  
  
## 测试  
每个 PR 必须有对应测试。集成测试放 tests/integration/,单元测试和源码同目录。  
  
## 关键路径  
- 支付相关代码在 services/payments/,任何改动需要额外审查  
- 共享类型定义在 packages/types/,改动会影响所有服务  
- 不要直接修改 generated/ 目录,那是自动生成的
```

子目录 CLAUDE.md 只放局部的东西:

```
# 支付服务  
  
## 测试命令  
cd services/payments && go test ./... -tags=integration  
  
## 部署  
不要直接 kubectl apply。走 internal/deploy.sh,它会做 canary 检查。  
  
## 注意  
Stripe webhook 处理在 handlers/webhook.go。幂等性逻辑很脆,改之前读注释。
```

从 `services/payments/` 启动 Claude,它会同时加载两CLAUDE.md。根级上下文不会丢。

错误做法是把什么都堆进根目录。内容越多，每次会话的噪音越大，性能反而下降。

原则很简单，只放广泛适用的内容,专项知识放 Skills。

**从子目录启动,不要总从 repo 根目录启动**

其实这点和Codex APP的打开方式非常一致，详情在[10分钟Codex桌面端极速入门使用指南](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516504&idx=1&sn=47e2d155ffac039e35f6a1d9e5a14a78&scene=21#wechat_redirect)，从子目录进去效果明显更好。

```
# 不推荐:在 repo 根目录启动,上下文太宽  
cd ~/projects/myrepo  
claude  
  
# 推荐:在任务相关的子目录启动  
cd ~/projects/myrepo/services/payments  
claude
```

也不用担心根级的CLAUDE.md被丢失，因为它会自动地进行向上加载，不会丢失全局的约定。

**用 .ignore 排除噪音，权限配置提交到版本库**

一个非常小，但是见效特别快的配置。

生成文件、构建产物、第三方代码不应该出现在 Claude 的搜索结果里。

后续可以把排除规则提交进版本库,整个团队共享同一套配置:

```
// .claude/settings.json  
{  
  "permissions": {  
    "deny": [  
      "Read(.next/**)",  
      "Read(dist/**)",  
      "Read(node_modules/**)",  
      "Read(vendor/**)",  
      "Read(generated/**)",  
      "Read(**/*.pb.go)"  
    ]  
  }  
}
```

对于只在专门处理生成代码的情况，可以在本地的 `~/.claude/settings.json` 里覆盖，不影响其他人。

**对代码库结构写一份地图**

目录结构本身不够直观时,在根目录放一个 markdown 文件当索引。格式越简单越好:

```
# 代码库地图  
  
## 核心服务  
- services/api/       — REST API 网关,处理鉴权和路由  
- services/payments/  — 支付处理,对接 Stripe 和微信支付  
- services/notify/    — 消息推送,支持短信/邮件/APP  
  
## 基础设施  
- infra/terraform/    — 所有云资源定义  
- infra/k8s/          — Kubernetes manifests  
  
## 共享库  
- packages/types/     — 跨服务共享的类型定义  
- packages/utils/     — 公共工具函数  
  
## 不要碰  
- generated/          — proto 自动生成,不要手动修改  
- vendor/             — 依赖快照
```

几百个顶层目录的情况分层处理:根目录地图只描述最高层结构,子目录CLAUDE.md 提供下一层细节,按需加载。

**接 LSP 加速代码搜索**

这是大型代码库里收益最高的单项投入之一。

没有 LSP 时,Claude 搜一个常见函数名,在大型代码库里可能返回几千个匹配项:

```
# Claude 没有 LSP 时的搜索方式  
grep -r "handlePayment" .  
# 返回 3247 个结果,Claude 要逐个判断哪个是目标符号
```

接了 LSP 之后，Claude 能直接查"这个符号的所有引用"，过滤在 LSP 侧完成,结果精准:

```
# 通过 LSP 查询符号引用  
# → 只返回真正引用了 payments.HandlePayment 这个符号的 12 个调用点  
# → 不包含其他包里同名但不相关的函数
```

配置方式是安装对应语言的代码智能插件，再在机器上安装对应的 language server binary。Claude Code 文档里有各语言的插件列表和排错指引。

更多关于LSP的可以看这里：[Claude Code 2.0.74更新，越来越IDE了！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247511159&idx=1&sn=d27a36318b5dad7f8bf69221b4375dc9&scene=21#wechat_redirect)

---

## harness五个扩展点

Anthropic 把配置层叫做 harness，分五个扩展点。

**CLAUDE.md** 已经讲过了。每次会话自动加载，放全局约定。

**Hooks:确定性执行,不依赖模型记忆**

需要每次都执行的事情用 Hooks,不要用 prompt 提醒。

最常见的用法是写完文件自动跑格式化和 lint:

```
// .claude/settings.json  
{  
  "hooks": {  
    "PostToolUse": [  
      {  
        "matcher": "Write",  
        "hooks": [{  
          "type": "command",  
          "command": "npm run lint:fix"  
        }]  
      }  
    ]  
  }  
}
```

也可以在提交前做安全检查:

```
# .claude/hooks/pre-commit.sh  
#!/bin/bash  
# 阻止提交包含密钥的文件  
if git diff --cached --name-only | grep -qE '\.(env|key|pem)$|creds\.'; then  
  echo "BLOCKED: 检测到可能包含密钥的文件"  
  exit 1  
fi
```

Hooks 是确定性的，Skills 是概率性的。需要每次都发生的事情,不要靠 prompt 提醒模型，用 Hooks 保证执行。

Hooks 还有一个被低估的用途:Stop hook 在会话结束后运行，趁上下文还在可以触发任意脚本。

比如把会话摘要写入日志,或者提示工程师手动更新 CLAUDE.md:

```
{  
  "hooks": {  
    "Stop": [{  
      "hooks": [{  
        "type": "command",  
        "command": "echo '[会话结束] 如果发现新的代码约定,记得更新 CLAUDE.md' >> ~/.claude/session-reminders.log"  
      }]  
    }]  
  }  
}
```

更多关于Hooks的高级应用可以查看[AI编程高效开发指南](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIzMzQyMzUzNw==&action=getalbum&album_id=3955838883623043087&from_itemidx=1&from_msgid=2247515311#wechat_redirect)的[Hooks工作流！Claude Code Hooks的正确打开方式](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247506197&idx=1&sn=c6414715bd0e4e4788700faaa0fb9b3c&scene=21#wechat_redirect)

**Skills:上下文按需加载**

一个大型代码库可能有几十种任务类型。Skills 解决的是上下文膨胀问题:Claude 读取 skill 的描述,判断当前任务是否相关，相关才加载。

比如给支付服务单独写一个部署 skill:

```
<!-- services/payments/.claude/skills/deploy/SKILL.md -->  
---  
description: 支付服务的生产环境部署流程  
---  
  
# 部署支付服务  
  
## 部署前检查  
1. 确认所有集成测试通过: `cd services/payments && go test ./... -tags=integration`  
2. 检查 Stripe webhook 配置未变动  
3. 确认 feature flag 状态: `./scripts/check-flags.sh payments`  
  
## 执行部署  
```bash  
./internal/deploy.sh payments --env=production --canary=10%
```

等待 5 分钟观察错误率,无异常再执行:

```
./internal/deploy.sh payments --env=production --promote
```

## 回滚

```
./internal/deploy.sh payments --rollback
```

```
把这个 skill 放在 `services/payments/.claude/skills/` 下,它只在支付服务目录的会话里自动激活。在 `services/api/` 里工作时,这个 skill 不会出现在上下文里。  
  
还可以建一个安全审查 skill,只在涉及鉴权代码时触发:  
  
```markdown  
<!-- .claude/skills/security-review/SKILL.md -->  
---  
description: 安全相关代码的审查清单,涉及鉴权、加密、用户数据处理时使用  
---  
  
# 安全审查清单  
  
## 鉴权  
- [ ] 所有接口是否有鉴权中间件  
- [ ] JWT 有效期是否合理(不超过 24h)  
- [ ] 刷新 token 是否有轮换机制  
  
## 数据处理  
- [ ] 用户 PII 是否加密存储  
- [ ] 日志里是否有敏感字段泄露  
...
```

**Plugins:把好配置打包分发**

团队里往往只有少数人搭出了好用的配置，Plugin 解决分享问题。

Plugin 结构:

```
company-claude-plugin/  
├── .claude-plugin/  
│   └── plugin.json        # 插件元数据  
├── skills/  
│   ├── deploy/  
│   │   └── SKILL.md       # 部署流程  
│   └── security-review/  
│       └── SKILL.md       # 安全审查清单  
├── hooks/  
│   └── hooks.json         # lint、格式化、密钥检查  
└── mcp/  
    └── mcp.json           # 内部工具连接配置
```

如果有新的员工接手：

```
claude plugins install @company/claude-plugin  
# 安装后立即获得:部署流程 skill、安全审查 skill、自动 lint hook、内部搜索 MCP
```

拿到的是和之前完全一样的配置，不用从零摸索。

MCP:连接内部工具

MCP 让 Claude 访问它原本够不到的东西:内部文档、系统数据库、自建工具。

对大型代码库最直接的价值是把结构化代码搜索暴露给 Claude:

```
// .mcp.json  
{  
  "mcpServers": {  
    "codesearch": {  
      "command": "npx",  
      "args": ["-y", "@internal/codesearch-mcp"],  
      "env": {  
        "INDEX_URL": "https://search.internal.company.com",  
        "TOKEN": "${CODESEARCH_TOKEN}"  
      }  
    },  
    "jira": {  
      "command": "npx",  
      "args": ["-y", "@internal/jira-mcp"],  
      "env": {  
        "JIRA_URL": "https://company.atlassian.net",  
        "JIRA_TOKEN": "${JIRA_TOKEN}"  
      }  
    }  
  }  
}
```

接了内部搜索 MCP 之后,Claude 可以直接调工具查询:

```
# Claude 在会话里可以做的事:  
"查一下 handlePayment 这个符号在哪些服务里被调用"  
→ 调用 codesearch.find_references(symbol="handlePayment")  
→ 返回精确的跨 repo 引用列表,不是 grep 结果  
  
"看一下 PAY-1234 这个 ticket 的需求"  
→ 调用 jira.get_issue(id="PAY-1234")  
→ 直接读取需求描述,不用离开终端
```

---

## 配置要随模型版本迭代

Anthropic 建议每三到六个月做一次配置 review，在大版本模型发布后也做一次。

原因是模型能力在变。比如可能之前CLAUDE.md 里面可以这样写:

```
## 重构规范  
每次只改一个文件,改完确认无误再改下一个。
```

旧模型做跨文件重构时不行，但新模型跨文件协调能力强了，这条规则反而变成约束,让本来可以一次完成的重构被强制拆成十几步。

所以定期清理过期配置和写新配置一样重要。

review 的时候可以问自己，这条规则是为了弥补模型的局限写的，还是代码库本身的约定?前者要定期重新评估，后者长期有效。

---

## 组织层面怎么落地

技术配置做好了，在团队和公司中推广还是会卡在组织层面。

Anthropic 总结了几个规律。

**先把基础设施做好,再推给所有人**

推广效果好的团队，在大范围推广之前都有一个小的先行投入。

从最低配置版本开始，推广前一周，指定一个人把下面这几件事做完:

```
# 1. 写根目录 CLAUDE.md(全局约定)  
# 2. 把常见噪音文件加入 .claude/settings.json 的 deny 列表  
# 3. 把 lint/格式化 hook 配好并提交  
# 4. 写一份代码库地图(CODEBASE.md)  
# 5. 打包成 plugin,让所有人 install 即用
```

未来可能有一个专门的Agent Manager工程师。

这个角色类似于PM/工程师混合定位，管 CLAUDE.md 体系、Plugin 市场、权限策略,负责让好配置在组织内传播。

如果没有专职团队，最低配置是一个 DRI:一个人对整套 Claude Code 配置有决策权和维护责任。

具体工作包括:

```
- 维护根目录和各子系统的 CLAUDE.md  
- 管理公司内部的 plugin 版本和分发  
- 定期做配置 review(新模型发布后、采用率停滞时)  
- 收集各团队的好配置,整合进公司 plugin  
- 处理权限和安全策略(哪些工具 Claude 可以调用)
```

更多关于Claude Code的大型项目的实践，可以查看之前写的[Claude Code 长程任务的记忆管理方案](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516009&idx=1&sn=397712c1681433f6f60c1456e62fd9b5&scene=21#wechat_redirect)
