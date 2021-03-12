import telebot
import requests
import time
from telebot import types
#bot TOKEN
bot = telebot.TeleBot(TOKEN)
#get my ip
_ip = requests.get('https://ip.beget.ru').text
#bot start
@bot.message_handler(commands = ['start'])
def startmessage(message):
	bot.send_message(message.chat.id,"<b>Создатель - @johnma188\nЛичный блог - @oempsm</b>",parse_mode = 'html')	

	bot.send_message(message.chat.id,"/start — начать"+
		"\n/search_ip - получаем информацию IP-адреса"+
		"\n/my_ip - получаем свой IP-адрес ")
#take user ip
@bot.message_handler(commands = ['search_ip'])
def ipinfo(message):
	sent = bot.send_message(message.chat.id,"Send IP")
	bot.register_next_step_handler(sent, hello)
#doesn't working
@bot.message_handler(commands = ['my_ip'])
def ipinfo(message):
	bot.send_message(message.chat.id,"Your IP-address "+_ip)

#searching some info about this ip
def hello(message):
	try:
		ip = message.text
		bot.send_message(message.chat.id,"Searching... "+ip)
		time.sleep(3)

		data = requests.get('http://ip-api.com/json/' + ip).json()
		bot.send_message(message.chat.id,"IP-Information:\n\n"+"Country: "+data["country"]+"\nCity: "+data["city"]+
			"\nCountry Code: "+data["countryCode"]+"\nRegion: "+data["region"]+"\nRegion Name:"+data["regionName"]+
			"\nISP: "+data["isp"]+
			"\nORG: "+data["org"]+
			"\nAS: "+data["as"]+
			"\nIP: "+data["query"]+
			"\n\nISP - Интернет-провайдер"+
			"\nORG - общий домен верхнего уровня"+
			"\nIP - Internet Protocol"+
			"\n\nОбратите внимание, что узнать местоположение по IP можно только с точностью до города.")

	except Exception as e:
		bot.send_message(message.chat.id,'incorrect ip address correct and send again')
		bot.send_message(message.chat.id,"/start — начать"+
		"\n/search_ip - получаем информацию для IP-адреса"+
		"\n/my_ip - получаем свой IP-адрес ")
#THAT'S SHIT 
@bot.message_handler(content_types = ['text'])
def madinaspam(message):
	try:
		a = 20
		if message.text.lower() == "мадина" or message.text.lower() == "madina":
			listm = ["УМРИ СУКА!!!","УМРИ!!!!!","СУКА BLEEED"]
			while 0<a:
				a-=1
				print(a)
				for item in listm:
					bot.send_message(message.chat.id,item)
			bot.send_message(message.chat.id,"Умер?Вот и отлично")
			bot.send_message(message.chat.id,"/start — начать"+
			"\n/search_ip - получаем информацию IP-адреса"+
			"\n/my_ip - получаем свой IP-адрес ")

	except Exception as e:
		bot.send_message(message.chat.id,"Умер?")

if __name__ == '__main__':
  bot.polling(none_stop=True)