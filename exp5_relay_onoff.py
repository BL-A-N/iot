import RPi.GPIO as GPIO
import time

pin = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, True)
        time.sleep(5)
        GPIO.output(pin, False)
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
