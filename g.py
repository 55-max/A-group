# raspberry py でテンキーを使うためのテストプログラム

import RPi.GPIO as GPIO
import time

# Set the Row Pins
ROW_1 = 5
ROW_2 = 6
ROW_3 = 13
ROW_4 = 19

# Set the Column Pins
COL_1 = 12
COL_2 = 16
COL_3 = 20
COL_4 = 21

GPIO.setwarnings(False)
# BCM numbering
GPIO.setmode(GPIO.BCM)

# Set Row pins as output
GPIO.setup(ROW_1, GPIO.OUT)
GPIO.setup(ROW_2, GPIO.OUT)
GPIO.setup(ROW_3, GPIO.OUT)
GPIO.setup(ROW_4, GPIO.OUT)

# Set column pins as input and Pulled up high by default
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# function to read each row and each column
def readRow(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(COL_1) == 1):
        print(f"Using Polling, Input Received ::  {characters[0]}")
        return    
    if(GPIO.input(COL_2) == 1):
        print(f"Using Polling, Input Received ::  {characters[1]}")
        return
    if(GPIO.input(COL_3) == 1):
        print(f"Using Polling, Input Received ::  {characters[2]}")
        return
    if(GPIO.input(COL_4) == 1):
        print(f"Using Polling, Input Received ::  {characters[3]}")
        return
    GPIO.output(line, GPIO.LOW)

# Endless loop by checking each row
try:
    print("Press buttons on your keypad. Ctrl+C to exit.")
    while True:
        if(GPIO.input(ROW_1) == GPIO.HIGH):
            readRow(ROW_1, ["1","2","3","A"])
        if(GPIO.input(ROW_2) == GPIO.LOW):
            readRow(ROW_2, ["4","5","6","B"])
        if(GPIO.input(ROW_3) == GPIO.LOW):
            readRow(ROW_3, ["7","8","9","C"])
        if(GPIO.input(ROW_4) ==GPIO.LOW):
            readRow(ROW_4, ["*","0","#","D"])
        time.sleep(0.1) # adjust this per your own setup
except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()



