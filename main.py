import time
from time import sleep
import RPi.GPIO as GPIO
#from config import *
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#import gpiozero
#from gpiozero import Servo
#from gpiozero.pins.pigpio import PiGPIOFactory
#gpiozero.Device.pin_factory=PiGPIOFactory('127.0.0.1')
#servo = Servo(25)

MOTOR_A_1           = 12
MOTOR_A_2           = 20
MOTOR_B_1           = 16
MOTOR_B_2           = 21

def setup():
    # Set pin states
    GPIO.setup(MOTOR_A_1, GPIO.OUT)
    GPIO.setup(MOTOR_A_2, GPIO.OUT)
    GPIO.setup(MOTOR_B_1, GPIO.OUT)
    GPIO.setup(MOTOR_B_2, GPIO.OUT)
 
def servin_time():
    servo.mid()
    sleep(0.5)
    servo.max()
    sleep(0.5)
    return
 
# Function for step sequence
def setStep(w1, w2, w3, w4):
    GPIO.output(MOTOR_A_1, w1)
    GPIO.output(MOTOR_A_2, w2)
    GPIO.output(MOTOR_B_1, w3)
    GPIO.output(MOTOR_B_2, w4)
    return

# Loop through step sequence based on number of steps
def clockwise(steps, delay):
    for i in range(0, steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)
    return

# Loop through step sequence based on number of steps
def cclockwise(steps,delay):
    for i in range(0, steps):
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,0,1,0)
        time.sleep(delay)
    return

# Rotate clockwise or counterclockwise based off boolean value 
#def rotate(direction,steps,delay):
#    for i in range(0, steps):
#        setStep(direction,!direction,!direction,direction)
#        time.sleep(delay)
#        setStep(!direction,direction,!direction,direction)
#        time.sleep(delay)
#        setStep(!direction,direction,direction,!direction)
#        time.sleep(delay)
#        setStep(direction,!direction,direction,!direction)
#        time.sleep(delay)
#    return

if __name__ == '__main__':     # Program start from here
    try:
        setup()
        #print("Fuji feeding time! Fuji will be fed.")

        delay = 0.0028
        clicks = 100

        sleep(1)
        clockwise(clicks, delay)
        cclockwise(clicks, delay)
        sleep(1)
        
        #Feeding time verification
        #print("Fuji has been fed.")

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("Keyboard interrupt")
        #destroy()
        #except RuntimeError:
                # this gets thrown when control C gets pressed
                # because wait_for_edge doesn't properly pass this on
		#destroy()
                #pass
