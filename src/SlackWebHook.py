#!/usr/bin/env python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from src.Agents import AgentClass
from src.Storage import add_user
from dotenv import load_dotenv
import logging
import os

def setup_logging():
    """设置日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('slack_connection.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# 加载环境变量
load_dotenv()

# 验证必要的环境变量
required_env_vars = ["SLACK_BOT_TOKEN", "SLACK_APP_TOKEN"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Initialize the Slack app
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# Initialize the AI agent
agent = AgentClass()

@app.event("message")
def handle_message_events(body, say):
    """处理消息事件"""
    try:
        # 忽略机器人自己的消息
        if "bot_id" in body["event"]:
            return

        # 获取消息文本和用户ID
        text = body["event"].get("text", "")
        user_id = body["event"].get("user")
        channel_id = body["event"].get("channel")
        
        if not text or not user_id:
            return

        # 添加用户到存储，使用 channel_id 作为会话ID
        session_id = f"{user_id}_{channel_id}"
        add_user(user_id, {"userid": session_id})
        
        # 使用 AI 代理处理消息，传入session_id
        response = agent.run_agent(text, session_id)
        
        # 发送回复
        if response and "output" in response:
            say(text=response["output"])
        else:
            say(text="抱歉，我现在无法处理您的消息。")
        
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        say(text="抱歉，处理您的消息时出现了问题。")

def main():
    """启动 Slack 机器人"""
    try:
        # Start the app in Socket Mode
        handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
        logger.info("Starting Slack bot in Socket Mode...")
        handler.start()
    except Exception as e:
        logger.error(f"Failed to start Slack bot: {str(e)}")
        raise

if __name__ == "__main__":
    main() 