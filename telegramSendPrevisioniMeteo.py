import ConfigParser
import json
import requests
import telegram
import io
import logging

#istruzioni telegram wrapper https://python-telegram-bot.org/

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')
filepathLog = config.get('log', 'telegramMeteoBotLogPath')
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
telegramChannel_1 = config.get('telegram', 'chatId_channel_1')
channelUpdateStatus = config.get('telegram', 'channelStatus')

#variabili
previsionSourceList = [instructionPrevisioniMeteo_1,instructionPrevisioniMeteo_2,instructionPrevisioniMeteo_3]
nameFilePrevisionList = [nomeFilePrevisioniMeteo_1,nomeFilePrevisioniMeteo_2,nomeFilePrevisioniMeteo_3]
descrPrevisioniList = [descrPrevisioneMeteo_1,descrPrevisioneMeteo_2,descrPrevisioneMeteo_3]

#configurazione log
logging.basicConfig(filename=filepathLog,level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')


for i in range(len(previsionSourceList)):
    logging.info("Grabber request to endpoint: %s for getting data from: %s",endPointGrabberService,previsionSourceList[i])
    #prepare data for call grabber
    response=requests.get(endPointGrabberService,params=previsionSourceList[i])
    data = json.loads(response.text)
    #retrive data from grabber and print
    currentPrevision=data[0]["element"]
    logging.debug("Data from grabber: %s",currentPrevision)

    #caricamento ultima previsione disponibile
    with io.open(nameFilePrevisionList[i], 'r') as lastData:
        lastPrevision = lastData.read()
    
    logging.debug("Data from file: %s last prevision: %s",nameFilePrevisionList[i],lastPrevision)

    #se diversi i dati sono stati aggiornati, se uguali nessun aggiornamento
    if len(currentPrevision)<300:
        logging.warn("Lunghezza inferiore a 300 caratteri, testo non valido")
    elif len(currentPrevision)>2000:
        logging.warn("Lunghezza superiore a 2000 caratteri, testo non valido")
    elif lastPrevision == currentPrevision:
        logging.info("Same data, nothing to do here");
    else:
        file = io.open(nameFilePrevisionList[i], 'w')
        file.write(currentPrevision)
        file.close()
    
        #sent telegram message to chat
        message = descrPrevisioniList[i]+' '+currentPrevision
        bot = telegram.Bot(token=telegramTokenBot)
        logging.info("Info about telegram bot: %s",bot.get_me());
        bot.send_message(chat_id=telegramChatId_1, text=message,parse_mode=telegram.ParseMode.MARKDOWN)
        logging.info("Telegram message send");
        
        logging.debug("Status of telegram channel: %s",channelUpdateStatus);
        if channelUpdateStatus=='ON':
            bot.send_message(chat_id=telegramChannel_1, text=message,parse_mode=telegram.ParseMode.MARKDOWN)
            logging.debug("Telegram message send to channel");


