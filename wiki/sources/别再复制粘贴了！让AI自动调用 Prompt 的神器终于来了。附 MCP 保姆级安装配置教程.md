---
title: 别再复制粘贴了！让AI自动调用 Prompt 的神器终于来了。附 MCP 保姆级安装配置教程
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/别再复制粘贴了！让AI自动调用 Prompt 的神器终于来了。附 MCP 保姆级安装配置教程.md
tags: [evernote, impression, yinxiang]
---

# 别再复制粘贴了！让AI自动调用 Prompt 的神器终于来了。附 MCP 保姆级安装配置教程

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzAwODIyOTQ4Mw==&mid=264944...](https://mp.weixin.qq.com/s?__biz=MzAwODIyOTQ4Mw==&mid=2649443439&idx=1&sn=e7774beb3ccfc96f0648fe7dffd4575d&chksm=8289958f2889e292dc11a977ad7ebfc720fdbb600545ebb2fc375545956563c2ee5b70478b30&scene=90&xtrack=1&sessionid=1747810778&subscene=93&clicktime=1747810955&enterid=1747810955&flutter_pos=5&biz_enter_id=4&ranksessionid=1747810782&jumppath=20020_1747810781746,1104_1747810861273,20020_1747810873655,1104_1747810949180&jumppathdepth=4&ascene=56&devicetype=iOS18.5&version=18003b2a&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8+cpZA7OsN0ZAqjmWlHVmRLTAQIE97dBBAEAAAAAAF4JN2lfZEQAAAAOpnltbLcz9gKNyK89dVj0vH3xe5WSCHna9IYA3MaM6F/gHV3j8IAmUqReR2MH24G78nUWLrBeyItCRi/toXl+1BzYaxCHUcFoyzCVm5h9eaqZuW4UeaMdhxadhP5FIr3KfEwlHfJKJ2ZHLaZLc+l8wT8XCY99yoLltYeWU6lnyCSXeyKY+uztO0jXr9ijqfP3QJU2m05NSPlArK6Hbt9TSNlRMTLuBuWy43yZhwWdnIcHlKDcT8YLe4CLFdc=&pass_ticket=T5ziK24bPLIiRVLp4FMkthPT4pgCbpdKkGqSQT9jqbsDIY/C07+SOjfqjD8FE/X+&wx_header=3)

别再复制粘贴了！让AI自动调用 Prompt 的神器终于来了。附 MCP 保姆级安装配置教程
==============================================

Original向阳乔木向阳乔木推荐看

Prompt太多，但用不起来
--------------

不知道你是不是像我一样。

积累一大堆Prompt，但经常想不起来用。

即使想起来，每次都要复制粘贴，非常繁琐。

有人放在 AI 编程工具的规则（Rules）里，能解决一部分问题。

但我想，是否可以把常用的Prompt也做成 MCP。

每个 Prompt 都是这个 MCP 的一个工具（Tool）

让 AI 根据用户要求，自动选 Prompt 生成。

一个管理Prompt的MCP
--------------

谷歌一搜，果然已经有人做了。

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/3209F999-0CC8-4E00-8D1C-8AECF42DCDE3.png)

**Github 开源地址**

> https://github.com/gdli6177/mcp-prompt-server

原作者应该是程序员，MCP 自带 Prompt 全是和开发、测试相关。

所以我复制了一份代码，把下面的常用 Prompt 选了些，改造后放进去。

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/69E01C67-1A08-4728-BFB1-11DC6EE750B6.png)

**Github 开源地址**

> https://github.com/joeseesun/mcp-prompt-server

效果演示
----

理论上任何支持MCP的客户端都可以用。

如 Raycast AI，Cherry Studio、Trae、Cursor、Windsurf都行。

个人用 Raycast 比较多。

先秀下效果，再教大家如何安装。

### 案例 1：一句话生成PRD和原型

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/FF0803FB-1FB4-47C9-89A4-38DF7BAA8646.png)

