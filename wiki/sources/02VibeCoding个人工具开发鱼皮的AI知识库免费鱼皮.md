---
title: 02 Vibe Coding 个人工具开发 - 鱼皮的 AI 知识库（免费） - 鱼皮AI导航
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/02 Vibe Coding 个人工具开发 - 鱼皮的 AI 知识库（免费） - 鱼皮AI导航.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
---

---
title: "02 Vibe Coding 个人工具开发 - 鱼皮的 AI 知识库（免费） - 鱼皮AI导航"
source: evernote
type: note
export_date: 2026-06-25
guid: e86ea8aa-57b3-4814-b7c2-bcd8f2578153
---

# 02 Vibe Coding 个人工具开发 - 鱼皮的 AI 知识库（免费） - 鱼皮AI导航

# Vibe Coding 个人工具开发

你好，我是鱼皮。

在上一篇文‍章中，我们学习了完整的 5 步开发﻿流程。现在，是时候把‌这套流程真正用起来﻿了！CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

这篇文章，我会‍带你做 5 个实用的个人工具项目：个人作品集网站、待﻿办事项应用（进阶版）、Ma‌rkdown 笔记应用、番﻿茄钟计时器、天气查询应用。

需要先说明的是，本节教程‍更多的是做一个思路和项目开发流程的指导，目的是引导大家学会使用 Vibe Coding 开发﻿项目的方法，需要大家自行动手实践。如果你需要更‌完整的 Vibe Coding 图文和视频教程﻿，可以看看鱼皮的原创项目实战部分。

下面这些项目都是我精心挑选‍的，实用性强，做出来真的能用，不是玩具。难度适中，适合新手练手，不会太难也不会太简单。技术上涵盖了前﻿端、数据存储、API 调用等常见场景，完成基础版后‌还可以继续添加新功能。更重要的是，这些项目都可以放﻿到你的作品集里，向别人展示你的能力。iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

每个项目我都‍会提供完整的开发指南，包括需求分析、技术选型﻿、开发步骤和扩展思路。‌你可以根据自己的兴趣选﻿择项目，不需要按顺序完成。

## 一、项目实战 - 个人作品集网站

个人作品集网站是展示‍你能力的最好方式。无论你是找工作、接私活，还是想在社交媒体上分享你的作品，一﻿个漂亮的作品集网站都能给你加分。而且，‌这个项目本身就是你的第一个作品，可以放﻿到作品集里展示，是不是很有意思？rqSLrC9+VsupyuuN5CJXBcTogV3TB0PLFwn6Ar40W6Y=

这个网站要包含几个‍部分：个人介绍（姓名、头像、简介、联系方式）、技能展示（你会哪些技术﻿）、项目展示（你做过的项目，包括截‌图、描述、链接）。界面要做响应式设﻿计，在手机和电脑上都能正常显示。

技术选型上，我们使用 React + TypeScript + Vite 作为前端框架，Tailwind CSS 来写样式，最后部署到 Vercel 上线。这套技术栈很现代，也是目前最流行的前端开发方案。

8RBiBYXetftKEo4hgOQA6ySzS53uVFgx9cUh7w3EZYU=

### 开发步骤

1）需求研究

开发任何项目前，都要‍先做需求研究。你可以去看看别人的作品集网站是什么样的，比如在网上搜索 "deve﻿loper portfolio exam‌ples"，找找灵感。记录下你喜欢的设计﻿风格和功能，这些都可以作为你的参考。CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

2）写 PRD 文档

有了灵感后，就要写 PRD 文档了。创建一个 PRD.md 文件，明确你要展示哪些内容。下面是一个参考示例：

▼

markdown

复制代码

# 个人作品集网站 PRD

## 核心功能

1. 首页：大标题 + 简介 + 头像

2. 关于我：详细介绍 + 技能列表

3. 项目展示：项目卡片列表，每个卡片包含项目名称、项目截图、简短描述、技术栈、项目链接

4. 联系方式：邮箱、GitHub、社交媒体链接

## 设计要求

- 简洁现代的设计风格

- 深色主题

- 流畅的滚动动画

- 移动端适配

这个文档不需要写得很复杂，把核心功能和设计要求说清楚就行。

3）写技术设计文档

接下来写技术设计文档 TECH\_DESIGN.md。在这里确定具体的技术方案：fd4f1tQfAPm+pXdvnKYvdM1zeGurbULppuNaRqONYls=

▼

markdown

复制代码

