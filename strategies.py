from typing import Tuple, Dict, Any

def format_rr(tp: float, sl: float) -> str:
    try:
        rr = abs((tp - sl) / (sl - tp)) if tp != sl else 0
        return f"1:{round(rr, 2)}"
    except:
        return "-"

class BaseStrategy:
    def evaluate(self, data: Dict[str, Any]) -> Tuple[str, int, Dict[str, Any]]:
        raise NotImplementedError

class XAUStrategy(BaseStrategy):
    def evaluate(self, data):
        price = data.get("price", 0)
        confidence = data.get("confidence", 0)
        stoploss = data.get("stoploss", 0)
        takeprofit = data.get("takeprofit", 0)
        rsi = data.get("rsi", 0)
        macd = data.get("macd", 0)
        kd = data.get("kd", 0)
        bollinger = data.get("bollinger", 0)
        ma = data.get("ma", 0)
        fib = data.get("fib", 0)
        leverage = data.get("leverage", 0)

        rr_ratio = format_rr(takeprofit, stoploss)

        message = f"\n🪙 XAUUSD 黃金訊號\n"
        message += f"📊 信心指數：{confidence} 分（RR：{rr_ratio}）\n"
        message += f"🔹 RSI：{rsi} 分\n🔹 MACD：{macd} 分\n🔹 KD：{kd} 分\n"
        message += f"🔹 MA：{ma} 分\n🔹 Bollinger：{bollinger} 分\n🔹 Fibonacci：{fib} 分\n"
        message += f"💰 現價：{price}\n🛡️ 止損：{stoploss}\n🎯 止盈：{takeprofit}\n⚖️ 槓桿建議：{leverage} 倍"

        score_detail = {
            "rsi": rsi,
            "macd": macd,
            "kd": kd,
            "bollinger": bollinger,
            "ma": ma,
            "fib": fib,
            "stoploss": stoploss,
            "takeprofit": takeprofit,
            "leverage": leverage,
            "rr_ratio": rr_ratio
        }

        return message, confidence, score_detail

class BTCStrategy(BaseStrategy):
    def evaluate(self, data):
        # 專屬邏輯（略）
        return "BTC 訊號尚未實作", 0, {}

STRATEGY_MAP = {
    "XAUUSD": XAUStrategy(),
    "BTCUSDT": BTCStrategy(),
}

def get_strategy(symbol: str):
    return STRATEGY_MAP.get(symbol.upper())
