---
title: "通过 Mathpix API 将公式识别为 LaTeX - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/通过 Mathpix API 将公式识别为 LaTeX - 少数派.md
tags: [印象笔记]
---

# 通过 Mathpix API 将公式识别为 LaTeX - 少数派

# 通过 Mathpix API 将公式识别为 LaTeX - 少数派 --- 通过 Mathpix API 将公式识别为 LaTeX =========================== ### 

---

# 通过 Mathpix API 将公式识别为 LaTeX - 少数派

---

通过 Mathpix API 将公式识别为 LaTeX
===========================

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

在编写理工科文本的时候，有一大痛点是如何处理各种公式，虽然大部分 Markdown 编辑器支持通过 `$ $` 行内或 `$$ $$` 独自一行插入 LaTeX 公式，但是编写公式本身依旧是一个枯燥的工作。

后来我发现了一个服务 / 软件叫 [Mathpix OCR](https://mathpix.com/ocr)，其首先是一个 OCR 服务，不同之处是它可以将打印和手写的公式转换成 LaTeX：

![](.evernote-content/F3E58491-E754-4E5D-98F0-3D01DB9D4533/7392781E-7E07-439A-A835-A7B3AE3B5E48.png)

图片来自 Mathpix 官网：https://mathpix.com/

通过其 macOS 客户端试用了一阵子，发现效果非常不错，速度很快，而且识别率非常高，唯一的问题是价格太贵 —— 免费用户一个月只能识别 50 次，无识别次数限制的 Pro 账户一个月要 4.99 美元。

后来我发现其提供的 API 收费要合理很多：每个账户每个月的头 1000 次请求免费；随后的第 1-100 千次，每次 0.004 美元；第 100- 300 千次，每次 0.002 美元。 算下来 5 美元可以在免费额度之后使用 1250 次，对于像我这种虽然不是重度用户，但是 50 次每月的免费额度完全不够的用户来说，使用 API 显然是更经济的选择。

![](.evernote-content/F3E58491-E754-4E5D-98F0-3D01DB9D4533/D2AABEB3-1E7B-4BAF-8250-31AA45D5B4D3.png)

API 的定价

首先注册一个账户：<https://dashboard.mathpix.com/login>，注意使用 API 的账户和使用客户端的账户是分开的两个系统，不是统一的账户。输入信用卡信息以后就能看到自己的 `app_id` 和 `app_key`。

macOS 平台使用方法
------------

通过阅读 [官方文档](https://docs.mathpix.com/#introduction)，很简单就可以构建一段 Python 脚本：

```
#!/usr/bin/env python3

# example from https://github.com/Mathpix/api-examples/blob/master/python/mathpix.py

import os,base64,requests,json
from PIL import ImageGrab

env = os.environ
HOME = env.get('HOME') + "/Desktop/"

default_headers = {
    'app_id': env.get('APP_ID', '你的 APP'),
    'app_key': env.get('APP_KEY', '你的 APPKey'),
    'Content-type': 'application/json'
}

service = 'https://api.mathpix.com/v3/latex'

# Return the base64 encoding of an image with the given filename.
def image_uri(filename):
    image_data = open(filename, "rb").read()
    return "data:image/jpg;base64," + base64.b64encode(image_data).decode()

# Call the Mathpix service with the given arguments, headers, and timeout.
def latex(args, headers=default_headers, timeout=30):
    r = requests.post(service, data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)

def mathpix(): 
# 从剪贴板获取公式  
    im = ImageGrab.grabclipboard()
    im.save(HOME+'screen.png','PNG')
    r = latex({
        'src': image_uri(HOME+"screen.png"),
        "ocr": ["math", "text"], 
        'formats': ['latex_styled']
    })
    print(r['latex_styled'])

if __name__ == '__main__':
    # 调用 macOS 的 screencapture 命令行工具
    os.system("screencapture -i -c")
    mathpix()
```

把其中的 `app_id` 和 `app_key` 替换成你自己的对应的值，然后放到 Keyboard Maestro 里面就可以用了，运行后识别的结果会复制到剪贴板内。

![](.evernote-content/F3E58491-E754-4E5D-98F0-3D01DB9D4533/91E8D7E9-C9C9-4870-9B26-2D25868AE556.png)

Keyboard Maestro Macro

这个动作的 Keyboard Maestro Macro 可以点击 [这里](https://cl.ly/47139fdf1de8) 下载。

iOS 平台使用方法
----------

在 iOS 上通过 Shortcuts 也可以实现类似的流程：

![](.evernote-content/F3E58491-E754-4E5D-98F0-3D01DB9D4533/6D715D79-7B1F-4A87-AA35-29DC903A8907.jpg)

iOS Shortcuts

与 Mac 不同，为了更好利用 iPad 特性，这个 Shortcut 被分成了两部分：

* 一部分与 Mac 一样，获取相册图片然后识别；
* 另一部分会下载我预先上传好的空白图片，然后使用 iOS 系统的标注功能进行标注，借此达到识别手写公式的目的。  

  ![](.evernote-content/F3E58491-E754-4E5D-98F0-3D01DB9D4533/05B540BC-999A-48E7-94C1-6F5C3C14E412.gif)

  shortcuts gif

点击 [此处](https://www.icloud.com/shortcuts/191c7ca3eedc41f89c1776de137440fa) 下载这个动作的快捷指令。

后注：在 GitHub 上看到了一个基于 Python + TensorFlow 的开源 [方案](https://github.com/yeayee/LaTeX_OCR_PRO)，等我学会 TensorFlow 了再研究吧。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，让你的学习更有效率 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

---

[🌐 原始链接](https://sspai.com/post/57181)

[📎 在印象笔记中打开](evernote:///view/207087/s1/48bf513e-ba84-4c39-997b-37bf7dc51f73/48bf513e-ba84-4c39-997b-37bf7dc51f73/)