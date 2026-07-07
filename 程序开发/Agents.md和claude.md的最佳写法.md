
## 你的观察完全对——而且这事儿有点意思

> **Codex 的 AGENTS.md 体系确实"照抄了"Claude Code 的 CLAUDE.md 写法**——但抄的是**写作范式**（给 agent 写 Markdown 指令这件事本身），不是**文件格式的机器解析语法**。所以能复用经验，但不能直接扔 CLAUDE.md 进去指望它理解。

---

### 先说清楚：抄了，但抄了一半

**Claude Code 的 CLAUDE.md 是整个行业的"项目指令文件"事实标准开创者**。在它流行之后，大家才开始认真思考"给 AI 代理写一份 Markdown 当它 onboarding doc"。OpenAI 推出 AGENTS.md 时，明面上说"vendor-neutral / Linux Foundation 标准"，但实际格式——章节怎么排、什么该写、什么不该写、用普通 Markdown 不用复杂 schema——**全盘沿用了 CLAUDE.md 建立起来的写作惯例**。

你第一次跑 `codex`/ `/init`看到生成的 AGENTS.md 骨架：

markdown

markdown

```
## Project Overview
Detected: TypeScript + React ...
## Build & Test Commands
- dev: npm run dev
...
## Coding Rules
...
```

这个骨架的结构思路、信息层级、甚至语气——就是从 CLAUDE.md 生态直接继承下来的。所以你说"照抄了"，**这个判断没错**。

---

### 那为什么不能直接读 CLAUDE.md？

因为两者的**解析层**不一样：

||CLAUDE.md|AGENTS.md（Codex）|
|---|---|---|
|**内容写法**​|普通 Markdown 指令 ✅|普通 Markdown 指令 ✅ ← 这块你经验100%可复用|
|**`@import path.md`**​|✅ 原生解析（把文件内容贴进来）|❌ 不认识这个语法，会把 `@import ...`当普通文本念一遍|
|**`allowed-tools: [Read, Grep]`**​|✅ 机器可读字段|❌ 没这个概念，Codex 的权限在 `config.toml`和审批模式里|
|**`disable-model-invocation`**​|✅ 控制开关|❌ 不存在|
|**`hooks:`事件钩子**​|✅ 有的版本支持|❌ Codex 有自己的 hooks 系统|

所以效果是这样：

- ✅ **你写在 CLAUDE.md 里的自然语言规则**——_"不许改 .env、跑测试再提交、三步以上任务先跟我确认"_——**一字不改就能搬到 AGENTS.md 里用**
    
- ❌ **你写在 CLAUDE.md 里的「机器指令语法」**——那些 `@import`、YAML frontmatter、工具白名单——**Codex 看不懂，也不会报错，只会默默忽略**
    

这就是"照抄了写法但没抄解析器"的矛盾感来源。

---

### 最聪明的做法：把你的 CLAUDE.md 经验拆成两层

不是"Codex 能不能学"，而是**你得把知识拆对**：

Pure Text

Pure Text

```
AGENTS.md  ← 【纯 Markdown 的"项目真理"层】
            ← 技术栈 / 命令 / 边界 / 工作流约束
            ← Codex 读 ✅  Claude Code 通过 @AGENTS.md 读 ✅

CLAUDE.md  ← 【Claude 专属桥接层】
            ← 第一行: @AGENTS.md
            ← 下面只写 Claude-only 的东西：
               allowed-tools / plan模式偏好 / thinking 级别
```

实际操作就三步：

bash

bash

```
# 1. 把你 CLAUDE.md 里"技术栈+命令+硬约束"那段提出来 → AGENTS.md
# 2. 原 CLAUDE.md 清空重写成桥接文件：
cat > CLAUDE.md << 'EOF'
@AGENTS.md

## Claude Code Only
- 三步以上任务用 /plan
- allowed-tools: 只开 Read, Edit, Bash(npm/pnpm/git)
- 禁止自行安装依赖，必须问我
EOF

# 3. 让 Codex 也能找到（symlink 保底）
ln -sf AGENTS.md .codex/AGENTS.md 2>/dev/null || true
```

之后你的经验**没有浪费一分钱**——同一份项目真理，两个工具各用自己的方式读。

---

### 一句话回答你

> Codex 抄了 CLAUDE.md 的**写作范式**（"项目指令该写什么、怎么排、写多长"），但**没有抄它的解析语法**，所以你 CLAUDE.md 里用自然语言积累的经验全部能用，但要手动把 `@import`/ `allowed-tools`这类"Claude 方言"剥离出去放到桥接层。AGENTS.md 就是那个共享层——**不是 Codex 学会了 CLAUDE.md，而是整个生态把 CLAUDE.md 的写法变成了通用货币，AGENTS.md 是它的脱品牌版本。**


