def evaluate_xau_strategy(signal_data):
    price = float(signal_data.get("price", 0))
    side = signal_data.get("side", "").lower()
    confidence = int(signal_data.get("confidence", 0))
    stoploss = float(signal_data.get("stoploss", 0))
    takeprofit = float(signal_data.get("takeprofit", 0))
    leverage = int(signal_data.get("leverage", 10))

    rsi = int(signal_data.get("rsi", 0))
    macd = int(signal_data.get("macd", 0))
    kd = int(signal_data.get("kd", 0))
    bollinger = int(signal_data.get("bollinger", 0))
    ma = int(signal_data.get("ma", 0))

    total_score = rsi + macd + kd + bollinger + ma

    message = f"🪙 XAUUSD 黃金訊號\n"
    message += f"📊 信心指數：{confidence} 分\n"
    message += f"RSI：{rsi} 分\n"
    message += f"MACD：{macd} 分\n"
    message += f"KD：{kd} 分\n"
    message += f"Bollinger：{bollinger} 分\n"
    message += f"MA Crossover：{ma} 分\n"
    message += f"🎯 價格：{price}\n"
    message += f"🛡️ 止損：{stoploss}\n"
    message += f"🎁 止盈：{takeprofit}\n"
    message += f"📈 槓桿：{leverage} 倍"

    return message
