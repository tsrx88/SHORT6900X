# SHORT6900X
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

---

✅ **Support:**
Need help? DM Zara for assistance! 😎
