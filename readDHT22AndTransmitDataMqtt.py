import requests
import configparser
import sys
import requests
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json

#get constant info
config = configparser.ConfigParser()
config.read('nasProperties.properties')

host = config.get('mqtt', 'host')
port = config.get('mqtt', 'port')
pin = config.get('raspberryPi', 'dht22Pin')


#read data
humidityRaw, temperatureRaw = Adafruit_DHT.read_retry(22, pin)

#print data for debugging
print('{0:0.2f};{1:0.2f}%'.format(temperatureRaw, humidityRaw))

#prepare data to send
temp = str('{0:0.2f}'.format(temperatureRaw))
hum = str('{0:0.2f}%'.format(humidityRaw))
data = {"temperature": temp,"humidity": hum}
# convert into JSON:
payloadContent = json.dumps(data)

#pushmqt
client = mqtt.Client()
client.connect(host, int(port))
client.publish(topic="TestingTopic", payload=payloadContent, qos=0, retain=False)



