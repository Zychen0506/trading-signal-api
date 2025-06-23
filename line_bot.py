from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# 從環境變數抓 token
line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))

def send_line_message(user_id: str, message: str):
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text=message)
    )
