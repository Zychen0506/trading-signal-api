import csv
import os
from datetime import datetime

CSV_FILE = "trade_records.csv"

def record_trade(data, confidence, score_detail):
    file_exists = os.path.isfile(CSV_FILE)
    fieldnames = [
        "timestamp", "symbol", "side", "price", "confidence", 
        "stoploss", "takeprofit", "leverage", "rr_ratio"
    ] + list(score_detail.keys())

    row = {
        "timestamp": datetime.now().isoformat(),
        "symbol": data["symbol"],
        "side": data["side"],
        "price": data["price"],
        "confidence": confidence,
        "stoploss": data["stoploss"],
        "takeprofit": data["takeprofit"],
        "leverage": data["leverage"],
        "rr_ratio": score_detail.get("rr_ratio", "-")
    }
    row.update(score_detail)

    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
