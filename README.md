# Trading Signal System (Webhook + LINE)
## 使用方式
1. 安裝需求：`pip install -r requirements.txt`
2. 啟動：執行 `start_all.bat`
3. TradingView 設定：
   - Webhook URL: `http://你的伺服器IP:8000/webhook`
   - POST JSON 內容範例：
```json
{
  "symbol": "BTCUSDT",
  "price": 65432,
  "confidence": 95
}
```
4. LINE 官方帳號
   - 建立 Messaging API channel
   - 取得 Token 與你的個人 User ID，填入 config.py
