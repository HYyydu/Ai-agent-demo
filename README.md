## 项目简介

聊天助手是一个基于 LangChain 框架开发的智能 Agent 教学案例，旨在展示如何构建一个具有实际应用价值的 AI 助手。在当前 AI 技术快速迭代的背景下，掌握 AI Agents 开发已成为技术从业者的必备技能。本项目通过实战案例，帮助开发者快速入门 AI Agents 开发领域。

## 🚀 核心功能

- 🤖 基础 Agent 交互系统
- 📚 基于 RAG (检索增强生成) 的知识库查询
- 🔍 实时在线搜索能力
- 📅 Google Calendar 与 Tasks 自然语言交互
- 🎭 情绪识别与多轮对话策略

## 🛠️ 技术栈

- LangChain
- Python 3.9+
- Slack Bolt Framework
- Google Calendar API
- Google Tasks API
- Vector Database
- Emotion Analysis Models

## ⚙️ 安装说明

### 1. 系统要求

- Python 3.9 或更高版本
- Redis Stack 服务器
- Git（用于克隆项目）

### 2. 安装步骤

#### 2.1 安装 Redis Stack

根据您的操作系统选择相应的安装方式：

**MacOS**:

```bash
brew install redis-stack
```

**Ubuntu/Debian**:

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis-stack-server
```

**Windows**:

- 访问 [Redis 下载页面](https://redis.io/download/)
- 下载并安装 Redis Stack

#### 2.2 安装 Python 依赖

使用 Poetry 安装项目依赖：

```bash
# 安装 Poetry（如果未安装）
pip install poetry

# 安装项目依赖
poetry install

# 激活虚拟环境（二选一）：
# 方式1：使用新的 env activate 命令（推荐）
poetry env use python3
source $(poetry env info --path)/bin/activate  # Unix/MacOS
# 或
.\$(poetry env info --path)\Scripts\activate   # Windows

# 方式2：安装并使用 shell 插件
poetry self add poetry-plugin-shell
poetry shell
```

### 3. 环境配置

在项目根目录创建 `.env` 文件，配置以下必要参数：

```env
# API Keys
SERPAPI_API_KEY=your_serpapi_key          # 搜索引擎 API key
OPENAI_API_KEY=your_openai_key            # OpenAI API key
OPENAI_API_BASE=your_openai_proxy         # OpenAI 代理地址（如果需要）

# 主模型配置
BASE_MODEL=gpt-4o                         # 主模型名称
OPENAI_API_KEY=your_openai_key            # OpenAI API key
OPENAI_API_BASE=your_openai_proxy
BACKUP_MODEL=gpt-4                        # 备用模型名称

# 嵌入模型配置
EMBEDDING_MODEL=“text-embedding-3-small”
EMBEDDING_API_KEY=open_ai_key
EMBEDDING_API_BASE=open_ai_base
EMBEDDING_COLLECTION=langchain_docs

# 向量数据库配置
PERSIST_DIR=./vector_db
CHUNK_SIZE=800
CHUNK_OVERLAP=50
MEMORY_KEY=chat_history

# Slack 配置
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token

# Google API 配置
# 将 credentials.json 放在项目根目录
```

## 🔧 使用指南

### 1. 启动服务

#### 1.1 启动 Redis 服务

```bash
# MacOS
redis-stack-server

# Ubuntu/Debian
sudo systemctl start redis-stack-server

# Windows
# 通过安装程序启动 Redis 服务
```

#### 1.2 启动聊天助手

```bash
# 确保虚拟环境已激活（命令行前缀应显示虚拟环境名称）
# 运行主程序
poetry run python -m src.SlackWebHook
```

### 2. Slack 配置

1. 访问 [Slack API 网站](https://api.slack.com/apps)
2. 创建新的 Slack 应用
3. 配置以下权限：
   - `chat:write`
   - `app_mentions:read`
   - `channels:history`
   - `groups:history`
   - `im:history`
   - `mpim:history`
4. 安装应用到工作区
5. 获取并配置以下信息：
   - Bot User OAuth Token (SLACK_BOT_TOKEN)
   - App-Level Token (SLACK_APP_TOKEN)
6. 在需要使用的频道中添加机器人

### 3. Google Calendar 配置

1. 访问 [Google Cloud Console](https://console.cloud.google.com)
2. 创建新项目
3. 启用 Google Calendar API 和 Google Tasks API
4. 创建 OAuth 2.0 凭据
5. 下载凭据文件并重命名为 `credentials.json`
6. 将 `credentials.json` 放在项目根目录
7. 首次运行时，会打开浏览器要求授权访问

### 4. 基本使用

- **知识库查询**：直接向机器人提问，它会从知识库中检索相关信息
- **日程管理**：使用自然语言创建、查询或修改 Google Calendar 日程
- **待办事项**：通过对话方式管理 Google Tasks 待办任务
- **实时搜索**：询问实时信息，机器人会通过搜索引擎获取答案

### 5. 常见问题处理

- **Redis 连接失败**：检查 Redis 服务是否正常运行
- **知识库添加**: 入口在 localhost:8000/docs 中，目前只支持批量添加 url
- **Google API 授权失败**：检查 credentials.json 是否正确配置
- **Slack 连接失败**：检查 Bot Token 和 App Token 是否正确

## 📈 项目亮点

- **教学导向设计**：项目结构清晰，代码注释完善，适合学习和二次开发
- **实际应用场景**：与 Slack 深度集成，展示了 AI 在企业协作中的实际应用
- **情感计算集成**：创新性地引入情绪识别，实现更智能的人机交互
- **自动化工作流**：通过自然语言处理，简化日常工作流程
# Ai-agent-demo
