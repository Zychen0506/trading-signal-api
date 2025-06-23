from fastapi import FastAPI
from pydantic import BaseModel
from strategy_dispatcher import dispatch_strategy
from line_bot import send_line_message
from signal_logger import log_signal
from typing import Optional

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

    # 分派策略與計算
    message, confidence, score_detail = dispatch_strategy(signal_data)

    # 發送通知（使用 LINE Messaging API）
    if confidence >= 80:
        status, resp_text = send_line_message(os.environ.get("LINE_USER_ID"), message)
        print(f"LINE status: {status}, response: {resp_text}")  # 可以協助 debug

    # 記錄訊號
    log_signal(signal_data, confidence)

    return {
        "status": "received",
        "confidence": confidence,
        "details": score_detail
    }
