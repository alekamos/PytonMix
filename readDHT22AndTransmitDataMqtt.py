import requests
import configparser
import sys
import requests
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import time

#get constant info
config = configparser.ConfigParser()
config.read('nasProperties.properties')

host = config.get('mqtt', 'host')
port = config.get('mqtt', 'port')
topic = config.get('mqtt', 'topicDht22')
pin = config.get('raspberryPi', 'dht22Pin')

humTolerance = 5;
tempTolerance = 0.5;


#read data
humidityRaw, temperatureRaw = Adafruit_DHT.read_retry(22, pin)
#second read after 2secon
time.sleep(2);
humidityRaw2, temperatureRaw2 = Adafruit_DHT.read_retry(22, pin)

if abs(humidityRaw-humidityRaw2)>humTolerance or abs(temperatureRaw2-temperatureRaw)>tempTolerance:
    print('Differenza maggiore della tolleranza stabilita')
    print('{0:0.2f};{1:0.2f}'.format(temperatureRaw, humidityRaw))
    print('{0:0.2f};{1:0.2f}'.format(temperatureRaw2, humidityRaw2))
    sys.exit()

#print data for debugging
print('{0:0.2f};{1:0.2f}'.format(temperatureRaw2, humidityRaw2))

#prepare data to send
temp = str('{0:0.2f}'.format(temperatureRaw2))
hum = str('{0:0.2f}'.format(humidityRaw2))
data = {"temperature": temp,"humidity": hum}
# convert into JSON:
payloadContent = json.dumps(data)

#pushmqt
client = mqtt.Client()
client.connect(host, int(port))
client.publish(topic=topic, payload=payloadContent, qos=0, retain=False)



