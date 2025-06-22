from fastapi import FastAPI, Request
from strategy import should_send_signal
from line_bot import send_line_message
from signal_logger import log_signal

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message, confidence = should_send_signal(data)

    if confidence >= 80:
        send_line_message(message)
    log_signal(data, confidence)
    return {"status": "received"}
