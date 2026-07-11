# Obsidian Git 备份到 GitHub + Gitee 配置记录

**日期**: 2026-07-11  
**系统序列号**: `cec8021f-5254-44f8-a282-37ee65bf5530`  
**会话ID**: `019ea725-a614-7112-8808-980bf8af5fff`  
**任务**: 搭建 Obsidian 笔记自动备份到 GitHub，Gitee 为镜像

---

## 最终结果

| 仓库 | GitHub 地址 | 内容 |
|------|-----------|------|
| 笔记库（20260520） | `github.com/maxpan0811/obsidian.git` | wiki、印象笔记导出(35k篇)、知乎笔记(130篇)、程序开发、老婆邮件、随笔、股票分析 |
| 主库配置 | `github.com/maxpan0811/obsidian-config.git` | .obsidian 配置（插件、主题、设置） |
| Gitee 镜像 | `gitee.com/maxpan0811/obsidian.git` | GitHub Actions 自动同步（维护结束后生效） |

---

## 操作记录

### 1. 环境评估
- 用户已有 GitHub 账号 `maxpan0811`，`gh` CLI 已认证
- Obsidian 数据在 `~/Obsidian/20260520/`，已有 git 但未设置自动备份
- `印象笔记管理工具/`（35k 文件, 563MB）和 `知乎管理工具/` 在 `.gitignore` 中被排除
- `wiki/vector_store/chroma.sqlite3`（242MB）从第一个 commit 就被 git 跟踪

### 2. 百度云盘评估 → 不采用
- 无官方 CLI，第三方工具（bypy/BaiduPCS-Go）可能随时失效
- 下载限速，恢复体验差
- 不适合高频小文件增量备份
- 替代方案：Git + GitHub（首选）

### 3. Gitee vs GitHub 选择
- 用户已有 GitHub 认证和工作流，保留为主备份
- Gitee 做镜像以防 GitHub 被墙
- 镜像方式：GitHub Actions workflow（无需本地依赖）

### 4. Obsidian Git 插件安装
- 手动下载插件文件到 `.obsidian/plugins/obsidian-git/`
- 更新 `community-plugins.json` 注册
- 关键配置：Base path = `20260520`（指向子库 git 仓库）
- 自动 commit 间隔：15 分钟
- 自动 push 间隔：15 分钟
- 注意：需在 Obsidian 设置中启用「第三方插件」

### 5. Token 权限修复
```
gh auth refresh --scopes repo
```
- 原有 token scopes = `none`，只能读公开仓库
- 刷新后获得 `repo`, `workflow`, `gist`, `read:org` scopes

### 6. 印象笔记导出纳入备份
- 从 `.gitignore` 移除 `印象笔记管理工具/`
- 首次 commit：35,000+ 文件，563MB
- 完整附件保留（仅 1.3MB 图片）

### 7. 知乎笔记纳入备份
- 从 `.gitignore` 移除 `知乎管理工具/`，改为排除 `知乎管理工具/attachments/`
- 仅跟踪 .md 笔记文件（129 篇, ~2MB）
- 排除二进制附件（2,494 文件, 233MB）

### 8. 大文件从 git 历史清理
```
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch -r wiki/vector_store/' \
  --prune-empty --tag-name-filter cat -- --all
git push --force origin main
git reflog expire --all --expire=now
git gc --aggressive --prune=now
```
- 移除 `wiki/vector_store/chroma.sqlite3`（242MB）及相关文件
- 重写 32 个 commit 历史
- **重要**：force push 后本地 Obsidian Git 插件需 `git fetch origin && git reset --hard origin/main` 同步

### 9. 超长文件名修复（Linux ext4 兼容）
- 6 个文件 basename >255 字节（UTF-8 编码下的中文字符）
- 截短至 50 字符 + `...` 后缀
- 原因：GitHub Actions runner 使用 Linux，ext4 文件名上限 255 字节

### 10. Gitee 镜像同步配置
- GitHub Actions workflow：`.github/workflows/sync-to-gitee.yml`
- 触发条件：push 到 main 分支 + 支持手动触发
- 需要：Gitee Personal Access Token → GitHub Secrets (`GITEE`)
- **注意**：Gitee 于 2026-07-11 23:00-00:00 维护，维护后生效

---

## 关键决策与取舍

| 选项 | 选择 | 理由 |
|------|------|------|
| 备份方案 | Git + GitHub | 纯文本最适合 git，增量快，版本历史完整 |
| 自动方式 | Obsidian Git 插件 | 内建于 Obsidian，无需额外守护进程 |
| 镜像 | GitHub Actions | 不依赖本地机器，push 即同步 |
| 大文件处理 | filter-branch 移除 | 可重新生成的缓存，不值得 LFS 管理 |
| 附件处理 | 排除二进制 | git 不适合二进制文件 diff/存储 |
| 仓库拆分 | 笔记库 + 配置库 | 互不干扰，变更频率不同 |

---

## 已知问题
- Gitee 同步 workflow 因维护未验证，预计 00:00 后可手动触发测试
- 如果 Gitee PAT 过期需重新生成并更新 GitHub Secrets
