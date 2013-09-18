#!/usr/bin/python
import RPIO, time

# John Scuteri's Button Board tester program
# This program is for John Jay's Button board
# This program was inspired by programs from the following website
# http://www.savagehomeautomation.com/projects/raspberry-pi-john-jays-8-led-button-breakout-board.html
# This program uses Python to make use of the Raspberry Pi's GPIO
# GPIO.RPI is replaced in this program with RPIO which need to be downloaded
# RPIO adds the resistor value modification
# As I am new at Python the following needs to be noted
# This program does not make use of arrays
# Future versions of this program will attempt to make use of arrays

# Setting resistor values for the switches
RPIO.setup(15, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(17, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(18, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(21, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(22, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(23, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(24, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(25, RPIO.IN, pull_up_down=RPIO.PUD_UP)

# Starting the LEDs
# LED 1
RPIO.setup(0, RPIO.OUT)
RPIO.output(0, RPIO.HIGH)
# LED 2
RPIO.setup(1, RPIO.OUT)
RPIO.output(1, RPIO.HIGH)
# LED 3
RPIO.setup(4, RPIO.OUT)
RPIO.output(4, RPIO.HIGH)
# LED 4
RPIO.setup(7, RPIO.OUT)
RPIO.output(7, RPIO.HIGH)
# LED 5
RPIO.setup(8, RPIO.OUT)
RPIO.output(8, RPIO.HIGH)
# LED 6
RPIO.setup(9, RPIO.OUT)
RPIO.output(9, RPIO.HIGH)
# LED 7
RPIO.setup(10, RPIO.OUT)
RPIO.output(10, RPIO.HIGH)
# LED 8
RPIO.setup(11, RPIO.OUT)
RPIO.output(11, RPIO.HIGH)

# Seed values
inputValue1 = True
inputValue2 = True
inputValue3 = True
inputValue4 = True
inputValue5 = True
inputValue6 = True
inputValue7 = True
inputValue8 = True
while True:
	# Memories of past values
	# these will be used for making sure the button push
	# only registers once per press
	hold1 = inputValue1
	hold2 = inputValue2
	hold3 = inputValue3
	hold4 = inputValue4
	hold5 = inputValue5
	hold6 = inputValue6
	hold7 = inputValue7
	hold8 = inputValue8
	inputValue1 = RPIO.input(15)
	# ^ Gets the input value from Pin 15
    if (inputValue1 == False):
        if (hold1 == True):
        	# ^ Tests for previous value to make sure it registers once
        	print("Button 1 pressed ")
        	RPIO.output(0, RPIO.LOW)
        	# ^ Turns the LED off
        else:
        	RPIO.output(0, RPIO.HIGH)
        	# ^ Turns the LED back on
        time.sleep(.3)
        # ^ Prevents the Led from blinking really fast
        # but creates the problem of the LED not turning
        # back on if the button is pressed too fast
    inputValue2 = RPIO.input(17)
    if (inputValue2 == False):
        if (hold2 == True):
        	print("Button 2 pressed ")
        	RPIO.output(1, RPIO.LOW)
        else:
        	RPIO.output(1, RPIO.HIGH)
        time.sleep(.3)
    inputValue3 = RPIO.input(18)
    if (inputValue3 == False):
        if (hold3 == True):
        	print("Button 3 pressed ")
        	RPIO.output(4, RPIO.LOW)
        else:
        	RPIO.output(4, RPIO.HIGH)
        time.sleep(.3)
    inputValue4 = RPIO.input(21)
    if (inputValue4 == False):
        if (hold4 == True):
        	print("Button 4 pressed ")
        	RPIO.output(7, RPIO.LOW)
        else:
        	RPIO.output(7, RPIO.HIGH)
        time.sleep(.3)
	inputValue5 = RPIO.input(22)
    if (inputValue5 == False):
		if (hold5 == True):
        	print("Button 5 pressed ")
        	RPIO.output(8, RPIO.LOW)
        else:
        	RPIO.output(8, RPIO.HIGH)
        time.sleep(.3)
    inputValue6 = RPIO.input(23)
    if (inputValue6 == False):
        if (hold6 == True):
        	print("Button 6 pressed ")
        	RPIO.output(9, RPIO.LOW)
        else:
        	RPIO.output(9, RPIO.HIGH)
        time.sleep(.3)
    inputValue7 = RPIO.input(24)
    if (inputValue7 == False):
		if (hold7 == True):
        	print("Button 7 pressed ")
        	RPIO.output(10, RPIO.LOW)
        else:
        	RPIO.output(10, RPIO.HIGH)
        time.sleep(.3)
    inputValue8 = RPIO.input(25)
    if (inputValue8 == False):
    	if (hold8 == True):
        	print("Button 8 pressed ")
        	RPIO.output(11, RPIO.LOW)
        else:
        	RPIO.output(11, RPIO.HIGH)
        time.sleep(.3)
    time.sleep(.01)
