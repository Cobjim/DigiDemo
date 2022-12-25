# https://pimylifeup.com/raspberry-pi-rfid-rc522/
# sudo pip3 install mfrc522
# sudo pip3 install spidev
# VCC  Pin 1  3.3V
# RST  Pin 22 Brown/Yellow
# GND  Pin 25
# MISO Pin 21 Gold
# MOSI Pin 19 Purple
# SCK  Pin 23 Blue
# NSS/SDA Pin 24 Grey

#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()