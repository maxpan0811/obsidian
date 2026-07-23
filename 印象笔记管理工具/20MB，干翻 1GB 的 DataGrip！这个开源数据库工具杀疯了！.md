# 20MB，干翻 1GB 的 DataGrip！这个开源数据库工具杀疯了！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU2MTI4MjI0MQ==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247544798&idx=1&sn=ef20d8b0bd452fed3afb1f746900b329&chksm=fd1376b44e84714a3d4bcf37dc7d1ece522581ba079c86f64a1061b41bf8dfb18f2da350b15c&scene=90&xtrack=1&req_id=1784471320256811&sessionid=1784471136&subscene=93&clicktime=1784471695&enterid=1784471695&flutter_pos=6&biz_enter_id=4&ranksessionid=1784471320&jumppath=20020_1784471390695,1104_1784471404538,20020_1784471411452,1104_1784471691016&jumppathdepth=4&ascene=56&devicetype=iOS26.5.2&version=18004b40&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQlbduuJt2YvzqKuY9qQx70xLVAQIE97dBBAEAAAAAACpACTF4BKoAAAAOpnltbLcz9gKNyK89dVj0/u1vYLopfxPzncDPDv9J5pX1B+0swdZj8oGI3NP9vMdRuUFQiN2vH/5FuBTwgRgOJJl01OkGxWWWSR/81fvELrXCF7H9lP3DIDnTQk1S4+ya38t5TY2ydDD0b6iDjqfsqqiHfyipD9q/wqIb4LPR380LbZ82/47TCsq/DuTnxPBlHFl9bnaXncFqvAP0CBeGdasoUj7jhi1sbk7S5lV8FYLGzxeAJa96lBhAIAukew==&pass_ticket=ersSL74R/dAKYR79j8FtN+UDHnO7DFwRped0Y6MgfRhd89PK8xuE0Ca6QfuVI+Rp&wx_header=3)

20MB，干翻 1GB 的 DataGrip！这个开源数据库工具杀疯了！
====================================

Original丛林 极客之家

 

上周刷 GitHub Trending，一个叫 dbx 的项目挂在 Rust 榜前排，star 破了一万，之前我推荐过一个基于 AI 的数据库管理客户端，大家挺感兴趣的，但是很多人说不如 dbx，正好刷到，必须下载研究一波！

我是 Java 出身，DBeaver 在我电脑上躺了好几年。每次启动先等 JVM 热身，懂的都懂。Navicat 好用但要钱，DataGrip 得吃全家桶的内存。dbx 我看介绍只有20MB，然后能管 60 多种数据库，这还真是有点东西啊！

用了几天，这玩意儿确实可以，必须给还不知道这个管理工具的道友再聊聊它。

先看简介
====

dbx 是一个开源数据库客户端，Tauri 2 框架，Rust 写后端，Vue 3 加 TypeScript 写前端，编辑器用的 CodeMirror 6。Apache-2.0 协议，功能全免费，官方明确说不收集任何使用数据。

macOS、Windows、Linux 都有原生安装包。不想装客户端也行，它给了 Docker 版，跑起来就是个 Web 版，团队可以共用一套连接配置。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/0F775E81-4300-44B7-BBB8-B52D46C43860.png)

跟我们手里现有工具摆在一起看：

|  | dbx | DBeaver | Navicat | DataGrip |
| --- | --- | --- | --- | --- |
| 价格 | 免费开源 | 社区版免费 | 收费，不便宜 | 订阅制 |
| 体积 | 15MB | 几百 MB，要 Java | 一百多 MB | 接近 1GB |
| 数据库数量 | 60+ | 多 | 十几种 | 主流够用 |
| AI 能力 | 原生内置 | 插件 | 部分版本有 | 要订阅 AI |
| MCP | 原生支持 | 没有 | 没有 | 没有 |

功能我挑重点说
=======

### 60 多种数据库，一个图标全管

MySQL、PostgreSQL、SQLite、Redis、MongoDB 这些就不用提了，ClickHouse、DuckDB、SQL Server、Oracle 也都在名单里。

国产库跟得很紧，TiDB、OceanBase、openGauss、GaussDB、达梦、人大金仓、TDengine 全能连。

搞向量检索的 Qdrant、Milvus、Weaviate 也支持了，连 Kafka、RocketMQ、Pulsar 的消息队列管理都塞了进去。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/6E9B293C-4FB6-4C17-AD40-B37D51BF4C05.png)

