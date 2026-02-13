# Telegram Media Downloader Bot Template

## Project Structure

telegram_downloader_bot/ ├── bot.py ├── config.py ├── handlers/ │ ├── init.py │ ├── start_handler.py │ └── callback_handler.py ├── downloaders/ │ ├── init.py │ ├── telegram_downloader.py │ └── public_api_downloader.py ├── utils/ │ ├── init.py │ ├── file_handler.py │ └── validators.py ├── requirements.txt └── README.md

# Update Termux packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install git (for cloning)
pkg install git

# Clone or create project directory
cd ~
git clone https://github.com/Rifatttc/T-Bot.git
mkdir telegram_bot && cd telegram_bot

# Install dependencies
pip install -r requirements.txt

# Configure bot token
nano .env  # Add BOT_TOKEN=your_token_here

# Run bot
python bot.py

# Run in background (optional)
nohup python bot.py &

START
  ↓
User sends /start
  ↓
Bot displays: "Choose platform: [Telegram Public] [Other Platform]"
  ↓
User clicks button
  ↓
Bot: "Send public channel/group URL"
  ↓
User sends URL
  ↓
Bot validates URL → [Invalid] → Error message → Return to menu
  ↓ [Valid]
Bot checks accessibility → [Private/Restricted] → Error: "Content is private" → Return to menu
  ↓ [Public]
Bot: "Downloading... ⏳"
  ↓
Download media → [Success] → Send to user → Cleanup temp files → Done
  ↓ [Failure]
Error message → Return to menu

