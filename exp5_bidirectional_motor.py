import RPi.GPIO as GPIO
import time

relay1 = 22
relay2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(relay2, GPIO.OUT, initial=GPIO.LOW)

def motor(r1, r2, label, seconds):
    GPIO.output(relay1, r1)
    GPIO.output(relay2, r2)
    print(label)
    time.sleep(seconds)

try:
    while True:
        motor(True, False, "Clockwise", 5)
        motor(False, False, "Stop", 2)
        motor(False, True, "Anticlockwise", 5)
        motor(False, False, "Stop", 2)
except KeyboardInterrupt:
    GPIO.cleanup()
