#!/usr/bin/env python3
#import Adafruit_BBIO.GPIO as GPIO
#from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2b, eQEP1
from os import system, name
from flask import Flask, render_template, request
import smbus
import time
import blynklib
import blynktimer
import os

bus = smbus.SMBus(2)	# Use i2c bus 2
matrix = 0x70		# Use Address 0x70

BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispacther instacne
#timer = blynktimer.Timer()
# Returns modified hex number
def modifyBit(number, position, value):
  mask = 1 << position
  return (number & ~mask) | ((value << position) & mask)

LED_screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

# initializes etcher LED screen
bus.write_byte_data(matrix, 0x21, 0)	# Starts oscillator (page 10)
bus.write_byte_data(matrix, 0x81, 0) 	# Display on, blink off (page 11)
bus.write_byte_data(matrix, 0xe7, 0)	# Full Brightness (page 15)

bus.write_i2c_block_data(matrix, 0, LED_screen) # clears LED screen
cursor_position = [0,0]

# Register Virtual Pins
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
	# print('Current V{} value: {}'.format(pin, value))
	global LED_screen
	global cursor_position
	global matrix
	global bus
	# detects which button was pressed and responds to press
	if (pin == 3 and value==['1']):
		if cursor_position[0] != 0:
			cursor_position[0] -= 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if (pin == 4 and value==['1']):
		if cursor_position[0] != 7:
			cursor_position[0] += 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if (pin == 5 and value==['1']):
		if cursor_position[1] != 0:
			cursor_position[1] -= 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if (pin == 6 and value==['1']):
		if cursor_position[1] != 7:
			cursor_position[1] += 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)

# Created by Eric Morse
while True:
   blynk.run()
