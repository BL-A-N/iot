import time
import board
import adafruit_dht
import requests

KEY = "YOUR_API_KEY"
sensor = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temp, hum = sensor.temperature, sensor.humidity
            r = requests.post(
                "https://api.thingspeak.com/update",
                data={"api_key": KEY, "field1": temp, "field2": hum},
                timeout=15,
            )
            print(f"Temperature: {temp}°C  Humidity: {hum}%  ->  {r.status_code}, entry {r.text}")
            time.sleep(15)          # ThingSpeak free-tier limit
        except (RuntimeError, requests.RequestException) as e:
            print("Retrying:", e)   # DHT11 glitch or network hiccup
            time.sleep(15)
finally:
    sensor.exit()                   # releases GPIO and the libgpiod helper