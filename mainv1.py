# P_SERVO1  Pin 32 Green
# P_SERVO2  Pin 33 Green
# Red= VCC and input

# Black = GND
# Blue = Output

# Input Pin 36 Blue button for Pump1 #########################
# Input Pin 37 Blue button #########################

# VCC  Pin 17  3.3V
# RST  Pin 22 Brown/Yellow
# GND  Pin 25
# MISO Pin 21 Gold
# MOSI Pin 19 Purple
# SCK  Pin 23 Blue
# NSS/SDA Pin 24 Grey/use a FF


# Trigger1 Pin 11
# Echo1 Pin 13
# Trigger2 Pin 18
# Echo2 Pin 16

#!/usr/bin/env python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from mfrc522 import SimpleMFRC522
from pynput.keyboard import Key, Listener
#from datetime import *

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


#Set up for the Ultra Sonic Sensors
PIN_TRIGGER1 = 11 #The trigger can be connected straight to the RasPi
PIN_ECHO1 = 13 # The Echo needs a Voltage Divider in order to not damage the Raspi
PIN_TRIGGER2 = 18 #The trigger can be connected straight to the RasPi
PIN_ECHO2 = 16 # The Echo needs a Voltage Divider in order to not damage the Raspi

#Set up for the Motor
P_SERVO1 = 32 # GPIO port = Number of the port in the RasPi
P_SERVO2 = 33 # GPIO port = Number of the port in the RasPi
fPWM = 82 # Hz (50 soft PWM，limit the frequecies)
button = 0 # button state
reader = SimpleMFRC522() # RFID Reader

channel=0

flag=0  # Flag to enter the Readers loop
text=("")


def setup():
    global pwm1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO1, GPIO.OUT) #setup P_SERVO as an output 
    pwm1 = GPIO.PWM(P_SERVO1, fPWM) #setup P_SERVO as an PWM and its frequency
    pwm1.start(0)                  #Starts the PWM at 0 Hz
    
    global pwm2
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_SERVO2, GPIO.OUT) #setup P_SERVO as an output 
    pwm2 = GPIO.PWM(P_SERVO2, fPWM) #setup P_SERVO as an PWM and its frequency
    pwm2.start(0)
    

    GPIO.setup(PIN_TRIGGER1, GPIO.OUT) 
    GPIO.setup(PIN_ECHO1, GPIO.IN)
    GPIO.output(PIN_TRIGGER1, GPIO.LOW)

    GPIO.setup(PIN_TRIGGER2, GPIO.OUT) 
    GPIO.setup(PIN_ECHO2, GPIO.IN)
    GPIO.output(PIN_TRIGGER2, GPIO.LOW)

def loop():
    
        text=identifier()
        
        GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 36 to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 37 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(36,GPIO.BOTH,callback=button_callback)# Setup event on pin 36 rising edge
        GPIO.add_event_detect(37,GPIO.BOTH,callback=button_callback)# Setup event on pin 37 rising edge
        
        while channel!=0:
                button_callback
       
        identifier()
           
        
        
                 
        
        


def button_callback(channel):
    #Channel is the pin number that has been triggered
    #Button will become a boolean number
    button = GPIO.input(channel) 
    startpump(button,channel)
    
           
        
        
def startpump(button,channel):
    t0= time.time()
    print("Serving Water")
    
    if channel==36:
        
        duty1 = button*2
        pwm1.ChangeDutyCycle(duty1)

        ultrasonic1() # Prints the distance of the level of liquids in the tank
        time.sleep(2) #30 how much I want the program to stay in this phase
        t1=time.time()
        duty1=0
        print("The pump was on ", t1-t0,"s")
        
        return (time.time())
    
    elif channel==37:
        duty2 = button*2
        pwm2.ChangeDutyCycle(duty2)

        ultrasonic2() # Prints the distance of the level of liquids in the tank
        time.sleep(2) #30 how much I want the program to stay in this phase
        t1=time.time()
        duty2=0
        print("The pump was on ", t1-t0,"s")
        
        return (time.time())

#################################################################

#################################################################



def ultrasonic1():
    
      GPIO.output(PIN_TRIGGER1, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER1, GPIO.LOW)

      while GPIO.input(PIN_ECHO1)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO1)==1:
            pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            # Ultrasonic Speed Time travels at 34300 cm/s
            #Since it is going to hit the object and bounce back it is diveded by 2
      print("ULTRASONIC SENSOR 1")         
      if (distance> 15): 
          print("Please fill up the Water supply")
          
          
      else: 
           print("Distance:",distance,"cm")
           
def ultrasonic2():
    
      GPIO.output(PIN_TRIGGER2, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER2, GPIO.LOW)

      while GPIO.input(PIN_ECHO2)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO2)==1:
            pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            # Ultrasonic Speed Time travels at 34300 cm/s
            #Since it is going to hit the object and bounce back it is diveded by 2
      print("ULTRASONIC SENSOR 2")      
      if (distance> 15): 
          print("Please fill up the Water supply")
          
          
      else: 
           print("Distance:",distance,"cm")
    
def identifier():
    id, text = reader.read()
    print(id)
    print("Hello", text) 
    time.sleep(0.5)
    return (text)


    


            

#with Listener(pumpon=pumpon,pumpoff=pumpoff) as listener:
#     listener.join()
#Footer         
           
setup()
loop()

print("Stop 1") #Program go here stop here
####################


###########################






message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up



###################################################
# NEXT STEPS
#  Include the US Sensor
#  Include the STOP button function
#  Create the variables to safe the amount of liquids stored
#  Measure the Volumen of liquid give in function of the time.
#  Create the physical model


#Nodos 19 Raspi
#Power supply Switch 4
#PS US 4
#PS Pump 4 