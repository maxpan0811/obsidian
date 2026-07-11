# 办公新利器：DeepSeek+Word，让你的工作更高效

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c0081ba0f77f92b66c46cad0d013179...](https://mp.weixin.qq.com/s?chksm=c0081ba0f77f92b66c46cad0d01317995c4470cba96dd922673b64624d0b211f9b1f8180a55a&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738510260_1&scene=169&mid=2247484035&sn=c318cb8ae883ea099cf0fbe07c3a3f89&idx=1&__biz=Mzg5NTg5NzY3Ng==&sessionid=1738509696&subscene=200&clicktime=1738510916&enterid=1738510916&flutter_pos=16&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQluerftByaCDjyk20bFQsVhLWAQIE97dBBAEAAAAAANpQJHAzkD8AAAAOpnltbLcz9gKNyK89dVj0SYdm9mARKSSb58RziEFK3clBEI713g502sKLhv5xBta3ENTP8iOeeJAgq0ZjnOv6zDyjbrRCxCdeuChxOGWxlhHPyDHYbgu053XKWjXMNeAyhOAscReAeBnetiFzvT7un9QRwm3SGtz/eaACpiNf5MlHusmlO4bL2fKVWyLt2BJucMCefno7+KszDUNvyQ8QvNoUXjwZ+dSEm8D/6kG+q05kPja1ewNcoG4g9U/d7Bk=&pass_ticket=XM3jyaVPB/EIPzhHZ/qWqdteYpcrv12k3x86Ut85XPFrmhUtv4xnxhhySjjJopXl&wx_header=3)

原创根根GEN根根AI

DeepSeek与Word的梦幻联动，将为你开启高效办公的新篇章！熟悉的Word界面中，只需轻点鼠标，就能召唤出强大的DeepSeek，让它为你快速检索信息、精准翻译文本、智能生成内容……  告别在不同软件间来回切换的繁琐，告别低效的信息获取方式，让办公效率飞起来！

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/AE393BE4-15ED-406F-A534-128B566D7A27.png)

**01**

**效果演示**

按照文本教程完成操作后，Word的选项卡中将会出现DeepSeek的生成图标，选中文本并点击生成，即可实现模型回复！例如，我们想要将一段中文文本翻译成英文：

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/F825D3A9-ECCD-47EF-9E53-E777405A014D.png)

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/11119AA6-E922-40B8-80AB-D564DFD60FD8.png)

接下来我将详细介绍，如何实现DeepSeek与Word的结合。

**02**

**获取API key**

API key的获取教程可以参照我之前的一篇文章，在获取API key之后，回到这里。

PyCharm接入DeepSeek实现AI编程

**03**

**配置Word**

新建一个Word文档，点击 文件 -> 选项 -> 自定义功能区，勾选“开发者工具”。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/9C16C9F2-5142-4C73-ACA0-2D4EF577E1A6.png)

点击 信任中心 -> 信任中心设置，选择“启用所有宏”与“信任对VBA......”。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/CA5E02E5-C717-4631-B573-C113EE420F71.png)

接下来点击确定，我们发现选项卡中出现了“开发者工具”，点击开发者工具，点击Visual Basic，将会弹出一个窗口。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/3EE911B8-C6ED-4519-8067-953CC0EE2FD3.png)

我们点击新窗口中的插入，点击模块。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/B8F8FB70-1539-4CF5-AC87-CFDD8CC47251.png)

点击后将会弹出一个编辑器，我们把如下代码复制到编辑区中。注意不要忘记替换你自己的API key。

