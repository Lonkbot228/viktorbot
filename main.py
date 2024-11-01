import telebot
from telebot.types import Message

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7926513353:AAGLYjNWhKBvwPMNMFNIqeGO5yjOmeUb_1M')

# Контактные данные менеджера
manager_contact = (
    "<b>@TehnoViktor_Manager</b>"
)

# Сообщение предупреждения с использованием HTML
warning_message = (
    "Здравствуйте 👋\n"
    "Спасибо за комментарий.\n\n"
    "Будьте осторожны, вам могут ответить мошенники.\n"
    "<b>Мы не берем предоплату за товар!</b>\n\n"
    "Наш менеджер: <b>@TehnoViktor_Manager</b>"
)

# Словарь для отслеживания, кому отправлено приветственное сообщение
replied_users = set()

# Статистика
statistics = {
    "messages_sent": 0,
    "users_banned": 0
}

@bot.message_handler(commands=['stats'])
def send_stats(message: Message):
    if message.chat.type == "private" and message.from_user.username == "lonkigor":
        bot.send_message(
            message.chat.id,
            (f"Статистика бота:\n"
             f"Отправлено сообщений: {statistics['messages_sent']}\n"
             f"Забанено пользователей: {statistics['users_banned']}"),
            parse_mode="HTML"
        )

@bot.message_handler(func=lambda message: True)
def handle_message(message: Message):
    user_id = message.from_user.id
    text = message.text.lower()

    # Отправка приветственного сообщения при первом сообщении
    if user_id not in replied_users:
        bot.reply_to(message, warning_message, parse_mode="HTML")
        replied_users.add(user_id)
        statistics['messages_sent'] += 1
    elif "контакт" in text or "можно купить" in text:
        bot.reply_to(
            message,
            f"Здравствуйте, {message.from_user.first_name}, вот наши контактные данные:\n{manager_contact}",
            parse_mode="HTML"
        )
        statistics['messages_sent'] += 1

# Запуск бота
print("Бот запущен...")
bot.polling()

