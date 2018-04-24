import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

print config.get('domoticz', 'url');
print config.get('domoticz', 'port');