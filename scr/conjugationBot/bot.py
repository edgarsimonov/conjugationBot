from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv
import os

load_dotenv()  # Загружаем переменные из .env

token = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, который помогает с спряжениями!")

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
