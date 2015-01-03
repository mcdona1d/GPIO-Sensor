#!/usr/bin/python
#coding: utf8
import sys
import RPi.GPIO as GPIO

LIGHTPORT=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LIGHTPORT,GPIO.OUT)
if sys.argv[1]=="open":
        GPIO.setup(LIGHTPORT,GPIO.LOW)
elif sys.argv[1]=="close":
        GPIO.setup(LIGHTPORT,GPIO.HIGH)


