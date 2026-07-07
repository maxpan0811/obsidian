---
title: 半年调教出的 Claude Code 顶级配置栈
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=224754...]
source_path: 印象笔记管理工具/别再瞎用Claude了！我花了半年调教出的顶级配置，效率直接降维打击.md
tags: [claude-code, configuration, best-practice, power-user]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "别再瞎用Claude了！我花了半年调教出的顶级配置，效率直接降维打击"
source: evernote
type: note
export_date: 2026-06-27
guid: c00d94f7-408d-4442-b84f-e9d40a50cf45
---

# 别再瞎用Claude了！我花了半年调教出的顶级配置，效率直接降维打击

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0NDQ0ODU3MA==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547455&idx=1&sn=8a2d2e17a712361af7f6f1955437e2a9&chksm=e86f00dfc2be3ce26450165fa367034149c716e711ccab05c47216d8cfb06efef67ad7377bb8&scene=90&xtrack=1&req_id=1777680895941412&sessionid=1777679692&subscene=93&clicktime=1777681454&enterid=1777681454&flutter_pos=10&biz_enter_id=4&ranksessionid=1777680896&jumppath=30024_1777681061638,1104_1777681398426,30024_1777681414757,1104_1777681442630&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004822&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQcOZCnbOv1/9eVtfRrS4zzxLVAQIE97dBBAEAAAAAAONROfU72UMAAAAOpnltbLcz9gKNyK89dVj03Ka4rqX2h2TGhJh2KcyGigYHlN/EzA10hwXhEZWUZF3v1WRMI+DnoG+4ukVR5bdhC/hliRA0LqAXUT10GRBhxWWj4JmRACyvt7IUd1uNfkxsEyKnKlVlvyVJONJOkTbWhbdFQ2WExU5AvNv9u+ioY7Itq4qC4t2KESdM8M3bHVplhjXScJPQNUGxNh0Aizq4A/eStgzAJCIJDo7AJZXS+t0J+r8F8GHfPEMoM+0kOg==&pass_ticket=Ag8zhIrpduB8U9MNYcSj751k0GHo9VzGAm/yrWUIV5hkmFj3OuLUrbLB+atwyH1n&wx_header=3)

# 别再瞎用Claude了！我花了半年调教出的顶级配置，效率直接降维打击

Originaldef 大迁世界

我调了 6 个月 Claude Code，最后才明白一件事：

真正拉开差距的，根本不是你那一句 prompt 写得有多漂亮。

而是你有没有把 `.claude` 这套配置栈搭起来。

现在，打开终端，进入你的主力 AI 项目，运行：

tree .claude

对很多正在用 Claude Code 的工程师来说，结果大概率是：

`command not found`

或者，里面只有一个孤零零的文件，写着几句很虚的指令，比如“请写干净代码”“请遵循最佳实践”。

这也不是不能用。

但这等于把 Claude Code 80% 的能力直接扔在地上。

一个真正被 power user 配好的仓库，通常会长这样：

.claude/
.claude/
├── CLAUDE.md
├── rules/
│   ├── langgraph.md
│   ├── retrieval.md
│   ├── tests.md
│   └── python-types.md
├── agents/
│   ├── retrieval-reviewer.md
│   ├── prompt-auditor.md
│   └── eval-runner.md
├── skills/
│   ├── new-rag-eval/
│   │   └── SKILL.md
│   └── claude-pr-checklist/
│       └── SKILL.md
├── settings.json
└── .mcp.json

重点不是文件多。

重点是，每个文件都很短、很准、很有边界。主 memory 文件故意控制在 500 tokens 以下。每个 rules 文件只负责某个路径下的行为。每个 subagent 大概三十行。hooks 只做一个 pre-tool gate 和一个 post-tool formatter。MCP server 也不是装十五个，而是只保留五个真正有用的。

想象两个工程师接到同一个任务：

给现有 retrieval service 增加带引用的答案生成； 补上 evaluation； 然后基于 main 分支开一个 PR。

