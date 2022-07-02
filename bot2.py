import telebot

token = ""

bot = telebot.TeleBot(token)

HELP = """
help - Вывести список доступных команд.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня"""

@bot.message_handler(commands=["help"]
def help(message):
    bot.send_message(message.chat.id, HELP)



bot.polling(none_stop=True)