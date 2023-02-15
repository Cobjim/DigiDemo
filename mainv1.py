# P_SERVO  Pin 32 Green
# Red= VCC and input
# Black = GND
# Blue = Output
# Output Pin 36 Blue
# VCC  Pin 1  3.3V
# RST  Pin 22 Brown/Yellow
# GND  Pin 25
# MISO Pin 21 Gold
# MOSI Pin 19 Purple
# SCK  Pin 23 Blue
# NSS/SDA Pin 24 Grey/use a FF

#!/usr/bin/env python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering



P_SERVO = 32 # GPIO port = Number of the port in the RasPi
fPWM = 82 # Hz (50 soft PWM，limit the frequecies)
button = 0 # button state
reader = SimpleMFRC522() # RFID Reader
flag=0  # Flag to enter the Readers loop
text=("")

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT) #setup P_SERVO as an output 
    pwm = GPIO.PWM(P_SERVO, fPWM) #setup P_SERVO as an PWM and its frequency
    pwm.start(0)                  #Starts the PWM at 0 Hz

def startpump(button):
    #duty = a / 180 * direction + b  # 2 is the fastest
    print("Serving Water")
    duty = button*2
    pwm.ChangeDutyCycle(duty)
    #print ("direction =", direction, "-> duty =", duty)
    time.sleep(3) #30 how much I want the program to stay in this phase
    return (duty/2)

def button_callback(channel):

    button = GPIO.input(36)
    #print("flag1 button: ",button)
    startpump(button)
    #print ("HERE",button)
    while button<0:
        loop()
    
def identifier():
    id, text = reader.read()
    print(id)
    print("Hello", text) 
    time.sleep(0.5)
    return (text)

def loop():
    
        text=identifier()
        
        GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 36 to be an input pin and set initial value to be pulled low (off)
                 
        GPIO.add_event_detect(36,GPIO.BOTH,callback=button_callback)# Setup event on pin 10 rising edge
        
        while (True):
            try:
                button_callback
        
            finally:
                identifier()
            
                

setup()
loop()
####################


###########################


print(GPIO.input(36))



message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up



###################################################
# NEXT STEPS
#  Include the US Sensor
#  Include the STOP button function
#  Create the variables to safe the amount of liquids stored
#  Measure the Volumen of liquid give in function of the time.
#  Create the physical model


