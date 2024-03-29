# Software PWM Servo.py
# Taken from https://www.dfrobot.com/product-1698.html?tracking=5f17f93376db3
# Written by 夏青 
# Modified by Ian Coberly
# P_SERVO  Pin 32 Green

import RPi.GPIO as GPIO
import time


P_SERVO = 32 # GPIO port = Number of the port in the RasPi
P_SERVO2 = 33 # GPIO port = Number of the port in the RasPi
fPWM = 82 # Hz (50 soft PWM，limit the frequecies)
#a = 10  # Side "a" is the one nearest to the cables
#b = 2   # Side "b" its furthest away from the cables

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_SERVO, GPIO.OUT) #setup P_SERVO as an output 
    pwm = GPIO.PWM(P_SERVO, fPWM) #setup P_SERVO as an PWM and its frequency
    pwm.start(0)                  #Starts the PWM at 0 Hz
    
    global pwm2
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_SERVO2, GPIO.OUT) #setup P_SERVO as an output 
    pwm2 = GPIO.PWM(P_SERVO2, fPWM) #setup P_SERVO as an PWM and its frequency
    pwm2.start(0)                  #Starts the PWM at 0 Hz

def setDirection():
    #duty = a / 180 * direction + b  # 2 is the fastest
    print("Serving Water")
    duty = 2
    pwm.ChangeDutyCycle(duty)
    pwm2.ChangeDutyCycle(duty)
    #print ("direction =", direction, "-> duty =", duty)
    time.sleep(3) #30 how much I want the program to stay in this phase

print ("starting")
setup()

direction = 0
setDirection()
#for direction in range(0, 181, 10): #the smaller the step the longer the program runs
 #   setDirection(direction)
  #  direction = 0
   # setDirection(0)
GPIO.cleanup()
print ( "done")

