import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.5)
