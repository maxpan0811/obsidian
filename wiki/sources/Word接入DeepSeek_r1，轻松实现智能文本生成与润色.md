---
title: Word接入DeepSeek r1，轻松实现智能文本生成与润色
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Word接入DeepSeek r1，轻松实现智能文本生成与润色.md
tags: [AI技术]
updated: 2026-06-27
---

---
title: "Word接入DeepSeek r1，轻松实现智能文本生成与润色"
source: evernote
type: note
export_date: 2026-06-25
guid: e53fb39f-a8db-4f0e-bc56-c0ef10511766
---

# Word接入DeepSeek r1，轻松实现智能文本生成与润色

原文链接: [https://mp.weixin.qq.com/s?chksm=c362e6f2f4156fe46e83ed103966930...](https://mp.weixin.qq.com/s?chksm=c362e6f2f4156fe46e83ed1039669300beb914c299b4ca16295e8ad5f6a4396d816fca320f1a&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_1&scene=169&mid=2247485450&sn=ae72cd28f39ade0bd0a88cfc4eb046b4&idx=1&__biz=Mzk0ODY5ODAwNw==&sessionid=1738654840&subscene=200&clicktime=1738657959&enterid=1738657959&flutter_pos=43&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQO5n+WG6rO4AKI/TuxLq2YBLWAQIE97dBBAEAAAAAAHYYGkVZK18AAAAOpnltbLcz9gKNyK89dVj0sLCw8pKRfYWY0FtEzxKeoaobXIQDs49765DODC15Iw7gbWkBQGK5u5GTsJLtmnJUmX60vBro07JGIHV8htQnuRZrDH+RDsKZcxr6LA4MiZzHAFdb5IsBFuggojrP0zBCrNt2kpZIC0I732HpKOSVP7bumMlAZleCBA2Z3TgbWsD/NH7i9D25ULaMT0JTAUyVSspqFQ+yKOuE9kkAYaNBvjxaPiwVUaAjyd5/KjhbV3Q=&pass_ticket=W+0ggrruXqcbg8e/C3eMwZefJUPIfNoASYISxn6LyPHq7FwFye4MmAIdEtPh9ujG&wx_header=3)

# Word接入DeepSeek r1，轻松实现智能文本生成与润色

原创 陈文茂  环境猫er

之前我曾利用Word的VBA宏接入ChatGPT 3.5的API。然而，由于OpenAI对中国大陆地区的限制，这一方案难以持续使用。随后出现的大型语言模型要么难以调用，要么收费昂贵。如今，随着DeepSeek的开源，结合Word这一办公常用场景，我决定将DeepSeek模型接入Word，实现文本生成和文本润色两大功能。

## Vba  code

### 文本生成模块代码

通过VBA调用英伟达的API(具体获取方式之前已提到多次不再赘述)，采用非流式生成方式。用户只需选中文字并点击模块名称，稍等片刻即可生成结果。该模块基于推理文本模型，并保留了模型的思考过程。

Sub DeepSeek()
    Dim selectedText As String
    Dim apiKey As String
    Dim response As Object, re As String
    Dim midString As String
    Dim ans As String
    If Selection.Type = wdSelectionNormal Then
        selectedText = Selection.Text
        selectedText = Replace(selectedText, ChrW$(13), "")
        apiKey = "your\_api\_key\_here"
        URL = "https://integrate.api.nvidia.com/v1/chat/completions"
        Set response = CreateObject("MSXML2.XMLHTTP")
        response.Open "POST", URL, False
        response.setRequestHeader "Content-Type", "application/json"
        response.setRequestHeader "Authorization", "Bearer " + apiKey
        response.Send "{""model"":""deepseek-ai/deepseek-r1"", ""messages"":[{""role"":""user"",""content"":""" & selectedText & """}], ""temperature"":0.7}"
        
        re = response.responseText
        midString = Mid(re, InStr(re, """content"":""") + 11)
        ans = Split(midString, """")(0)
        ans = Replace(ans, "\n", "")
        Selection.Text = selectedText & vbNewLine & ans
        Else
        Exit Sub
    End If
End Sub

### 文本润色模块

文本润色模块内置了提示词，大家可根据需要修改提示词，实现翻译、润色、续写等功能。

Sub DeepSeekPolish()
    Dim selectedText As String
    Dim apiKey As String
    Dim response As Object, re As String
    Dim midString As String
    Dim ans As String
    Dim polishPrompt As String
    
    ' 检查是否有正常选中的文本
    If Selection.Type = wdSelectionNormal Then
        ' 获取选中文本并去除不需要的字符
        selectedText = Selection.Text
        selectedText = Replace(selectedText, ChrW$(13), "")
        
        ' 定义API密钥和请求URL
        apiKey = "your\_api\_key\_here"
        URL = "https://integrate.api.nvidia.com/v1/chat/completions"
        
        ' 设置润色提示词
        polishPrompt = "请润色以上文字，要求语句通顺，条理清晰，专业而合理。"
        
        ' 创建HTTP请求对象并设置参数
        Set response = CreateObject("MSXML2.XMLHTTP")
        response.Open "POST", URL, False
        
        ' 添加必要的头部信息
        response.setRequestHeader "Content-Type", "application/json"
        response.setRequestHeader "Authorization", "Bearer " + apiKey
        
        ' 发送请求，注意在JSON字符串中添加了polishPrompt
        response.Send "{""model"":""deepseek-ai/deepseek-r1"", ""messages"":[{""role"":""user"",""content"":""" & selectedText & """}, {""role"":""assistant"", ""content"":""" & polishPrompt & """}], ""temperature"":0.7}"
        
        ' 处理响应数据
        re = response.responseText
        midString = Mid(re, InStr(re, """content"":""") + 11)
        ans = Split(midString, """")(0)
        ans = Replace(ans, "\n", "")
        
        ' 将原选中文本与润色后的文本一起插入文档中
        Selection.Text = selectedText & vbNewLine & ans
    Else
        Exit Sub
    End If
End Sub

## 宏的使用

宏的使用有很多方法，快捷键、放在功能区都行，这里以自定义功能区简单介绍。

### 添加宏

1. 开启开发工具。
2. 点击“开发工具”选项卡。
3. 点击“Visual Basic”。
4. 右键当前文稿下的“模块”，选择“插入模块”。
5. 复制上述代码到新建的模块中。

![](attachments/30b0bc63c9cd9a59.png)

### 自定义功能区

1. 点击“文件”->“选项”->“自定义功能区”。
2. 选择“宏”，在右侧自定义功能区新建选项卡和组。
3. 将宏添加至组中，重命名并更换图标。

![](attachments/5aa8000cfdc26d6c.png)

### 效果预览

![](attachments/1a2db75081c1c3c0.png)

## 小结

最近几天，我一直在探索DeepSeek的应用，深感其高性能和低成本对工作生活的普惠意义。对于个人和小企业而言，人工智能的应用应紧密结合自身场景，无需考虑在本地搭建模型。尽管DeepSeek模型开源，但在本地运行全功能模型成本较高。随着各大厂商的跟进，生成式模型可能成为基础设施，如同GitHub一样普及。我们需要做的是提前跑通整个流程，以便在新模型出现时能迅速应用。目前，DeepSeek虽强大，但运行速度仍有提升空间，尤其是RI推理模型。让我们保持热情，持续关注其发展。

## BY

纯个人经验，如有帮助，请收藏点赞，如需转载，请注明出处。

微信公众号：环境猫 er

CSDN : 细节处有神明

个人博客： https://maoyu92.github.io/


---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c362e6f2f4156fe46e83ed1039669300beb914c299b4ca16295e8ad5f6a4396d816fca320f1a&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_1&scene=169&mid=2247485450&sn=ae72cd28f39ade0bd0a88cfc4eb046b4&idx=1&__biz=Mzk0ODY5ODAwNw==&sessionid=1738654840&subscene=200&clicktime=1738657959&enterid=1738657959&flutter_pos=43&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQO5n+WG6rO4AKI/TuxLq2YBLWAQIE97dBBAEAAAAAAHYYGkVZK18AAAAOpnltbLcz9gKNyK89dVj0sLCw8pKRfYWY0FtEzxKeoaobXIQDs49765DODC15Iw7gbWkBQGK5u5GTsJLtmnJUmX60vBro07JGIHV8htQnuRZrDH+RDsKZcxr6LA4MiZzHAFdb5IsBFuggojrP0zBCrNt2kpZIC0I732HpKOSVP7bumMlAZleCBA2Z3TgbWsD/NH7i9D25ULaMT0JTAUyVSspqFQ+yKOuE9kkAYaNBvjxaPiwVUaAjyd5/KjhbV3Q=&pass_ticket=W+0ggrruXqcbg8e/C3eMwZefJUPIfNoASYISxn6LyPHq7FwFye4MmAIdEtPh9ujG&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/e53fb39f-a8db-4f0e-bc56-c0ef10511766/e53fb39f-a8db-4f0e-bc56-c0ef10511766/)
