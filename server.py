from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8568478352:AAEEUdtCrlJBWVR6xD8bhL_2fpCgZ2I4W4c"
CHAT_ID = "7858998403"

@app.post("/webhook")
def webhook():
    data = request.json

    message = f"""
📢 *SINAL DETECTADO*

Ativo: {data.get('symbol')}
Direção: {data.get('signal')}
Timeframe: {data.get('time')}
    """

    send_telegram(message)
    return {"status": "ok"}

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
