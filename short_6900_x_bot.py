# SHORT6900X: Short Squeeze Scanner Bot for Telegram
# ================================================
# Scans low-float stocks with high short interest and volume surges
# Sends 3x/day alerts to Telegram with squeeze alerts

import requests
import pandas as pd
from datetime import datetime
import time

# --- USER CONFIG ---
TELEGRAM_TOKEN = "7890317349:AAFubUqZ8WhnYdcKJ8H-hsYCTBKN8a8UDi0"
TELEGRAM_CHAT_ID = "7890317349:AAFubUqZ8WhnYdcKJ8H-hsYCTBKN8a8UDi0"
MAX_ALERTS_PER_RUN = 5
ALERT_TIMES = ["09:00", "12:00", "15:00"]

# --- MOCK DATA (Replace with real API later) ---
stocks = [
    {"ticker": "HUDI", "float": 2.8, "short_float": 29, "volume": 3200000, "avg_volume": 700000, "price": 4.21, "market_cap": 95, "last_alerted": None},
    {"ticker": "TOP", "float": 0.9, "short_float": 34, "volume": 1800000, "avg_volume": 500000, "price": 6.40, "market_cap": 70, "last_alerted": None},
    {"ticker": "JZXN", "float": 3.0, "short_float": 42, "volume": 5300000, "avg_volume": 900000, "price": 2.87, "market_cap": 55, "last_alerted": None},
    {"ticker": "BRSH", "float": 6.2, "short_float": 24, "volume": 1600000, "avg_volume": 600000, "price": 1.95, "market_cap": 40, "last_alerted": None},
    {"ticker": "XYZ", "float": 4.2, "short_float": 18, "volume": 900000, "avg_volume": 700000, "price": 3.20, "market_cap": 30, "last_alerted": None}
]

# --- SEND ALERT TO TELEGRAM ---
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# --- FORMAT ALERT ---
def format_alert(stock):
    float_tag = "🧨 Ultra Low Float" if stock["float"] < 1 else "🔥 Very Low Float" if stock["float"] <= 5 else "✅ Low Float"
    float_rotated = round(stock["volume"] / (stock["float"] * 1_000_000), 1)
    alert = f"\n🧨 *Squeeze Alert*: ${stock['ticker']}\n"
    alert += f"{float_tag} ({stock['float']}M)\n"
    alert += f"📈 Short Float: {stock['short_float']}%\n"
    alert += f"💥 Volume: {stock['volume']:,} (avg {stock['avg_volume']:,})\n"
    alert += f"🔁 Float Rotation: {float_rotated}x\n"
    alert += f"💰 Price: ${stock['price']} | Cap: ${stock['market_cap']}M"
    if float_rotated > 3:
        alert += f"\n⚠️ *Warning*: Float rotated {float_rotated}x — squeeze may exhaust soon"
    return alert

# --- MAIN SCANNER FUNCTION ---
def run_scanner():
    now = datetime.now().strftime("%H:%M")
    if now not in ALERT_TIMES:
        return

    alerts = []
    for stock in stocks:
        if stock["float"] <= 10 and stock["short_float"] > 20 and stock["volume"] > 2 * stock["avg_volume"]:
            alerts.append(stock)

    alerts = sorted(alerts, key=lambda x: x["short_float"], reverse=True)[:MAX_ALERTS_PER_RUN]

    if alerts:
        send_telegram(f"📡 *SHORT6900X Scanner* — {now} Update")
        for stk in alerts:
            send_telegram(format_alert(stk))

# --- ENTRY POINT ---
if __name__ == "__main__":
    run_scanner()
