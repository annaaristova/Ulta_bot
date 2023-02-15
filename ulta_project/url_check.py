import requests
from bs4 import BeautifulSoup
import json
import telebot
import sqlite3 as sl


def product_check(user_url):
    token = "5986648960:AAEzdmh31o4FwtBr7tYywiLKzH8GJ6soaGU"
    bot=telebot.TeleBot(token)

    url_parser(user_url)
    name = url_parser(user_url)[1]
    price = url_parser(user_url)[0]
    image = url_parser(user_url)[2]

    product_id = user_url.partition("prod")
    product_id = product_id[2]


    connect = sl.connect('ulta.db')
    cur = connect.cursor()

    add = "INSERT INTO ulta (id, image, url, name, price) VALUES(?, ?, ?, ?, ?)"
    cur.execute(add, (product_id, image, user_url, name, price))
    new_item_added = "New item " + str(name) + " is added " + str(user_url)
    bot.send_message("373068554", new_item_added) 

    connect.commit()
    cur.close()

def url_parser(user_url):

    try:
        user_url_html = requests.get(user_url)

        ulta_soup_html = BeautifulSoup(user_url_html.text, 'html.parser')

        image_path = ulta_soup_html.find(class_="MediaWrapper__Image_img")
        image = image_path.get("src")

        product_container = ulta_soup_html.find_all(type="application/ld+json")

        product_container = product_container[1]
        product_container = product_container.get_text()

        json_file = json.loads(product_container)

        name = json_file["name"]

        price = json_file["offers"]["price"]

        return price, name, image
    
    except IndexError:
        message = "The link doesn't work\n" + str(user_url)
        bot.send_message("373068554", message) 
        return print("The link doesn't work")

