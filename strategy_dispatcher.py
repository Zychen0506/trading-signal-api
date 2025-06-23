from strategies import get_strategy

def dispatch_strategy(data):
    symbol = data["symbol"].upper()
    strategy = get_strategy(symbol)

    if strategy:
        return strategy.evaluate(data)
    else:
        return (f"⚠️ 不支援的交易對：{symbol}", 0, {})
