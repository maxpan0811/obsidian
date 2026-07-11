# Claude Code隐藏技巧新手必看

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0NTIxOTg1Ng==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzk0NTIxOTg1Ng==&mid=2247484056&idx=1&sn=3749726e965471befbd08774bd5f6f61&chksm=c319f2e7f46e7bf1a32a5ccc61a7fc66d4791d673f5053713d6fe02b8ec50100949d63b73124&from_masonry=1&sessionid=0&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQtAlaCfBwlRId6UA7cRtxWhLTAQIE97dBBAEAAAAAAGy4BBB6o4IAAAAOpnltbLcz9gKNyK89dVj0WWOy+4G8va1j4VsSawALr9ynCtLrupIcE93d1Y7dN4hkjrJqmai6j+SueE2SW4n99Zi7MRZK1+QXb9gEMCix3oM9YW/xAFQGlrbldO3ycsdBOfGBsjVXEcRyLASoARa4y6BOf6TqdQiscIN7WqxV4lUR+ihL3Ctn2dpUqWTXJ2YexRnu736zrdMU+Y4eh3gbA+swUdbCMjILe6vJgRZZSI3sOCXTLT3ol66cJlk=&pass_ticket=tpu6hhaEqX8CC8wVdlzr26YcmLp3tdqUIsj415ZsPd8t1i5cGKnsX6D02s5JVH2e&wx_header=3)

![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/907CD4C9-25EC-481C-8CC7-89182F6FF9F9.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/E6018BCB-B92A-42DA-8599-EE1A6E02C69B.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/9635ED2B-ACCB-4B14-9244-DC1FC580163C.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/425E44A0-69D1-4C26-9C50-A992F881607A.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/9A4A9DF1-28AC-40EB-A348-A5C034982C2E.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/27D799B5-A3D9-41D7-A32F-921A7FA70FF6.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/0A42C99A-E55B-4D7E-86D4-E6B1340BB653.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/7D5060E7-C3A3-44EA-AA35-386F85A1C4B6.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/E33361A0-3FF3-48C8-85D3-ABAB8FE2782E.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/4DAFF250-A94B-4551-A614-F6E9255823B3.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/BB7171F7-5827-4076-A501-3F3FFFECBE33.jpg)![](.evernote-content/38BC619C-B3DD-4689-8D64-033AB89BBAC0/468F45BE-1385-4D12-B350-8640F782D542.jpg)

很多人用了好几个月 Claude Code，依然只会"叫它写代码"。

其实它内置了大量提效功能，用好之后工作方式会完全不同。以下 10 个技巧，是新手最值得优先掌握的。

① CLAUDE.md — 一次配置，永久生效 在项目根目录创建 CLAUDE.md，写入编码规范和项目约定。Claude Code 每次启动自动读取，无需重复说明。

② 斜杠命令 — 内置工作流，一键触发 输入 / 可查看所有内置命令。/commit 自动提交、/review-pr 代码审查，常用操作无需手动描述。

③ ! 前缀命令 — 终端输出进上下文 在对话框输入 ! 命令，结果自动加入上下文，AI 基于真实输出继续分析，无需复制粘贴。

④ MCP 服务器 — 扩展 AI 的能力边界 通过 MCP 协议接入数据库、邮件、浏览器等外部工具，让 AI 真正参与业务流程。

⑤ Shift+Enter — 多行输入提升质量 换行不发送，发送前组织完整需求，输入越清晰，输出质量越高。

⑥ /plan 模式 — 先规划再执行 只输出计划，不修改文件。确认方向后再执行，大型改动必备。

⑦ Hooks 自动化 — 系统级强制执行 在特定事件前后自动运行脚本，彻底告别"每次提醒 AI"的低效方式。

⑧ --model 切换 — 按需选择模型 简单任务用 Haiku，日常开发用 Sonnet，复杂设计用 Opus，兼顾成本与质量。

⑨ 贴入上下文 — 截图直接粘贴 报错截图、设计稿、数据表格直接粘贴到对话框，AI 基于真实内容分析，零翻译成本。

⑩ /compact — 长会话保持高效 定期压缩历史对话，释放上下文空间，避免 AI 遗忘早期需求。

每个技巧单独用都能明显提升效率，组合起来更是质的飞跃。建议收藏备用。

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0NTIxOTg1Ng==&mid=2247484056&idx=1&sn=3749726e965471befbd08774bd5f6f61&chksm=c319f2e7f46e7bf1a32a5ccc61a7fc66d4791d673f5053713d6fe02b8ec50100949d63b73124&from_masonry=1&sessionid=0&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQtAlaCfBwlRId6UA7cRtxWhLTAQIE97dBBAEAAAAAAGy4BBB6o4IAAAAOpnltbLcz9gKNyK89dVj0WWOy+4G8va1j4VsSawALr9ynCtLrupIcE93d1Y7dN4hkjrJqmai6j+SueE2SW4n99Zi7MRZK1+QXb9gEMCix3oM9YW/xAFQGlrbldO3ycsdBOfGBsjVXEcRyLASoARa4y6BOf6TqdQiscIN7WqxV4lUR+ihL3Ctn2dpUqWTXJ2YexRnu736zrdMU+Y4eh3gbA+swUdbCMjILe6vJgRZZSI3sOCXTLT3ol66cJlk=&pass_ticket=tpu6hhaEqX8CC8wVdlzr26YcmLp3tdqUIsj415ZsPd8t1i5cGKnsX6D02s5JVH2e&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7b9b4499-deee-4182-9f6a-7cdfad764e49/7b9b4499-deee-4182-9f6a-7cdfad764e49/)