第一个工程师 `.claude` 目录几乎为空。

第二个工程师有上面那套配置，还有 wired-up headless mode。

第一个人可能花一下午，晚上才发出去。第二个人可能 30 分钟就能开出 PR。

差别不在他们临时输入的 prompt。

差别在那套没人愿意花时间搭的配置栈。

## 第一层：Memory Hierarchy

先从 memory 文件开始。

因为只要这一层足够短，后面所有层都会更便宜。

Claude Code 有一套五层 memory hierarchy：你的个人偏好、项目根目录文件、路径级规则、本地未提交覆盖，以及每个 session 自动写入的 memory。

其中，项目根目录的 `CLAUDE.md` 会在每次 session 开始时加载。

也就是说，它会永久消耗 token。

很多团队把整个工程 wiki 都塞进这个文件里，把它当成一个向量数据库，而不是一个热缓存。结果就是，每次 Claude 启动都要背一大堆并不总是相关的内容。

这很贵，也很慢。

我自己的工作流里，当这个文件超过大约 500 tokens 后，cache hit rate 会明显下降。而新的 Opus 4.7 tokenizer 会把已有 prompt 映射成大约 1.0 到 1.35 倍 tokens。换句话说，如果你不严格控制 ambient context，同样的工作流现在会更贵。

所以，根 memory 文件应该短。

控制在 200 行以内。语气要命令式。不要写“write clean code”这种建议。要写会真正改变行为的规则，比如：

“所有函数必须有 TypeScript type annotations。”

每一行都应该能影响 Claude 的动作。

以一个 RAG service 为例，最小可用的 `CLAUDE.md` 可以这样写：

# citation-rag
Retrieval + answer-generation service. LangGraph-based pipeline,
PostgreSQL+pgvector retrieval, Gemini answer generation, eval harness
in `evals/`.
## Layout

- `services/retrieval/`  — chunking, embedding, reranker, citation packer
- `services/answer/`     — prompt templates, generator node, guardrails
- `shared/`              — schemas, tracing, settings
- `evals/`               — golden sets, runners, scoring
## Build & test

- Install:           `uv sync`
- Unit tests:        `uv run pytest -q`
- Eval harness:      `uv run python -m evals.run --suite citations`
- Lint + types:      `uv run ruff format . && uv run mypy .`
## Canonical conventions

- The canonical answer prompt lives at `services/answer/prompts/v4.md`.
  Do not edit `v3.md` because it is frozen for regression evals.
- All LLM outputs are validated with the pydantic models in
`shared/schemas/answers.py`. No raw dict returns from generator nodes.
- Retrieval always returns `Chunk` objects with a `citation\_id`.
  The answer node must emit citations using those exact ids.
## Guardrails (Claude: follow these literally)

- Never bump the model version string without updating
`evals/snapshots/<version>.json` in the same commit.
- Never introduce network calls inside `tests/unit/`. Use fixtures in
`tests/fixtures/` and the fakes in `tests/fakes/`.
- Prefer editing existing modules over adding new top-level packages.
- If a change touches `services/retrieval/`, read `.claude/rules/retrieval.md`
  before planning.
- Keep functions under ~40 lines. Split by responsibility, not by length.
## Before opening a PR

- Run the eval harness and attach the diff output to the PR body.
- Update `CHANGELOG.md` under `## Unreleased`.
- Use the `claude-pr-checklist` skill.

这个文件没有废话。

它告诉 agent 每个目录负责什么；定义 retrieval node 和 answer node 之间严格的 citation contract；也给 test suite 加了硬约束，避免模型脑补一个网络 mock。

这才是 memory 文件该做的事。

不是塞知识库。

而是放真正高频、关键、会影响决策的规则。

![](attachments/a08e629f65cdbfb1.png)

## 第二层：Path-Scoped Rules

把根 memory 控制住之后，你仍然会遇到文件级、目录级的特殊规则。

这些东西不要继续塞进 `CLAUDE.md`。

应该放进 path-scoped rules。

