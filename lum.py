#!/usr/bin/python
#coding: utf8
import RPi.GPIO as GPIO #调入GPIO库
import time #调入时间库

LUMPORT=15
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LUMPORT,GPIO.IN) 

while True:
    inputValue = GPIO.input(LUMPORT)
    if(inputValue==0):
        print("THE LED IS ON NOW")
    else:
        print("THE LED IS OFF NOW")
    time.sleep(1.0)



