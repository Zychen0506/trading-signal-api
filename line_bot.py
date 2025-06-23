import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 初始化 LineBotApi
line_bot_api = LineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))

def send_line_message(user_id: str, message: str):
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text=message)
    )
    return 200, "OK"
