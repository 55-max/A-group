import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO26を出力端子設定
# 今回は、18番を使用すること。
NUM = 18
GPIO.setup(NUM, GPIO.OUT)

#GPIO26をPWM設定、周波数は50Hz
p = GPIO.PWM(NUM, 50)

#Duty Cycle 0%
p.start(0.0)

class motor:
    def __init__(self):
        self.dc = 0.0
        self.p = p

    def set_dc(self, dc):
        self.dc = dc
        self.p.ChangeDutyCycle(dc)
        time.sleep(0.4)
        self.p.ChangeDutyCycle(0.0)

    def get_dc(self):
        return self.dc

if __name__ == '__main__':
    motor = motor()
    try:
        while True:
            print("input Duty Cyle (2.5 - 12)")
            dc = float(input())
            
            if dc > 5.3:
                continue
            if dc < 3.2:
                continue

            motor.set_dc(dc)
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()

if __name__ == '__main__':
    motor = motor()
    try:
        while True:
            print("input Duty Cyle (2.5 - 12)")
            dc = float(input())
            
            if dc > 5.3:
                continue
            if dc < 3.2:
                continue

            motor.set_dc(dc)
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()