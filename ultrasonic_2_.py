import RPi.GPIO
import time
import sys

Trig = 27
Echo = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo)

# test