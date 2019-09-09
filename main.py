from adafruit_ads1x15.analog_in import AnalogIn

import adafruit_ads1x15.ads1015 as ADS
import RPi.GPIO as GPIO
import board
import busio
import time

MOISTURE_LIMIT = 500
GPIO.setup(4, GPIO.OUT)

def irrigate():
    GPIO.output(4, True)
    time.sleep(5)
    GPIO.output(4, False)

def check_moisture():
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    chan = AnalogIn(ads, ADS.P0)
    mode = GPIO.getmode()

    print(mode)
    if chan.value <= MOISTURE_LIMIT:
        print("Moisture level is low, current level is %d" % chan.value)
        irrigate()
    else:
        print("Moisture level is fine, current level is %d" % chan.value)

def run():
    try:
        while True:
            time.sleep(3)
            check_moisture()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    run()






