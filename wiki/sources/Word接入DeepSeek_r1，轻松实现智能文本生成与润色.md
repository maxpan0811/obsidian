---
title: Word接入DeepSeek r1，轻松实现智能文本生成与润色
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Word接入DeepSeek r1，轻松实现智能文本生成与润色.html
tags: [AI技术]
---

# Word接入DeepSeek r1，轻松实现智能文本生成与润色

原文链接: https://mp.weixin.qq.com/s?chksm=c362e6f2f4156fe46e83ed103966930...

Word接入DeepSeek r1，轻松实现智能文本生成与润色 原创 陈文茂  环境猫er 
之前我曾利用Word的VBA宏接入ChatGPT 3.5的API。然而，由于OpenAI对中国大陆地区的限制，这一方案难以持续使用。随后出现的大型语言模型要么难以调用，要么收费昂贵。如今，随着DeepSeek的开源，结合Word这一办公常用场景，我决定将DeepSeek模型接入Word，实现文本生成和文本润色两大功能。
Vba  code文本生成模块代码通过VBA调用英伟达的API(具体获取方式之前已提到多次不再赘述)，采用非流式生成方式。用户只需选中文字并点击模块名称，稍等片刻即可生成结果。该模块基于推理文本模型，并保留了模型的思考过程。

Sub DeepSeek()
    Dim selectedText As String
    Dim apiKey As String
    Dim response As Object, re As String
    Dim midString As String
    Dim ans As String
    If Selection.Type = wdSelectionNormal Then
        selectedText = Selection.Text
        selectedText = Replace(selectedText, ChrW$(13), "")
        apiKey = "your_api_key_here"
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

...文本润色模块文本润色模块内置了提示词，大家可根据需要修改提示
