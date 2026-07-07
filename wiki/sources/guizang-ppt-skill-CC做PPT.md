---
title: Claude Code 做 PPT：guizang-ppt-skill
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://github.com/op7418/guizang-ppt-skill]
source_path: 印象笔记管理工具/Claude Code 做 PPT 也太猛了：一句话生成高颜值网页PPT.md
tags: [claude-code, ppt, skill, tool-recommendation, guizang]
updated: 2026-06-27
---

---
title: "Claude Code 做 PPT 也太猛了：一句话生成高颜值网页PPT"
source: evernote
type: note
export_date: 2026-06-24
guid: 108f4233-d140-44ee-96da-9d9cef60fe99
---

# Claude Code 做 PPT 也太猛了：一句话生成高颜值网页PPT

🌟星标+👆关注，带给你更多有意思的GitHub项目

一做 PPT 就头大，标题放哪、配色怎么搭、图片怎么配、页面风格怎么统一。现在这些事，AI 统统可以帮你搞定，直接做出一份漂亮的 PPT。

今天给大家介绍一个宝藏 PPT skill：guizang-ppt-skill。这是歸藏老师在 GitHub 上维护的 AI PPT skill 项目，目前已有 7K+ Star，而且还在持续增长。

项目定位：一个适配 Claude Code / Codex 等 Agent 环境的网页 PPT 技能，用于生成单文件 HTML 横向翻页 PPT、PPT 配图和多平台封面。

Github地址：

https://github.com/op7418/guizang-ppt-skill

这篇文章按以下部分介绍：

效果展示：展示使用 skill 生成的 PPT 效果

skill 介绍：介绍 skill 内容

安装方法：介绍如何安装 skill

使用技巧：介绍如何使用 skill 生成高颜值 PPT

适用场景：介绍 skill 的适用场景

效果展示

我用这个 Skill 生成了一份关于《百年孤独》的读书分享 PPT，先看一下实际效果。

![](attachments/c99556d61ad5b545.png)

关闭

观看更多

更多

退出全屏

切换到竖屏全屏

退出全屏

AI煮代码汤已关注

分享视频

，时长 00:37

0/0

00:00/00:37

切换到横屏模式

继续播放

播放

00:00

/

00:37

00:37

倍速

全屏

倍速播放中

观看更多

转载

,

Claude Code 做 PPT 也太猛了：一句话生成高颜值网页PPT

AI煮代码汤已关注

分享点赞在看

已同步到看一看写下你的评论

视频详情

skill 介绍

1. 输出内容

skill 输出的是单文件 HTML，不需要构建，也不需要服务器，浏览器打开就能演示。支持键盘翻页、滚轮操作、触屏滑动、底部圆点导航，也可以按 ESC 打开页面索引。

2. 两套视觉系统

skill 内置两套视觉系统：

Style A: 电子杂志 × 电子墨水

Style B: 瑞士国际主义

Style A 电子杂志风

Style A 电子杂志风提供 5 套电子墨水主题，并内置 10 种常用页面布局。封面、章节页、数据大字报、图文页、图片网格、流程页、对比页这些场景，基本都能覆盖。

|  |  |
| --- | --- |
| 主题 | 适合场景 |
| 🖋 墨水经典 | 通用默认、商业发布、不知道选啥 |
| 🌊 靛蓝瓷 | 科技 / 研究 / AI / 技术发布会 |
| 🌿 森林墨 | 自然 / 可持续 / 文化 / 非虚构 |
| 🍂 牛皮纸 | 怀旧 / 人文 / 文学 / 独立杂志 |
| 🌙 沙丘 | 艺术 / 设计 / 创意 / 画廊 |

![](attachments/a65d597d821839a7.png)

Style B 瑞士国际主义

Style B 瑞士风更偏理性和秩序感，提供 22 种锁定版式，比如封面页、观点页、关键数据页、循环流程页、双栏对比页、大图页和结尾页等。它还内置 4 套高饱和锚点色，整体强调 16 列网格、直角色块、1px 发丝线，以及无阴影、无渐变、无圆角的干净视觉。如果只说“做一份瑞士风 PPT”，没有指定颜色，默认会推荐克莱因蓝 IKB。

|  |  |
| --- | --- |
| 主题 | 适合场景 |
| 克莱因蓝 IKB | 通用默认、商业发布、AI 产品、方法论 |
| 柠檬黄 | 年轻、运动、零售、Y2K 复古 |
| 柠檬绿 | 生态、可持续、Z 世代品牌 |
| 安全橙 | 警示、新闻、活力主题 |

![](attachments/c36e07919a5efc0d.png)

3. 主题和版式约束

