


token = "5986648960:AAEzdmh31o4FwtBr7tYywiLKzH8GJ6soaGU"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def telegram_bot_welcome(message):
    bot.reply_to(message, 'Welcome to ulta sale bot')
    chatId = message.chat.id
    print(chatId)
bot.polling()





import sqlite3 as sl

def delete_link(user_url):
    connect = sl.connect('ulta.db')
    cur = connect.cursor()
    delete = """DELETE from ulta"""
    cur.execute(delete)
    connect.commit()
    cur.close()