```
Function CallDeepSeekAPI(api_key As String, inputText As String) As String  
    Dim API As String  
    Dim SendTxt As String  
    Dim Http As Object  
    Dim status_code As Integer  
    Dim response As String  
  
    API = "https://api.deepseek.com/chat/completions"  
    SendTxt = "{""model"": ""deepseek-chat"", ""messages"": [{""role"":""system"", ""content"":""You are a Word assistant""}, {""role"":""user"", ""content"":""" & inputText & """}], ""stream"": false}"  
  
    Set Http = CreateObject("MSXML2.XMLHTTP")  
    With Http  
        .Open "POST", API, False  
        .setRequestHeader "Content-Type", "application/json"  
        .setRequestHeader "Authorization", "Bearer " & api_key  
        .send SendTxt  
        status_code = .Status  
        response = .responseText  
    End With  
  
    ' 弹出窗口显示 API 响应（调试用）  
  
    ' MsgBox "API Response: " & response, vbInformation, "Debug Info"  
  
    If status_code = 200 Then  
        CallDeepSeekAPI = response  
    Else  
        CallDeepSeekAPI = "Error: " & status_code & " - " & response  
    End If  
  
    Set Http = Nothing  
End Function  
  
Sub DeepSeekV3()  
    Dim api_key As String  
    Dim inputText As String  
    Dim response As String  
    Dim regex As Object  
    Dim matches As Object  
    Dim originalSelection As Object  
  
    api_key = "替换为你的api key"  
    If api_key = "" Then  
        MsgBox "Please enter the API key."  
        Exit Sub  
    ElseIf Selection.Type <> wdSelectionNormal Then  
        MsgBox "Please select text."  
        Exit Sub  
    End If  
  
    ' 保存原始选中的文本  
    Set originalSelection = Selection.Range.Duplicate  
  
    inputText = Replace(Replace(Replace(Replace(Replace(Selection.text, "\", "\\"), vbCrLf, ""), vbCr, ""), vbLf, ""), Chr(34), "\""")  
    response = CallDeepSeekAPI(api_key, inputText)  
  
    If Left(response, 5) <> "Error" Then  
        Set regex = CreateObject("VBScript.RegExp")  
        With regex  
            .Global = True  
            .MultiLine = True  
            .IgnoreCase = False  
            .Pattern = """content"":""(.*?)"""  
        End With  
        Set matches = regex.Execute(response)  
        If matches.Count > 0 Then  
            response = matches(0).SubMatches(0)  
            response = Replace(Replace(response, """", Chr(34)), """", Chr(34))  
  
            ' 取消选中原始文本  
            Selection.Collapse Direction:=wdCollapseEnd  
  
            ' 将内容插入到选中文字的下一行  
            Selection.TypeParagraph ' 插入新行  
            Selection.TypeText text:=response  
  
            ' 将光标移回原来选中文本的末尾  
            originalSelection.Select  
        Else  
            MsgBox "Failed to parse API response.", vbExclamation  
        End If  
    Else  
        MsgBox response, vbCritical  
    End If  
End Sub
```

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/2AE9B378-460A-4BB6-AD6E-0E2ABC6470F2.png)

完成后，可直接关闭弹窗。

点击 文件 -> 选项 -> 自定义功能区，右键开发工具，点击添加新组。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/EBC7C3A1-7FEB-48B7-AA44-BC659159E8B9.png)

在添加的新建组点击右键，点击重命名。将其命名为DeepSeek，并选择心仪的图标，最后点击确定。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/D289EA6E-4AC9-4A90-97EA-9848750CF7D3.png)

首先选择DeepSeek（自定义），选择左侧的命令为“宏”，找到我们添加的DeepSeekV3，选中后点击添加。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/5F5B02BF-932B-4EA7-83AC-7EBFC47C9E5A.png)

随后，选中添加的命令，右键点击重命名，选择开始符号作为图标，并重命名为“生成”。

随后，选中添加的命令，右键点击重命名，选择开始符号作为图标，并重命名为“生成”。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/FC0E7ED9-1922-43E3-B49F-A88F96962475.png)

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/D0E426FC-028C-4407-A110-866C0F7B8256.png)

最后点击确定。

至此，Word成功接入DeepSeek大模型。

选中文字，点击生成，就可以直接将选中的文本发送给大模型，大模型将会按照你选中的文本，做出响应。

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/81C1876E-BE49-4202-B524-42222B08A1B6.png)

![](.evernote-content/CFE62EB1-597C-405C-BBB5-37BC5E961DEF/1A43468E-BCD8-429A-B3B0-207E36CC8C75.png)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c0081ba0f77f92b66c46cad0d01317995c4470cba96dd922673b64624d0b211f9b1f8180a55a&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738510260_1&scene=169&mid=2247484035&sn=c318cb8ae883ea099cf0fbe07c3a3f89&idx=1&__biz=Mzg5NTg5NzY3Ng==&sessionid=1738509696&subscene=200&clicktime=1738510916&enterid=1738510916&flutter_pos=16&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQluerftByaCDjyk20bFQsVhLWAQIE97dBBAEAAAAAANpQJHAzkD8AAAAOpnltbLcz9gKNyK89dVj0SYdm9mARKSSb58RziEFK3clBEI713g502sKLhv5xBta3ENTP8iOeeJAgq0ZjnOv6zDyjbrRCxCdeuChxOGWxlhHPyDHYbgu053XKWjXMNeAyhOAscReAeBnetiFzvT7un9QRwm3SGtz/eaACpiNf5MlHusmlO4bL2fKVWyLt2BJucMCefno7+KszDUNvyQ8QvNoUXjwZ+dSEm8D/6kG+q05kPja1ewNcoG4g9U/d7Bk=&pass_ticket=XM3jyaVPB/EIPzhHZ/qWqdteYpcrv12k3x86Ut85XPFrmhUtv4xnxhhySjjJopXl&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/093728cd-44d2-43af-a75c-155539969af6/093728cd-44d2-43af-a75c-155539969af6/)