以前我电脑上 MySQL 一个客户端、Redis 一个 GUI、MongoDB 再开一个，切来切去，现在可以只留一个图标。

### SQL 编辑器是正经编辑器

编辑器用的是 CodeMirror 6。语法高亮肯定有，补全做得挺聪明，它会读我们的表结构，敲到一半表名字段名自己往外跳。写完按 Cmd+Enter 执行，选中哪段就只跑哪段，写长 SQL 的时候全指望这个。格式化是自带的，不用装插件。主题给了 9 个，我们喜欢的深色也有。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/38B82426-AEDE-4E5A-BBF2-5F018720543A.png)

查询历史自动存着，常用的 SQL 可以收进片段库，下次直接调出来。标签页关掉再打开，内容还在。这些功能单拎出来都挺无聊的，但少一个，干活的时候就浑身难受。

### AI 助手长在编辑器里

选中一张表，用大白话说我要什么，SQL 直接就出来了。看不懂的语句丢给它，它会说清楚这条 SQL 在干嘛。慢查询可以让它优化，报错了也能让它修。生成的 SQL 执行之前会先过一道安全检查，防止 AI 手滑干出删表的事。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/D74DF2FB-D86E-413E-9064-CBBA0F5D2B05.png)

模型接谁我们自己定：Claude、OpenAI、Ollama 本地模型，或者任何 OpenAI 兼容接口。换句话说，DeepSeek、Kimi、通义这些国内直接能用的模型全能接，不挑。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/988D68A6-9793-479B-A9E2-C78687E977F9.png)

### MCP，让 AI 编程工具直接查我们的库

我觉得这是最值钱的功能，dbx 自带一个 MCP server，我们在 Claude Code、Cursor、Windsurf 里配一行，AI 就能用 dbx 里已经配好的连接去查库，表结构不用再复制粘贴喂给它了。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/7A4682EE-ED6A-42A5-A612-9560AF93CA3E.png)

配置长这样：

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/A8041411-136B-4ACB-B4EF-78C8DCBBD9AD.png)

终端党还有个独立 CLI，`npm install -g @dbx-app/cli`，配 Codex 跑脚本也行。

### 数据网格和导出

查出来的结果用的是虚拟滚动，几十万行也不会把页面拖死。数据可以直接在表格里改，改完它不会立刻落库，先把要执行的 SQL 摆出来给我们过目，确认没问题再保存。

过滤器明显是照着 DataGrip 做的，右键一按，LIKE、NOT LIKE 都在菜单里，用过 DataGrip 的人基本没有学习成本。

导出的格式给得也全，CSV、JSON、Markdown、XLSX 都有，还能直接生成 INSERT 语句，往别的库里搬东西很方便。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/89FA53FF-E426-4DAA-BAD7-63253ED442CC.png)

### Schema 工具给得很全

ER 图能直接画出来，表之间的外键关系一眼就能看清。跨连接的结构对比很实用，测试库和生产库差在哪几列，对一遍就知道。执行计划做成了可视化的图，慢查询卡在哪一步，不用对着文字猜。字段级血缘和全库对象搜索是给大库准备的，表一多就靠这俩找东西。

改表结构的时候它不会直接动手，列怎么变、索引怎么动，先列一份清单出来，我们确认完它才执行。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/BC291E33-1DD7-458F-99D3-40FC8E5F56A0.png)

ER 图这功能，我一般只在付费工具里见过能用的。

### 搬数据的活它也接

CSV 和 Excel 能直接导成表，跨库迁移支持，整库导出也有。两个库的数据可以拉出来对比，差在哪、同步过去会变成什么样，它先把结果给我们看。

还有个很顺手的点：拖一个 Parquet、CSV 或者 JSON 文件进去，底下是 DuckDB 在干活，文件内容直接预览，表都不用建。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/FA3F7B04-46D6-47B8-AB28-D1402B14EE08.png)

换工具的成本它也替我们想好了，DBeaver 和 Navicat 的连接配置可以直接导入，这一条摆明了就是来抢人的。

### Redis 和 MongoDB 有专属待遇

