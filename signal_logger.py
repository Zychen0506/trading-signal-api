import csv
from datetime import datetime

def log_signal(data, confidence):
    with open("signals.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data.get("symbol", "???"),
            data.get("price", "???"),
            confidence
        ])
