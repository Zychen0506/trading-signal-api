from btc_strategy import evaluate_btc_strategy
from xau_strategy import evaluate_xau_strategy

def dispatch_strategy(data):
    symbol = data["symbol"].upper()

    if symbol == "BTCUSDT":
        return evaluate_btc_strategy(data)
    elif symbol == "XAUUSD":
        return evaluate_xau_strategy(data)
    else:
        return (f"⚠️ 不支援的交易對：{symbol}", 0)
