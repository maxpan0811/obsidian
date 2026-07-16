---
title: "如何在移除 Word 文档样式的同时保留格式"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在移除 Word 文档样式的同时保留格式.md
tags: [印象笔记]
---

# 如何在移除 Word 文档样式的同时保留格式

# 如何在移除 Word 文档样式的同时保留格式 --- 样式（style）是 Word 中用于快速更改文本格式的功能。将一种样式应用于文档中不同段落之后，只需更改一次该样式，即可同时更改这些文本的格

---

# 如何在移除 Word 文档样式的同时保留格式

---

样式（style）是 Word 中用于快速更改文本格式的功能。将一种样式应用于文档中不同段落之后，只需更改一次该样式，即可同时更改这些文本的格式。同时，样式还能使文档结构化，指定不同「标题」层次的样式后，即可快速生成目录。

但样式有时也会带来麻烦。例如，需要将别人传过来的多份 Word 文档进行整合、统一其格式时，他人文档中预设的样式可能会给排版造成混乱和不便。但是，如果一刀切地将其粘贴为纯文本，不仅会丢失所有的格式，增加不必要的工作量，又会导致文本层级难以辨识。其实，利用 Office 中的 VBA 脚本，就能在移除样式的同时保留文本格式。

下图中，左侧是使用粘贴为纯文本方法所得结果，右侧则是用 VBA 可以实现的效果，可以看出，原本的标题样式已经被移除，但仍然保留了全部的格式设定：

![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/0DD16380-3C6C-496D-B0D3-9197AD288B96.png)

具体的实现方法如下：

### A. 如果你使用 macOS 和 Office 2016 for Mac

1. 正常使用样式功能来编排文档；
2. 依次点击菜单中的「工具」–「宏」–「Visual Basic 编辑器…」；

   ![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/3813474F-AB96-4190-BE67-191BC324BE18.jpg)
3. 在弹出的窗口右侧粘贴如下脚本：

   ```
    Sub DirectFormat()
        Dim para As Paragraph
        Dim fnt As Font
        Dim pfmt As ParagraphFormat
        For Each para In ActiveDocument.Paragraphs
            With para
                If .Style <> ActiveDocument.Styles("Normal") Then
                Set fnt = .Style.Font
                Set pfmt = .Style.ParagraphFormat
                .Style = ActiveDocument.Styles("Normal")
                .Range.Font = fnt
                .Range.ParagraphFormat = pfmt
                End If
            End With
        Next
    End Sub
   ```
4. 点击下方的「运行程序」按钮，执行上述命令；

   ![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/3269171F-D31F-4286-A98C-7C74A2957659.jpg)
5. 所有的样式现在已经被清除。

   要检查是否运行成功，在「主页」选项卡中点击打开「样式面板」，然后试着在之前设置有样式的段落中单击。如果右侧的样式面板中始终显示为「Normal」样式，则表明已经运行成功。

   ![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/CEF49D52-9CC1-48DA-A245-476201DA2516.jpg)

### B. 如果你使用 Windows 和 Office 2016

1. 正常使用样式功能来编排文档；
2. 按下 Alt + F11 组合键；
3. 在弹出的窗口中，双击左侧的「ThisDocument」选项，并在右侧弹出的空白窗口中粘贴如下脚本：

   ```
    Sub DirectFormat()
        Dim para As Paragraph
        Dim fnt As Font
        Dim pfmt As ParagraphFormat
        For Each para In ActiveDocument.Paragraphs
            With para
                If .Style <> ActiveDocument.Styles("Normal") Then            
                Set fnt = .Style.Font
                Set pfmt = .Style.ParagraphFormat
                .Style = ActiveDocument.Styles("Normal")
                .Range.Font = fnt
                .Range.ParagraphFormat = pfmt
                End If
            End With
        Next
    End Sub
   ```
4. 点击上方工具栏中的「运行」按钮，执行上述命令；

   ![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/DE876017-30EB-427D-BAA9-B30E9E631E31.jpg)
5. 所有的样式现在已经被清除。

   要检查是否运行成功，在「主页」选项卡中，点击「样式」区域右下角的展开按钮，展开样式窗格，然后试着在之前设置有样式的段落中单击。如果右侧的样式窗格中始终显示为「Normal」样式，则表明已经运行成功。

   ![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/872336DF-651E-4646-A92F-170A0B4E657E.jpg)

### 备注

需要注意的是，如果你同时打开了多份 Word 文档，那么在上述 VBA 编辑器的左侧，也会出现多个文档的选项。这种场合，请保证选中了 `Project(需要去除样式的文档)-Microsoft Word Objects-ThisDocument` 并使其高亮，然后再在右侧粘贴并执行代码。

![](.evernote-content/F91CFEED-5A77-469C-951D-7E3E3C263951/4B39EB0A-9F64-4973-9DB8-D3D7F0F9A539.png)

### Facts for Nerds

上述命令的作用如下：遍历文档中所有段落并检查其样式，如果某一段落的样式不是「Normal（正文）」，则记住其当前格式设置，然后清除该段落的样式，最后将先前记住的格式重新应用到该段落上。

---

[🌐 原始链接](https://sspai.com/post/38852)

[📎 在印象笔记中打开](evernote:///view/207087/s1/83760205-a4a5-4dfa-b445-f8ab28f47ec4/83760205-a4a5-4dfa-b445-f8ab28f47ec4/)