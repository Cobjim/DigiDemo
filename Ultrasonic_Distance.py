# Taken from https://pimylifeup.com/raspberry-pi-distance-sensor/
# Written by Gus
# Modified by Ian Coberly 

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

flag=0 #Flag is a Variable that it is used t
PIN_TRIGGER = 18 #The trigger can be connected straight to the RasPi
PIN_ECHO = 24 # The Echo needs a Voltage Divider in order to not damage the Raspi

GPIO.setup(PIN_TRIGGER, GPIO.OUT) 
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

print ("Waiting for sensor to settle")


print ("Calculating distance")


while flag==0:  # This while loops the whole system
  
  GPIO.output(PIN_TRIGGER, GPIO.HIGH)

  time.sleep(0.00001)

  GPIO.output(PIN_TRIGGER, GPIO.LOW)

  while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
  while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        # Ultrasonic Speed Time travels at 34300 cm/s
        #Since it is going to hit the object and bounce back it is diveded by 2
        
  time.sleep(0.5) #Controls how fast are the results printed
  
  if (distance> 7): 
      print("Please fill up the Water supply")
      print ("Distance:",distance,"cm")
      #flag=1
  else: 
       print ("Distance:",distance,"cm")     

