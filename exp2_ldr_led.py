import RPi.GPIO as GPIO

LDR_PIN = 26
LED_PIN = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LDR_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.input(LDR_PIN))
except KeyboardInterrupt:
    GPIO.cleanup()
