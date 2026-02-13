from telegram import Update
from telegram.ext import ContextTypes

async def handle_platform_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "telegram":
        text = "Send public channel/group URL for Telegram."
    else:
        text = "Send URL for other platform."
    
    await query.edit_message_text(text=text)
