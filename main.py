import telebot
from telebot.types import Message

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7926513353:AAEy1uQy-pDSJQJ_gKcQjzqAZTmngrlrIAA')

# Контактные данные менеджера
manager_contact = (
    "**@TehnoViktor_Manager**"
)

# Сообщение предупреждения
warning_message = (
    "Здравствуйте 👋\n"
    "Спасибо за комментарий.\n\n"
    "Будьте осторожны, вам могут ответить мошенники.\n"
    "**Мы не берем предоплату за товар!**\n\n"
    "Наш менеджер: **@TehnoViktor_Manager**"
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
             f"Забанено пользователей: {statistics['users_banned']}")
        )

@bot.message_handler(func=lambda message: True)
def handle_message(message: Message):
    user_id = message.from_user.id
    text = message.text.lower()

    # Отправка приветственного сообщения при первом сообщении
    if user_id not in replied_users:
        bot.reply_to(message, warning_message)
        replied_users.add(user_id)
        statistics['messages_sent'] += 1
    elif "контакт" in text or "можно купить" in text:
        bot.reply_to(
            message,
            f"Здравствуйте, {message.from_user.first_name}, вот наши контактные данные:\n{manager_contact}"
        )
        statistics['messages_sent'] += 1

# Запуск бота
print("Бот запущен...")
bot.polling()
