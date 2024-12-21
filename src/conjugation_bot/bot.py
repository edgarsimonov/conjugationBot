import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from telegram import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from src.utils.presente import presente


# Загрузка токена
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Flask-приложение
app = Flask(__name__)

@app.route("/conjugate", methods=["POST"])
def conjugate():
    data = request.json
    verb = data.get("verb")
    if not verb:
        return jsonify({"error": "Глагол не указан"}), 400

    # Спрягаем глагол
    conjugation = presente(verb)
    return jsonify(conjugation)

# Обработчик команды /start для Telegram
async def start(update: ContextTypes.DEFAULT_TYPE, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Открыть Web App", web_app=WebAppInfo(url="https://edgarsimonov.github.io/conjugationBot/"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:", reply_markup=reply_markup
    )

def run_telegram_bot():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    from threading import Thread

    # Запускаем Flask и Telegram-бота в отдельных потоках
    Thread(target=run_telegram_bot).start()
    app.run(port=5000)
