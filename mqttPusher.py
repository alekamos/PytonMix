import paho.mqtt.client as mqtt
import configparser

config = configparser.ConfigParser()
config.read('nasProperties.properties')

host = config.get('mqtt', 'host')
port = config.get('mqtt', 'port')

print(host,port)

temp = 52
hum = 45

payloadTest = {"""temperature""": temp, "humidity" : hum}
print(payloadTest)

client = mqtt.Client()
client.connect(host, int(port))
client.publish(topic="TestingTopic", payload=payloadTest, qos=0, retain=False)
