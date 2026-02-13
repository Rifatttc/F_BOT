# Update Termux packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install git (for cloning)
pkg install git

# Clone or create project directory
mkdir telegram_bot && cd telegram_bot

# Install dependencies
pip install -r requirements.txt

# Configure bot token
nano .env  # Add BOT_TOKEN=your_token_here

# Run bot
python bot.py

# Run in background (optional)
nohup python bot.py &
