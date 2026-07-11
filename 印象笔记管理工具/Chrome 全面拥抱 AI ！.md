# Chrome 全面拥抱 AI ！

---

速读摘要

在网页开发中，加入AI模型，尤其是大型语言模型，通常需要依赖服务器端解决方案。Chrome的内置AI主要依托于Web平台API和浏览器功能，可以直接在浏览器中运行AI模型，而无需依赖服务器端解决方案。Summarizer API的使用也非常简单，开发者只需几步即可完成摘要生成任务。Summarizer API使用强大的AI模型来生成高质量的摘要，该模型会在首次使用时自动下载到本地。

原文约4356 字|图片5张|建议阅读9分钟|[评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2024-11-24&nu=c67a8515-6d06-4513-aded-87c47fa932ca&fr=myyxbj&ud=328ef&v=2&sig=A9B06B81C0944EA756922558EA88D1C3)

原文链接: [http://mp.weixin.qq.com/s?\_\_biz=Mzk0MDMwMzQyOA==&mid=2247501...](http://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247501921&idx=1&sn=cf58ea5e068abb772c8244fa17822d82&chksm=c3545cd0c75f059949c30eda9eb7caca8bc5dc161d7dd42c21032a3a7df1fdfdbfb19552feee&mpshare=1&scene=1&srcid=112460v6vcgKRRIoEbUajp59&sharer_shareinfo=5bf2adebd1b4e95ccc01759c2d84a972&sharer_shareinfo_first=5bf2adebd1b4e95ccc01759c2d84a972#rd)

大家好，我是 [ConardLi](https://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247493407&idx=1&sn=41b8782a3bdc75b211206b06e1929a58&chksm=c2e11234f5969b22a0d7fd50ec32be9df13e2caeef186b30b5d653836b0725def8ccd58a56cf&scene=21#wechat_redirect)。

最近 Chrome 在 AI 领域持续发力，提供了内置 AI 的基础能力，并且推出了多项 AI 相关的 API。

* Translation API
* Summarizer API
* Prompt API

![](.evernote-content/7034AE15-27EE-4730-BAA1-1BE4EC4F50B6/4AF8C01A-3DFD-47E4-AED7-BBD9E241F5BC.jpg)

下面我们来详细了解下。

Chrome 内置 AI
------------

在网页开发中，加入 AI 模型，尤其是大型语言模型，通常需要依赖服务器端解决方案。这是因为，即使是最小的生成式 AI 模型，其体积也远超网页平均大小。

这种情况下，每个网站都必须在页面加载时下载模型，这对开发者和用户来说都很不切实际。 为解决这个问题，Chrome 正在开发能够将 AI 模型（包括大型语言模型（LLM））直接集成到浏览器的 Web 平台 API 和浏览器功能。

借助内置 AI，我们的网站或 Web 应用程序可以执行 AI 驱动的任务，而无需部署或管理自己的 AI 模型。

### 内置 AI 的优势

Chrome 的内置 AI 主要依托于  `Web 平台 API`  和浏览器功能，可以直接在浏览器中运行 AI 模型，而无需依赖服务器端解决方案。

#### 1.  高效便捷

* **无需部署和管理模型**: 开发者无需操心模型的下载、更新、存储和维护，这些都由浏览器接管，大大简化了开发流程。
* **轻松调用 AI 能力**: 通过  `Web 平台 API`  ，开发者可以方便地调用各种 AI 功能，例如翻译、摘要、文本生成等，就像使用其他  `Web API`  一样简单。

#### 2.  性能卓越

* **本地运行，速度更快**: 模型在本地运行，无需网络请求，大大降低了延迟，提升了用户体验，例如，在翻译场景下，用户可以获得近乎实时的翻译结果。
* **硬件加速，性能更强**: Chrome 的 AI 运行时经过优化，可以充分利用设备的硬件资源，例如  `GPU` 、 `NPU`  等，最大程度地提升 AI 模型的运行效率。

#### 3.  安全可靠

* **保护用户隐私**: 敏感数据可以在用户设备上进行本地处理，无需上传到服务器，有效保护了用户隐私，例如，在涉及个人信息的 AI 应用中，可以避免数据泄露的风险。
* **持续更新**: 浏览器会自动更新 AI 模型，确保用户始终使用最新、最安全的版本，开发者无需手动更新模型，也无需担心模型版本 compatibility 问题。

### 客户端 AI  vs.  服务器端 AI

* **客户端 AI**:  更适合轻量级、对实时性要求高的任务，例如文本自动完成、语法纠正等，能够提供更流畅、更快速的用户体验，同时还能增强用户隐私保护。
* **服务器端 AI**:  更适合计算密集型、需要大量数据的任务，例如大型语言模型的训练和推理，可以处理更复杂的 AI 任务，并支持更广泛的平台和设备。

Chrome 倡导 **混合 AI**  架构，根据实际需求，灵活地结合客户端 AI 和服务器端 AI，例如：

* **默认使用服务器端 AI**，在设备性能足够、网络条件良好的情况下，可以将部分任务迁移到客户端，利用客户端 AI 提升性能和效率。
* **在设备离线或网络连接不稳定的情况下**，可以无缝切换到客户端 AI，保证用户仍然可以正常使用 AI 功能。

### Chrome  内置 AI  API  概览

Chrome 提供了多种  `API`  来帮助开发者使用内置 AI 功能：

* **任务 API**:  用于执行特定任务，例如  `Translator API` （翻译）、 `Summarizer API` （摘要）等，这些  `API`  通常使用针对特定任务优化的专家模型。
* **探索性 API**: 用于探索新的 AI 用例，例如  `Prompt API`  ，开发者可以使用这些  `API`  在本地进行实验，并向 Chrome 团队提供反馈。

#### `Gemini Nano` :  专为浏览器而生

![](.evernote-content/7034AE15-27EE-4730-BAA1-1BE4EC4F50B6/D55D9A1C-4570-4C7A-A7E5-9FA7B951FF24.png)

Chrome 的内置 AI 主要使用  `Gemini Nano`  模型，这是  `Gemini`  系列  `LLM`  中最高效的版本，专为在大多数现代台式机和笔记本电脑上本地运行而设计，最适合与语言相关的用例，例如摘要、改写、分类等。

为了进一步提高模型性能，Chrome 还使用了微调技术，针对特定任务动态优化  `Gemini Nano`  模型，而无需下载新的模型。

#### 更多  API  和  LoRA  支持

![](.evernote-content/7034AE15-27EE-4730-BAA1-1BE4EC4F50B6/37084DB9-3190-4BF5-A1F9-724AFADA4B95.png)

Chrome 团队正在积极开发更多内置 AI  API ，并计划在未来提供对  `LoRA`  技术的支持，允许开发者通过调整模型权重来进一步提升内置模型的性能，扩展 AI 应用场景。

### 抢先体验

为了更好地满足开发者需求，Chrome 团队推出了一系列项目，让开发者可以提前体验内置 AI 的强大功能：

* **Origin Trials**:  开发者可以注册  `Origin Trials`  ，在正式发布之前，在真实的网站上测试新的  `API`  ，并向 Chrome 团队提供反馈，例如， `Translator API`  和  `Summarizer API`  目前都处于  `Origin Trials`  阶段。
* **Early Preview Program**:  开发者可以加入  `Early Preview Program` ，提前了解新的内置 AI  API  ，并参与邮件列表讨论。

下面我们来具体介绍一下 Chrome 新推出的三个 API：

打破语言障碍： Chrome  内置  `Translation API`
-------------------------------------

在全球化的今天，网站的多语言支持已经成为标配，但传统的翻译方式往往依赖于云服务，用户需要在本地和服务器之间来回传输数据，不仅速度慢，成本高，还存在泄露隐私的风险。

Chrome 推出的  `Translation API`  为 Web 开发者提供了一种全新的解决方案，可以直接在浏览器中调用本地 AI 模型进行翻译，为用户带来更流畅、更快速、更安全的翻译体验。

### `Translation API`  的优势

* **速度更快**:  翻译过程在本地完成，无需网络请求，大大缩短了翻译时间，用户可以获得近乎实时的翻译结果，例如，在浏览外文网站时，可以即时翻译网页内容，无需等待。
* **成本更低**:  由于无需调用云服务，开发者可以节省服务器成本和带宽成本，降低运营成本，让开发者可以将更多资源投入到产品创新中。
* **隐私更强**:  翻译过程在用户设备上进行，无需将文本数据上传到服务器，有效保护了用户隐私，避免了敏感信息泄露的风险，让用户可以更放心地使用翻译功能。

### 如何使用  `Translation API`

`Translation API`  的使用非常简单，开发者只需几行代码即可完成翻译任务。

#### 1.  功能检测

在使用  `Translation API`  之前，首先需要检测当前浏览器是否支持该 API。

```
if ('translation' in self && 'createTranslator' in self.translation) {//  `Translation API`  支持}
```

#### 2.  检查语言对支持

`Translation API`  使用语言包来进行翻译，语言包就像是一个特定语言的词典，在进行翻译之前，需要先检查浏览器是否支持目标语言对，以及是否需要下载相应的语言包。

```
const supportResult = await translation.canTranslate({sourceLanguage: 'en',targetLanguage: 'fr',});switch (supportResult) {case 'no':// 浏览器不支持该语言对，无法进行翻译break;case 'readily':// 浏览器支持该语言对，可以直接进行翻译break;case 'after-download':// 浏览器需要下载相应的语言包才能进行翻译translator.ondownloadprogress = progressEvent => {// 更新下载进度条updateDownloadProgressBar(progressEvent.loaded, progressEvent.total);};break;}
```

#### 3. 创建并运行翻译器

```
// 创建一个将英语翻译成法语的翻译器。const translator = await self.translation.createTranslator({sourceLanguage: 'en',targetLanguage: 'fr',});// 调用 translate() 方法进行翻译const translatedText = await translator.translate('Where is the next bus stop, please?');// 打印翻译结果console.log(translatedText); // "Où est le prochain arrêt de bus, s'il vous plaît ?"
```

### Origin Trial 阶段的限制

Translation API 目前处于 Origin Trial 阶段，开发者可以注册并体验该功能，但也需要注意一些限制：

* 支持的语言对: 目前最多可以下载三个语言包进行翻译，并且语言对的选择需要满足一定的条件，以保护用户隐私，避免潜在的指纹识别风险。
* 顺序翻译: 翻译任务是按顺序处理的，如果发送大量文本进行翻译，后续的翻译任务会被阻塞，直到之前的任务完成。
* Web Worker 支持: 目前 Translation API 仅支持在主线程中使用，未来会支持在 Web Worker 中使用。

### Demo

https://chrome.dev/web-ai-demos/translation-language-detection-api-playground/

![](.evernote-content/7034AE15-27EE-4730-BAA1-1BE4EC4F50B6/FE2E2335-DFA9-42AC-A7BA-0F4C355DB09C.png)

一键提炼摘要： Chrome  内置  `Summarizer API`
------------------------------------

想象一下，只需轻轻一点，就能将冗长的文章、复杂的文档甚至热闹的聊天对话，提炼成简洁精炼的摘要，这将为用户节省多少时间和精力！

Chrome  新推出的  `Summarizer API`  就能实现这个效果！它可以根据用户的需求，生成不同类型、不同长度和格式的摘要，例如句子、段落、项目符号列表等，为用户提供更便捷、更高效的信息获取方式。

### `Summarizer API`  的应用场景

* **快速了解文章要点**:  用户无需阅读整篇文章，即可快速了解文章的核心内容，例如，在浏览新闻网站时，可以快速了解新闻事件的来龙去脉。
* **生成文章标题和摘要**:  帮助内容创作者更轻松地生成吸引人的标题和摘要，提高内容的曝光率和点击率。
* **提炼聊天对话关键信息**:  用户可以快速回顾聊天记录，提取重要信息，例如，在客服聊天中，可以快速了解客户的问题和诉求。

### 如何使用  `Summarizer API`

`Summarizer API`  的使用也非常简单，开发者只需几步即可完成摘要生成任务。

#### 1.  功能检测

与  `Translation API`  类似，在使用  `Summarizer API`  之前，首先需要检测当前浏览器是否支持该 API。

```
if ('ai' in self && 'summarizer' in self.ai) {//  `Summarizer API`  支持}
```

#### 2.  模型下载

`Summarizer API`  使用强大的 AI 模型来生成高质量的摘要，该模型会在首次使用时自动下载到本地。

```
const summarizer = await ai.summarizer.create({monitor(m) {m.addEventListener('downloadprogress', (e) => {// 可以通过监听 'downloadprogress' 事件来追踪下载进度console.log(`Downloaded ${e.loaded} of ${e.total} bytes.`);});}});
```

#### 3.  运行摘要器

`Summarizer API`  提供了两种摘要生成方式：

```
// 获取需要摘要的文本内容const longText = document.querySelector('article').innerText;// 调用 summarize() 方法生成摘要const summary = await summarizer.summarize(longText, {// 可以通过 context 参数来提供额外的上下文信息，帮助模型生成更准确的摘要context: 'This article is intended for a tech-savvy audience.',});// 打印摘要结果console.log(summary);
```

```
// 获取需要摘要的文本流const textStream = fetch('long-article.txt').then(res => res.body);// 调用 summarizeStreaming() 方法生成摘要流const summaryStream = await summarizer.summarizeStreaming(textStream);// 逐段处理摘要流const reader = summaryStream.getReader();let summary = '';while (true) {const { done, value } = await reader.read();if (done) {break;}summary += value;// 可以在这里实时更新摘要内容}// 打印最终的摘要结果console.log(summary);
```

### `Origin Trial`  阶段的限制

`Summarizer API`  目前也处于  `Origin Trial`  阶段，开发者需要注意以下限制：

* **语言支持**:  目前仅支持英文文本的摘要生成。
* **使用限制**:  在  `Origin Trial`  阶段， `Summarizer API`  的使用次数可能会有限制。

### Demo

https://chrome.dev/web-ai-demos/summarization-api-playground/

Chrome 内置 Prompt API
--------------------

Chrome 扩展程序一直以来都是增强浏览器功能、提升用户体验的利器。现在，借助  `Prompt API`  ，开发者可以让扩展程序具备更强大的 AI 能力，为用户带来更智能、更便捷的服务。

### 使用场景：

1. **即时日历事件：** 开发一个 Chrome 扩展程序，自动从网页中提取事件详情，让用户仅需几步就能创建日历条目。
2. **无缝联系人提取：** 创建一个扩展程序，从网站中提取联系信息，方便用户联系业务或将详细信息添加到他们的联系人列表中。
3. **动态内容过滤：** 开发一个 Chrome 扩展程序，分析新闻文章，并根据用户定义的主题自动模糊或隐藏内容。

### 使用方法

#### 加入 Prompt API 起源试用

Prompt API 起源试用将在 Chrome 131 到 136 版本中运行，开放给所有开发者进行早期访问。如果您对起源试用不熟悉，这些是时间有限的项目，旨在让开发者测试实验性平台功能、收集用户反馈并逐步迭代，最终推出正式版。

#### 参与起源试用步骤

1. 在 `manifest.json` 文件中添加 `"aiLanguageModelOriginTrial"` 权限，例如：

```
    {"permissions": ["aiLanguageModelOriginTrial"],"trial_tokens": ["GENERATED_TOKEN"]}
```

2. 使用 URL `chrome-extension://YOUR_EXTENSION_ID` 作为 Web Origin 注册您的扩展。例如：`chrome-extension://ljjhjaakmncibonnjpaoglbhcjeolhkk`
3. 注册后，您将获得一个生成的令牌，该令牌需要传递给 `manifest.json` 文件中的 `trial_tokens` 字段。

请注意，这种权限授予是临时的，仅在起源试用期间有效。如果 API 正式发布，您需要更新并重新上传扩展，移除过期的权限并替换为最终权限。

#### 模型下载并检查其可用性

Prompt API 使用 `Gemini Nano` 模型，每次扩展首次使用时需要单独下载模型。

```
const capabilities = await chrome.aiOriginTrial.languageModel.capabilities();if (capabilities.available === 'after-download') {const session = await chrome.aiOriginTrial.languageModel.create({monitor(m) {m.addEventListener("downloadprogress", (e) => {console.log(`Downloaded ${e.loaded} of ${e.total} bytes.`);});}});}
```

#### 会话与提示操作

每个会话可以使用 `topK` 和 `temperature` 参数进行自定义，并通过 `session.prompt` 或 `session.promptStreaming` 函数向模型发送提示。

##### 创建会话

```
const capabilities = await chrome.aiOriginTrial.languageModel.capabilities();const session = await chrome.aiOriginTrial.languageModel.create({temperature: Math.max(capabilities.defaultTemperature * 1.2, 2.0),topK: capabilities.defaultTopK,});
```

##### 系统提示

```
const session = await chrome.aiOriginTrial.languageModel.create({systemPrompt: '你是一个乐于助人的友好助手。',});await session.prompt('意大利的首都是哪里？');// '意大利的首都是罗马。'
```

##### 初始提示

```
const session = await chrome.aiOriginTrial.languageModel.create({initialPrompts: [{ role: 'system', content: '你是一个乐于助人的友好助手。' },{ role: 'user', content: '意大利的首都是哪里？' },{ role: 'assistant', content: '意大利的首都是罗马。'},{ role: 'user', content: '那里讲什么语言？' },{ role: 'assistant', content: '意大利的官方语言是意大利语。[...]' }]});
```

##### 提示和会话持久性

```
const session = await chrome.aiOriginTrial.languageModel.create({systemPrompt: '你是 code秘密花园 的编程小助手，擅长回答编程领域的问题。'});const result1 = await session.prompt('如何学习 JavaScript ？');console.log(result1);const result2 = await session.prompt('如何学习 React？');console.log(result2);
```

##### 停止运行提示和会话终止

```
const controller = new AbortController();stopButton.onclick = () => controller.abort();const result = await session.prompt('给我写一首诗！', { signal: controller.signal });// 终止会话session.destroy();
```

通过这些步骤和示例，开发者可以利用 Prompt API 开发功能强大的 Chrome 扩展程序，提升用户体验。Prompt API 结合了 Chrome 浏览器的内置功能和 `Gemini Nano` 语言模型，让开发者能够构建更加智能和高效的应用程序。

Demo
----

下面是一个浏览器扩展的源码：

https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/ai.gemini-on-device

![](.evernote-content/7034AE15-27EE-4730-BAA1-1BE4EC4F50B6/71DC57C0-D2CB-4F75-B8F7-34299100E895.png)

最后
--

抖音前端架构团队目前放出不少新的 HC ，有看起会的小伙伴可以看看这篇文章：[抖音前端架构团队正在寻找人才！ FE/Client/Server/QA](https://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247499434&idx=1&sn=8c7497876efc458dca19b6f6a27cadd4&chksm=c2e10b81f5968297533fcfced9ebad6eba072f6436bf040eaa8920256577258ef1077d1f122a&token=1091255868&lang=zh_CN&scene=21#wechat_redirect)，25 届校招同学可以直接用内推码：`DRZUM5Z`，或者加我微信联系。

参考资料：https://developer.chrome.com/docs/ai/built-in

如果你想加入高质量前端交流群，或者你有任何其他事情想和我交流也可以添加我的个人微信 [ConardLi](https://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247493407&idx=1&sn=41b8782a3bdc75b211206b06e1929a58&chksm=c2e11234f5969b22a0d7fd50ec32be9df13e2caeef186b30b5d653836b0725def8ccd58a56cf&scene=21#wechat_redirect) 。

`点赞`和`在看`是最大的支持⬇️❤️⬇️

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247501921&idx=1&sn=cf58ea5e068abb772c8244fa17822d82&chksm=c3545cd0c75f059949c30eda9eb7caca8bc5dc161d7dd42c21032a3a7df1fdfdbfb19552feee&mpshare=1&scene=1&srcid=112460v6vcgKRRIoEbUajp59&sharer_shareinfo=5bf2adebd1b4e95ccc01759c2d84a972&sharer_shareinfo_first=5bf2adebd1b4e95ccc01759c2d84a972#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/817ee2a3-350b-48e1-9262-7b265d5bbc39/817ee2a3-350b-48e1-9262-7b265d5bbc39/)