这种模式通常用 YAML frontmatter。你定义一组 glob paths，只有当 Claude 触碰匹配文件时，规则才会被加载。平时，它不消耗 token。

如果 agent 正在编辑数据库 migration，它根本不需要知道前端样式规范。

这就是省 token 的关键。

不过有个现实小坑：虽然 `paths:` 是文档里的 schema key，但当前一些版本有时会因为已知 bug 忽略它。如果你发现规则没有生效，可以尝试用 `globs:` 或 CSV 格式，通常更可靠。

比如 retrieval service 的规则文件可以这样写：

---
name: retrieval-rules
description: Conventions for services/retrieval/\*\*. Loaded only when
  Claude is editing or planning changes inside the retrieval service.
globs:
  - "services/retrieval/\*\*"
  - "tests/retrieval/\*\*"
---
# Retrieval service rules
## Chunking

- Use `shared/chunking.semantic\_chunker` for all document ingest.
  Do not introduce a second chunker without updating the eval snapshot.
- Chunk size target: 512 tokens, 64 overlap. Changes require an ADR.
## Reranker

- The reranker interface is `services/retrieval/reranker.Reranker`.
  New backends must implement it, not parallel it.
- Never rerank more than the top 50 hits from vector search. Rerank latency
  is the #1 service SLO risk.
## Citations

- Every `Chunk` returned from retrieval must carry a stable `citation\_id`.
- Citation ids are produced by `shared/citations.make\_citation\_id`. Do not
  hand-roll ids anywhere else.
- The answer node assumes `citation\_id` is URL-safe. Do not change that
  without updating `services/answer/citation\_packer.py` in the same diff.
## Tests

- Unit tests for retrieval must never hit the embedding API. Use the fake
  embedder in `tests/fakes/embeddings.py`.
- Integration tests live under `tests/retrieval/integration/` and are
  opt-in via `pytest -m integration`.

三四个短规则文件，远远胜过一个巨大的根文件。

因为它们只在需要时加载。

这种 token 节省会在每一轮对话里持续复利。

![](attachments/6ca980d117135dac.png)

## 第三层：Plan Mode

很多人从来不用 Plan Mode。

他们输入一个 prompt，然后直接看 Claude 开始改文件。

这很刺激。

也很危险。

Plan Mode 的价值在于，它把“思考”和“动手”分开。

探索发生在主执行上下文之外。它会生成一个明确的计划文档，让你先审阅、修改、确认，然后才允许发生破坏性动作。

Claude Code 通常提供三个规划层级：

Simple Plan，适合单文件短任务； Visual Plan，适合结构很重要的多文件修改； Deep Plan，适合跨服务变更和高风险重构。

Deep Plan 会使用 subagents 做风险评估和架构审查。规划 subagent 默认是只读的，明确没有写入和编辑权限。它在梳理依赖时，不会误改你的代码库。

回到 RAG service 的例子。

我们可以用 Deep Plan 追踪现有 answer generation path。explore subagent 把相关文件收进一个短上下文里，planner 输出明确的编辑列表、evaluation 添加项，以及 PR 描述草稿。

你审查计划，锁定方案。

真正的修改，只发生在退出 Plan Mode 之后。

这一步看似慢，其实是在防止后面更慢。

因为 AI 最贵的错误，不是它不知道。

是它太自信地直接改。

![](attachments/1739a0252853f55e.png)

## 第四层：Custom Subagents

Subagents 是 Claude Code 里最被低估的功能之一。

工具本身带了一些内置 subagents。explore agent 负责只读代码库搜索；general-purpose agent 处理需要干净上下文的多步骤任务；code-reviewer 和 code-architect 则负责更专门的角色。

但真正强的，是你自己写 custom subagent。

什么时候该写？

当某类任务反复出现； 当你需要一个有明确工具限制的角色； 当某个 system prompt 和主配置冲突； 当你想把审查、执行、评估拆到独立上下文里。

在这个 RAG service 里，可以配置三个 custom agents：

