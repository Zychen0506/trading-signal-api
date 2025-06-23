import requests
import os

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

def send_line_message(user_id: str, message: str):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"
    }
    payload = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code, response.text
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
