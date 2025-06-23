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
    fib: Optional[int] = 0  # 有些策略可能包含斐波納契，保留欄位

@app.get("/")
def read_root():
    return {"message": "Trading Signal API is active."}

@app.post("/webhook")
async def webhook(data: SignalData):
    signal_data = data.dict()

    # 根據 symbol 分派策略 + 回傳 LINE 訊息 + 分數
    message, confidence = dispatch_strategy(signal_data)

    # 若信心分數達門檻則推送 LINE
    if confidence >= 80:
        send_line_message(message)

    # 儲存訊號與分析
    log_signal(signal_data, confidence)

    return {"status": "received", "confidence": confidence}
