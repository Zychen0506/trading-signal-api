def evaluate_btc_strategy(data):
    symbol = data.get("symbol")
    price = float(data.get("price"))

    # 模擬指標狀況（正式版可接 TradingView Data API or Binance API）
    rsi = 28
    macd_cross = True
    macd_histogram_positive = True
    k = 32
    d = 29
    bollinger_position = "lower_band"
    ma5 = 65200
    ma20 = 65000
    is_fibonacci_zone = True

    score = 0
    components = []

    # RSI 評分
    if rsi < 30:
        score += 18
        components.append(("RSI", 18))
    elif rsi < 40:
        score += 10
        components.append(("RSI", 10))
    else:
        components.append(("RSI", 0))

    # MACD 評分
    if macd_cross:
        macd_score = 12
        if macd_histogram_positive:
            macd_score += 5
        score += macd_score
        components.append(("MACD", macd_score))
    else:
        components.append(("MACD", 0))

    # KD 評分
    if k > d and k < 50:
        score += 12
        components.append(("KD", 12))
    else:
        components.append(("KD", 0))

    # 布林通道位置
    if bollinger_position == "lower_band":
        score += 10
        components.append(("Bollinger", 10))
    else:
        components.append(("Bollinger", 0))

    # 均線
    if ma5 > ma20:
        score += 10
        components.append(("MA Crossover", 10))
    else:
        components.append(("MA Crossover", 0))

    # 斐波那契區域
    if is_fibonacci_zone:
        score += 20
        components.append(("Fibonacci", 20))
    else:
        components.append(("Fibonacci", 0))

    # 總結訊息文字
    msg_lines = [f"🚀 {symbol} 買進訊號", f"📊 信心指數：{score} 分"]
    for comp, pts in components:
        msg_lines.append(f"{comp}：{pts} 分")
    msg_lines += [
        f"🎯 價格：{price}",
        f"🛡️ 止損：{data.get('stoploss')}",
        f"🎁 止盈：{data.get('takeprofit')}",
        f"📈 槓桿：{data.get('leverage')} 倍"
    ]
    message = "\n".join(msg_lines)

    return message, score
