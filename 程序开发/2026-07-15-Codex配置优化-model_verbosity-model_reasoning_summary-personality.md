# Codex 配置优化：model_verbosity + model_reasoning_summary + personality

**日期**：2026-07-15  
**会话序列号**：`019ea735-9700-71a2-a1c6-3025304704c7`  
**安装ID**：`cec8021f-5254-44f8-a282-37ee65bf5530`

---

## 对话记录

### 用户分享
从 OpenAI 社区刷到一组 Codex 配置，可以大幅减少 Codex 回复中的废话（铺垫、总结、鼓励式话术）。试用后回答清爽很多。到官方文档核实后确定可以放心抄作业。

三条配置写入 `~/.codex/config.toml`：

```toml
model_reasoning_summary = "concise"  # 简短摘要
model_verbosity = "low"              # 输出极简
personality = "pragmatic"            # 务实风格
```

### 各参数说明

| 参数 | 说明 | 有效值 | 注意事项 |
|------|------|--------|---------|
| `model_verbosity` | 控制 Codex 输出详细程度 | `low \| medium \| high` | 仅对 Responses API provider 生效；Chat Completions 忽略此设置 |
| `model_reasoning_summary` | 推理摘要的详细程度 | `auto \| concise \| detailed \| none` | 控制展示给用户的推理过程摘要长度 |
| `personality` | 沟通风格 | `friendly \| pragmatic \| none` | 支持 `/personality` 命令实时切换 |

### 官方验证
通过 Codex Manual 确认：
- `model_verbosity` 定义在 Advanced Configuration → Model reasoning, verbosity, and limits 章节
- `personality` 定义在 Communication style 章节
- `personality` 需要在 `[features]` 下加 `personality = true` 开启功能开关，顶层 `personality = "pragmatic"` 设值，两者都要配置

### 当前配置
写入 `~/.codex/config.toml`：
- `model_reasoning_summary = "concise"`
- `model_verbosity = "low"`
- `personality = "pragmatic"`
- `[features]` 下新增 `personality = true`

### 效果预期
Codex 变得直给——以代码和命令为主，不再有大段解释和重复总结。风格偏向工程师之间的沟通方式而非助手式客套。

---

*本次会话由 Codex 自动保存到 Obsidian。*
