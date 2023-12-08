import RPi.GPIO as GPIO
import time

LED_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

class light:
    def __init__(self):
        pass

    def on(self):
        print('light onします')
        GPIO.output(LED_PIN, GPIO.HIGH)

    def off(self):
        print('light offします')
        GPIO.output(LED_PIN, GPIO.LOW)