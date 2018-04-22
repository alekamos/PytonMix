import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

print config.get('DEFAULT','serviceTemperatureComman');
print config.get('DEFAULT','domoticzPort');