`prompt-auditor`，检查 prompt 改动是否符合规则；`eval-runner`，执行 harness 并产出结构化结果；`retrieval-reviewer`，用领域标准审查 reranker 相关代码。

比如 retrieval reviewer 可以这样写：

---
name: retrieval-reviewer
description: Reviews changes under services/retrieval/ for chunking,
  reranker, and citation-contract regressions. Read-only. Invoke
  proactively before opening a PR that touches retrieval code.
tools: Read, Grep, Glob, Bash(git diff:*\*), Bash(uv run pytest:\**)
model: sonnet
---
You are a retrieval-service reviewer for the citation-rag repo.
Scope:
- Only review files under `services/retrieval/\*\*` and their tests.
- Do not comment on unrelated files even if they appear in the diff.
Review checklist, in order:
1. Chunking: does the change respect the 512/64 target, and does it keep
   `shared.chunking.semantic\_chunker` as the single entry point?
2. Reranker: if the reranker interface changed, is every implementation
   updated, and is the top-k cap still ≤ 50?
3. Citations: every returned `Chunk` must have a `citation\_id` produced
   by `shared.citations.make\_citation\_id`. Flag any hand-rolled ids.
4. Tests: no new network calls in unit tests. Integration tests gated
   by `pytest -m integration`.
5. Eval impact: if behavior changed, confirm `evals/snapshots/\*.json`
   has been regenerated in the same commit.
Output format:
- A short "Verdict" (pass / needs-changes / blocker).
- Bullet list of findings, each with the file path and a one-line fix.
- Do not suggest unrelated refactors.

注意 frontmatter。

`tools` 是一个很窄的 allowlist，只给读取权限和受限 bash 执行。`model: sonnet` 则把这个 subagent 下放到更便宜的模型。

主循环继续使用昂贵模型做高难推理，subagent 则用更低成本在后台完成专门审查。

这才是合理分工。

![](attachments/10196c23a1af6680.png)

## 第五层：Skills

Skills 的作用，是把稳定工作流打包起来。

你可以通过名字触发它。

一个 skill 通常是一个文件夹，里面有带 YAML frontmatter 的 markdown 文件。它也可以捆绑 Python 脚本、bash 命令和测试 fixture。

它的架构依赖 progressive disclosure：

metadata 在 session 启动时加载； 真正的 instructions 只有触发 skill 时才加载； 捆绑资源只有被引用时才加载。

所以，即使你安装 50 个 skills，也不一定会显著增加 ambient token cost。

比如我们可以写一个叫 `new-rag-eval` 的 skill。它负责从模板创建新的 eval case，把 case 接进 harness，针对当前 pipeline 跑一次，然后写出结果摘要。

---
name: new-rag-eval
description: Support a new RAG eval case from a golden example, wire it
  into the eval harness, run it against the current pipeline, and write
  a result summary. Use when the user asks to "add an eval for ..."
  or "cover this regression with an eval."
allowed-tools: Read, Write, Edit, Bash(uv run:*\*), Bash(git add:\**)
---
# new-rag-eval
## When to use
Trigger when the user wants to add a new eval case to
`evals/suites/citations/` or reproduce a regression in the eval harness.
## Inputs to gather first

1. A natural-language description of the query.
2. The expected citation ids (or the expected answer text).
3. Optional: the failing trace id from production.
## Steps

1. Read `evals/templates/case.json` — this is the case template.
2. Ask the user for the query, expected citations, and any notes.
3. Write a new case file at `evals/suites/citations/<slug>.json` using
   the template. Slug is kebab-case from the query.
4. Run the harness for just this case:
   `uv run python -m evals.run --suite citations --case <slug>`
5. Parse the JSON output at `evals/out/<slug>.json`. Summarize:
   - pass / fail
   - grounded-citation rate
   - unsupported-claim rate
   - any new latency outliers
6. If failing, add a short "why this is expected to fail today" note
   to the case file under `notes:`.
7. Stage the new case with `git add evals/suites/citations/<slug>.json`.
## Do not