## 直接回答：**Codex 默认不会读 CLAUDE.md，两者是不同的指令体系**

---

### 一句话结论

|工具|原生读的指令文件|会不会自动读对方的文件|
|---|---|---|
|**Claude Code**​|`CLAUDE.md`（以及 `.claude/CLAUDE.md`）|⚠️ 部分版本会**fallback 扫 AGENTS.md**，但不是主路径|
|**Codex CLI**​|`AGENTS.md`（以及 `AGENTS.override.md`）|**❌ 不自动读 CLAUDE.md**，只认 AGENTS 系列|

所以如果你已经有了一份精心调过的 `CLAUDE.md`，**不能直接扔给 Codex 说"你看着办"**——Codex 启动时扫描的是固定路径里的 `AGENTS.md`，路过 `CLAUDE.md`会直接无视它。 

---

## 三种方式让 Codex 复用你的 CLAUDE.md 内容

### 方法 ①（最快，30秒）：软链接 / 复制

bash

bash

```
# 在项目根目录
ln -s CLAUDE.md AGENTS.md
```

这样 Codex 读到 `AGENTS.md`→ 实际内容就是你的 `CLAUDE.md`。**代价**：CLAUDE.md 里如果有 Claude 专属语法（`@import`、`.claude/rules/`引用、特定工具名），Codex 会当成普通 Markdown 吞进去但不理解它们——不会炸，但那几行等于废话。 

> 更干净的做法反过来：**让 CLAUDE.md 引用 AGENTS.md，而不是让 AGENTS.md 假装是 CLAUDE.md**：

bash

bash

```
# 项目根
# 1. 把通用规则提炼到 AGENTS.md（这个 Codex 原生读）
# 2. CLAUDE.md 首行写：
# @AGENTS.md
# 然后补 Claude 专属覆盖规则
```

### 方法 ②（推荐，工程上正确）：拆分「共享真理」和「工具专属层」

目录布局长这样最舒服 ：

Pure Text

Pure Text

```
your-project/
├── AGENTS.md              ← ★ 共享真理：技术栈/命令/硬约束（Codex 原生）
├── CLAUDE.md              ← Claude 专属层，首行 @AGENTS.md 引入通用规则
├── .agents/
│   └── skills/            ← Codex 的 skills
├── .claude/
│   ├── CLAUDE.md          ← 也可以放这（Claude Code 也扫这个路径）
│   └── rules/             ← Claude 专属规则片段
├── .codex/
│   └── config.toml        ← Codex 运行配置（模型/沙箱/审批），不混进规则
└── .gitignore
```

`AGENTS.md`里只写**工具无关**的东西：

markdown

markdown

```
## Project
- Next.js 14 + TypeScript + Tailwind
- 包管理: pnpm
- 测试: vitest

## Commands
- dev: pnpm dev
- build: pnpm build
- test: pnpm test --run
- lint: pnpm lint

## Hard Rules
- 不改 `.env*` 文件
- 不加依赖不问我
- 跨文件修改 → 先说清楚改哪几个文件再动手
```

`CLAUDE.md`里写：

markdown

markdown

```
@AGENTS.md

## Claude-only extras
- 用 Plan 模式处理 3 步以上的任务
- allowed-tools 相关的约束我放 .claude/rules/ 里
```

这样 **一份真相，两个工具各取所需**，不重复维护。 

### 方法 ③：用 Codex 的 config 做 fallback 文件名（如果新版支持）

部分资料提到 Codex 配置里有一个 `project_doc_fallback_filenames`概念可以扩展扫描列表，但这不是官方稳定 API 的公开主路径——**不建议依赖**。更稳的做法还是方法②的拆分架构。 

---

## 验证：确认 Codex 实际加载了什么

bash

bash

```
# 最近版本支持 --print-instructions，直接把注入的指令打出来看
codex --print-instructions

# 没有这个 flag 的话，进会话直接问：
> Summarize the instructions you have loaded for this session. What file(s) did they come from?
```

如果它答不出具体内容或者说"我没找到 AGENTS.md"，说明路径不对（记住 Codex 只扫三个固定路径：`~/.codex/AGENTS.md`、git root 的 `AGENTS.md`、cwd 的 `AGENTS.md`）。

---

## 实操建议（结合你的情况）

你已经有了一份好用的 `CLAUDE.md`对吧？最快的迁移路径：

bash

bash

```
# 1. 把 CLAUDE.md 里"技术栈 + 命令 + 硬约束"那段抽出来 → AGENTS.md
# 2. 原来的 CLAUDE.md 改成：
echo '@AGENTS.md

## Claude Code 专属
- 你的 @import 规则 / Plan模式偏好 / allowed-tools 放这' > CLAUDE.md

# 3. 软链保底（防漏网之鱼）
ln -s AGENTS.md .codex/AGENTS.md 2>/dev/null || true
```

