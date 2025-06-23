from typing import Tuple, Dict, Any

def format_rr(price: float, sl: float, tp: float) -> str:
    try:
        risk = abs(price - sl)
        reward = abs(tp - price)
        rr = reward / risk if risk != 0 else 0
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
        leverage = data.get("leverage", 10)
        side = data.get("side", "").lower()

        rr_ratio = format_rr(price, stoploss, takeprofit)
        direction = "做多 🟢" if side == "buy" else "做空 🔴"
        lot_size = round(leverage / 10.0, 2)

        message = f"""🪙 XAUUSD 黃金訊號
📊 信心指數：{confidence} 分（RR：{rr_ratio}）
🔹 RSI：{rsi} 分 | MACD：{macd} 分 | KD：{kd} 分
🔹 MA：{ma} 分 | Bollinger：{bollinger} 分 | Fibonacci：{fib} 分

📌 方向：{direction}
💰 現價：{price}
🛡️ 止損：{stoploss}
🎯 止盈：{takeprofit}
📦 建議手數：{lot_size} 手
"""

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
            "lot_size": lot_size,
            "rr_ratio": rr_ratio,
            "side": side
        }

        return message, confidence, score_detail

class BTCStrategy(BaseStrategy):
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
        leverage = data.get("leverage", 10)
        side = data.get("side", "").lower()

        rr_ratio = format_rr(price, stoploss, takeprofit)
        direction = "做多 🟢" if side == "buy" else "做空 🔴"

        message = f"""🟠 BTCUSDT 比特幣訊號
📊 信心指數：{confidence} 分（RR：{rr_ratio}）
🔹 RSI：{rsi} 分 | MACD：{macd} 分 | KD：{kd} 分
🔹 MA：{ma} 分 | Bollinger：{bollinger} 分 | Fibonacci：{fib} 分

📌 方向：{direction}
💰 現價：{price}
🛡️ 止損：{stoploss}
🎯 止盈：{takeprofit}
⚖️ 槓桿建議：{leverage} 倍
"""

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
            "rr_ratio": rr_ratio,
            "side": side
        }

        return message, confidence, score_detail



STRATEGY_MAP = {
    "XAUUSD": XAUStrategy(),
    "BTCUSDT": BTCStrategy(),
}

def get_strategy(symbol: str):
    return STRATEGY_MAP.get(symbol.upper())
