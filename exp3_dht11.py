import time
import board
import adafruit_dht
import psutil

for proc in psutil.process_iter():
    if proc.name() in ('libgpiod_pulsein', 'libgpiod_pulsei'):
        proc.kill()

sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        print("Temperature: {}*C   Humidity: {}%".format(
            sensor.temperature, sensor.humidity))
    except RuntimeError as error:
        print(error.args[0])
    except Exception:
        sensor.exit()
        raise
    time.sleep(2)