# 技术设计

## 技术栈

- React + TypeScript + Vite

- Tailwind CSS

- React Router（如果需要多页面）

- Framer Motion（动画效果）

## 项目结构

src/

components/

Header.tsx

Hero.tsx

About.tsx

Projects.tsx

Contact.tsx

Footer.tsx

data/

projects.ts

skills.ts

App.tsx

main.tsx

## 数据管理

- 项目数据和技能数据存储在 TypeScript 文件中

- 使用数组存储，方便后续添加和修改

这个文档的‍作用是让 AI 知道你要用什么技术，﻿项目结构是什么样的‌。

4）写 AGENTS.md 文件fd4f1tQfAPm+pXdvnKYvdM1zeGurbULppuNaRqONYls=

然后创建 AGENTS.md 文件，告诉 AI 开发规范：

▼

markdown

复制代码

# 个人作品集网站开发指令

## 项目概述

使用 React + TypeScript + Tailwind CSS 开发的个人作品集网站。

## 开发规范

- 使用函数式组件 + Hooks

- 使用 Tailwind CSS 编写样式

- 组件要可复用

- 代码要有注释

## 设计要求

- 深色主题（背景 #0a0a0a，文字 #ffffff）

- 使用渐变色作为强调色

- 添加平滑的滚动动画

- 确保移动端适配

## 注意事项

- 保持设计简洁，不要过度设计

- 性能优化：图片使用懒加载

- 确保所有链接可点击

这个文件是‍给 AI 的开发规范，让它知道代码要﻿怎么写，设计要什‌么风格。8RBiBYXetftKEo4hgOQA6ySzS53uVFgx9cUh7w3EZYU=

5）开始开发

有了这三个‍文档，就可以开始开发了。打开 Cur﻿sor 等 AI ‌代码编辑器，开始和 A﻿I 对话。

第一个提示词是初始化项目：CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

▼

text

复制代码

请根据 PRD.md、TECH\_DESIGN.md 和 AGENTS.md 的要求，初始化一个 React + TypeScript + Vite 项目，并安装 Tailwind CSS。

这个提示词很‍简单，但包含了所有必要的信息。AI 会读取这三个﻿文档，然后按照要求创建项‌目结构，安装依赖，配置 ﻿Tailwind CSS。

然后逐步实现每个组件。比如创建 Hero 组件：iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

▼

text

复制代码

创建 Hero 组件，包含大标题、简介和头像。使用 Tailwind CSS 实现深色主题和渐变色效果。

这个提示词‍告诉 AI 要创建什么组件，包含哪些﻿内容，用什么技‌术实现。AI 会生成完整的﻿组件代码。

接着创建 Projects 组件：CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

▼

text

复制代码

创建 Projects 组件，展示项目列表。每个项目卡片包含截图、标题、描述和技术栈标签。

就这样一步‍一步，完成整个网站。每完成一个组件，﻿就在浏览器中预览一‌下效果，确保符合预﻿期。

6）部署上线9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

开发完成后，就可以部署上线了。部署的流程很简单：

- 把代码推送到 GitHub
- 登录 Vercel，导入 GitHub 仓库
- 点击部署，等待完成
- 获得你的网站链接

Vercel‍ 会自动检测你的项目类型，配置构建命令，非常﻿智能。部署完成后，你就‌有了一个可以访问的网站﻿链接，可以分享给别人看。CSbHtX/eCnivsAmDWOtPqwFLUaHPkJDjFn7sBYBeqB8=

### 扩展思路

基础版完成后，你还可以‍继续扩展功能。比如添加博客功能，写文章分享你的学习经验；添加深色/浅色主题切换，让用户可﻿以选择喜欢的主题；支持多语言，吸引国际用户；‌添加访问统计，了解网站访问情况；甚至可以加个﻿留言板功能，让访客可以给你留言。

## 二、项目实战 - 待办事项应用（进阶版）

完成了作品集网站后‍，让我们来做一个功能更复杂的项目。在快速上手部分，我们做过一个简单的待办﻿事项应用，只有最基本的添加和删除功能‌。现在，让我们做一个功能更强大的版本﻿，学习如何处理更复杂的业务逻辑。

这个进阶版的功能要丰富得多‍。添加待办事项时，除了标题，还可以设置描述、截止日期、优先级、分类。查看列表时，支持按分类、优先级、状态筛选，还有﻿搜索功能可以快速找到特定的待办事项。当然也支持编辑和删除‌。数据用 LocalStorage 保存，刷新页面不会丢﻿失。另外还有统计功能，显示完成率、待办数量等。

