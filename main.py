import os
from fastapi import FastAPI
from pydantic import BaseModel
from strategy_dispatcher import dispatch_strategy
from line_bot import send_line_message
from signal_logger import log_signal
from typing import Optional
from google_sheet_logger import append_trade_to_sheet

app = FastAPI()

class SignalData(BaseModel):
    symbol: str
    side: str
    price: float
    confidence: int
    stoploss: float
    takeprofit: float
    leverage: int
    rsi: Optional[int] = 0
    macd: Optional[int] = 0
    kd: Optional[int] = 0
    bollinger: Optional[int] = 0
    ma: Optional[int] = 0
    fib: Optional[int] = 0

@app.get("/")
def read_root():
    return {"message": "Trading Signal API is active."}

@app.post("/webhook")
async def webhook(data: SignalData):
    signal_data = data.dict()

    # 分派策略並取得推播內容與分數
    message, confidence, score_detail = dispatch_strategy(signal_data)

    # 若信心足夠，發送 LINE 推播
    if confidence >= 80:
        user_id = os.environ.get("LINE_USER_ID")
        status, resp_text = send_line_message(user_id, message)
        print(f"LINE status: {status}, response: {resp_text}")

    record_trade(signal_data, confidence, score_detail)
    append_trade_to_sheet(signal_data, confidence, score_detail)

    return {
        "status": "received",
        "confidence": confidence,
        "details": score_detail
    }
