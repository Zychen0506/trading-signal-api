import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def append_trade_to_sheet(data, confidence, score_detail):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("Trading Records").sheet1 

        row = [
            datetime.now().isoformat(),
            data["symbol"],
            data["side"],
            data["price"],
            confidence,
            data["stoploss"],
            data["takeprofit"],
            data["leverage"],
            score_detail.get("rr_ratio", "-"),
            score_detail.get("rsi", 0),
            score_detail.get("macd", 0),
            score_detail.get("kd", 0),
            score_detail.get("bollinger", 0),
            score_detail.get("ma", 0),
            score_detail.get("fib", 0),
        ]

        sheet.append_row(row, value_input_option="USER_ENTERED")
        print("[google_sheet_logger] ✅ 成功寫入 Google Sheet")

    except Exception as e:
        print(f"[google_sheet_logger] ❌ 寫入失敗：{e}")
