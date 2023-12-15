

DISTANCE_THRESHOLD = 10

import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24 # 27
GPIO_ECHO = 18 # 23

GPIO_TRIGGER = 27 # 27
GPIO_ECHO = 23 # 23
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# GPIO.setwarnings(False)                 # BPIO警告無効化


class Ultra_sonic:
    def __init__(self):
        self.distance = 0
        self.near_flag = False

    def get_distance(self):
        print('get_distance...')
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            print('in')
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            print('in2')
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        self.distance = distance

        print("Measured Distance = %.1f cm" % distance)
        print(self.near_flag)

        if distance < DISTANCE_THRESHOLD:
            self.near_flag = True
        else:
            self.near_flag = False

        time.sleep(0.3)


if __name__ == '__main__':
    Ultra_sonic = Ultra_sonic()
    try:
        while True:
            print('x')
            Ultra_sonic.get_distance()
            dist = Ultra_sonic.distance
            print(Ultra_sonic.near_flag)
            print("x1")
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()