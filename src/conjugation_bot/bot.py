import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from src.utils.presente import presente
"""
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_conjugations(verb):
    pronouns = ["io", "tu", "lui","lei","noi","voi","loro","loro"]
    presente_arr = presente(verb)
    dict_res = {}
    for i in range(8):
        dict_res[pronouns[i]] = presente_arr[i]
    return dict_res

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Update in start:", update.to_dict())  # Отладочная информация
    web_app_url = "https://edgarsimonov.github.io/conjugationBot/"
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", web_app=WebAppInfo(url=web_app_url))]
    ]
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("handle_web_app_data triggered", update.to_dict())  # Отладка
    verb = update.message.web_app_data.data
    conjugations = get_conjugations(verb)
    response = f"Спряжение глагола '{verb}':\n\n"
    for person, form in conjugations.items():
        response += f"{person}: {form}\n"
    await update.message.reply_text(response)

async def debug_updates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("DEBUG UPDATE:", update.to_dict())
    # Не возвращаем ничего. В новой версии PTB возврат значения не влияет.

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Сначала отладчик (группа 0)
    app.add_handler(MessageHandler(filters.ALL, debug_updates), group=0)

    # Затем основной функционал (группа 1)
    app.add_handler(CommandHandler("start", start), group=1)
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data), group=1)

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
"""


import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, filters, Updater, CallbackContext

# Загрузка токена из .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)

@app.route("/", methods=["POST"])
def handle_webapp_request():
    data = request.json
    word = data.get("word", "")
    if word:
        return jsonify({"message": word})
    return jsonify({"error": "Слово не было предоставлено"}), 400

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Добро пожаловать в веб-приложение. Используй его для ввода слов!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Привет {update.message.text}")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