### 案例 2：读取网页文档，生成爆款标题

Raycast 支持多个工具@组合调用。

先调用 @browser 读取当前正在看的网页内容。

再组合这个Prompt管理MCP，生成微信公众号爆款标题。

对于自媒体创作者来说。

真的相当实用了！

我就是经常写完稿，不知道如何起标题。

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/6CE6E00F-12A4-4569-BB78-B3DA6E8D38F4.png)

### 案例 3：生成可视化网页

今天，卡兹克熬夜肝了一篇谷歌AI产品发布会的文章。

干货相当多。

问题：谷歌一次性发布了太多 AI 产品，有些是期货，有些付费，有些免费，有些只有美国IP才能用。

过于复杂，普通人很难搞懂。

于是我调用这个MCP，快速生成了网页。

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/4705939D-EB30-488B-B5BF-F2D8C2F5B010.png)

生成效果：

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/7122B309-9218-41F3-A5B6-802EFBE34612.png)

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/B1A1318F-FFD7-41BB-A3C9-B7C0090862DD.png)

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/95085391-DC07-4A9C-B2E7-D4A6205D09D6.png)

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/DBAB6857-FAA7-48CC-9F59-06B095598D96.png)

**访问地址**

> https://www.32kw.com/view/8fd9e15

MCP 安装教程
--------

参考下面文档，先在电脑安装上Nodejs和Git等基础工具

> https://xiangyangqiaomu.feishu.cn/wiki/XPhPwO32Eimb7skLdwhcsERxnlh?fromScene=spaceOverview

如果懂 Git 命令（改天科普）

打开任意终端，cd进入你想保存MCP代码的文件夹，输入：

```
git clone https://github.com/joeseesun/mcp-prompt-server.git
```

cd进入克隆好的mcp-prompt-server文件夹。

命令行输入

```
npm install
```

安装相关依赖文件。

然后命令行再输入

```
npm start
```

启动后，就算本地装好了。

如果电脑没有装git，可以下载文件包，同样执行上面的安装和启动步骤。

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/D6943FB8-01A0-4632-A36A-0C3548BCF52D.png)

如何配置 MCP
--------

### Raycast MCP配置

1. 1. 在 Raycast 搜索 `install server（MCP）`

   ![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/FC78CF48-5780-45C6-BAE1-37AD4A8F4148.png)
2. 2. 给MCP输入一个名字，建议简单点，方便以后@使用，比如叫 `prompt`
3. 3. Command 填写 `node`
4. 4. Argument 填写你的 `index.js` 路径地址

   ![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/C8D3583E-07E7-496B-B2D2-A4ADBAF13C66.png)
5. 5. 保存即可，Raycast会自动集成MCP Prompt Server。

#### 注意事项

* • 未来新增Prompt，可以复制已有模版让AI参考生成YAML文件。
* • **模版中的 `arguments: []` 要么为空，要么参数设置为非必填（false），否则Raycast会报错。**
* • 如果报错，可以在Raycast中搜"manage server（MCP）"卸载后重装。
* • 每次新增Prompt，都需要卸载重装MCP，暂时没找到更优解。

### Cursor MCP配置

菜单->首选项->Cursor Settings->MCP->Add new global MCP server

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/066FD220-841A-4658-8ABE-DC7BC782DF2B.png)

或者直接编辑 `~/.cursor/mcp_config.json`，添加如下内容（请将路径替换为你实际的项目路径）：

```
{  
  "servers": [  
    {  
      "name": "Prompt Server",  
      "command": "node",  
      "args": [  
        "/你的文件实际路径/mcp-prompt-server/src/index.js"  
      ],  
      "transport": "stdio"  
    }  
  ]  
}
```

### Windsurf MCP配置

点账号头像->Windsurf Settings->Cascade->Add Server

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/92BDA6EF-CAF7-4445-8B80-02ED34763819.png)

或直接编辑 `~/.codeium/windsurf/mcp_config.json`，添加：

