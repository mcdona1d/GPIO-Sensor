#!/usr/bin/python
#coding: utf8
import RPi.GPIO as GPIO #调入GPIO库
import time #调入时间库


BODYPORT = 12
LIGHTPORT = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(BODYPORT,GPIO.IN)
GPIO.setup(LIGHTPORT,GPIO.OUT)


while True:
        inValue = GPIO.input(BODYPORT)
        if (inValue == 0):
                print("Light Power ON")
                #GPIO.output(LIGHTPORT, False)
                GPIO.setup(LIGHTPORT,GPIO.LOW)
                time.sleep(5.0)
                #GPIO.output(LIGHTPORT, True)
                GPIO.setup(LIGHTPORT,GPIO.HIGH)
                print("Light Power OFF")
        time.sleep(0.01)
# Reset GPIO settings
GPIO.cleanup()
