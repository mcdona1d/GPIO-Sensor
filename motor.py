#!/usr/bin/python
#coding: utf8

import RPi.GPIO as GPIO
import time
import sys
from array import *

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

steps    = int(sys.argv[1]);
clockwise = int(sys.argv[2]);

arr = [0,1,2,3];
if clockwise!=1:
    arr = [3,2,1,0];

ports = [40,38,36,35]
#步进电机IN1,IN2,IN3,IN4 GPIO 21（Pin 40），GPIO 20（Pin 38）, GPIO 16（Pin 36）, GPIO 19（Pin 35）

for p in ports:
    GPIO.setup(p,GPIO.OUT)
    
for x in range(0,steps):
    for j in arr:
        time.sleep(0.01)
        for i in range(0,4):
            if i == j:            
                GPIO.output(ports[i],True)
            else:
                GPIO.output(ports[i],False)
