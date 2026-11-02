import http.client
import urllib.parse
import time
import board
import adafruit_dht
import psutil

key = "KEY"    # Write API Key

for proc in psutil.process_iter():
    if proc.name() in ('libgpiod_pulsein', 'libgpiod_pulsei'):
        proc.kill()

sensor = adafruit_dht.DHT11(board.D4)
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
    except RuntimeError:
        time.sleep(2)
        continue

    params = urllib.parse.urlencode({'field1': temp,
                                     'field2': humidity,
                                     'key': key})
    try:
        conn = http.client.HTTPConnection("api.thingspeak.com")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print("Temperature: {}*C   Humidity: {}%".format(temp, humidity))
        print(response.status, response.reason)
        conn.close()
    except Exception:
        print("connection failed")

    time.sleep(15)
