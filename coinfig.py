import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "your_token_here")
TEMP_DIR = "/tmp/telegram_bot"
FILE_SIZE_LIMIT = 50 * 1024 * 1024  # 50MB
SUPPORTED_MEDIA_FORMATS = ['image/jpeg', 'image/png', 'video/mp4', 'application/pdf']
