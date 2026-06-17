---

name: claude-code-ch5-mcp
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（五）（教不会我吃民法典！）：MCP—连接外部工具.html

---

# 法律人的 Claude Code 教程（五）：MCP — 连接外部工具

> 来源：智律积成（微信公众号）

## 核心概念

- **MCP** = Model Context Protocol（模型上下文协议），一套标准接口让 Claude Code 调用外部工具和数据源
- MCP 服务器运行在用户本地电脑上
- Claude Code 自动判断何时调用哪个 MCP

## 安装方式

- **推荐**：CC-Switch 桌面工具，点点鼠标管理
- **CLI**：`claude mcp add <名称> -- <启动命令>`
- 也可将 MCP 配置直接发给 Claude Code，它会自动安装

## 推荐 MCP

| MCP | 用途 |
|-----|------|
| 企查查类 | 企业信息查询、工商/诉讼/知识产权 |
| 法宝MCP | 案例和法规检索 |
| 高德/百度地图 | 地理信息、侵权门店调查 |
| Arxiv 论文助手 | 论文检索与解读 |
| AntV 可视化图表 | 数据可视化 |

## 安全原则

MCP 获取的数据 = 手动粘贴给 Claude Code 的数据。公开信息放心用，客户敏感信息别碰。

[Related: [[features/MCP]]]
