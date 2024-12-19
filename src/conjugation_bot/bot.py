import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from flask import Flask, request, jsonify
from src.utils.presente import presente

# Загружаем переменные окружения
load_dotenv()

# Бот токен
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Telegram bot setup
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app_url = "https://edgarsimonov.github.io/conjugationBot/"
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", web_app=WebAppInfo(url=web_app_url))]
    ]
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Flask app setup (для обработки запросов от Web App)
flask_app = Flask(__name__)

# Пример функции для спряжения глагола
def get_conjugations(verb):
    # Пример функции (замените своей логикой)
    pronouns = ["io", "tu", "lui","lei","noi","voi","loro","loro"]
    presente_arr = presente(verb)
    dict = {}
    for i in range(8):
        dict[pronouns[i]] = presente_arr[i]
    return dict

# Маршрут для обработки запросов от Web App
@flask_app.route('/conjugate', methods=['GET'])
def conjugate():
    verb = request.args.get('verb', '')
    if not verb:
        return jsonify({"error": "No verb provided"}), 400

    conjugations = get_conjugations(verb)
    return jsonify(conjugations)

if __name__ == "__main__":
    import threading

    # Запускаем Flask и Telegram bot параллельно
    threading.Thread(target=flask_app.run, kwargs={"port": 5000}).start()
    app.run_polling()
