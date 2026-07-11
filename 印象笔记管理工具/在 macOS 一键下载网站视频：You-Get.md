# 在 macOS 一键下载网站视频：You-Get

---

本文目的是用 You-Get 下载支持网站的视频，**You-Get 支持的网站请查看**[You-Get 官方说明](https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E#supported-sites) **。**

**出于版权考虑，不建议下载有版权的视频。**

![](.evernote-content/703E11B8-6DF2-4A90-A7C2-E08E571C27C5/DEC76C45-FF33-406B-94B3-65D1BA7623FA.png)例图

费多看码！

打开一个视频网页，例：

1. 首先我们要安装 You-Get 工具，需先安装 [homebrew](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwi466uzsuTTAhWGrJQKHYlpDfgQFgglMAA&url=https%3A%2F%2Fbrew.sh%2F&usg=AFQjCNEK9RsqMgSc6Ai3v0jEiRniLzuTIQ&sig2=d0mc-HGf6wuMRsfhfYJV_Q) ，如果已安装，跳过此步骤。打开终端，输入：

   ```
   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```

   安装完成后即可安装 You-Get ：

   ```
   brew install you-get
   ```

   因评论区有小伙伴提到，**建议通过pip3安装**，官方说明文档里面的方式。[You-Get 中文说明](https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E)

   ```
   pip3 install you-get
   ```

   另外，因视频网站的视频是分段视频，如果需要合并需要另外一个工具：ffmpeg ，安装方法和You-Get一样。

   ```
   brew install ffmpeg
   ```

   下载完成后，You-Get 会自动调用 ffmpeg 合并成完整视频。接下来的工作需要在另一个工具里面完成。
2. 打开**Automator** ，**新建文稿**，选取**服务**。「服务」收到选定**没有输入**。位于 **Safari.app** 。将左侧的流程按顺序拖到右侧，**从 Safari 中获得当前网页**，**运行 Shell 脚本**（传递输入选择**作为自变量**，内容：

   ```
   LC_CTYPE=UTF-8 /usr/local/bin/you-get -o "/Users/usr/Downloads" "$1"
   ```

   其中 **/Users/usr/Downloads** 可随自己喜好更改（当然，要是你的电脑命名 usr 你可以不改…），**显示通知**（标题 **You-Get** ，信息**下载已完成**）。**详见例图**。强烈建议在这一步完成后**测试过后再进行下一步**。打开一个视频网页，例：[【笑实验】1期:当街遇上阿拉伯人！](http://v.youku.com/v_show/id_XMTU3MjE1MDMxMg==.html?spm=a2h0z.8244218.2371631.52)然后点击右上角**运行**。日志显示无错误后便可建立服务，设置快捷键。
3. 存储会弹出命名，建议再导出一份作为备份。打开**系统偏好设置——键盘——快捷键——应用快捷键**里面点+号对所命名的服务添加快捷键（如题图的 ⌃D）。

至此，教程结束，你可以使用快捷键一键下载网页视频了。

**本文由本人首发于知乎**[macOS 一键下载 You-Get 支持网站的视频](https://zhuanlan.zhihu.com/p/26733474)**。未经许可，禁止转载**。

---

[🌐 原始链接](https://sspai.com/post/39107)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4ecf5008-630d-4b0b-8164-3aed2ffc0669/4ecf5008-630d-4b0b-8164-3aed2ffc0669/)