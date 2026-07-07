---
title: 物尽其用！在Codex和Codex桌面端当中使用Deepseek 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/物尽其用！在Codex和Codex桌面端当中使用Deepseek 2.md
tags: [evernote, impression, yinxiang]
---

# 物尽其用！在Codex和Codex桌面端当中使用Deepseek

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517003&idx=2&sn=f1a544c9d84feb20ff9ddd159cdc870d&chksm=e9d66386416c50a910ddb481f75cfcd181b459859361f14b103aaf1103e384833fef232f5927&mpshare=1&scene=24&srcid=0609TnO818h3RTf0j7FtQbwx&sharer_shareinfo=dfc5940325c654994398497dcc661712&sharer_shareinfo_first=dfc5940325c654994398497dcc661712&clicktime=1780992816&enterid=1780992816&ascene=14&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1pdYqQJK40O3ACgjr1RuChLTAQIE97dBBAEAAAAAAAmBGZn+2XYAAAAOpnltbLcz9gKNyK89dVj0L/UVz+b2iOdzQhxGT58Paa4HUKmxovfdV1focgbw0w6Y8NoQmQqatfZ27+X8XwFOUDl1zuMD0Mf2owFup5TR3Pr0r948DMP1FQq+u9+ca3ZobOIZ7HLIx26//7kflCPt5d336cre/hhbQYyGo6AzmPuh/DRbbow1Uy/nusw+Jlr0wOGOLgTqZw7QsZFnbjRQHzeDtBke+qqc5NJopo5DNRibAlPwsL0HwpUYj0U=&pass_ticket=dtVAEb7WRQyBF9D/K0Dw2teFnusfIhqsCdyzyogKxz4/24Z7Sh2hGXMkrCRzelFo&wx_header=3)

物尽其用！在Codex和Codex桌面端当中使用Deepseek
================================

字节笔记本 字节笔记本

除了从缓存的角度来[榨干DeepSeek！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516950&idx=1&sn=8c3e98ce4fc38d8f4515645274a6d8cb&scene=21#wechat_redirect)，我们还可以在不同的其他工具来充分使用Deepseek，[国货之光DeepSeek永久2.5 折！以及我的DeepSeek+使用工具链](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516934&idx=1&sn=88b86ec76b8e955f430728b2b69beae7&scene=21#wechat_redirect)。

其中最好用的当属Codex 桌面端了，对于新手朋友，非常的友好，不用再面对黑漆漆的桌面端了，项目管理以及Skills在GUI的界面下，非常的趁手。

下面是配置指南：

1.基础的环境配置

需要你本地安装 Node.js以及Go，可以自行搜索一下，建议最新版本，具体的安装步骤，这里就不再赘述了。

2.安装 Codex CLI
--------------

ssh mini "export PATH=\$HOME/local/bin:\$PATH && npm install -g @openai/codex"
ssh mini "export PATH=\$HOME/local/bin:\$PATH && codex --version"
# codex-cli 0.133.0

3.克隆 Moon Bridge
----------------

ssh mini "cd ~ && git clone https://github.com/ZhiYi-R/moon-bridge.git"

4.创建 Moon Bridge 配置
-------------------

创建 config.yml

cat > ~/moon-bridge/config.yml << 'EOF'
mode: "Transform"
server:
  addr: "127.0.0.1:38440"
models:
  deepseek-v4-pro:
    context\_window: 1000000
    max\_output\_tokens: 384000
    default\_reasoning\_level: "high"
    supported\_reasoning\_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports\_reasoning\_summaries: true
    default\_reasoning\_summary: "auto"
    extensions:
      deepseek\_v4:
        enabled: true
  deepseek-v4-flash:
    context\_window: 1000000
    max\_output\_tokens: 384000
    default\_reasoning\_level: "high"
    supported\_reasoning\_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports\_reasoning\_summaries: true
    default\_reasoning\_summary: "auto"
    extensions:
      deepseek\_v4:
        enabled: true
providers:
  deepseek:
    base\_url: "https://api.deepseek.com/anthropic"
    api\_key: "sk-xxxxxxxxxxxxxxxxxxxxxxxx"   # 填入 DeepSeek API Key
    offers:
      - model: deepseek-v4-pro
      - model: deepseek-v4-flash
routes:
  moonbridge:
    model: deepseek-v4-pro
    provider: deepseek
  gpt-5.5:
    model: deepseek-v4-pro
    provider: deepseek
  gpt-5.4:
    model: deepseek-v4-pro
    provider: deepseek
  gpt-5.3-codex:
    model: deepseek-v4-pro
    provider: deepseek
  gpt-5.2:
    model: deepseek-v4-flash
    provider: deepseek
  gpt-4.1:
    model: deepseek-v4-pro
    provider: deepseek
  gpt-4.1-mini:
    model: deepseek-v4-flash
    provider: deepseek
defaults:
  model: moonbridge
  max\_tokens: 65536
EOF

`gpt-5.x` 系列路由是后来补加的兜底路由，建议一开始就加上。

5.编译并启动 Moon Bridge
-------------------

编译

cd ~/moon-bridge
export PATH=$HOME/local/go/bin:$PATH
go build ./cmd/moonbridge
# 首次编译会下载依赖，需要等待

生成 Codex 配置

Moon Bridge 提供工具命令，可自动生成 `~/.codex/config.toml` 和 `models_catalog.json`：

CODEX\_HOME\_DIR="${CODEX\_HOME:-$HOME/.codex}"
mkdir -p "$CODEX\_HOME\_DIR"
# 备份旧配置
cp "$CODEX\_HOME\_DIR/config.toml" "$CODEX\_HOME\_DIR/config.toml.bak" 2>/dev/null || true
MODEL=$(./moonbridge --config config.yml --print-codex-model 2>/dev/null | head -1)
# 输出：moonbridge
./moonbridge \
  --config config.yml \
  --print-codex-config "$MODEL" \
  --codex-base-url "http://127.0.0.1:38440/v1" \
  --codex-home "$CODEX\_HOME\_DIR" \
  > "$CODEX\_HOME\_DIR/config.toml" 2>/dev/null

生成后的 config.toml 内容

model = "moonbridge"
model\_provider = "moonbridge"
model\_context\_window = 1000000
model\_max\_output\_tokens = 384000
model\_catalog\_json = "/Users/pan/.codex/models\_catalog.json"
[model\_providers.moonbridge]
name = "Moon Bridge"
base\_url = "http://127.0.0.1:38440/v1"
wire\_api = "responses"
[mcp\_servers.deepwiki]
url = "https://mcp.deepwiki.com/mcp"
startup\_timeout\_sec = 3600
tool\_timeout\_sec = 3600

6.配置开机自启动（launchd）
------------------

我本地使用的是Mac OS，把它加入到了自动启动当中。

macOS 使用 `launchd` 管理服务。

创建 plist 文件

cat > ~/Library/LaunchAgents/com.user.moonbridge.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.moonbridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/pan/moon-bridge/moonbridge</string>
        <string>--config</string>
        <string>/Users/pan/moon-bridge/config.yml</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/pan/moon-bridge</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/pan/moon-bridge/moonbridge.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/pan/moon-bridge/moonbridge.log</string>
</dict>
</plist>
EOF

加载服务

launchctl load ~/Library/LaunchAgents/com.user.moonbridge.plist

常用管理命令

# 查看状态（第一列是 PID，0 表示未运行）
launchctl list | grep moonbridge
# 停止
launchctl unload ~/Library/LaunchAgents/com.user.moonbridge.plist
# 重启
launchctl unload ~/Library/LaunchAgents/com.user.moonbridge.plist
launchctl load ~/Library/LaunchAgents/com.user.moonbridge.plist
# 查看日志
tail -f ~/moon-bridge/moonbridge.log

7.验证
----

查看模型列表

curl http://127.0.0.1:38440/v1/models

返回：

{
  "models": [
    {"slug": "deepseek/deepseek-v4-flash", ...},
    {"slug": "deepseek/deepseek-v4-pro", ...},
    {"slug": "gpt-5.5", ...},
    {"slug": "gpt-5.4", ...},
    {"slug": "moonbridge", ...}
  ]
}

发送测试请求

curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonbridge",
    "input": "你好，用一句话介绍你自己。",
    "max\_output\_tokens": 128
  }'

