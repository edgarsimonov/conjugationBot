import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загружаем переменные из .env
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ссылка на ваш Telegram Web App
    web_app_url = "https://edgarsimonov.github.io/conjugationBot/"

    # Создаём кнопку с Web App
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть Web App:",
        reply_markup=reply_markup
    )


# Главная функция для запуска бота
def main():
    # Создаём приложение Telegram
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()


# Запуск бота
if __name__ == "__main__":
    main()