Redis 这块做得不像附属品，key 可以按模式搜，批量操作支持，TTL 直接改，还给想敲命令的人留了命令执行器。String、Hash、List、Set、ZSet、Stream 六种类型，每种都有对应的展示方式，不是糊成一坨文本。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/9D883C61-70FF-4B24-884E-DE256098F390.png)

MongoDB 是文档式的增删改查，带分页，Atlas 和副本集的连接串填进去就能连。

### 安全这块没省

SSH 隧道密钥和密码两种方式都支持，走跳板机的环境够用了。代理是分开设的，数据库走一个，AI 走一个，公司网络管得严的可以自己调。断线会自动重连，删数据这类操作会弹确认框，导出的配置文件是加密的。

连接可以标颜色，我的习惯是生产库一律标红，扫一眼就知道这个窗口不能乱来。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/19F31C1B-885F-4799-A860-F3752013C1F9.png)

装一个试试
=====

我们用 macOS 的直接 brew：

brew install --cask dbx

Windows 用 Scoop 或 WinGet：

scoop bucket add dbx https://github.com/t8y2/scoop-bucket
scoop install dbx
winget install t8y2.dbx

也可以去 GitHub Releases 页面直接下安装包。

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/3AD20B31-7697-4FE5-8EF4-C0FD27825098.png)

团队想上 Web 版，一行 Docker：

docker run -d --name dbx -p 4224:4224 -v dbx-data:/app/data t8y2/dbx

浏览器打开 `http://localhost:4224` 就能用。

装完点新建连接，填地址和账号，完事，界面长这样：

![](.evernote-content/94F30C06-B355-4B19-AC4F-6EDC3B2F91E7/10C075D2-5E12-48DE-93F1-1A846B096188.png)

我的看法
====

15MB 干到这个完成度，确实牛逼，感觉这个开发者都有点炫技的味道了。AI 和 MCP 是原生长在产品里的，不是后期挂的插件，这点跟市面上那些加了个对话框就敢叫 AI 版的工具不是一路货。

泼点冷水，我翻了翻，这项目主要靠作者一个人扛，issue 区躺着 800 多条反馈，一大半没解决，迭代快归快，长期维护还得观察。生产环境的饭碗库，我建议 DataGrip 先别卸，dbx 当主力玩可以，关键操作留个后手。

适合谁很清楚：电脑上堆了一堆客户端的多库杂食选手，还有想让 Claude Code、Codex 直接查库的 AI 编程玩家，反正不要钱，装一个不亏。

开源地址
====

*https://github.com/t8y2/dbx*

 

***点击下方卡片，关注极客之家***

这个公众号曾分享过许多有趣的开源项目。如果你不想逐篇翻阅历史文章，也可以直接关注微信公众号“极客之家”，通过后台留言与我们互动交流

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247544798&idx=1&sn=ef20d8b0bd452fed3afb1f746900b329&chksm=fd1376b44e84714a3d4bcf37dc7d1ece522581ba079c86f64a1061b41bf8dfb18f2da350b15c&scene=90&xtrack=1&req_id=1784471320256811&sessionid=1784471136&subscene=93&clicktime=1784471695&enterid=1784471695&flutter_pos=6&biz_enter_id=4&ranksessionid=1784471320&jumppath=20020_1784471390695,1104_1784471404538,20020_1784471411452,1104_1784471691016&jumppathdepth=4&ascene=56&devicetype=iOS26.5.2&version=18004b40&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQlbduuJt2YvzqKuY9qQx70xLVAQIE97dBBAEAAAAAACpACTF4BKoAAAAOpnltbLcz9gKNyK89dVj0/u1vYLopfxPzncDPDv9J5pX1B+0swdZj8oGI3NP9vMdRuUFQiN2vH/5FuBTwgRgOJJl01OkGxWWWSR/81fvELrXCF7H9lP3DIDnTQk1S4+ya38t5TY2ydDD0b6iDjqfsqqiHfyipD9q/wqIb4LPR380LbZ82/47TCsq/DuTnxPBlHFl9bnaXncFqvAP0CBeGdasoUj7jhi1sbk7S5lV8FYLGzxeAJa96lBhAIAukew==&pass_ticket=ersSL74R/dAKYR79j8FtN+UDHnO7DFwRped0Y6MgfRhd89PK8xuE0Ca6QfuVI+Rp&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/10543561-c520-4269-80b3-e30bbb40352b/10543561-c520-4269-80b3-e30bbb40352b/)