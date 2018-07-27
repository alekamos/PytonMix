import ConfigParser
import json
import requests
import re

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

urlAndPort = config.get('domoticz', 'urlPort')
basePath = config.get('domoticz', 'basePath')
idxSensor = config.get('domoticz', 'idxSensorExternalTempHum')
instructionGrabberTempExt = config.get('grabber', 'instructionGrabberTempExt')
instructionGrabberHumExt = config.get('grabber', 'instructionGrabberHumExt')
endPointGrabberService = config.get('grabber', 'endPointGrabberService')
idxSensor = config.get('domoticz', 'idxSensorExternalTempHum')
comfort = config.get('domoticz', 'comfortHumidityDefaultValue')
loginCredentialBase64 = config.get('domoticz', 'loginCredentialBase64')
endpoint = urlAndPort+'/'+basePath
#regular expressione per machare i numeri con la virgola
NumberRegex = '[^0-9,]';

#prepare data for call grabber
response=requests.get(endPointGrabberService,params=instructionGrabberTempExt)
data = json.loads(response.text)
temperatureRaw=data[0]["element"]
temperatureRaw = re.sub(NumberRegex,'', temperatureRaw)
temperatureRaw = temperatureRaw.replace(',','.')

response=requests.get(endPointGrabberService,params=instructionGrabberHumExt)
data = json.loads(response.text)
humidityRaw=data[0]["element"]
humidityRaw = re.sub(NumberRegex,'', humidityRaw)
humidityRaw = humidityRaw.replace(',','.')

print(temperatureRaw)
print(humidityRaw)
temperatureRawN = float(temperatureRaw)
humidityRawN = float(humidityRaw)


print('{0:0.2f};{1:0.2f}%'.format(temperatureRawN, humidityRawN))

#prepare data
dataCluster = str('{0:0.2f}'.format(temperatureRawN))+';'+str('{0:0.2f}%'.format(humidityRawN))+';'+str(comfort)
payloadTest = {'type': 'command', 'param': 'udevice', 'nvalue': 0, 'idx':  idxSensor, 'svalue': dataCluster}
headers = {'Authorization': 'Basic '+str(loginCredentialBase64)}

#call api
response=requests.get(endpoint,params=payloadTest,headers=headers)