技术选型上，前端用 React + TypeScript + Vite，状态管理用 Zustand（一个轻量级的状态管理库，比 Redux 简单很多），样式用 Tailwind CSS，日期处理用 date-fns，数据存储用 LocalStorage。iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

### 开发步骤

1）定义数据模型9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

开发的第一步是定义数据模型。你需‍要明确待办事项包含哪些字段：id（唯一标识）、title（标题）、description（描述）、category（分类）、pr﻿iority（优先级：低、中、高）、dueDate（截止日期）、‌completed（是否完成）、createdAt（创建时间）。﻿把这些字段定义清楚，后面的开发就会很顺畅。

2）按功能模块开发

然后按功能模块来开发。建议‍的顺序是：先实现数据存储层，封装 LocalStorage 的读写操作；再实现状态管理，用 Zustan﻿d 创建全局 store；然后实现添加功能；接着实现‌列表展示和筛选；最后实现搜索和统计。这样循序渐进，每﻿完成一个模块就测试一下，确保正常工作。77OHVU1bP8xtDtJFw+mHdfuCmN9Qc3DIO4QsNHPUtcQ=

和 AI 对话时，可以这样说：

▼

text

复制代码

创建 Todo 数据模型和 LocalStorage 工具函数。

AI 会帮你‍定义数据结构和封装存储操作。这个提示词虽然简﻿单，但 AI 知道要做‌什么，因为它会参考你的﻿ PRD 和技术设计文档。9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

然后说：

▼

text

复制代码

使用 Zustand 创建全局状态管理，包括添加、删除、更新、筛选等方法。

AI 会创建一‍个完整的 store，包含所有需要的方法。Zusta﻿nd 是一个很轻量的状态管‌理库，比 Redux 简单﻿很多，但功能足够强大。iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

接着说：

▼

text

复制代码

创建 AddTodo 组件，包含表单输入和验证。

AI 会实‍现添加功能的界面和逻辑，包括输入框、下拉﻿选择、日期选择器等。‌每完成一个功能，就测﻿试一下，确保正常工作。fd4f1tQfAPm+pXdvnKYvdM1zeGurbULppuNaRqONYls=

### 关键技术点

这个项目有几个关键‍的技术点需要注意。首先是状态管理，因为功能比较多，用 Zustand 来﻿管理全局状态会方便很多。你可以让 A‌I 帮你创建一个 store，包含添﻿加、删除、更新、筛选等方法。

筛选功能要支持多‍条件筛选，比如同时按分类和优先级筛选。搜索功能要支持模糊搜索﻿，在标题和描述中查找关键词。这‌些逻辑都可以让 AI 帮你实现﻿，你只需要告诉它具体的需求就行。iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

### 扩展思路

基础版完成后，还可以‍继续扩展。比如添加标签功能，让待办事项可以打多个标签；支持子任务，一个大任务可以﻿分解成多个小任务；添加提醒功能，到期前自‌动提醒；支持数据导出为 CSV；甚至可以﻿用 Firebase 实现云端同步。

## 三、项目实战 - Markdown 笔记应用

掌握了状态管理和数‍据筛选后，我们来学习如何处理文本编辑和实时预览。Markdown 是程序﻿员最常用的文档格式，做一个 Mark‌down 笔记应用可以让你学习如何处﻿理文本编辑、实时预览等功能。

这个项目要实现一个完整的 ‍Markdown 笔记应用。用户可以创建笔记，输入标题和内容。界面采用左右分栏，左侧是编辑器，右侧实﻿时预览渲染后的效果。左侧还要显示笔记列表，支持搜索‌。数据保存在 LocalStorage，支持删除笔﻿记。代码块要有语法高亮，这样看起来更专业。

技术选型上，前端用 React + TypeScript + Vite，Markdown 解析用 react-markdown，代码高亮用 react-syntax-highlighter，样式用 Tailwind CSS，数据存储用 LocalStorage。77OHVU1bP8xtDtJFw+mHdfuCmN9Qc3DIO4QsNHPUtcQ=

### 开发步骤

1）实现基础布局iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

开发的第一步是‍实现基础布局，创建左右分栏的布局，左侧是编辑器，右侧是预﻿览区。这个布局用 Tailw‌ind CSS 的 Flex﻿ 或 Grid 很容易实现。

