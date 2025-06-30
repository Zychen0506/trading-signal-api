import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from strategy_dispatcher import dispatch_strategy
from line_bot import send_line_message
from signal_logger import log_signal
from typing import Optional
from google_sheet_logger import append_trade_to_sheet
import json

app = FastAPI()

class SignalData(BaseModel):
    id: Optional[str] = None
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
async def webhook(request: Request):
    """
    這是 TradingView 用的端點
    接收原始純文字，通常為 JSON 字串格式
    """
    body = await request.body()
    raw_text = body.decode("utf-8")

    signal_type = "正式"
    
    # 預信號處理
    if raw_text.startswith("【預信號】"):
        signal_type = "預信號"
        raw_text = raw_text.replace("【預信號】", "")

    try:
        data = json.loads(raw_text)
        signal_data = SignalData(**data)
    except Exception as e:
        return {"status": "error", "message": f"格式錯誤：{e}"}

    # 分派策略並取得推播內容與分數細節
    message, confidence, score_detail = dispatch_strategy(signal_data.dict())

    # 發送 LINE 推播（只有正式信號才送）
    if signal_type == "正式" and confidence >= 80:
        user_id = os.environ.get("LINE_USER_ID")
        status, resp_text = send_line_message(user_id, message)
        print(f"LINE status: {status}, response: {resp_text}")

    # 寫入 Google Sheet（含 signal_type）
    append_trade_to_sheet(signal_data.dict(), confidence, score_detail, signal_type)

    return {
        "status": "received",
        "signal_type": signal_type,
        "confidence": confidence,
        "details": score_detail
    }

@app.post("/webhook-json")
async def webhook_json(signal_data: SignalData):
    """
    新增：提供 Swagger 文件用的端點
    可直接傳送 JSON 格式測試
    """
    # 分派策略並取得推播內容與分數細節
    message, confidence, score_detail = dispatch_strategy(signal_data.dict())

    # 發送 LINE 推播（只有正式信號才送）
    if confidence >= 80:
        user_id = os.environ.get("LINE_USER_ID")
        status, resp_text = send_line_message(user_id, message)
        print(f"LINE status: {status}, response: {resp_text}")

    # 寫入 Google Sheet（信號類型固定為 正式）
    append_trade_to_sheet(signal_data.dict(), confidence, score_detail, "正式")

    return {
        "status": "received",
        "signal_type": "正式",
        "confidence": confidence,
        "details": score_detail
    }