项目对颜色和布局都有明确限制。Style A 和 Style B 都提前约束了主题、颜色和页面结构，避免每页风格不同。

AI 做设计最容易出现的问题，就是每一页都想“发挥一下”，最后页面看起来很热闹，但整体不统一。guizang-ppt-skill 的思路是：先收窄自由度，再提高完成度。

4. GPT Image 2 配图

需要配图时，可以用 GPT Image 2.0 生成纪实照片、信息图、流程图、系统关系图、UI 情景图等素材，再按模板比例插入页面。图片质量上来了，PPT 的质感也会跟着提升，这也是做出高颜值 PPT 的关键一步。

skill 明确规定了图片原则：图片只是 PPT 里的嵌入素材，不要自带页脚、标题、角标、页码或装饰边框。

5. 封面生成

skill 也可以基于文章或 PPT 核心观点生成平台封面。典型规格:

|  |  |
| --- | --- |
| 主题 | 适合场景 |
| 公众号头图 | 21:9，主标题优先,右侧或边缘保留视觉锚点 |
| 公众号分享卡 | 1:1，与头图共用主题色、关键词和视觉元素 |
| 小红书封面/轮播 | 3:4，大标题优先,多张时统一字号和视觉节奏 |
| 视频号/横版封面 | 16:9，适合标题 + 副标题 + 单一视觉焦点 |

封面原则和 PPT 一样:只用少量关键词,视觉重心落在大标题上,不要把正文堆满。

安装方法

1. 命令行安装

npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill

2. Agent 安装

把下面这段话复制粘贴给 Claude Code / Codex / Cursor / 任何有 shell 权限的 AI Agent,它会自动完成安装。

帮我安装 guizang-ppt-skill skill，github地址：

https://github.com/op7418/guizang-ppt-skill

安装完成后进行验证，对应的 skill 文件夹中应该看到 SKILL.md、assets/、references/ 三项

3. 手动安装

将项目下载下来，然后放到对应 Agent 的 skill 文件夹下。

Claude Code：~/.claude/skills/guizang-ppt-skill

Codex：~/.codex/skills/guizang-ppt-skill

使用技巧

使用时不需要一上来就写完整大纲，用自然语言说清楚需求就行，比如“帮我做一份 15 分钟的产品发布 PPT”。

以下是我自己测试的具体步骤：

自然语言输入要求

使用guizang-ppt-skill生成一份PPT，主题是讲解《百年孤独》。

使用时建议加上：“请按工作流程逐一询问”，避免 skill 偷懒直接套模板。这样 Agent 会通过一问一答的方式，依次确认受众、时长、素材、配图等内容，把需求先捋清楚，再开始生成，减少返工。

skill 会按流程提问，根据需要进行回答即可。

![](attachments/a13e33d797f78e4f.png)

![](attachments/7208d6edc7eb4f63.png)

![](attachments/cc3dfd92a53eb43a.png)

![](attachments/69929454dff72de2.png)

这一问可以直接提供已有素材，比如文档、文章链接、旧 PPT 或图片。如果手头没有素材，也可以像我一样，直接告诉 Agent：

去网上尽可能搜索相关内容，再整理成 PPT

![](attachments/1f03fd0a1181c099.png)

这一问可以明确使用 GPT Image 2生成图片，直接提示：

按需自行生成图片，可以调用gpt-image-2生成图片

这样 Agent 会根据 PPT 内容和页面需求，自动补充合适的图片，让整份 PPT 更丰富。想让 PPT 做得好看，这一步很关键。

![](attachments/e506afd59a3dc7fe.png)

![](attachments/d7e57de8b25d64da.png)

这一问可以按需添加一些硬性约束，比如：

不能太学术，要让没有读过的人能了解

七个问题都确认后，Agent 会根据前面的回答整理出 PPT 大纲和页面规划。这个阶段如果还有细节想调整，可以继续沟通修改；如果整体方向没问题，就可以让 Agent 开始生成 PPT。

这是我实际测试生成的一版，后面只做了微调，整体效果已经比较完整。

![](attachments/c99556d61ad5b545.png)

适用场景

skill 最适合这几类内容：

线下分享

行业内部讲话

私享会

AI 产品发布

demo day

带个人风格的演讲

大段表格数据、培训课件、多人协作编辑这几类需求，和它的定位不太匹配。

原因是：它的产物是静态 HTML，适合演讲表达和视觉呈现，不适合把所有信息密密麻麻塞进页面。

写在最后

大家可以试一下这个 skill，看看能生成什么样的 PPT。 欢迎在评论区分享 PPT 生成效果；也欢迎推荐自己用过的好用 skill。
