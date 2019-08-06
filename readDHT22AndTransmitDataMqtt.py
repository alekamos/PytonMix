import requests
import configparser
import sys
import requests
import Adafruit_DHT
import paho.mqtt.client as mqtt

config = configparser.ConfigParser()
config.read('nasProperties.properties')

host = config.get('mqtt', 'host')
port = config.get('mqtt', 'port')
pin = config.get('raspberryPi', 'dht22Pin')


#read data
humidityRaw, temperatureRaw = Adafruit_DHT.read_retry(22, pin)
print('{0:0.2f};{1:0.2f}%'.format(temperatureRaw, humidityRaw))

#prepare data
temp = str('{0:0.2f}'.format(temperatureRaw))
hum = str('{0:0.2f}%'.format(humidityRaw))

payloadTest = str({'temperature': temp, 'humidity':hum})

#pushmqt
client = mqtt.Client()
client.connect(host, int(port))
client.publish(topic="TestingTopic", payload=payloadTest, qos=0, retain=False)



