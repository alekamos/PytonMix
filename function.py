import requests
import json
from pprint import pprint




def detectLightStatus():
    r = requests.get("http://192.168.0.12:8084/json.htm?type=devices&filter=light&used=true&order=Name")
    return r.content


dataStr = str(detectLightStatus())
data = json.loads(dataStr)

#per stampare tutti i dati
#pprint(data)

print(data["Sunrise"])
print(data["Sunset"])
print(data["result"][1]["idx"])
print(data["result"][1]["LastUpdate"])
print(data["result"][1]["Status"])