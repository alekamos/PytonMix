import ConfigParser
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM) BCM e il numero dopo "GPIO
GPIO.setmode(GPIO.BOARD)

config = ConfigParser.RawConfigParser()
config.read('nasProperties.properties')

# set GPIO Pins
gpio_trigger = int(config.get('raspberryPi', 'hcsr04_1_trigger'))
gpio_echo = int(config.get('raspberryPi', 'hcsr04_1_echo'))
print("gpio_trigger: "+ str(gpio_trigger))
print("gpio_echo: "+str(gpio_echo))

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
    distance = (TimeElapsed * 34300) / 2

    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()