import ConfigParser
import json
import requests
import telegram

#istruzioni telegram wrapper https://python-telegram-bot.org/

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')
instructionPrevisioniMeteo = config.get('grabber', 'instructionPrevisioniMeteo')
endPointGrabberService = config.get('grabber', 'endPointGrabberService')
telegramTokenBot = config.get('telegram', 'tokenBot')
telegramChatId_1 = config.get('telegram', 'chatId_1')
telegramChatId_2 = config.get('telegram', 'chatId_2')
#regular expressione per machare i numeri con la virgola

#prepare data for call grabber
response=requests.get(endPointGrabberService,params=instructionPrevisioniMeteo)
data = json.loads(response.text)
#retrive data from grabber and print
previsioniMeteo=data[0]["element"]
print(previsioniMeteo)


#sent telegram message to chat
bot = telegram.Bot(token=telegramTokenBot)
print(bot.get_me())

#da usare con cautela dopo aver verificato il resto
#bot.send_message(chat_id=telegramChatId_1, text=previsioniMeteo)
#bot.send_message(chat_id=telegramChatId_2, text=previsioniMeteo)