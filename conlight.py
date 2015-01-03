#!/usr/bin/python
#coding: utf8
import RPi.GPIO as GPIO 
import time
import sys

LUMPORT=15
LIGHTPORT=11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LUMPORT,GPIO.IN)
GPIO.setup(LIGHTPORT,GPIO.OUT)

if sys.argv[1]=="open":
    while True:
        inputValue = GPIO.input(LUMPORT)
        if(inputValue==0):
            print("THE LED IS ON NOW")
            GPIO.setup(LIGHTPORT,GPIO.LOW)
        else:
            print("THE LED IS OFF NOW")
            GPIO.setup(LIGHTPORT,GPIO.HIGH)
        time.sleep(5.0)

elif sys.argv[1]=="close":
    print("Auto light close")
    sys.exit()