- Do not edit `evals/templates/case.json`.
- Do not touch other eval suites.
- Do not open a PR from this skill. The PR flow lives in the
`claude-pr-checklist` skill.

这里的 allowed tools 很重要。

它可以跑 eval，可以 stage 文件。

但不能推生产，也不能自己开 PR。

PR 流程被明确指向另一个 skill。

这就是 deterministic workflow。不是让 agent 想干什么就干什么，而是让它在清晰轨道里完成重复工作。

## 第六层：Hooks 和 Determinism

Hooks 的作用，是让 agent 在更少人工盯着的情况下安全运行。

它们给概率系统加上确定性护栏。

hooks 写在 settings 文件里。事件包括 session start、user prompt submit 和 tool use。2026 年 4 月的版本还增加了针对 safety classifier rejection 的 hook，这样你可以审计被拒绝的操作。

最重要的新能力之一，是 Deferred Permissions。

pre-tool hook 现在可以返回 defer decision，让 agent 在 headless mode 中途暂停。你检查 session，线下批准动作。agent 再从原位置继续运行。

在 deferred permissions 出现之前，一个夜间任务如果需要 push 到 main，要么开 `--dangerously-skip-permissions`，要么凌晨 3 点失败。

现在，可以把风险动作拦住。

对于 RAG service，可以配置两个非常实用的 hooks：

post-tool hook，在每次写文件后静默运行 formatter； pre-tool hook，拦截任何推送到 main 分支的 git push。

{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/gate\_git\_push.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "uv run ruff format $CLAUDE\_TOOL\_FILE\_PATH >/dev/null 2>&1 || true"
          }
        ]
      }
    ],
    "PermissionDenied": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "jq -c . >> .claude/logs/denied.jsonl"
          }
        ]
      }
    ]
  }
}

配套的 shell script 可以这样写：

#!/usr/bin/env bash
*# Defer any `git push` that targets main. The session pauses. A human*
*# approves out-of-band and the agent resumes via `claude --resume`.*
set -euo pipefail
payload="$(cat)"
cmd="$(printf '%s' "$payload" | jq -r '.tool\_input.command // empty')"
case"$cmd"in
  \*"git push"\*"origin main"\*|\*"git push"\*" main"\*)
    jq -nc '{
      "permissionDecision": "defer",
      "reason": "Push to main requires human approval."
    }'
    ;;
  \*)
    jq -nc '{"permissionDecision": "allow"}'
    ;;
esac

post-tool hook 故意很无聊。

但这种一行 formatter hook，往往是最高 ROI 的配置。agent 写了一个缩进很乱的文件，hook 自动跑 linter。下一轮对话前，文件已经是干净的。

Claude 也不会被自己刚写出来的糟糕格式误导。

这就是小自动化的价值。

## 第七层：Server Stack

MCP，也就是 Model Context Protocol，用来把 agent 接到外部工具上。

很多开发者一口气装十五个 servers，然后奇怪为什么 agent 变得混乱。

原因很简单：

每个 server 都会提供 tool schemas。

这些 schemas 会在每一轮消耗 context tokens。

Anthropic 的 Tool Search 文档提到，如果没有 lazy loading，50 个工具每轮可能消耗 10,000 到 20,000 tokens。Tool search lazy loading 可以减少大约 85%，但最好的策略仍然是：少装。

认真做工程，五个 servers 就够了：

一个 code graph server，带持久 session memory； 一个 GitHub server，负责 branch 和 commit 管理； 一个 filesystem server，提供跨目录访问； 一个 live web search server，查当前文档； 一个专用 context server，拉取特定版本的库文档。

示例配置：

