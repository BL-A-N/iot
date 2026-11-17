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
        GPIO.output(relay1,True)
        GPIO.output(relay2,True)
        time.sleep(2)
        GPIO.output(relay1,True)
        GPIO.output(relay2,False)
        time.sleep(1)
        GPIO.output(relay1,False)
        GPIO.output(relay2,True)
        time.sleep(2)
        GPIO.output(relay1,False)
        GPIO.output(relay2,False)
        time.sleep(2)
        GPIO.output(relay1,True)
        GPIO.output(relay2,False)
        time.sleep(1)
        GPIO.output(relay1,False)
        GPIO.output(relay2,True)
              
except KeyboardInterrupt:
    GPIO.cleanup()
