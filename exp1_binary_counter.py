import RPi.GPIO as GPIO
import time

led_pins = [17, 27, 22, 23]      # LSB to MSB

GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for count in range(16):
            for bit, pin in enumerate(led_pins):
                GPIO.output(pin, (count >> bit) & 1)
            print("Count: {:2d}   Binary: {:04b}".format(count, count))
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
