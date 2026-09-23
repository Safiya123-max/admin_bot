# **Telegram Admin & Roleplay Bot**

A feature-rich Telegram bot designed for group chat moderation and member engagement. Built with **Python 3.10+** and the **Aiogram 3.x** framework, featuring architectural middlewares for efficient permission management and request handling.

## **📌 Features**

### **🛡️ Moderation**

> * **/ban** — Ban a user from the chat (with an optional reason).  
> * **/mute** — Restrict a user's messaging permissions for a specified duration (e.g., /mute 10m or /mute 1h).  
> * **/warn** — Issue a warning to a user (warning tracking system).  
> * **/pin** — Pin a targeted message (requires admin rights).

### **🎭 Interactive / Roleplay (RP) Commands**

Commands can be triggered in reply to a target user's message:

> * **/hug** — Hug the selected user.  
> * **/kiss** — Kiss the selected user.  
> * **/hit** — Slap or hit the selected user playfully.

### **⚙️ Middlewares**

The bot incorporates custom middlewares for smooth execution flow:

> 1. **AdminCheckMiddleware** — Verifies administrator permissions before executing moderation commands.  
> 2. **LoggingMiddleware** — Logs all incoming commands and events.  
> 3. **ThrottlingMiddleware** — Rate-limiting and anti-flood protection.

## **📁 Project Structure**

.  
├── bot/  
│   ├── handlers/  
│   │   ├── admin.py       \# Moderation commands (ban, mute, warn, pin)  
│   │   ├── games.py       \# Roleplay commands (hug, kiss, hit)  
│   │   └── common.py      \# Basic commands (/start, /help)  
│   ├── middlewares/  
│   │   ├── admin\_check.py \# Admin rights verification  
│   │   └── throttling.py  \# Anti-flood middleware  
│   ├── config.py          \# Environment variables management (.env)  
│   └── loader.py          \# Bot and Dispatcher initialization  
├── .env.example           \# Example environment configuration  
├── main.py                \# Entry point  
├── requirements.txt       \# Project dependencies  
└── README.md

## **🚀 Quick Start**

### **1\. Clone the Repository**

git clone https://github.com/your-username/telegram-admin-bot.git  
cd telegram-admin-bot

### **2\. Set Up a Virtual Environment**

\# On Linux/macOS  
python3 \-m venv venv  
source venv/bin/activate

\# On Windows  
python \-m venv venv  
venv\\Scripts\\activate

### **3\. Install Dependencies**

pip install \-r requirements.txt

### **4\. Configure Environment Variables**

Create a .env file based on .env.example:  
cp .env.example .env

Fill in your bot details in .env:  
BOT\_TOKEN=1234567890:ABCdEfGhIjKlMnOpQrStUvWxYz  
ADMIN\_IDS=123456789,987654321

### **5\. Run the Bot**

python main.py

## **🛠️ Group Commands Reference**

| Command | Description | Example Usage |
| :---- | :---- | :---- |
| /ban | Ban a user (reply to message) | /ban Spamming |
| /mute \<duration\> | Mute a user (reply to message) | /mute 30m Rule violation |
| /warn | Issue a warning to a user | /warn Excessive caps |
| /pin | Pin a message (reply to message) | /pin |
| /hug | Hug a chat member | *(in reply)* /hug |
| /kiss | Kiss a chat member | *(in reply)* /kiss |
| /hit | Slap/hit a chat member | *(in reply)* /hit |

