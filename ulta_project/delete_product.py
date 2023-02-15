import sqlite3 as sl
import telebot

def delete_link(product_id):

    token = "5986648960:AAEzdmh31o4FwtBr7tYywiLKzH8GJ6soaGU"
    bot=telebot.TeleBot(token)

    connect = sl.connect('ulta.db')
    cur = connect.cursor()
    cur.execute("SELECT name FROM ulta WHERE id=?", (product_id,))
    name = str(cur.fetchone()[0])
    cur.execute("DELETE FROM ulta WHERE id=?", (product_id,))

    item_deleted = str(name) + " was removed"
    bot.send_message("373068554", item_deleted) 

    connect.commit()
    cur.close()