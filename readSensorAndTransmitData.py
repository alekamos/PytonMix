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


# only for fake test, this value will be updated next
#temperature,humidity = 0, 60

#22 is the sensor type(dht22) pin is get from property file
humidityRaw, temperatureRaw = Adafruit_DHT.read_retry(22, pin)
print('{0:0.2f};{1:0.2f}%'.format(temperatureRaw, humidityRaw))



dataCluster = str('{0:0.2f}'.format(temperatureRaw))+';'+str('{0:0.2f}%'.format(humidityRaw))+';'+str(comfort)

payloadTest = {'type': 'command', 'param': 'udevice', 'nvalue': 0, 'idx':  idxSensor, 'svalue': dataCluster}
response=requests.get(endpoint,params=payloadTest)


