import requests

url = "http://127.0.0.1:8000/webhook"
payload = {
    "symbol": "BTCUSDT",
    "price": 65555,
    "confidence": 90
}
res = requests.post(url, json=payload)
print("回應：", res.status_code, res.text)