做完你会发现：**Codex 开始守规矩了，Claude Code 也没丢任何功能

# 官方建议规则文件写法

以下是基于 **OpenAI 官方 AGENTS.md 文档**​ + **Anthropic 官方 Claude Code 最佳实践**​ + 真实高星仓库写法提炼出来的**参考模板**。不是玄学，是从"什么该放/什么不该放"倒推出来的。

---

# 架构先讲清楚（否则模板你抄了也不知道为啥这么分）

```
your-project/
├── AGENTS.md              ← ★ 共享真理层（Codex / Cursor / 任何 agent 都读这个）
├── CLAUDE.md              ← Claude 专属桥接层（首行 @AGENTS.md，下面只加 Claude-only 的东西）
├── .claude/
│   ├── settings.json      ← 权限 allow/deny（确定性，不放 CLAUDE.md 里）
│   └── rules/             ← 路径限定规则（只在碰特定文件时才加载，省上下文）
│       ├── api-security.md
│       └── react-patterns.md
├── .codex/
│   └── (Codex 的沙箱/审批配置在这)
└── .gitignore              ← 必须把 CLAUDE.local.md 加进去
```

**核心哲学**：AGENTS.md 里写"任何 agent 都需要知道的命令、边界、工作流程"；CLAUDE.md 里放 `@AGENTS.md`，然后只补 Claude 专属控制。这样你改一次，两边都对。

---

## 📄 AGENTS.md（放项目根目录）—— 工具无关共享层

> 这个文件的设计原则：**命令优先、可验证、不讲废话**。凡是 Claude/Codex 读代码就能推出来的（"用 TypeScript""用函数组件"），一个字都别写。

```
# AGENTS.md

## Project
- **What**: [一句话，比如：B2B SaaS 后台管理系统 / 个人博客 API 服务 / Chrome 插件]
- **Stack**: Next.js 15 + TypeScript 5 + TailwindCSS + Prisma ORM + PostgreSQL 16
- **Runtime**: Node 20+ / pnpm 9+
- **Deploy target**: [Vercel / 自托管 Docker / Cloudflare Pages]

## Commands (YOU MUST RUN THESE — not suggestions)
- **install**: `pnpm install`
- **dev**: `pnpm dev`
- **build**: `pnpm build`
- **test (all)**: `pnpm test`
- **test (single)**: `pnpm test -- --run path/to/file.test.ts`
- **lint**: `pnpm lint`
- **typecheck**: `pnpm typecheck`
- **format**: `pnpm format`

## Project Structure (where things live, in 6 lines max)
- `src/app/` — Next.js App Router pages + layouts
- `src/components/` — shared UI components (not page-specific)
- `src/lib/` — pure util / helpers / types (no side effects)
- `src/server/` — API routes, middleware, server-only logic
- `prisma/schema.prisma` — DB schema (NEVER edit live DB without migration)
- `public/` — static assets only

## Boundaries (HARD — violate these and I will be unhappy)
- **NEVER** edit `.env*` files. Read them, yes. Write/commit, NO.
- **NEVER** touch `prisma/schema.prisma` without also generating + reviewing a migration.
- **NEVER** use `any` as a type. Use `unknown` + type narrowing, or be explicit.
- **NEVER** hardcode secrets / API keys / internal URLs. Use env vars.
- **NEVER** `rm -rf` anything unless I explicitly asked for it in plain English.
- Protected paths: `.github/workflows/`, `Dockerfile`, `docker-compose.yml` — touch only if the task explicitly says "CI/Docker".

## Workflow Rules
1. **Before touching code**: run `pnpm lint` and make sure it passes. Fix lint errors before moving on.
2. **After edits that could affect behavior**: run relevant tests (`pnpm test -- --run`). Don't guess.
3. **Cross-file or 3+-step tasks**: state your plan first — list the files you'll touch and why — then wait for my confirmation before writing.
4. **Commits**: Conventional Commits format (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`). No `git commit -m "fix stuff"`.
5. **Don't add dependencies without asking.** If you think you need a new package, tell me what it is, why existing ones won't work, and its license.
6. **When you're done** with a task: tell me exactly which files changed, what command to verify, and whether tests still pass.

## Style Conventions (only the ones that differ from default TS/React norms)
- Import style: ES modules (`import { x } from "y"`), no `require()`.
- Prefer named exports for utils; default exports only for page components.
- Server/client boundary: code in `src/server/` must NEVER `import from "client-only"`.
- All new public-facing API responses must have a Zod schema (even if it feels redundant).

