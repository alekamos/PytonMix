temperatureRaw,humidityRaw,comfort = 13.5546548,56.66655,1
dataCluster = str('{0:0.2f}'.format(temperatureRaw))+';'+str('{0:0.2f}%'.format(humidityRaw))+';'+str(comfort)
print(dataCluster)