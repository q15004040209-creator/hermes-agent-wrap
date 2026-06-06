# Hermes Agent Wrapper🤖

[English](#english) | [中文](#中文)

---

## English

### What is Hermes Agent?

**Hermes Agent** is a self-improving AI agent built by [Nous Research](https://nousresearch.com). It's the most powerful open-source agent framework available — the only agent with a built-in learning loop that:

- 📖 **Creates skills from experience** — learns from your interactions
- 🔄 **Self-improves during use** — continuously optimizes itself
- 🧠 **Persists knowledge** — remembers across sessions
- 🔍 **Searches past conversations** — recalls context from history
- 👤 **Builds a model of you** — deepens understanding over time

>⭐ **184,292 GitHub stars** — one of the most popular AI agent projects  
> 📈 **+11,333 stars this week** — rapidly growing community

### Key Features

| Feature | Description |
|---------|-------------|
| **Real Terminal Interface** | Full TUI with multiline editing, slash commands, conversation history, streaming tool output |
| **Multi-Platform Messaging** | Telegram, Discord, Slack, WhatsApp, Signal, Email — single gateway |
| **Closed Learning Loop** | Agent-curated memory, autonomous skill creation, FTS5 session search |
| **Scheduled Automation** | Cron scheduler with platform delivery — reports, backups, audits |
| **Subagent Parallelization** | Spawn isolated subagents for parallel workflows |
| **Runs Anywhere** | Local, Docker, SSH, Singularity, Modal, Daytona — $5 VPS to GPU cluster |

### Quick Start

```bash
# Linux / macOS / WSL2
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Windows (PowerShell)
iex (irm https://hermes-agent.nousresearch.com/install.ps1)

# After installation
hermes
```

### Python Integration

```python
from hermes_agent import Hermes

# Initialize the agent
agent = Hermes(model="openai:gpt-4o")

# Chat interactively
response = agent.chat("Hello, help me write a Python function")
print(response)
```

### Supported Providers

Use any model from **Nous Portal**, **OpenRouter** (200+ models), **NovitaAI**, **NVIDIA NIM**, **Xiaomi MiMo**, **z.ai/GLM**, **Kimi/Moonshot**, **MiniMax**, **Hugging Face**, **OpenAI**, or your own endpoint.

Switch with one command:
```bash
hermes model openai:gpt-4o
```

###Documentation

📖 [Full Documentation](https://hermes-agent.nousresearch.com/docs/)
💬 [Discord Community](https://discord.gg/NousResearch)  
📦 [Skills Hub](https://agentskills.io)

### License

MIT License — see [LICENSE](LICENSE)

---

## 中文

### 什么是 Hermes Agent？

**Hermes Agent** 是由 [Nous Research](https://nousresearch.com) 构建的自我进化 AI Agent。它是当前最强的开源 Agent 框架——唯一内置学习循环的 Agent：

- 📖 **从经验中创造技能** — 从交互中学习
- 🔄 **使用中自我改进** — 持续优化自身
- 🧠 **持久化知识** — 跨会话记忆
- 🔍 **搜索历史对话** — 从历史中召回上下文
- 👤 **构建用户模型** — 随时间加深对你的理解

> ⭐ **184,292 GitHub 星标** — 最受欢迎的 AI Agent 项目之一  
> 📈 **本周新增 +11,333** — 社区快速增长中

### 核心特性

| 特性 | 描述 |
|------|------|
| **真实终端界面** |完整 TUI，多行编辑，斜杠命令，自动补全，对话历史，流式工具输出 |
| **多平台消息** | Telegram、Discord、Slack、WhatsApp、Signal、Email — 统一网关 |
| **闭环学习系统** | Agent 策划的记忆、自主技能创建、FTS5 会话搜索 |
| **定时自动化** | Cron 调度器，支持任意平台投递 — 报告、备份、审计 |
| **子 Agent 并行化** | 派生隔离子 Agent，并行处理工作流 |
| **任意环境运行** | 本地、Docker、SSH、Singularity、Modal、Daytona — $5 VPS 到 GPU 集群 |

### 快速安装

```bash
# Linux / macOS / WSL2
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Windows (PowerShell)
iex (irm https://hermes-agent.nousresearch.com/install.ps1)

# 安装后启动
hermes
```

### Python 集成示例

```python
from hermes_agent import Hermes

# 初始化 Agent
agent = Hermes(model="openai:gpt-4o")

# 发送对话
response = agent.chat("你好，帮我写一个 Python 函数")
print(response)

# 使用工具
response = agent.chat("帮我搜索今天的天气", tools=["web_search"])
print(response)

# 多模型切换
agent.set_model("openrouter:anthropic/claude-3-5-sonnet")
response = agent.chat("用中文回答")
print(response)
```

### 支持的模型提供商

可使用 **Nous Portal**、**OpenRouter**（200+ 模型）、**NovitaAI**、**NVIDIA NIM**、**小米 MiMo**、**z.ai/GLM**、**Kimi/Moonshot**、**MiniMax**、**Hugging Face**、**OpenAI** 或自有端点。

一行命令切换：
```bash
hermes model openai:gpt-4o
```

### 文档资源

📖 [完整文档](https://hermes-agent.nousresearch.com/docs/)  
💬 [Discord 社区](https://discord.gg/NousResearch)  
📦 [技能中心](https://agentskills.io)

### 开源许可

MIT License — 见 [LICENSE](LICENSE)

---

>⚠️ **注意**: 本仓库为 Hermes Agent 的 Python 封装示例，非官方 Nous Research 维护项目。  
> **Notice**: This repository is a Python wrapper example for Hermes Agent, not an official Nous Research project.

*Built with ❤️ by Nous Research — Wrapped with ❤️ here*