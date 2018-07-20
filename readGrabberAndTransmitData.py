import requests
import ConfigParser
import sys
import json
import requests

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

urlAndPort = config.get('domoticz', 'urlPort')
basePath = config.get('domoticz', 'basePath')
idxSensor = config.get('domoticz', 'idxSensorExternalTempHum')
instructionGrabberTempExt = config.get('grabber', 'instructionGrabberTempExt')
instructionGrabberTempExt = config.get('grabber', 'instructionGrabberHumExt')
endPointGrabberService = config.get('grabber', 'endPointGrabberService')
idxSensor = config.get('domoticz', 'idxSensorExternalTempHum')
comfort = config.get('domoticz', 'comfortHumidityDefaultValue')
loginCredentialBase64 = config.get('domoticz', 'loginCredentialBase64')
endpoint = urlAndPort+'/'+basePath

#prepare data for call grabber
response=requests.get(endPointGrabberService,params=instructionGrabberTempExt)
data = json.loads(response.text)
temperatureRaw=data[0]["element"]
print('{0:0.2f};{1:0.2f}%'.format(temperatureRaw, humidityRaw))
#p = l.index("a")
#newstr = data[0]["element"].replace("°C", "")
#print(newstr)

#read data

#print('{0:0.2f};{1:0.2f}%'.format(temperatureRaw, humidityRaw))

#prepare data
#dataCluster = str('{0:0.2f}'.format(temperatureRaw))+';'+str('{0:0.2f}%'.format(humidityRaw))+';'+str(comfort)
#payloadTest = {'type': 'command', 'param': 'udevice', 'nvalue': 0, 'idx':  idxSensor, 'svalue': dataCluster}
#headers = {'Authorization': 'Basic '+str(loginCredentialBase64)}

#call api
#response=requests.get(endpoint,params=payloadTest,headers=headers)


