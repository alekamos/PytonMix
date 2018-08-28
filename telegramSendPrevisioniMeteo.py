import ConfigParser
import json
import requests
import telegram
import io

#istruzioni telegram wrapper https://python-telegram-bot.org/

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')
instructionPrevisioniMeteo_1 = config.get('grabber', 'instructionPrevisioniMeteo_1')
nomeFilePrevisioniMeteo_1 = config.get('util', 'nomeFilePrevisioniMeteo_1')
descrPrevisioneMeteo_1 = config.get('util', 'descrPrevisioneMeteo_1')
instructionPrevisioniMeteo_2 = config.get('grabber', 'instructionPrevisioniMeteo_2')
nomeFilePrevisioniMeteo_2 = config.get('util', 'nomeFilePrevisioniMeteo_2')
descrPrevisioneMeteo_2 = config.get('util', 'descrPrevisioneMeteo_2')
instructionPrevisioniMeteo_3 = config.get('grabber', 'instructionPrevisioniMeteo_3')
nomeFilePrevisioniMeteo_3 = config.get('util', 'nomeFilePrevisioniMeteo_3')
descrPrevisioneMeteo_3 = config.get('util', 'descrPrevisioneMeteo_3')
endPointGrabberService = config.get('grabber', 'endPointGrabberService')
telegramTokenBot = config.get('telegram', 'tokenBot')
telegramChatId_1 = config.get('telegram', 'chatId_1')
telegramChatId_2 = config.get('telegram', 'chatId_2')

#variabili
previsionSourceList = [instructionPrevisioniMeteo_1,instructionPrevisioniMeteo_2,instructionPrevisioniMeteo_3]
nameFilePrevisionList = [nomeFilePrevisioniMeteo_1,nomeFilePrevisioniMeteo_2,nomeFilePrevisioniMeteo_3]
descrPrevisioniList = [descrPrevisioneMeteo_1,descrPrevisioneMeteo_2,descrPrevisioneMeteo_3]


for i in range(len(previsionSourceList)):
    #prepare data for call grabber
    response=requests.get(endPointGrabberService,params=previsionSourceList[i])
    data = json.loads(response.text)
    #retrive data from grabber and print
    currentPrevision=data[0]["element"].replace(u"\uFFFD", "?")
    print(currentPrevision)

    #caricamento ultima previsione disponibile
    with io.open(nameFilePrevisionList[i], 'r') as lastData:
        lastPrevision = lastData.read()
    
    print(lastPrevision)

    #se diversi i dati sono stati aggiornati, se uguali nessun aggiornamento
    if lastPrevision == currentPrevision:
        print('Nothing to do here, same data')
    else:
        file = io.open(nameFilePrevisionList[i], 'w')
        file.write(currentPrevision)
        file.close()
    
    #sent telegram message to chat
        message = descrPrevisioniList[i]+' '+currentPrevision
        bot = telegram.Bot(token=telegramTokenBot)
        print(bot.get_me())
        bot.send_message(chat_id=telegramChatId_1, text=message,parse_mode=telegram.ParseMode.MARKDOWN)