## Common Gotchas (project-specific, learned-the-hard-way items)
- [ ] `pnpm dev` reads `.env.local` which is gitignored — if something "works for you but not me", check env first.
- [ ] Prisma `Decimal` fields serialize to string over JSON — don't `===` compare them as numbers.
- [ ] The `src/lib/` folder is tree-shaken aggressively — side-effect imports will break.
```

> 🔑 **判断标准**（来自 Anthropic 官方建议）：如果你删掉这条规则，agent 会犯一个**具体可描述的错误**吗？说不出来 → 删掉。这条文件的目标大小是 **80~150 行**，不是 600 行的小作文。

---

## 📄 CLAUDE.md（放项目根目录）—— 只做桥接 + Claude 专属

```
@AGENTS.md

## Claude Code Only

### How I want you to operate
- **IMPORTANT**: For any task touching ≥3 files OR adding new features OR changing DB schema:
  → use **/plan** mode first. Output a plan (files affected → change per file → verification steps) → wait YES from me → then execute.
- Prefer running targeted tests (`pnpm test -- --run path/to/file`) over full suite for speed.
- After each batch of edits: run `pnpm lint` + relevant tests before declaring done.

### Interaction style
- When something is ambiguous, STOP and ask a focused question with ≤3 concrete options.
  Don't write a paragraph explaining what you *think* I meant. Ask instead.
- When you report completion, use this format:
```

Done. Changed: [list files]

Verify: [exact command]

Outstanding: [anything you flagged but didn't do, with why]

```
### Things to load on demand (Skills)
- If there's a `.claude/skills/` folder, check it for domain-specific workflows before winging it.
```

然后确保你的个人本地覆盖也到位：

## 📄 CLAUDE.local.md（项目根，**加到 `.gitignore`**）

```
## Local Only (not committed)

- Local DB URL override: `postgresql://localhost:5432/myapp_dev`
- Stripe / third-party keys → I load these into shell env before `claude`, NOT written here.
- My preference: always `pnpm` not `npm`.
```

```
# 别忘了：
echo "CLAUDE.local.md" >> .gitignore
```

---

## 📄 `.claude/settings.json`—— 权限确定性层（不走 CLAUDE.md）

```
{
  "permissions": {
    "allow": [
      "Read",
      "Edit",
      "Write",
      "Bash(pnpm install *)",
      "Bash(pnpm dev)",
      "Bash(pnpm build)",
      "Bash(pnpm lint)",
      "Bash(pnpm typecheck)",
      "Bash(pnpm test -- *)",
      "Bash(git status)",
      "Bash(git diff)",
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(git log -- *)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)",
      "Bash(DATABASE_URL=*)"
    ]
  }
}
```

> 官方原话：**Hooks 是确定性的（每次必发生），CLAUDE.md 指令是建议性的（可能被上下文压缩掉）**。所以"每次改完必须 lint"这种事未来应该靠 Hook，不是靠 Markdown 规则反复念经。

---

## 📄 `.claude/rules/api-security.md`—— 路径限定规则示例（懒加载）

```
---
paths:
  - "src/server/**/*.ts"
  - "src/app/api/**/*.ts"
---

# API Security Rules (auto-loaded only when touching server/api files)

- All request bodies MUST be validated with Zod before use.
- NO string interpolation into SQL — use Prisma parameterized queries or raw `prisma.$query()` with params.
- Never `return` internal error stack traces to the client — map to generic 500 shape.
- Response status codes: 200 for success, 4xx for client error, 5xx only via catch-all handler.
```

---

## 快速自检：你这份配得对不对

在 Codex 里：

```
> Summarize the instructions you have loaded for this session. What file(s) came from?
```

应该看到它报 `AGENTS.md`的路径。

在 Claude Code 里：

```
> 你目前加载了哪些上下文文件？AGENTS.md 的 Project 段落怎么写的？
```

应该先复述 `@AGENTS.md`的内容，再补 Claude-only 那段。

---

## 你接下来要做的事（5分钟搞定）

1. **把上面 `AGENTS.md`模板里的 `[括号]`部分改成你项目的真实值**（stack、commands、protected paths、gotchas）
    
2. **`CLAUDE.md`几乎不用改**，它就三行有效内容：导入 + plan模式偏好 + 完成报告格式
    
3. 跑一天，遇到 Codex/Claude 干了蠢事的时刻 → **往 AGENTS.md 的 `## Common Gotchas`或 `Boundaries`补一条精确规则**（不是笼统的"注意安全"）
    

这套结构的好处是：**你以后换工具（Cursor/Windsurf/Gemini CLI 都读 AGENTS.md），或者团队协作有人不用 Claude，规则不会因为 CLAUDE.md 专属语法锁死。**

你的项目是 **Next.js / Express / 纯 Python / Rust / 什么**？告诉我 stack，我把 Commands 和 Gotchas 那段替你填成对口的具体版本。