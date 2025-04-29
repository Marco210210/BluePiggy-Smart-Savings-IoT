from bsp import board

# import the adc module
import adc
import gpio
import serial
import pwm


serial.serial()                  #create a serial port with default parameters

def angle2pulse(angle):
    return 1000+int(angle*1000/90)
pwm_pin=D15
gpio.mode(pwm_pin, OUTPUT)           #servo pwm    

angle2pulse(0)
period=20000
angle=0

def apri():
    if angle==110:
        #initial position
        angle=0
    pulse=angle2pulse(angle)
    pwm.write(pwm_pin, period, pulse,MICROS)
    sleep(100)

def chiudi():
    if angle == 0:
        angle = 110
    pulse=angle2pulse(angle)
    pwm.write(pwm_pin, period, pulse,MICROS)
    sleep(100)