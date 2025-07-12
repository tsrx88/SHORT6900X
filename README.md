# README.md

## 📦 SHORT6900X Bot

This is a simple Telegram bot that monitors new token listings from **Quanto (formerly Ox.Fun)** and sends alerts when a new token appears, including:
- Token name
- % pump from launch
- Time since listing
- Market cap

### 🚀 Features
- Automatic notifications for **new listings**
- Clean alert format for easy reading in Telegram
- Deployable on Railway for 24/7 uptime

### 🔧 Files included
- `short_6900x_bot.py` — Main bot logic
- `requirements.txt` — Dependencies
- `Procfile` — Railway worker definition
- `README.md` — Project overview

### ⚙️ Setup Instructions

1️⃣ **Clone repo:**
```bash
git clone https://github.com/YOUR_USERNAME/short6900x.git
cd short6900x
```

2️⃣ **Add config:**
- Edit `short_6900x_bot.py` and set your `BOT_TOKEN` and `CHAT_ID`.

3️⃣ **Push to Railway:**
- Make sure these files exist:
  - `requirements.txt`
  - `Procfile`
  - `short_6900x_bot.py`

4️⃣ **Deploy:**
- Link repo in [Railway](https://railway.app/)
- Add environment variables if needed
- Redeploy

### ⚠️ Notes
- Check Quanto API endpoint before running — the URL used is a placeholder.
- Bot scans every 5 minutes (adjustable).

### 📉 Suggested Shorting Strategy
The **SHORT6900X bot itself does not execute trades — it alerts you when a new meme coin is listed and how much it has pumped since launch.**

✅ Example manual shorting strategy:
- Look for tokens that have pumped **+100% to +500% in < 24 hours**
- Check market cap > $1M to ensure liquidity
- Monitor volume: short when momentum slows down (volume decreasing on lower timeframes)
- Enter short gradually to avoid volatility spikes
- Set tight stop-loss above recent high
- Target a 30–70% retracement on overextended pumps

The goal: **capitalize on meme coins that quickly overextend after launch, betting they’ll mean-revert as initial hype fades**. This strategy works because many new meme coins experience speculative hype right after listing, often pumping rapidly as early buyers rush in — but without fundamental value or sustained demand, these tokens tend to crash soon after. By shorting at or near the peak of this initial surge, traders aim to profit from the inevitable correction.

---

✅ **Support:**
Need help? DM Zara for assistance! 😎
