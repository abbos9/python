import telebot
from aiogram import executor
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
users = []


@bot.message_handler()
def ON_message(message):
    print(message)
    bot.send_message(message.from_user.id, message.text)
    users.append(message.from_user.id)


executor.start_polling(sk=True)
