from btc_strategy import evaluate_btc_strategy

def dispatch_strategy(data):
    symbol = data.get("symbol", "").upper()

    if symbol == "BTCUSDT":
        return evaluate_btc_strategy(data)
    
    return f"⚠️ 尚未支援的幣種：{symbol}", 0
