from fastapi import FastAPI, Request
from pydantic import BaseModel
from strategy import should_send_signal
from line_bot import send_line_message
from signal_logger import log_signal

app = FastAPI()

# === 定義訊號資料格式 ===
class SignalData(BaseModel):
    symbol: str
    side: str
    price: float
    confidence: int
    stoploss: float
    takeprofit: float
    leverage: int

# === 接收 Webhook 訊號 ===
@app.post("/webhook")
async def webhook(data: SignalData):
    message, confidence = should_send_signal(data.dict())

    if confidence >= 80:
        send_line_message(message)

    log_signal(data.dict(), confidence)
    return {"status": "received"}
