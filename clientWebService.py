import json
import requests
import ConfigParser
# install package

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')
# get di alcuni valori da file di properties
paramType = config.get('genericTest', 'paramType')
paramValue = config.get('genericTest', 'paramValue')
url = config.get('genericTest', 'urlTest')

# Simplerequest
response = requests.get('https://httpbin.org/get')
print('responseCode -->' + str(response))
print('json -->' + str(response.json()))

# Request with param
payload = {paramType: paramValue}
response = requests.get(url, params=payload)

print('responseCode -->' + str(response))
print('json -->' + str(response.json()))




