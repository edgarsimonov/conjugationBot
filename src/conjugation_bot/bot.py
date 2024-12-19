import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from src.utils.presente import presente
# Загружаем переменные окружения
load_dotenv()

# Получаем токен из .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Функция для получения спряжений (замените своей логикой)
def get_conjugations(verb):
    # Пример функции (замените своей логикой)
    pronouns = ["io", "tu", "lui","lei","noi","voi","loro","loro"]
    presente_arr = presente(verb)
    dict = {}
    for i in range(8):
        dict[pronouns[i]] = presente_arr[i]
    return dict


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app_url = "https://edgarsimonov.github.io/conjugationBot/"
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", web_app=WebAppInfo(url=web_app_url))]
    ]
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Обработчик данных из Web App
async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    verb = update.message.web_app_data.data  # Получаем данные из Web App
    conjugations = get_conjugations(verb)   # Генерируем спряжение

    # Формируем ответ
    response = f"Спряжение глагола '{verb}':\n\n"
    for person, form in conjugations.items():
        response += f"{person}: {form}\n"

    # Отправляем ответ пользователю
    await update.message.reply_text(response)


# Настройка бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))  # Для команды /start
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))  # Для данных из Web App

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()


if __name__ == "__main__":
    main()
