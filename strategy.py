from datetime import datetime

def should_send_signal(data):
    # 模擬策略：當 RSI < 30 就發出 Buy，信心 90
    message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 訊號：BUY {data.get('symbol', '???')} @ {data.get('price', '???')}"
    confidence = data.get('confidence', 90)
    return message, confidence
