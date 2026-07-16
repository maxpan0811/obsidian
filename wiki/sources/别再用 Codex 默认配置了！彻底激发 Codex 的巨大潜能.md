---
title: 别再用 Codex 默认配置了！彻底激发 Codex 的巨大潜能
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/别再用 Codex 默认配置了！彻底激发 Codex 的巨大潜能.md
tags: [evernote, impression]
---

---
title: "别再用 Codex 默认配置了！彻底激发 Codex 的巨大潜能"
source: evernote
type: note
export_date: 2026-06-22
guid: 20b87bb3-a3ef-48e1-b82d-428bbc72c8ca
---

# 别再用 Codex 默认配置了！彻底激发 Codex 的巨大潜能

来源：[打开原文](https://mp.weixin.qq.com/s/zLXxbRFjnvsIiBI85P7KIw)

随着 Codex 功能迭代提速，它的配置文件字段数量也在持续膨胀。

根据我的不完全统计，目前已经超过 90 余个。

手动维护这些 TOML 文件，既容易在嵌套结构里埋下难以察觉的错误，也会让本该专注写代码的时间白白消耗在翻文档、对格式上。

于是大多数人选择了最省力的方式，全用默认配置。

## 用，当然是能用的！

但是你用的只是毛坯版的 Codex，而不是一个真正为你的工作流量身定制的 Codex。

举两个典型例子：你可以针对不同工作流切换不同的推理模式，也可以让规划阶段调用顶级模型做决策，执行阶段切换到更快、更便宜的开源模型降低成本，这一进一出，效率和开销都能同时优化。

当然， Codex 的优化配置还远远不止这些。

为了真正把 Codex 的潜能压榨出来，

可视化的 Codex 配置网站

，方便的了解每个字段的意义，方便字段编辑，同步生成 Codex 规范和详细的Toml配置文件。

## 这个网站提供了包括Codex 基础配置，高级配置 ，集成与扩展在内的全配置字段。

![](attachments/c29d03576cb35696.png)

不需要从头开始，方便载入默认的示范，支持一键标准配置文件的下载和复制，直接拿到Codex的配置目录就可以使用。

![](attachments/107c7dcda92c6f51.png)

同时还提供基于llms.txt标准格式AI Schema，引用后可以直接在AI对话中作为上下文来使用，实现AI自动编辑。

当然对话前提依然需要你先了解 Codex的配置提供了哪些功能和对应字段的意义，不然可能你怎么提问都不知道，建议先通过网站快速把这些字段浏览一遍，再结合自己的业务场景做选择配置。

为了方便阅读和理解，每个字段都加了对应的中文名称，字段后都增加了相关的注解。

![](attachments/e252ed5beff577a2.png)

点击问号标识，就可以查看该字段的详细说明。

![](attachments/d90baddc1392e607.png)

对于比较复杂难懂的配置字段，还增加了相关的文章教程说明。

![](attachments/b2cbaa215c757e42.png)

## 文章内容里面会包含更加详细的解释和代码示范。

![](attachments/cb12d5687d0aa9f7.png)

如果完全不知道从哪里下手也没有关系，在配置案例里面提供了可以直接抄作业的示范，修改一下就可以套用到本地。

![](attachments/be2b06af72f50b6a.png)

生成后配置文件如何使用呢？可以看这里：

.codex 现在核心就是两个位置。

## 1. 全局配置路径

~/.codex/config.toml

如果没有这个文件，自己创建：

mkdir -p ~/.codex  
zed ~/.codex/config.toml

Codex 的本地状态默认都放在 CODEX\_HOME 下，默认是 ~/.codex，里面常见文件包括 config.toml、auth.json、history.jsonl、日志和缓存。

## 2. 项目级配置路径

在项目根目录下面放：

项目目录/.codex/config.toml

例如：

/Users/x/Desktop/next-demo/.codex/config.toml  
/Users/x/Desktop/r2-html-drop/.codex/config.toml

项目级 .codex/config.toml 只有在这个项目被 Codex 信任之后才会加载。

Codex 会从项目根目录一路往当前目录查找 .codex/config.toml，越靠近当前目录的配置优先级越高。

## 3. 配置优先级

从高到低大概是：

命令行参数 / --config  
项目 .codex/config.toml  
profile 配置  
用户 ~/.codex/config.toml  
系统 /etc/codex/config.toml  
内置默认值

这个加载顺序就是前面配置会覆盖后面，

## 4. 推荐基础配置

可以先这样写：

# ~/.codex/config.toml  
  
model = "gpt-5.5"  
model\_reasoning\_effort = "high"  
  
approval\_policy = "on-request"  
sandbox\_mode = "workspace-write"  
  
[sandbox\_workspace\_write]  
network\_access = true  
writable\_roots = [  
  "/Users/x/Desktop"  
]

相关的字段可以直接在配置网站上搜索，这里再做一下解释：

model = "gpt-5.5"

设置默认模型，这里是 gpt-5.5。

approval\_policy = "on-request"

表示需要危险操作、权限升级时再问你。

现在官方推荐交互使用 on-request，on-failure 已经过时。

sandbox\_mode = "workspace-write"

表示 Codex 可以写当前工作区，但不是完全放开系统权限。sandbox\_mode 支持 read-only、workspace-write、danger-full-access。

## 5. 如果你想少确认一点

最简单最简单的配置，如下：

model = "gpt-5.5"  
model\_reasoning\_effort = "high"  
  
approval\_policy = "never"  
sandbox\_mode = "workspace-write"  
  
[sandbox\_workspace\_write]  
network\_access = true  
writable\_roots = [  
  "/Users/pan/Desktop"  
]

## 6. Profile 配置

如果你想分不同模式，比如“日常开发”“深度审查”，可以建：

~/.codex/deep-review.config.toml

内容：

model = "gpt-5.5"  
model\_reasoning\_effort = "xhigh"  
approval\_policy = "on-request"  
sandbox\_mode = "workspace-write"

使用：

codex --profile deep-review  
codex exec --profile deep-review "review this change"

官方现在要求 profile 用单独文件，例如 ~/.codex/deep-review.config.toml，不要再写老式的 [profiles.xxx]。

## 7. 最实用目录结构

你可以按这个来：

~/.codex/  
├── config.toml                  # 全局默认配置  
├── auth.json                    # 登录/认证状态，可能也走系统钥匙串  
├── history.jsonl                # 历史记录  
├── deep-review.config.toml      # 深度审查 profile  
└── logs / caches                # 日志缓存

项目里：

your-project/  
├── .codex/  
│   └── config.toml              # 项目专用配置  
├── AGENTS.md                    # 项目规则、约定、执行说明  
├── package.json  
└── src/

可视化图形配置网址：

https://codexapp.cc

榨干GPT！ChatGPT Web变身本地Codex，额度直接翻倍

打脸Claude Code！Codex 全端支持第三方模型接入

掀Claude Code的桌子！Codex 一键搬家功能

Fable 5 下架，但它的工作流被 Codex 继承下来了！


---

[📎 在印象笔记中打开](evernote:///view/207087/s1/20b87bb3-a3ef-48e1-b82d-428bbc72c8ca/20b87bb3-a3ef-48e1-b82d-428bbc72c8ca/)
