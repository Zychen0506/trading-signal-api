# === strategies.py ===

from typing import Tuple, Dict, Any

# 策略基底類別
class BaseStrategy:
    def evaluate(self, data: Dict[str, Any]) -> Tuple[str, int, Dict[str, int]]:
        raise NotImplementedError("Each strategy must implement the evaluate method")

# === BTC 策略 ===
class BTCStrategy(BaseStrategy):
    def evaluate(self, data):
        price = data.get("price", 0)
        confidence = data.get("confidence", 0)
        rsi = data.get("rsi", 0)
        macd = data.get("macd", 0)
        kd = data.get("kd", 0)
        bollinger = data.get("bollinger", 0)
        ma = data.get("ma", 0)
        fib = data.get("fib", 0)

        message = f"🚀 BTCUSDT 比特幣訊號\n"
        message += f"📊 信心指數：{confidence} 分\n"
        message += f"RSI：{rsi} 分\nMACD：{macd} 分\nKD：{kd} 分\n"
        message += f"Bollinger：{bollinger} 分\nMA：{ma} 分\nFibonacci：{fib} 分\n"
        message += f"🎯 價格：{price}"

        score_detail = {
            "rsi": rsi,
            "macd": macd,
            "kd": kd,
            "bollinger": bollinger,
            "ma": ma,
            "fib": fib
        }

        return message, confidence, score_detail

# === XAU 策略 ===
class XAUStrategy(BaseStrategy):
    def evaluate(self, data):
        price = data.get("price", 0)
        confidence = data.get("confidence", 0)
        rsi = data.get("rsi", 0)
        macd = data.get("macd", 0)
        kd = data.get("kd", 0)
        bollinger = data.get("bollinger", 0)
        ma = data.get("ma", 0)
        fib = data.get("fib", 0)

        message = f"🪙 XAUUSD 黃金訊號\n"
        message += f"📊 信心指數：{confidence} 分\n"
        message += f"RSI：{rsi} 分\nMACD：{macd} 分\nKD：{kd} 分\n"
        message += f"Bollinger：{bollinger} 分\nMA：{ma} 分\nFibonacci：{fib} 分\n"
        message += f"🎯 價格：{price}"

        score_detail = {
            "rsi": rsi,
            "macd": macd,
            "kd": kd,
            "bollinger": bollinger,
            "ma": ma,
            "fib": fib
        }

        return message, confidence, score_detail

# === 註冊中心 ===
STRATEGY_MAP = {
    "BTCUSDT": BTCStrategy(),
    "XAUUSD": XAUStrategy(),
}

def get_strategy(symbol: str):
    return STRATEGY_MAP.get(symbol.upper())
