# Agent Mail CLI 安装配置与邮件签名工具

**日期**：2026-06-30  
**状态**：已配置完成，可正常使用

---

## 安装步骤

### Step 1: 安装 CLI

```bash
npm install -g @tencent-qqmail/agently-cli
```

### Step 2: 安装 skill（可选）

```bash
npx skills add https://agent.qq.com --skill -y
```

> ⚠️ 全局安装（`-g`）因 `.agents/` 目录权限限制，所有 agent 分发失败。但不影响 CLI 本身使用。

### Step 3: OAuth 授权

```bash
agently-cli auth login
```

命令输出授权 URL，浏览器打开完成登录。

### Step 4: 验证

```bash
agently-cli +me
```

**已验证邮箱**：`maxpan0811@agent.qq.com`

#### 权限范围
- `alias:read` — 读取别名
- `mail:delete` — 删除邮件
- `mail:read` — 读取邮件
- `mail:send` — 发送邮件

#### 限制
- 每日发送配额：50 封
- 每小时请求：200 次
- 每分钟请求：10 次
- 单附件最大：20MB

---

## 邮件签名设计

使用 `ᓚᘏᗢ`（横躺猫咪小黑脸）作为签名视觉锚点，可爱但不啰嗦：

```
--
ᓚᘏᗢ  邮件巡逻完毕，安稳着陆 ✦
maxpan0811@agent.qq.com
```

---

## agently-send 助手脚本

将签名自动追加到发出的每一封邮件。

**位置**：`/Users/panbo/.claude/skills/agently-mail-tools/bin/agently-send`
**软链**：`~/.local/bin/agently-send` → skill 目录

**用法**：
```bash
agently-send --to xxx@example.com --subject "标题" --body "正文"
```

**功能**：
- 自动在 `--body` 末尾追加签名
- 保留 agently-cli 的两阶段确认机制
- 交互式提示确认发送

---

## 使用示例

1. 发送笑话邮件给刘梦（myra.liu@trends.com.cn）✅ 已发送
2. 发送测试签名邮件给自己（panbo@hcgtravels.com）✅ 已收到

---

## 关键规则

### 发正式邮件前必须用户确认

这是用户明确提出的原则：
1. ✅ 拟稿后先展示完整邮件内容（收件人、主题、正文）
2. ✅ 等用户说"确认发送"或"发送"后再投递
3. ✅ 不经确认绝不直接发出

该规则已写入 `agently-mail-tools/SKILL.md` 的强制规则区。

---

## 常用 CLI 命令清单

| 命令 | 用途 |
|------|------|
| `agently-cli +me` | 查看当前用户信息 |
| `agently-cli message +list --limit 10` | 查看收件箱 |
| `agently-cli message +read --id msg_xxx` | 阅读某封邮件 |
| `agently-cli message +send --to ... --subject ... --body ...` | 发送邮件（两阶段确认） |
| `agently-cli message +search --q "关键词"` | 搜索邮件 |
| `agently-cli message +reply --id msg_xxx --body "..."` | 回复邮件 |
| `agently-cli message +forward --id msg_xxx --to ... --body "..."` | 转发邮件 |
| `agently-cli message +trash --id msg_xxx` | 移至废纸篓 |
| `agently-cli attachment +download --msg msg_xxx --att att_xxx` | 下载附件 |
| `agently-cli auth status` | 查看 OAuth 状态 |
| `agently-cli auth refresh` | 刷新 OAuth token |