可以这样告‍诉 AI：             ﻿         ‌         ﻿

▼

text

复制代码

创建左右分栏布局，左侧是 Markdown 编辑器（大文本框），右侧是预览区。使用 Tailwind CSS 实现响应式布局。

AI 会创‍建一个美观的分栏布局，在电脑上是左右﻿分栏，在手机上会自‌动变成上下布局。

2）集成 Markdown 解析

然后集成 Mar‍kdown 解析。使用 react-markdown 这个库，可﻿以很方便地将 Markdown ‌文本转换为 HTML。你只需要把﻿文本传给这个组件，它就会自动渲染。77OHVU1bP8xtDtJFw+mHdfuCmN9Qc3DIO4QsNHPUtcQ=

告诉 AI：

▼

text

复制代码

使用 react-markdown 将 Markdown 文本转换为 HTML，在预览区显示渲染后的效果。

这个提示词‍很简洁，但 AI 知道要做什么。它会安装﻿ react-mar‌kdown 库，导入﻿组件，然后在预览区使用。VprbsNNi06uIawNJLcFbxOcV+1AAkBa39eKpDvimHqc=

3）实现实时预览

接下来实现实‍时预览。这个功能的关键是监听编辑器的输入变化﻿，实时更新预览区。当用‌户在左侧编辑时，右侧要﻿同步显示渲染后的效果。

告诉 AI：VprbsNNi06uIawNJLcFbxOcV+1AAkBa39eKpDvimHqc=

▼

text

复制代码

监听编辑器的输入变化，实时更新预览区。用户在左侧编辑时，右侧同步显示 Markdown 渲染后的效果。

这个功能用 R‍eact 的状态管理很容易实现。AI 会把编辑器的内﻿容存储在 state 中，‌然后传给预览组件，每次内容﻿变化都会自动更新预览。

4）添加代码高亮9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

代码高亮也很重要，让代码块看起来更专业。告诉 AI：

▼

text

复制代码

配置 react-syntax-highlighter，让代码块支持语法高亮。支持多种编程语言，比如 JavaScript、Python、Java 等。

AI 会配置 ‍react-syntax-highlighter，当 M﻿arkdown 中有代码块时‌，会用语法高亮来渲染，不同的﻿语法元素会显示不同的颜色。iRu2gwlWvts42gYYX7UjwjFZ3N5lB3V8jhzvCf4HrWk=

5）添加笔记管理功能

最后添加笔记管理功能。告诉 AI：

▼

text

复制代码

实现笔记管理功能：

- 左侧添加笔记列表，显示所有笔记的标题

- 点击笔记可以切换到该笔记

- 支持创建新笔记、删除笔记

- 支持搜索笔记（按标题搜索）

- 数据保存在 LocalStorage

这个提示词‍包含了所有的功能要求，AI 会一次性﻿实现所有功能。

### 关键技术点

这个项目的关键是‍实现 Markdown 的实时预览。当用户在左侧编辑时，右侧﻿要实时显示渲染后的效果。这个功‌能用 react-markdo﻿wn 库可以很容易实现。9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

代码高亮也很重要，可以让 AI 帮你配置 react-syntax-highlighter，支持多种编程语言的语法高亮。为了更好的用户体验，可以让 AI 添加一些优化，比如 Tab 键插入空格而不是切换焦点，支持 Ctrl+B 加粗等快捷键，自动保存草稿等。

### 扩展思路

基础版完成后，可以继续‍扩展功能。比如支持图片上传，让笔记可以插入图片；添加目录导航，自动生成文章大纲；支持导出﻿为 PDF，方便分享；添加主题切换，提供多种‌编辑器主题；支持多种 Markdown 风格﻿，比如 GitHub 风格、标准风格等。CSbHtX/eCnivsAmDWOtPqwFLUaHPkJDjFn7sBYBeqB8=

## 四、项目实战 - 番茄钟计时器

前面的项目都是数‍据展示和管理，现在让我们做一个涉及定时器和通知的项目。番茄工﻿作法是一种流行的时间管理方法，‌做一个番茄钟应用可以让你学习如﻿何处理定时器、通知等功能。

番茄工作法的原理是工作 ‍25 分钟，休息 5 分钟，这样循环进行。这个应用要实现倒计时功能，支持开始、暂停、重置。用户可﻿以自定义工作和休息的时长。时间到了要发出通知提醒‌，还可以播放提示音。另外还要有统计功能，记录完成﻿的番茄钟数量，帮助用户了解自己的工作效率。77OHVU1bP8xtDtJFw+mHdfuCmN9Qc3DIO4QsNHPUtcQ=

