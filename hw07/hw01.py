#!/usr/bin/env python3
#import Adafruit_BBIO.GPIO as GPIO
#from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2b, eQEP1
from os import system, name
from flask import Flask, render_template, request
import smbus
import time

bus = smbus.SMBus(2)	# Use i2c bus 2
matrix = 0x70		# Use Address 0x70

# Returns modified hex number
def modifyBit(number, position, value):
  mask = 1 << position
  return (number & ~mask) | ((value << position) & mask)

app = Flask(__name__)
LED_screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

# initializes etcher LED screen
bus.write_byte_data(matrix, 0x21, 0)	# Starts oscillator (page 10)
bus.write_byte_data(matrix, 0x81, 0) 	# Display on, blink off (page 11)
bus.write_byte_data(matrix, 0xe7, 0)	# Full Brightness (page 15)

bus.write_i2c_block_data(matrix, 0, LED_screen) # clears LED screen
cursor_position = [0,0]

@app.route("/")
def index():
	global cursor_position
	global LED_screen
	templateData = {
		'title' : 'Etcher Sketch',
	}
	return render_template('index.html', **templateData)

@app.route("/<action>")
def action(action):
	global LED_screen
	global cursor_position
	if action == "up":
		if cursor_position[0] != 0:
			cursor_position[0] -= 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if action == "down":
		if cursor_position[0] != 7:
			cursor_position[0] += 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if action == "left":
		if cursor_position[1] != 0:
			cursor_position[1] -= 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	if action == "right":
		if cursor_position[1] != 7:
			cursor_position[1] += 1
			LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
			bus.write_i2c_block_data(matrix, 0, LED_screen)
	templateData = {
	}
	return render_template('index.html', **templateData)

# Created by Eric Morse
# displays instructions for user
system('clear')
print("Etcher Sketch program created by Eric Morse")
#print("The program uses rotary encoders for input")
# initializes rotary encoder pins
#system('config-pin P8_41 eqep')
#system('config-pin P8_42 eqep')
#system('config-pin P8_33 eqep')
#system('config-pin P8_35 eqep')

# Returns modified hex number
def modifyBit( number, position, value):
  mask = 1 << position
  return (number & ~mask) | ((value << position) & mask) 

# main loop
def main():
  bus = smbus.SMBus(2)       # Use i2c bus 2
  matrix = 0x70              # Use Addresss

  # enables the rotary encoders
  myEncoder1 = RotaryEncoder(eQEP2b)
  myEncoder2 = RotaryEncoder(eQEP1)
  myEncoder1.enable()
  myEncoder2.enable()
  myEncoder1.setAbsolute() # sets rotary position to 0
  myEncoder2.setAbsolute() # sets rotary position to 0

  dimensional_size = 8       # size of LED matrix
  # initializes etcher LED screen
  etcher_screen = [[" "]*dimensional_size for _ in range(dimensional_size)]
  LED_screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
  ]

  bus.write_byte_data(matrix, 0x21, 0)  # Starts oscillator (page 10)
  bus.write_byte_data(matrix, 0x81, 0)  # Display on, blink 0ff (page 11)
  bus.write_byte_data(matrix, 0xe7, 0)  # Full Brightness (page 15)

  bus.write_i2c_block_data(matrix, 0, LED_screen)  # clears LED screen
  cur_position1 = myEncoder1.position # current position of encoder 1
  cur_position2 = myEncoder2.position # current position of encoder 2
  etcher_string = ""
  cursor_position = [0, 0]
  # loop for the etcher sketch operation
  while True:
    # draws the etcher sketch board
    old_position1 = cur_position1
    old_position2 = cur_position2
    header_string = "    "
    for x in range(0, dimensional_size+1):
      if x == 0:
        for z in range(0, dimensional_size):
          header_string += str(z) + " "
        print(header_string)
      else:
        for y in range(0, dimensional_size):
          if y == 0: etcher_string = str(x-1) + ":" + "  "
          etcher_string = etcher_string + etcher_screen[x-1][y] + " "
        print(etcher_string)
        etcher_string = ""
    # gets user input for move_command and executes it
    print("right encoder clockwide moves up, counterclockwise moves down")
    print("left encoder clockwise moves right, counterclockwise moves left")
    # loop to wait for user movement on rotary encoders
    while((old_position1 == cur_position1) and (old_position2 == cur_position2)):
      cur_position1 = myEncoder1.position
      cur_position2 = myEncoder2.position
      time.sleep(0.2)
    system('clear')
    # processes rotary encoder movement
    if old_position1 > cur_position1:
      if cursor_position[1] == 0:
        print("Error: can't go left")
      else:
        cursor_position[1] -= 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
        LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
        bus.write_i2c_block_data(matrix, 0, LED_screen)
    elif old_position1 < cur_position1:
      if cursor_position[1] == dimensional_size - 1:
        print("Error: can't go right")
      else:
        cursor_position[1] += 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
        LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
        bus.write_i2c_block_data(matrix, 0, LED_screen)
    elif old_position2 > cur_position2:
      if cursor_position[0] == 0:
        print("Error: can't go up")
      else:
        cursor_position[0] -= 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
        LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
        bus.write_i2c_block_data(matrix, 0, LED_screen)
    elif old_position2 < cur_position2:
      if cursor_position[0] == dimensional_size - 1:
        print("Error: can't go down")
      else:
        cursor_position[0] += 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
        LED_screen[cursor_position[1]*2] = modifyBit(LED_screen[cursor_position[1]*2], 7-cursor_position[0], 1)
        bus.write_i2c_block_data(matrix, 0, LED_screen)
    else:
      print("Error: no movement detected")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8081, debug=True)
