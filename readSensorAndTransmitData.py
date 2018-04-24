import requests
import ConfigParser
import sys
import requests
import Adafruit_DHT

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

urlAndPort = config.get('domoticz', 'urlPort')
basePath = config.get('domoticz', 'basePath')
pin = config.get('raspberryPi', 'dht22Pin')
idxSensor = config.get('domoticz', 'idxSensor')
comfort = config.get('domoticz', 'comfortHumidityDefaultValue')

endpoint = urlAndPort+'/'+basePath



# only for fake test
# temperature = 12.0055
# humidity = 60


humidityRaw, temperatureRaw = Adafruit_DHT.read_retry(22, pin)
    print('{0:0.1f};{1:0.1f}%'.format(temperature, humidity))



dataCluster = str({0:0.1f}.format(temperature))+';'+str(humidity)+';'+str(comfort)

payloadTest = {'type': 'command', 'param': 'udevice', 'nvalue': 0, 'idx':  idxSensor, 'svalue': dataCluster}
response=requests.get(endpoint,params=payloadTest)