{
  "mcpServers": {
    "vexp": {
      "command": "npx",
      "args": ["-y", "@vexp/mcp-server@latest"],
      "env": {
        "VEXP\_PROJECT": "citation-rag",
        "VEXP\_MEMORY\_DIR": ".vexp"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB\_PERSONAL\_ACCESS\_TOKEN": "${GITHUB\_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${HOME}/code/citation-rag",
        "${HOME}/code/shared-prompts"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE\_API\_KEY": "${BRAVE\_API\_KEY}" }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}

如果你是 AI engineer，需要直接查询生产数据结构，也许可以加第六个数据库 server。

但原则仍然一样：

保持列表小。

vexp 这类 code graph / persistent memory server，按照它自己发布的 benchmark，在长时间 agent setup 中可以带来 65% 到 70% 的 token 降低。

另外，2026 年 4 月的版本还加入了一个很细但有用的 server-side 能力：servers 可以在 tool 的 `_meta` 字段里设置 `anthropic/maxResultSizeChars` annotation。

这让大型库文档拉取可以保持 inline，不必再走以前那些写文件再读取的绕路方案。

## 第八层：Parallel Worktrees 和 Headless Automation

Worktrees 是你停止等待 agent 慢慢打字的方式。

一条命令，工具就能创建 branch、worktree 和独立 session。每个 worktree 保留自己的编辑器状态和运行进程。你可以在多个 pane 里并行管理它们。

还是前面的 citation task。

一个 pane 实现核心 generation change； 第二个 pane 重写 evaluation harness； 第三个 pane 给新的 retrieval path 加 tracing； 第四个 pane 起草 PR。

每个 pane 有自己的 session 和自己的 context。

并行任务当然可能产生重叠编辑。但如果你把任务范围切清楚，比如一个 pane 只做 evals，一个 pane 只改 core logic，实际很少出现严重冲突。

最后一块，是 headless mode。

你可以让 agent 在 CI pipeline 里非交互运行。只允许特定工具，并剥离本地配置，从而获得可复现行为。

一个 GitHub Actions 的 nightly evaluation job 可以这样写：

name: claude-nightly-evals
on:
schedule:[{cron:"0 7 \* \* \*"}]
workflow\_dispatch:
jobs:
run-evals-and-open-pr:
    runs-on:ubuntu-latest
    permissions:
      contents:write
      pull-requests:write
    env:
      ANTHROPIC\_API\_KEY:${{secrets.ANTHROPIC\_API\_KEY}}
      GITHUB\_TOKEN:      ${{secrets.GITHUB\_TOKEN}}
    steps:
      -uses:actions/checkout@v4
      -uses:astral-sh/setup-uv@v3
      -run:uvsync
      -name:InstallClaudeCode
        run:npmi-g@anthropic-ai/claude-code@latest
      -name:Runnightlyeval+draftPR(headless)
        id:claude
        run:|
          set -o pipefail
          claude-p\
            --bare\
            --output-formatstream-json\
            --allowedTools"Bash(uv run:\*),Read,Grep,Glob,Write,Edit,mcp\_\_github\_\_\*"\
            --append-system-prompt"You are the nightly eval runner. \
              Run the citations eval suite. If regressions appear, \
              open a draft PR with a fix attempt and the eval diff."\
            "Run: uv run python -m evals.run --suite citations. \
             If any case regresses, implement the minimal fix and open \
             a draft PR against main via the GitHub MCP."\
          |teeclaude.ndjson
          ifgrep-q'"permissionDecision":"defer"'claude.ndjson;then
            echo"deferred=true">>"$GITHUB\_OUTPUT"
          fi
      -name:Resumeiftherundeferredonpush-to-main
        if:steps.claude.outputs.deferred=='true'
        run:|
          SESSION\_ID="$(jq -r 'select(.type=="deferred") | .session\_id' \
                        claude.ndjson | head -n1)"
          claude--resume"$SESSION\_ID"\
            --append-system-prompt"Approved. Continue."\
            --output-formatstream-json

这里 allowed tools 会和前面写的 hooks 配合起来。

job 跑 evaluation，起草 fix，尝试 push 到 main。hook 捕获 push 并 defer 权限。pipeline 解析 JSON log，设置 output variable，然后暂停。人类审查结构化日志并批准。最后 `claude --resume` 用同一个 session ID 接着跑完。

这才是比较安全的“让 agent 睡觉时干活”。

不是完全放飞。

而是把风险动作关进审批门里。

## 这套栈跑起来是什么样？

现在，把整套流程串起来看一遍。

session 启动。

工程师打开项目，创建 feature worktree。memory 文件和 rules 自动加载。五个 servers 连接。

工程师进入 Deep Plan mode。explore subagent 映射当前 retrieval paths，planner 输出明确文档：

## Implementation Plan: Citation-Backed Generation

1. \*\*Modify `services/retrieval/search.py`\*\*: Ensure `Chunk` objects attach `citation\_id` via `shared.citations.make\_citation\_id`.
2. \*\*Update `services/answer/generator.py`\*\*: Inject `[Source: {citation\_id}]` into the Gemini system prompt context block.
3. \*\*Create Eval\*\*: Add `evals/suites/citations/defective-charger.json` to verify strict citation formatting.

工程师审查计划，锁定。

实现开始。

当 agent 修改完 retrieval logic 后，自动调用 `retrieval-reviewer` subagent。subagent 根据 path-scoped rules 返回一个 blocker：

\*\*Verdict: blocker\*\*

\* `services/retrieval/search.py`: You hand-rolled a UUID for the citation ID on line 42. Rule `.claude/rules/retrieval.md` requires `shared.citations.make\_citation\_id`.
\* `tests/retrieval/test\_search.py`: Missing `@pytest.mark.integration` on the new database test.

agent 修掉手写 ID，又补上 decorator。post-tool hook 在每次写文件后保持格式干净。

与此同时，并行 worktree 开始工作。

第二个 worktree 用 `new-rag-eval` skill 重写 evaluations。headless run 执行最终 evaluation harness，并生成 diff：

{
  "suite": "citations",
  "cases\_run": 45,
  "grounded\_citation\_rate": {"previous": 0.82, "current": 0.98, "delta": "+0.16"},
  "unsupported\_claims": {"previous": 12, "current": 0, "delta": "-12"},
  "status": "PASS"
}

deferred permission 暂停 push。

工程师批准。

PR 通过 GitHub server 打开，完整 change set 和 evaluation diff 一起附上。

当然，这个 90 分钟交付有前提：任务本身范围清晰，而且配置栈已经搭好。

第一次搭这套东西，可能要花一个下午。

但后面的每个任务，都会复利。

## 下限和上限

这套配置也很容易被你亲手毁掉。

最常见的毁法，就是写一个巨大的 memory file，或者装十五个 MCP servers。

工具 schema 不是免费的。

上下文也不是无限的。

不要把应该交给 subagent 的探索和审查塞进 main session。探索和 review 应该放在隔离上下文里。主 session 应该负责决策和执行，而不是背着所有历史到处乱跑。

如果你没时间做完整套，至少做最小版本：

写一个短而强制的项目根 memory 文件； 给最常改的两个目录写 path-scoped rules； 加一个 formatter hook； 安装三个 servers：repository、filesystem、library docs； 对任何可能改错的任务，强迫自己先用 Plan Mode。

当某个任务反复出现，再加 subagent。

当某个工作流稳定下来，再封成 skill。

当你发现自己每小时切分支超过两次，就用 worktrees。

当你希望 agent 在你睡觉时也能推进工作，再上 headless mode。

## 最后

现在，我们的 agent 已经能很好地导航代码库。

但它仍然会在长任务里遇到另一个问题：context window 慢慢被过时观察填满，最终出现 Context Rot。

这就是下一层话题：Compaction、Tool-Result Clearing，以及怎样防止长时间运行的 agents 被自己的记忆淹死。

但这篇先说最核心的结论：

stack 才是 workflow。

workflow 才是 multiplier。

prompt 只是最后那 5%。

不要再让 Claude Code 裸奔了。

把 `.claude` 搭起来。

你会发现，真正提升效率的不是一句神奇提示词，而是一整套会持续工作的工程系统。
