import telebot

token = ""

def tele(message):
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id="", text=message)


tele("Hello World")