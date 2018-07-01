import ConfigParser
import RPi.GPIO as GPIO
import time

#funzione che invoca domoticz per capire se la luce è accesa o no, come input vuole l'indice della lampada
def detectLightStatus():







# GPIO Mode (BOARD / BCM) BCM e il numero dopo "GPIO
GPIO.setmode(GPIO.BCM)

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

# set GPIO Pins
gpio_pir = int(config.get('raspberryPi', 'hcsr01_1'))
print("gpio_pir: "+ str(gpio_pir))

GPIO.setup(gpio_pir, GPIO.IN)                          #Set pin as GPIO in
print "Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"
while True:
   if GPIO.input(gpio_pir):                            #Check whether pir is HIGH
      print "Motion Detected!"
      time.sleep(1)
   else:
      print "No motion"
      time.sleep(1)                               #D1- Delay to avoid multiple detection
   time.sleep(0.1)                                #While loop delay should be less than detection(hardware) del


