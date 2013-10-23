#!/usr/bin/python
import RPIO, time

# John Scuteri's Button Board tester program  v2.0
# This program is for John Jay's Button board
# This program was inspired by programs from the following website
# http://www.savagehomeautomation.com/projects/raspberry-pi-john-jays-8-led-button-breakout-board.html
# This program uses Python to make use of the Raspberry Pi's GPIO
# GPIO.RPI is replaced in this program with RPIO which need to be downloaded
# RPIO adds the resistor value modification
# The RPIO API is under LGPL V(3) licence
# The licence of RPIO is here https://github.com/metachris/RPIO/blob/master/LICENSE.txt
# I am new at Python

# Setting resistor values for the switches

Button = [15,17,18,21,22,23,24,25]
LED = [0,1,4,7,8,9,10,11]
Current = [True, True,True, True,True, True,True, True ]
Save = [True, True,True, True,True, True,True, True ]

# Setting resistor values for the switches
for x in Button:
        RPIO.setup(x, RPIO.IN, pull_up_down=RPIO.PUD_UP)

# Starting the LEDs
for x in LED:
        RPIO.setup(x, RPIO.OUT)
        RPIO.output(x, RPIO.HIGH)

while True:
while True:
        for l, c, s, b in zip(LED,Current, Save, Button):
                s = c
                c = RPIO.input(b)
                if (c == False):
                        if (s == True):
                                # ^ Tests for previous value to make sure it registers once
                                print("Button pressed ")
                                #Notes a button was pressed. Future versions will bring back which button
                                RPIO.output(l, RPIO.LOW)
                                # ^ Turns the LED off
                                time.sleep(2)
																# ^ Prevents the Led from blinking really fast

                else:
                        RPIO.output(l, RPIO.HIGH)
                                # ^ Turns the LED back on
                                