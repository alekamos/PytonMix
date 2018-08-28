import ConfigParser
import json
import requests
import telegram

#istruzioni telegram wrapper https://python-telegram-bot.org/

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')
instructionPrevisioniMeteo_1 = config.get('grabber', 'instructionPrevisioniMeteo_1')
nomeFilePrevisioniMeteo_1 = config.get('util', 'nomeFilePrevisioniMeteo_1')
instructionPrevisioniMeteo_2 = config.get('grabber', 'instructionPrevisioniMeteo_2')
nomeFilePrevisioniMeteo_2 = config.get('util', 'nomeFilePrevisioniMeteo_2')
instructionPrevisioniMeteo_3 = config.get('grabber', 'instructionPrevisioniMeteo_3')
nomeFilePrevisioniMeteo_3 = config.get('util', 'nomeFilePrevisioniMeteo_3')
endPointGrabberService = config.get('grabber', 'endPointGrabberService')
telegramTokenBot = config.get('telegram', 'tokenBot')
telegramChatId_1 = config.get('telegram', 'chatId_1')
telegramChatId_2 = config.get('telegram', 'chatId_2')

#variabili
previsionSourceList = [instructionPrevisioniMeteo_1,instructionPrevisioniMeteo_2,instructionPrevisioniMeteo_3]
nameFilePrevisionList = [nomeFilePrevisioniMeteo_1,nomeFilePrevisioniMeteo_2,nomeFilePrevisioniMeteo_3]


#prepare data for call grabber
response=requests.get(endPointGrabberService,params=instructionPrevisioniMeteo_1)
data = json.loads(response.text)
#retrive data from grabber and print
currentPrevision_1=data[0]["element"]
print(currentPrevision_1)

#caricamento ultima previsione disponibile
with open(nomeFilePrevisioniMeteo_1, 'r') as lastData:
    lastPrevision_1 = lastData.read()
    
print(lastPrevision_1)

#se diversi i dati sono stati aggiornati, se uguali nessun aggiornamento
if lastPrevision_1 == currentPrevision_1:
    return
else:
    file = open(nomeFilePrevisioniMeteo_1, 'w')
    file.write(currentPrevision_1)
    file.close()
    
    #sent telegram message to chat
    bot = telegram.Bot(token=telegramTokenBot)
    print(bot.get_me())
    
    
    
'''
versione con loop

for i in range(len(previsionSourceList)):
#prepare data for call grabber
response=requests.get(endPointGrabberService,params=previsionSourceList[i])
data = json.loads(response.text)
#retrive data from grabber and print
currentPrevision=data[0]["element"]
print(currentPrevision)

#caricamento ultima previsione disponibile
with open(nameFilePrevisionList[i], 'r') as lastData:
    lastPrevision = lastData.read()
    
print(lastPrevision)

#se diversi i dati sono stati aggiornati, se uguali nessun aggiornamento
if lastPrevision == currentPrevision:
    return
else:
    file = open(nameFilePrevisionList[i], 'w')
    file.write(currentPrevision)
    file.close()
    
    #sent telegram message to chat
    bot = telegram.Bot(token=telegramTokenBot)
    print(bot.get_me())




'''
#da usare con cautela dopo aver verificato il resto
#bot.send_message(chat_id=telegramChatId_1, text=previsioniMeteo)
#bot.send_message(chat_id=telegramChatId_2, text=previsioniMeteo)

#todo fare un array con le previsioni in maniera da essere tutto automatizzato
#todo passare ad un telegram channel