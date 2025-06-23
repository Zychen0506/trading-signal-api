import requests
from config import LINE_CHANNEL_ACCESS_TOKEN

def send_line_message(message: str):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"
    }
    payload = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code
