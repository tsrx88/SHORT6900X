# === SHORT6900X BOT ===
# Minimal working starter code

import time
import requests
from datetime import datetime
from telegram import Bot

# === CONFIG ===
BOT_TOKEN = "7890317349:AAFubUqZ8WhnYdcKJ8H-hsYCTBKN8a8UDi0"
CHAT_ID = "1274696171"
SCAN_INTERVAL = 300  # 5 minutes

# === SCRAPER ===
QUANTO_LISTINGS_URL = "https://api.quanto.fun/v1/listings"  # Example, inspect network to confirm actual endpoint

last_seen_tokens = set()

def get_new_listings():
    try:
        resp = requests.get(QUANTO_LISTINGS_URL)
        data = resp.json()
        listings = []
        for token in data.get('tokens', []):
            symbol = token.get('symbol')
            token_id = token.get('id')
            if token_id not in last_seen_tokens:
                last_seen_tokens.add(token_id)
                listings.append({
                    'symbol': symbol,
                    'price': float(token.get('current_price', 0)),
                    'initial_price': float(token.get('initial_price', 0)),
                    'market_cap': float(token.get('market_cap', 0)),
                    'listed_at': datetime.fromtimestamp(token.get('listed_at', time.time())),
                })
        return listings
    except Exception as e:
        print(f"Error fetching listings: {e}")
        return []

# === FORMAT MESSAGE ===
def format_message(token):
    pct_change = 0
    if token['initial_price'] > 0:
        pct_change = ((token['price'] - token['initial_price']) / token['initial_price']) * 100
    
    time_since = datetime.utcnow() - token['listed_at']
    minutes_since = int(time_since.total_seconds() // 60)

    mc_text = f"Market Cap: ${token['market_cap'] / 1_000_000:.2f}M" if token['market_cap'] else "Market Cap: N/A"

    return (
        f"⚡️ NEW LISTING on Quanto\n"
        f"Token: ${token['symbol']}\n"
        f"Pump: {pct_change:.2f}% 🚀\n"
        f"Time since listing: {minutes_since}m\n"
        f"{mc_text}"
    )

# === MAIN LOOP ===
bot = Bot(token=BOT_TOKEN)

while True:
    new_tokens = get_new_listings()
    for token in new_tokens:
        msg = format_message(token)
        bot.send_message(chat_id=CHAT_ID, text=msg)
        print(f"Sent alert for {token['symbol']}")
    time.sleep(SCAN_INTERVAL)
