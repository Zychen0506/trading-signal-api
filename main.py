from fastapi import FastAPI
from pydantic import BaseModel
from strategy_dispatcher import dispatch_strategy
from line_bot import send_line_message
from signal_logger import log_signal

app = FastAPI()

class SignalData(BaseModel):
    symbol: str
    side: str
    price: float
    confidence: int
    stoploss: float
    takeprofit: float
    leverage: int

@app.post("/webhook")
async def webhook(data: SignalData):
    signal_data = data.dict()
    
    # 策略分派 + 得分
    message, confidence = dispatch_strategy(signal_data)

    # 如果信心值高於門檻就發送
    if confidence >= 80:
        send_line_message(message)

    # 紀錄訊號
    log_signal(signal_data, confidence)

    return {"status": "received"}
