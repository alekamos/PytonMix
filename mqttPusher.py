import paho.mqtt.client as mqtt
import configparser
import json

config = configparser.ConfigParser()
config.read('nasProperties.properties')

host = config.get('mqtt', 'host')
port = config.get('mqtt', 'port')

print(host,port)

temp = 52
hum = 45

# object to send
data = {
  "temperature": temp,
  "humidity": hum
}

# convert into JSON:
payloadContent = json.dumps(data)


client = mqtt.Client()
client.connect(host, int(port))
client.publish(topic="TestingTopic", payload=payloadContent, qos=0, retain=False)