技术选型上，前端用 React + TypeScript + Vite，样式用 Tailwind CSS，通知用浏览器自带的 Notification API，数据存储用 LocalStorage。

### 开发步骤

1）实现倒计时逻辑

开发的核心是实现倒计时逻辑。告诉 AI：

▼

text

复制代码

实现番茄钟倒计时功能：

- 默认工作 25 分钟，休息 5 分钟

- 支持开始、暂停、重置

- 时间格式显示为 MM:SS

- 倒计时结束时触发提醒

这个提示词清楚‍地说明了要实现什么功能。AI 会用 JavaScri﻿pt 的 setInter‌val 来实现倒计时，每秒﻿减 1，到 0 时触发提醒。

2）实现通知功能

然后实现通‍知功能。浏览器的 Notificatio﻿n API 可以发送‌系统通知，但需要先请求﻿用户权限。告诉 AI：mQKtpv74BWKCp/xIVfU9iS80+xV5ZB7eSk1mngkp/rk=

▼

text

复制代码

实现浏览器通知功能：

- 页面加载时请求通知权限

- 倒计时结束时发送通知

- 通知标题是"番茄钟"，内容是"时间到了，该休息了！"

这个提示词‍说明了通知的触发时机和内容。AI 会先检﻿查浏览器是否支持通知‌，然后请求权限，最后﻿在时间到了的时候发送通知。

3）添加音‍效                 ﻿         ‌      CSbHtX/eCnivsAmDWOtPqwFLUaHPkJDjFn7sBYBeqB8=

还可以添加音效‍。时间到了播放一个提示音，这样即﻿使用户没看屏幕也能‌知道时间到了。告诉﻿ AI：

▼

text

复制代码

添加提示音功能：

- 准备一个提示音文件（放在 public 目录）

- 倒计时结束时播放提示音

AI 会用 Audio 对象来播放音频文件。77OHVU1bP8xtDtJFw+mHdfuCmN9Qc3DIO4QsNHPUtcQ=

4）添加统计功能

最后添加统计功能。告诉 AI：

▼

text

复制代码

实现统计功能：

- 记录完成的番茄钟数量

- 显示今日完成数量、本周完成数量

- 数据保存在 LocalStorage

这样用户可以看到自己的工作效率，更有成就感。

### 关键技术点

这个项目的核心‍是倒计时逻辑和通知功能。倒计时要准确，每秒减 1，不能有﻿误差。通知功能需要先请‌求用户权限，如果用户拒绝了﻿权限，要给出友好的提示。rqSLrC9+VsupyuuN5CJXBcTogV3TB0PLFwn6Ar40W6Y=

为了更好的用‍户体验，可以在计时时更新页面标题，这样用户切换到﻿其他标签页时也能看到剩‌余时间。还可以添加提示音，﻿时间到了播放一个声音。

### 扩展思路

基础版完成后，可以继续‍扩展功能。比如添加长休息功能，4 个番茄钟后休息 15 分钟；记录每天的番茄钟数量，生成﻿统计图表；添加任务列表，把番茄钟和具体任务关‌联起来；数据可视化，用图表展示工作效率；甚至﻿可以支持背景音乐，让工作更有氛围。mQKtpv74BWKCp/xIVfU9iS80+xV5ZB7eSk1mngkp/rk=

## 五、项目实战 - 天气查询应用

最后，让我‍们来做第一个需要调用外部 API 的﻿项目。这个项目可以让你学‌习如何与后端服务交互﻿，处理异步请求和错误。

这个项目要实现天气‍查询功能。用户输入城市名称，查询当前天气，显示温度、天气状况、湿度、风速等﻿信息。还要显示未来几天的天气预报。‌可以自动获取用户位置并显示天气。常用﻿的城市可以收藏起来，方便下次查询。CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

