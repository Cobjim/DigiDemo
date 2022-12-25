# https://pimylifeup.com/raspberry-pi-rfid-rc522/
# sudo pip3 install mfrc522
# sudo pip3 install spidev
# VCC  Pin 1  3.3V
# RST  Pin 22 Brown/Yellow
# GND  Pin 25
# MISO Pin 21 Gold
# MOSI Pin 19 Purple
# SCK  Pin 23 Blue
# NSS/SDA Pin 24 Grey/use a FF

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
flag=0

while flag==0:
    id, text = reader.read()
    print(id)
    print(text)
    time.sleep(1)

GPIO.cleanup()