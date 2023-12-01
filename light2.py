import RPi.GPIO as GPIO
from time import sleep

num = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(num,GPIO.OUT)

try:
    while True:
        GPIO.output(num, 1)
        sleep(0.5)
        GPIO.output(num, 0)
        sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()