正常时返回 `output_text` 字段，`model` 字段显示 `deepseek-v4-pro`。

测试 gpt-5.5 兜底路由

curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.5", "input": "你是谁？", "max\_output\_tokens": 64}'

返回正常说明兜底路由生效。

8.日常使用
------

Codex CLI是直接打开就可以使用，`Codex app`模型选择 **Moon Bridge** 下的任意模型即可。

![](.evernote-content/85192C42-879E-405D-941C-BC769C923E18/ABC493A6-E2EF-403C-BA3C-C43949B1B1E3.png)

在桌面端，可以完全使用Codex桌面端的Skills技能，不过插件系统是无法使用的。

![](.evernote-content/85192C42-879E-405D-941C-BC769C923E18/9BE20D3B-84DC-441B-B405-6351B55B9A0C.png)

要了Moon Bridge作为中转，我们也可以借助它在任意的Code Agent 的端使用，大大提升了Deepseek在多端的适用范围。

不过Deepseek目前还不支持多模态，如果你想让它支持多模态，可以参照如下的内容：

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517003&idx=2&sn=f1a544c9d84feb20ff9ddd159cdc870d&chksm=e9d66386416c50a910ddb481f75cfcd181b459859361f14b103aaf1103e384833fef232f5927&mpshare=1&scene=24&srcid=0609TnO818h3RTf0j7FtQbwx&sharer_shareinfo=dfc5940325c654994398497dcc661712&sharer_shareinfo_first=dfc5940325c654994398497dcc661712&clicktime=1780992816&enterid=1780992816&ascene=14&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1pdYqQJK40O3ACgjr1RuChLTAQIE97dBBAEAAAAAAAmBGZn+2XYAAAAOpnltbLcz9gKNyK89dVj0L/UVz+b2iOdzQhxGT58Paa4HUKmxovfdV1focgbw0w6Y8NoQmQqatfZ27+X8XwFOUDl1zuMD0Mf2owFup5TR3Pr0r948DMP1FQq+u9+ca3ZobOIZ7HLIx26//7kflCPt5d336cre/hhbQYyGo6AzmPuh/DRbbow1Uy/nusw+Jlr0wOGOLgTqZw7QsZFnbjRQHzeDtBke+qqc5NJopo5DNRibAlPwsL0HwpUYj0U=&pass_ticket=dtVAEb7WRQyBF9D/K0Dw2teFnusfIhqsCdyzyogKxz4/24Z7Sh2hGXMkrCRzelFo&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8aac9313-4f1c-45f1-942b-f8c9d5c49e1c/8aac9313-4f1c-45f1-942b-f8c9d5c49e1c/)
