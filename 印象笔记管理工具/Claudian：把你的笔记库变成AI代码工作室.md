# Claudian：把你的笔记库变成AI代码工作室

---

原文链接: [https://mp.weixin.qq.com/s?chksm=96c067d9a1b7eecf5b44998eadf60cd...](https://mp.weixin.qq.com/s?chksm=96c067d9a1b7eecf5b44998eadf60cdc21d44a74c392fdf5311aea018340a0474ef4c98a75b4&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782340110_1&req_id=1782340107152027&scene=169&mid=2247485806&sn=774f39743f6fb80692ba13e054820599&idx=1&__biz=MzIwNDM3Mjk1Mg==&sessionid=1782340109&subscene=200&clicktime=1782340119&enterid=1782340119&flutter_pos=2&biz_enter_id=5&jumppath=1101_1782339836610,1106_1782340107880,1001_1782340108811,1104_1782340110727&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQshvUbguFBsXxeFjTlhEJIhLTAQIE97dBBAEAAAAAAMKOBje1B+kAAAAOpnltbLcz9gKNyK89dVj0YmOLRRVcJQPaS+aK56pnPbRiB4YzXgmIz78g/Zw6+ns8WsmxzQa2LRA95NicqxuP71PsUfxB1WmQsOiJ2A2BdgOQR/C6yzTpygRAGA5Q47cU2DYyHT2sNV4IBmiTDICdARlRofs/0F+hN2C89xI7gMjbrb0wsn7owDiUFWR4qxOYwmK0ydyGgZC3UuGPRVVpql45MwM1nuV3UCU8LL0PW5pVXHE/bv54fi/RTRI=&pass_ticket=fXvSy2mG3WpCxA73Wl1uHdtni/Uwpc9q7wkC0JP5mVKndsmgxPGSegV6VORbSxFs&wx_header=3)

Claudian：把你的笔记库变成AI代码工作室
========================

Originalkunbo 观澜逸趣

![](.evernote-content/18A3D0E9-BB90-4166-9B18-7834D7810B24/B7FCDCCE-D158-405A-BAA0-46B8547DE0F6.jpg)

你每天用 Obsidian 记笔记、写文档、管理知识库。你的 AI 编程助手（Claude Code、Codex）每天在终端里写代码、改文件、跑测试。

这两个世界之间，隔着一道鸿沟：笔记在 Obsidian 里，代码在终端里。你想让 AI 读一篇你写的技术文档然后改代码？先复制粘贴。你想让 AI 把代码分析结果写回笔记？再复制粘贴。

**Claudian 解决的就是这个问题。**

它是一个 Obsidian 插件，能把 Claude Code、Codex、OpenCode、Pi 等 AI 编程助手直接嵌入到你的 Obsidian 笔记库中。你的笔记库就是 AI 的工作目录——它可以直接读写你的笔记、搜索你的文档、执行命令、运行多步骤工作流。

GitHub 上已经拿到了 **13.2k Star、822 Fork**。

---

一、Claudian 是什么？一句话讲清楚
---------------------

**Claudian = 把 Claude Code / Codex 塞进 Obsidian 的插件。**

安装之后，你的 Obsidian 右侧会出现一个聊天侧边栏。你可以像跟 Claude Code 对话一样跟它聊天，但它操作的不是远程服务器上的文件，而是**你当前这个 Obsidian 笔记库里的文件**。

### 它能做什么？

| 功能 | 说明 |
| --- | --- |
| **读写笔记** | AI 可以直接读取、编辑、创建你的 Obsidian 笔记 |
| **搜索文档** | 在你的整个笔记库里搜索关键词 |
| **执行命令** | 运行 bash 命令（在桌面端受限沙箱内） |
| **多步骤工作流** | 让 AI 自动完成一连串任务 |
| **内联编辑** | 选中一段文字，快捷键直接让 AI 改写 |
| **@提及** | `@任意文件` 让 AI 引用该文件内容 |
| **Skills** | `/` 或 `$` 调用可复用的 prompt 模板 |
| **MCP 服务器** | 连接外部工具（数据库、API、搜索等） |
| **Plan 模式** | AI 先设计后实施，给你展示计划再动手 |

![](.evernote-content/18A3D0E9-BB90-4166-9B18-7834D7810B24/B5F4FB16-5AE8-47BE-A2AF-C2B3D703C8E9.jpg)

---

二、为什么需要 Claudian？解决三个真实痛点
-------------------------

### 痛点 1：知识库和代码库割裂

你有一个 Obsidian 知识库，里面记录了：

* 项目的技术方案和设计决策
* API 文档和使用说明
* 踩过的坑和解决方案
* 团队的编码规范

同时你在终端里用 Claude Code 写代码。当你想让 AI 参考你的技术文档时，流程是：

1. 打开 Obsidian，找到文档
2. 复制内容
3. 切到终端，粘贴给 Claude Code
4. Claude Code 给出结果
5. 复制结果
6. 切回 Obsidian，粘贴到笔记

**Claudian 的做法：** AI 直接在你的笔记库里工作，无需复制粘贴。

### 痛点 2：AI 的"记忆"不持久

在终端里用 Claude Code，每次新开一个会话，之前的上下文就丢了。你想让 AI 记住"我们团队用 camelCase 命名变量"这个约定？每次都要重新告诉它。

**Claudian 的做法：** 把团队约定写在 Obsidian 笔记里（比如 `编码规范.md`），AI 在需要时自动读取。这些约定持久保存在你的笔记库中，不会丢失。

### 痛点 3：AI 的输出无处安放

AI 帮你分析了一堆代码，生成了一份优化建议。你想保存下来？只能：

* 复制粘贴到某个笔记里（格式全丢）
* 或者新建一个文件，手动整理

**Claudian 的做法：** AI 直接把输出写回 Obsidian 笔记，保持 Markdown 格式，自动分类归档。

---

三、核心功能详解：不只是"聊天"
----------------

Claudian 不是一个简单的"在 Obsidian 里聊天"的插件。它的设计深度和工程完整度，在很多方面都超出了预期。

### 1. 内联编辑（Inline Edit）—— 选中即改

这是 Claudian 最惊艳的功能之一。

**用法：**

1. 在 Obsidian 笔记里选中一段文字
2. 按快捷键（默认 `Ctrl+Shift+K` 或 `Cmd+Shift+K`）
3. 输入你想怎么改（比如"把这段改成更正式的风格"）
4. AI 直接修改，并显示**逐字差异预览**

**逐字差异预览是什么意思？**

不是直接把原文替换成新文本，而是像 Git diff 一样：

* 删除的文字标红划线
* 新增的文字标绿高亮
* 你一眼就能看到 AI 改了什么

如果满意，按 `Enter` 确认；如果不满意，按 `Esc` 取消。

这个功能把 AI 编辑从"盲盒"变成了"透明操作"——你知道 AI 做了什么，才决定是否接受。

### 2. @提及（@mention）—— 让 AI 引用任意内容

在聊天框里输入 `@`，Claudian 会弹出选择器：

| @类型 | 说明 |
| --- | --- |
| `@文件.md` | 让 AI 读取该笔记内容 |
| `@子代理` | 调用一个专门的子代理处理特定任务 |
| `@MCP服务器` | 连接外部 MCP 工具 |
| `@外部目录/文件` | 引用笔记库之外的文件 |

**实际场景：**

你："帮我根据 `@技术方案.md` 里的设计，在 `@src/components/` 目录下实现前端组件。"

AI 读取技术方案，然后在你指定的目录下创建组件文件。

### 3. Plan 模式 —— 先设计，后动手

默认模式下，你发一个指令，AI 立刻执行。但有时候你不想让它"立刻动手"，而是想先看看它的计划。

**Plan 模式（**`Shift+Tab` **切换）：**

1. 你输入任务描述
2. AI **不立刻执行**，而是先分析需求
3. AI 输出一份**执行计划**：

* 第一步做什么
* 第二步做什么
* 需要读取哪些文件
* 预计输出什么

4. 你检查计划，可以修改或补充
5. 批准后，AI 才开始执行

这个模式特别适合**复杂任务**，避免 AI "一上来就改，改完才发现方向错了"。

### 4. Skills —— 可复用的 Prompt 模板

Claudian 支持两种 Skill：

**用户级 Skill：** 存在 `~/.claudian/skills/`，所有笔记库共享 **笔记库级 Skill：** 存在 `vault/.claudian/skills/`，仅当前笔记库可用

# 用法
/chat 输入框里打 / 或 $
→ 弹出 Skill 选择器
→ 选择 "生成周报模板"
→ AI 自动按模板格式生成周报

Skill 本质上就是预定义的 prompt 模板，但 Claudian 让它们变成了**可发现、可复用、可版本控制**的资源。

### 5. MCP 服务器 —— 连接外部世界

Claude Code 支持 MCP（Model Context Protocol），Claudian 也继承了这一点。你可以在 Obsidian 里直接连接：

* 数据库（让 AI 查你的数据库）
* 搜索引擎（让 AI 联网搜索）
* 文件系统（让 AI 访问特定目录）
* 自定义 API（让 AI 调用你的内部服务）

Claude 的 MCP 由 Claudian 内置管理；Codex 的 MCP 走自己的 CLI 配置。

### 6. Instruction 模式（`#`）—— 临时追加指令

在聊天框里输入 `#`，可以追加自定义指令：

# 用中文回复
# 只修改函数实现，不要改接口
# 输出结果保存到 `review/2026-06.md`

这些指令只影响当前对话，不会持久化。适合临时调整 AI 的行为。

### 7. 多标签页和对话管理

Claudian 支持：

* **多标签页**：同时打开多个 AI 对话，像浏览器标签一样切换
* **对话历史**：保存所有对话记录，随时回看
* **分支（Fork）**：基于某轮对话分叉出新对话
* **恢复（Resume）**：中断后从上次位置继续
* **压缩（Compact）**：长对话自动压缩历史，节省上下文窗口

---

四、支持 4 种 AI 编程助手
----------------

Claudian 目前支持 4 种主流 AI 编程助手：

| 助手 | 连接方式 | 特点 |
| --- | --- | --- |
| **Claude Code** | Claude Code CLI | 最成熟，Anthropic 官方，支持 MCP |
| **Codex** | Codex CLI | OpenAI 出品，适合快速原型 |
| **OpenCode** | Opencode CLI | 开源替代品 |
| **Pi** | Pi RPC | 轻量级，快速响应 |

### Claude Code 配置

1. 安装 Claude Code CLI（推荐原生安装）
2. Claudian 自动检测 CLI 路径（如果检测不到，手动在设置里指定）
3. 订阅 Claude 或使用兼容 provider（OpenRouter、Kimi 等）

**注意 Windows 用户：**

* 原生安装用 `claude.exe`
* npm 安装用 `cli-wrapper.cjs`
* **不要用** `.cmd` **或** `.ps1` **脚本**（会有权限问题）

### 其他 Provider

Codex、OpenCode、Pi 的支持已经上线，但功能可能还在完善中，不同平台的兼容性也在持续测试。

---

五、技术架构：不是一个简单的"桥接"
------------------

Claudian 的代码结构展示了它的工程深度：

src/
├── main.ts                      # 插件入口
├── app/                         # 插件级存储和默认配置
├── core/                        # 核心运行时（Provider 无关）
│   ├── runtime/                 # ChatRuntime 接口和审批类型
│   ├── providers/               # Provider 注册表和工作区服务
│   ├── auxiliary/               # 共享辅助服务
│   ├── security/                # 审批工具
│   └── ...                      # 命令、MCP、提示、存储、工具
├── providers/
│   ├── claude/                  # Claude SDK 适配器、MCP、插件
│   ├── codex/                   # Codex app-server 适配器、JSON-RPC
│   ├── opencode/                # Opencode 适配器
│   ├── pi/                      # Pi RPC 适配器、模型发现
│   └── acp/                     # Agent Client Protocol 共享传输
├── features/
│   ├── chat/                    # 侧边栏聊天：标签页、控制器、渲染
│   ├── inline-edit/             # 内联编辑模态框
│   └── settings/                # 设置面板
├── shared/                      # 可复用 UI 组件
├── i18n/                        # 国际化（10 种语言）
└── style/                       # 模块化 CSS

### 关键设计

**Provider 抽象层：**

Claudian 没有为每个 AI 助手写一套独立代码，而是定义了一个 **Provider 接口**。Claude、Codex、OpenCode、Pi 都实现这个接口，核心逻辑（聊天、编辑、工具调用）对所有 Provider 通用。

这意味着：未来增加新的 AI 助手（比如 Gemini CLI、Qwen Code），只需要写一个 Provider 适配器，就能复用所有现有功能。

**安全审批机制：**

AI 执行破坏性操作（删除文件、执行 bash 命令）前，Claudian 会弹出审批对话框。这个机制在 `core/security/` 中统一实现，所有 Provider 共享。

**国际化：**

支持 10 种语言（i18n 目录），对非英语用户友好。

---

六、隐私和数据安全
---------

Claudian 在 README 里花了很大篇幅讲隐私，这一点值得称赞。

| 数据类型 | 处理方式 |
| --- | --- |
| **发送到 API** | 你的输入、附件、图片、工具调用输出。默认发给 Anthropic/OpenAI/配置的 Provider |
| **本地存储** | 设置和会话元数据存在 `vault/.claudian/`；Claude 的 provider 文件存在 `vault/.claude/` |
| **会话记录** | 存在 `~/.claude/projects/`（Claude）、`~/.codex/sessions/`（Codex）、`~/.pi/agent/sessions/`（Pi） |
| **环境变量** | 子进程继承 Obsidian 进程环境 + 你在 Claudian 里配置的变量 |
| **后台活动** | **没有遥测信标**。网络活动仅限于 Provider 工作、MCP 端点和必要的 SDK/CLI 调用 |

**关键点：Claudian 自己不上传任何数据到第三方服务器。** 所有网络请求都是发给你配置的 AI Provider。

---

七、快速上手：5 分钟安装
-------------

### 方法 1：Obsidian 社区插件（推荐）

1. 打开 Obsidian → 设置 → 社区插件 → 浏览
2. 搜索 "Claudian"，点击安装
3. 启用插件

### 方法 2：GitHub Release

1. 从 GitHub Release 下载 `main.js`、`manifest.json`、`styles.css`
2. 放到 `vault/.obsidian/plugins/claudian/`
3. 在设置里启用

### 方法 3：源码安装（开发）

cd /path/to/vault/.obsidian/plugins
git clone https://github.com/YishenTu/claudian.git
cd claudian
npm install
npm run build

### 配置 Provider

1. 打开 Obsidian 设置 → Claudian → Provider
2. 选择 Claude / Codex / OpenCode / Pi
3. 配置 API Key 或 CLI 路径
4. 开始使用

---

八、赞助和生态
-------

Claudian 获得了 **贝壳找房（Ke Holdings Inc.）和 MOMA 团队** 的赞助支持，这也是国内大厂对开源 AI 工具生态的投入信号。

**Star 增长曲线：** 从项目发布到 13.2k Star，增长非常稳健，说明社区认可度很高。

---

九、谁适合用 Claudian？
----------------

| 人群 | 适合度 | 原因 |
| --- | --- | --- |
| Obsidian 重度用户 | 非常适合 | 直接在笔记库里用 AI，无需切换工具 |
| 技术写作者 | 非常适合 | AI 辅助写作、润色、生成技术文档 |
| 程序员 + 笔记爱好者 | 非常适合 | 代码和笔记在同一个工具里管理 |
| 用 Claude Code / Codex 的人 | 非常适合 | 把 AI 能力扩展到笔记场景 |
| 需要 AI 处理本地文件的人 | 适合 | AI 直接读写你的 Obsidian 笔记 |
| 纯代码开发（不用笔记） | 不太适合 | 直接用终端里的 Claude Code 更简单 |

---

十、总结：笔记库和 AI 的边界正在消失
--------------------

Claudian 最打动我的不是它的功能列表，而是它的**设计哲学**：

**你的笔记库不应该只是"被读取"的，它应该是 AI 的"工作空间"。**

在传统工作流里，AI 是外部工具，笔记库是静态仓库。两者之间靠复制粘贴连接。

Claudian 打破了这个边界：

* AI 不是"客人"，而是"室友"——住在你的笔记库里
* 笔记不是"参考资料"，而是"工作上下文"——AI 随时读取、随时写入
* 知识不是"沉淀"，而是"流动"——在笔记和代码之间双向流转

贝壳找房赞助这个项目，也说明了一点：**企业级团队开始把 AI 嵌入到日常知识管理工作流中**，而不只是偶尔"问 AI 一个问题"。

如果你已经在用 Obsidian 管理知识，同时也在用 Claude Code 或 Codex 写代码，Claudian 是一个**不需要改变任何现有习惯**的升级——你的笔记库还是那个笔记库，只是现在里面多了一个 AI 助手。

---

引用链接

[1]*https://github.com/YishenTu/claudian*

[2]*https://community.obsidian.md/plugins/realclaudian*

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=96c067d9a1b7eecf5b44998eadf60cdc21d44a74c392fdf5311aea018340a0474ef4c98a75b4&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782340110_1&req_id=1782340107152027&scene=169&mid=2247485806&sn=774f39743f6fb80692ba13e054820599&idx=1&__biz=MzIwNDM3Mjk1Mg==&sessionid=1782340109&subscene=200&clicktime=1782340119&enterid=1782340119&flutter_pos=2&biz_enter_id=5&jumppath=1101_1782339836610,1106_1782340107880,1001_1782340108811,1104_1782340110727&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQshvUbguFBsXxeFjTlhEJIhLTAQIE97dBBAEAAAAAAMKOBje1B+kAAAAOpnltbLcz9gKNyK89dVj0YmOLRRVcJQPaS+aK56pnPbRiB4YzXgmIz78g/Zw6+ns8WsmxzQa2LRA95NicqxuP71PsUfxB1WmQsOiJ2A2BdgOQR/C6yzTpygRAGA5Q47cU2DYyHT2sNV4IBmiTDICdARlRofs/0F+hN2C89xI7gMjbrb0wsn7owDiUFWR4qxOYwmK0ydyGgZC3UuGPRVVpql45MwM1nuV3UCU8LL0PW5pVXHE/bv54fi/RTRI=&pass_ticket=fXvSy2mG3WpCxA73Wl1uHdtni/Uwpc9q7wkC0JP5mVKndsmgxPGSegV6VORbSxFs&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d84394c2-9c48-4aad-af33-881a010c7dc6/d84394c2-9c48-4aad-af33-881a010c7dc6/)