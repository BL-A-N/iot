import RPi.GPIO as GPIO
import time

relay1 = 22
relay2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(relay2, GPIO.OUT, initial=GPIO.LOW)


try:
    while True:
              
except KeyboardInterrupt:
    GPIO.cleanup()
