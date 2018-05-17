import ConfigParser
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

# GPIO Mode (BOARD / BCM) BCM e il numero dopo "GPIO
GPIO.setmode(GPIO.BCM)

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

# set GPIO Pins
gpio_trigger = int(config.get('raspberryPi', 'hcsr04_1_trigger'))
gpio_echo = int(config.get('raspberryPi', 'hcsr04_1_echo'))
gpio_dht22 = config.get('raspberryPi', 'dht22Pin')


# set GPIO direction (IN / OUT)
GPIO.setup(gpio_trigger, GPIO.OUT)
GPIO.setup(gpio_echo, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(gpio_trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpio_trigger, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(gpio_echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(gpio_echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    soundspeed = getSonicSpeed()
    distance = (TimeElapsed * soundspeed) / 2

    return distance


def getSonicSpeed():
    humidity, temperature = Adafruit_DHT.read_retry(22, gpio_dht22)
    soundspeed = (331.4 + (0.606 * temperature) + (0.0124 * humidity))*100

    print("temp: "+str(temperature)+" hum "+str(humidity)+" sound speed: "+str(soundspeed) + " cm/s")
    return soundspeed

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(5)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()