```
{  
  "mcpServers": {  
    "prompt-server": {  
      "command": "node",  
      "args": ["/path/to/mcp-prompt-server/src/index.js"]  
    }  
  }  
}
```

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/8EB0C53F-66C7-4754-AE9A-76D2F3132F38.png)

刷新Windsurf设置，Prompt Server即刻生效。

### Trae MCP配置

点右上角齿轮图标（设置） - > MCP -> 添加

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/E9A5168E-0329-40C9-9B4C-35F6A20A98AD.png)

* • 粘贴你的配置文件（注意修改路径）

  ```
  {  
    "mcpServers": {  
      "Prompt Server": {  
        "command": "node",  
        "args": [  
          "/你的文件实际路径/mcp-prompt-server/src/index.js"  
        ]  
      }  
    }  
  }
  ```

### 如何添加自己的 Prompt

1. 1. **新建YAML或JSON文件**，放入`src/prompts/`目录。
2. 2. **模板格式示例**：

   ```
   name: your_prompt_name  
   description: 这个Prompt的用途说明  
   arguments: []  
   messages:  
     - role: user  
       content:  
         type: text  
         text: |  
           你的Prompt内容，支持参数占位符{{param}}
   ```

最好让 AI 编程工具帮你写。

方法@已有的Prompt的yaml文件，让AI参考，再输入待处理的Prompt。

**参考提示词如下：**

![](.evernote-content/66FDCA68-64D4-40CE-9E6D-DFA55E9205B4/4CC53D74-8583-4FB8-BB36-235A4A876635.png)

### 存在的问题

Prompt的模版描述和定义要清晰，有差异化，且别放特别多。

否则大模型偶尔会识别错误。

如果不行，可以明确指定 Prompt 名称，例如：

> @prompt 调用gen\_html\_webpage 处理下面内容：

写在后面
----

这个 MCP 把常用 Prompt 变成“工具”，让 AI 能自动选择和调用。

大大提升了效率和创作力。

另外个好处，一次性安装，所有支持MCP的工具都能用，实现了共享 Prompt。

无论是内容生成、标题优化还是网页搭建，都能一键完成。

希望通过这个教程，帮你也用起来。

如果想了解更多 AI 工具评测和技巧，欢迎关注我的公众号。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzAwODIyOTQ4Mw==&mid=2649443439&idx=1&sn=e7774beb3ccfc96f0648fe7dffd4575d&chksm=8289958f2889e292dc11a977ad7ebfc720fdbb600545ebb2fc375545956563c2ee5b70478b30&scene=90&xtrack=1&sessionid=1747810778&subscene=93&clicktime=1747810955&enterid=1747810955&flutter_pos=5&biz_enter_id=4&ranksessionid=1747810782&jumppath=20020_1747810781746,1104_1747810861273,20020_1747810873655,1104_1747810949180&jumppathdepth=4&ascene=56&devicetype=iOS18.5&version=18003b2a&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8+cpZA7OsN0ZAqjmWlHVmRLTAQIE97dBBAEAAAAAAF4JN2lfZEQAAAAOpnltbLcz9gKNyK89dVj0vH3xe5WSCHna9IYA3MaM6F/gHV3j8IAmUqReR2MH24G78nUWLrBeyItCRi/toXl+1BzYaxCHUcFoyzCVm5h9eaqZuW4UeaMdhxadhP5FIr3KfEwlHfJKJ2ZHLaZLc+l8wT8XCY99yoLltYeWU6lnyCSXeyKY+uztO0jXr9ijqfP3QJU2m05NSPlArK6Hbt9TSNlRMTLuBuWy43yZhwWdnIcHlKDcT8YLe4CLFdc=&pass_ticket=T5ziK24bPLIiRVLp4FMkthPT4pgCbpdKkGqSQT9jqbsDIY/C07+SOjfqjD8FE/X+&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e0237d69-3f34-4d13-ada7-10aa9bde4796/e0237d69-3f34-4d13-ada7-10aa9bde4796/)