技术选型上，前端用 React + TypeScript + Vite，样式用 Tailwind CSS，天气数据通过 [OpenWeatherMap API](https://openweathermap.org/api "A ") 获取（免费），收藏的城市用 LocalStorage 保存。

8RBiBYXetftKEo4hgOQA6ySzS53uVFgx9cUh7w3EZYU=

### 开发步骤

1）注册 API

开发的第一步是注册‍ API。去 OpenWeatherMap 官网注册账号，获取免费的 A﻿PI Key。注册很简单，填写基本信息就‌可以了。免费版有一定的调用次数限﻿制，但对于学习和个人使用完全够用。rqSLrC9+VsupyuuN5CJXBcTogV3TB0PLFwn6Ar40W6Y=

2）封装 API 请求

然后封装 ‍API 请求。创建一个 API 工具﻿文件，把所有的 A‌PI 调用都封﻿装在这里。告诉 AI：

▼

text

复制代码

创建 API 工具文件，封装天气 API 调用：

- 定义 API 基础 URL 和 API Key（从环境变量读取）

- 创建 getCurrentWeather 函数，获取当前天气

- 创建 getForecast 函数，获取未来天气预报

- 支持按城市名称或经纬度查询

- 要有错误处理

这个提示词‍说明了要封装哪些功能，AI 会创建完﻿整的 API 工‌具文件。

3）实现搜索功能

接下来实现搜索功能。告诉 AI：CiPk3aA4dfyj9EjOfH45cIglBo+kOhrc5asBIK7ygAA=

▼

text

复制代码

实现天气查询功能：

- 用户输入城市名称，点击搜索

- 调用 API 获取天气数据

- 显示温度、天气状况、湿度、风速等信息

- 查询过程显示加载动画

- 查询失败显示友好提示（比如"找不到该城市"）

这个提示词‍包含了功能要求和用户体验要求。AI ﻿会实现完整的搜索功‌能，包括加载状态和﻿错误处理。

4）实现位‍置定位               ﻿         ‌        CSbHtX/eCnivsAmDWOtPqwFLUaHPkJDjFn7sBYBeqB8=

还可以实现位置定位功能。告诉 AI：

▼

text

复制代码

实现自动定位功能：

- 使用浏览器的 Geolocation API 获取用户位置

- 根据经纬度查询天气

- 如果用户拒绝定位权限，显示提示

这样用户不用手动输入城市名称，更方便。9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

5）添加收藏功能

最后添加收藏功能。告诉 AI：

▼

text

复制代码

实现城市收藏功能：

- 查询过的城市可以收藏

- 收藏列表保存在 LocalStorage

- 点击收藏的城市可以快速查询

- 支持删除收藏

这样用户可以快速查询常用城市的天气。

### 关键技术点

这个项目的关键是处‍理好 API 调用。API 请求可能失败，要做好错误处理。比如找不到城市﻿、API Key 无效、网络错误等，‌都要给出友好的提示。在请求过程中要显﻿示加载动画，让用户知道正在查询。9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=

还要注意 API Key 的安全。不要直接写在代码里，要使用环境变量。创建一个 .env.local 文件，把 API Key 放进去，然后在代码中通过环境变量读取。记得把 .env.local 添加到 .gitignore，不要提交到 Git，避免泄露。

### 扩展思路

基础版完成后，可以继‍续扩展功能。比如添加天气图标和动画，让界面更生动；显示空气质量指数，关注健康﻿；支持多城市对比，一次查看多个城市的天‌气；添加天气预警，及时提醒恶劣天气；甚﻿至可以查询历史天气，分析天气趋势。8RBiBYXetftKEo4hgOQA6ySzS53uVFgx9cUh7w3EZYU=

## 写在最后

通过这 5 个项目，你‍已经学习了 Web 开发的核心技能：组件开发、状态管理、数据持久化、API 调用、用户交﻿互等。从简单的作品集网站，到复杂的待办事项应‌用，从文本编辑器到定时器，再到调用外部 AP﻿I，每个项目都让你掌握了新的技能。

如果你在开‍发过程中遇到困难，或者想学习更多的开发技﻿巧和最佳实践，可以参‌考本教程的经验技巧板﻿块，那里有更详细的讲解。mQKtpv74BWKCp/xIVfU9iS80+xV5ZB7eSk1mngkp/rk=

掌握了个人‍工具开发后，在下一篇文章中，我会带你﻿做更酷的 AI 应‌用，让我们一起探索﻿ AI 的无限可能。

## 

9chWMQ7We23/Q9LjGF84uV9QonUxGOU3a5J+eWKzipk=


---

[🌐 原始链接](https://ai.codefather.cn/library/2010974707535777794)
[📎 在印象笔记中打开](evernote:///view/207087/s1/e86ea8aa-57b3-4814-b7c2-bcd8f2578153/e86ea8aa-57b3-4814-b7c2-bcd8f2578153/)
