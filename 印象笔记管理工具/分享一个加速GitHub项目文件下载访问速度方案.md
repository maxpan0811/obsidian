# 分享一个加速GitHub项目文件下载访问速度方案

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzAxNDYyNjI1OQ==&mid=245447...](https://mp.weixin.qq.com/s?__biz=MzAxNDYyNjI1OQ==&mid=2454474286&idx=1&sn=223a310918836b190b3abb849f0c459e&chksm=8dc392ad34dc069417f95e8b256d93434f9f9944e133c5b06d3d82b441d18c37823264e067f5&scene=90&xtrack=1&sessionid=1738454706&subscene=93&clicktime=1738455102&enterid=1738455102&flutter_pos=8&biz_enter_id=4&ranksessionid=1738455060&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQgsn+dOD1PYsZKVylLHdbQRLWAQIE97dBBAEAAAAAAPD+NYHe+koAAAAOpnltbLcz9gKNyK89dVj0qUCv/I5vO3HxVtHqDgnGiOIyBWGNg/HQ1sfHmJj30IZT0s5KRsgNYKgoVNVBtmdFFxQ8lRx5L3mFysjcG2+V8Zp9SQWGjWKZuCcf5U07RQEOiRFzG2ibHqJIzdopwahpPb9s/YEtQYhLNPCgMYp7S6Lp9eZTMSm7mFpJFbxEa0dEmqumn4QqkoIhQtM+1slk9TwbwgBq7iOV0U14btr5ScB/E7T2ot1ya0I1TUqYisc=&pass_ticket=xWml56mr723CzUS6axpOEtBwTSmWjCH+gQDWw3/llK1yyqUk9sXZXCe6BnC3LZ/D&wx_header=3)

分享一个加速GitHub项目文件下载访问速度方案
========================

原创 编程与架构 编程与架构

![](.evernote-content/04DE50A5-BDA8-4BE9-A2BF-49363EB3FF6D/FE40380A-CC04-4F98-A711-0BE1524B7D9F.gif)关注下方公众号，获取更多热点资讯![](.evernote-content/04DE50A5-BDA8-4BE9-A2BF-49363EB3FF6D/FE40380A-CC04-4F98-A711-0BE1524B7D9F.gif)

分享一个加速GitHub项目文件下载访问速度方案
========================

![](.evernote-content/04DE50A5-BDA8-4BE9-A2BF-49363EB3FF6D/AF1279B7-149F-4DB7-9705-D19375D312E2.png)

前言
--

开发者访问GitHub时经常遇到速度慢、下载失败等问题。为了提升GitHub项目文件的访问速度，`GH-Proxy`作为一种加速方案应运而生。

本文将详细介绍GH-Proxy的工作原理、搭建方法、配置技巧及最佳实践，帮助开发者快速实现GitHub项目的文件加速，提升开发效率。

GH-Proxy概述
----------

GH-Proxy 是一个专为加速 GitHub 资源下载而设计的工具，支持 GitHub Release、Archive 以及项目文件的快速下载，同时提供 Clone 加速功能。该项目提供了两种版本：基于 Cloudflare Workers 的无服务器版本和 Python 版本，用户可以根据需求选择部署方式。

如果你不想自行搭建，可以直接使用 GH-Proxy 的公共服务。例如，如果你想下载 Ollama 的安装包，可以通过以下命令直接加速下载：

```
https://gh.api.99988866.xyz/https://github.com/ollama/ollama/releases/download/v0.5.7/ollama-linux-amd64.tgz
```

通过 GH-Proxy，你可以显著提升 GitHub 资源的下载速度，尤其适合在国内网络环境下使用。

GH-Proxy的搭建步骤
-------------

支持两种方案：

* • cf worker版本部署
* • Docker版本部署

### Cloudflare Workers版本

**首页**：https://workers.cloudflare.com

1. 1. **注册并登录** Cloudflare Workers。
2. 2. 点击 `Start building`，选择一个子域名，然后点击 `Create a Worker`。
3. 3. 将 index.js 的内容复制到左侧代码框中，点击 `Save and deploy`。如果一切正常，右侧应显示首页。

**参数说明**：

* • `ASSET_URL`：静态资源的 URL（即当前显示的单页面输入框）。
* • `PREFIX`：路径前缀，默认为 `"/"`。如果自定义路由为 `example.com/gh/*`，请将 `PREFIX` 改为 `'/gh/'`。**注意**：少一个斜杠都会导致错误！

这样描述更加简洁明了，便于用户快速理解操作步骤和注意事项。

### Docker 版本

直接运行

```
docker run -d --name="gh-proxy-py" \  
  -p 0.0.0.0:80:80 \  
  --restart=always \  
  hunsh/gh-proxy-py:latest
```

### 使用方式

**方法一**

直接访问地址：`http://localhost`，在页面中下载

![](.evernote-content/04DE50A5-BDA8-4BE9-A2BF-49363EB3FF6D/AF1279B7-149F-4DB7-9705-D19375D312E2.png)

**方法二**

在需要下载的文件前添加`gh-proxy`地址即可，这里我们是：`http://localhost/`

输入格式支持（仅示例，文件不存在）：

**分支源码**：  
`https://github.com/hunshcn/project/archive/master.zip`  
**release源码**：  
`https://github.com/hunshcn/project/archive/v0.1.0.tar.gz`  
**release文件**：  
`https://github.com/hunshcn/project/releases/download/v0.1.0/example.zip`  
**分支文件**：  
`https://github.com/hunshcn/project/blob/master/filename`  
**commit文件**：  
`https://github.com/hunshcn/project/blob/1111111111111111111111111111/filename`  
**gist：**  
`https://gist.githubusercontent.com/cielpy/351557e6e465c12986419ac5a4dd2568/raw/cmd.py`

### 测试与验证

在浏览器中访问`http://localhost`，测试是否能够成功通过代理服务访问GitHub项目文件。如果一切正常，你将看到GitHub项目文件被加速访问。

也可以通过命令行进行下载

```
curl -L http://localhost/https://github.com/ollama/ollama/releases/download/v0.5.7/ollama-linux-amd64.tgz
```

直接使用 gh-proxy 提供的地址
-------------------

当然，如果你不想自建也可以使用`gh-proxy`提供的测试地址，但是有时候可能会不稳定，用的人太多了。

测试地址为`https://gh.api.99988866.xyz/`

结语
--

通过使用GH-Proxy，开发者可以显著提升GitHub项目文件的访问速度，这是一种简单而有效的解决方案。通过本文的介绍，你可以轻松搭建并配置GH-Proxy，提升开发效率。

> **Github:** https://github.com/hunshcn/gh-proxy

 

欢迎关注我的公众号“**编程与架构**”，原创技术文章第一时间推送。![](.evernote-content/04DE50A5-BDA8-4BE9-A2BF-49363EB3FF6D/8A3D5801-77E5-45E7-9CBA-ACC77F6F7482.jpg)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzAxNDYyNjI1OQ==&mid=2454474286&idx=1&sn=223a310918836b190b3abb849f0c459e&chksm=8dc392ad34dc069417f95e8b256d93434f9f9944e133c5b06d3d82b441d18c37823264e067f5&scene=90&xtrack=1&sessionid=1738454706&subscene=93&clicktime=1738455102&enterid=1738455102&flutter_pos=8&biz_enter_id=4&ranksessionid=1738455060&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQgsn+dOD1PYsZKVylLHdbQRLWAQIE97dBBAEAAAAAAPD+NYHe+koAAAAOpnltbLcz9gKNyK89dVj0qUCv/I5vO3HxVtHqDgnGiOIyBWGNg/HQ1sfHmJj30IZT0s5KRsgNYKgoVNVBtmdFFxQ8lRx5L3mFysjcG2+V8Zp9SQWGjWKZuCcf5U07RQEOiRFzG2ibHqJIzdopwahpPb9s/YEtQYhLNPCgMYp7S6Lp9eZTMSm7mFpJFbxEa0dEmqumn4QqkoIhQtM+1slk9TwbwgBq7iOV0U14btr5ScB/E7T2ot1ya0I1TUqYisc=&pass_ticket=xWml56mr723CzUS6axpOEtBwTSmWjCH+gQDWw3/llK1yyqUk9sXZXCe6BnC3LZ/D&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ef130489-cd81-435b-8b16-b280dcee2c46/ef130489-cd81-435b-8b16-b280dcee2c46/)