import time
import datetime
import MySQLdb
import RPi.GPIO as GPIO

pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

db = MySQLdb.connect(host="localhost", user="exampleuser",
                     passwd="pimylifeup", db="exampledb")
cur = db.cursor()

while True:
    state = GPIO.input(pin)
    now = datetime.datetime.utcnow()
    print(state)
    cur.execute("INSERT INTO Sensorstats (date_time, irsensorstat) VALUES (%s, %s)",
                (now, state))
    db.commit()
    time.sleep(1)
