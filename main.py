import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello, World!")


@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text.lower() == "привет".lower():
        bot.send_message(message.chat.id, "Пока")
    elif message.text.lower() == "пока".lower():
        bot.send_message(message.chat.id, "бот не в сети")
    elif message.text.lower() == "как дела?".lower():
        bot.send_message(message.chat.id, "у меня нет дел")
    else:
        bot.send_message(message.chat.id, f"я не знаю как ответить на <b>'{message.text}'</b>", parse_mode='html')


bot.infinity_polling()






