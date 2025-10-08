# main.py
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram bot tokenini muhit o'zgaruvchisidan olish
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Veb-ilovangizning URL manzili (muhit o'zgaruvchisidan olinadi)
WEB_APP_URL = os.environ.get("WEB_APP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not WEB_APP_URL:
        await update.message.reply_text("Veb-ilovaning URL manzili sozlanmagan. Iltimos, administratorga murojaat qiling.")
        return # <-- Mana bu yerda alohida qator bo'lishi kerak edi.
    
    # Endi bu qatorlar 'if' blokidan tashqarida va 'start' funksiyasi ichida to'g'ri indentsiya qilingan.
    keyboard = [
        [InlineKeyboardButton("Kod Muharriri", web_app=WebAppInfo(url=WEB_APP_URL))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Assalomu alaykum! Kod yozish va bajarish uchun quyidagi tugmani bosing:",
        reply_markup=reply_markup
    )

def main() -> None:
    if not TOKEN:
        print("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi o'rnatilmagan. Bot ishga tusha olmaydi.")
        return # <-- Mana bu yerda ham alohida qator bo'lishi kerak edi.
    
    # Endi bu qatorlar 'main' funksiyasi ichida to'g'ri indentsiya qilingan.
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

# Bu qism ham __name__ bilan to'g'ri yozilishi kerak.
if __name__ == "__main__":
    main()
    
