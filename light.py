import RPi.GPIO as GPIO
from time import sleep

# GPIO.cleanup()

num = 21
sleep_time = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(num, GPIO.OUT)
GPIO.output(num, 0)

print('点灯します')

GPIO.output(num, 1)
sleep(sleep_time)

print('消えます')

GPIO.output(num, 0)
sleep(sleep_time)

GPIO.cleanup(num)