import requests
import telebot
from config import TOKEN, APPID

bot = telebot.TeleBot(TOKEN)
btn = telebot.types.ReplyKeyboardMarkup(True, True)
btn.row("Погода на сегодня")
current_city = ""

def check_weather(city):
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={
                           'q': f'{city}, RU',
                           'units': 'metric',
                           'lang': 'RU',
                           'APPID': APPID})
    data = res.json()
    return f"Температура сегодня: {data['main']['temp']}, {data['weather'][0]['description']}"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Введите город")


@bot.message_handler(content_types=['text'])
def send_text(message):
    
    if message.text == "Погода на сегодня":
        bot.send_message(message.chat.id, check_weather("Иваново"))
        return
    city = message.text.lower().title()
    bot.send_message(message.chat.id, check_weather(city), reply_markup=btn)


bot.polling()


