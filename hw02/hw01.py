#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
from os import system, name
import time
import sys

# Created by Eric Morse
# displays instructions for user
system('clear')
print("Etcher Sketch program created by Eric Morse")
print("program will ask for a command for the cursor")

#initializes the buttons
button1="P8_14"
button2="P9_41"
button3="P9_42"
button4="P9_24"
button5="P9_26"

def gpio_setup(button):
  #callback function for gpio setup
  GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
  return 0;

def caller(func, button):
  return func(button)

#uses callback to set up gpio
caller(gpio_setup, button1)
caller(gpio_setup, button2)
caller(gpio_setup, button3)
caller(gpio_setup, button4)
caller(gpio_setup, button5)

# initializes etcher sketch
dimensional_size = int(sys.argv[1])
etcher_screen = [[" "]*dimensional_size for _ in range(dimensional_size)]

etcher_string = ""
cursor_position = [0, 0]
move_command = ""
while(move_command != "stop"):
  # draws the etcher sketch board
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
  move_command = 0
  while True:
    state1 = GPIO.input(button1)
    state2 = GPIO.input(button2)
    state3 = GPIO.input(button3)
    state4 = GPIO.input(button4)
    state5 = GPIO.input(button5)
    if  state1:   # up button is pressed (button 1)
      GPIO.wait_for_edge(button1, GPIO.PUD_UP)
      system('clear')
      if cursor_position[0] == 0:
        print("Error: can't go up")
      else:
        cursor_position[0] -= 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
      break
    elif state2:  # down button is pressed (button 2)
      GPIO.wait_for_edge(button2, GPIO.PUD_UP)
      system('clear')
      if cursor_position[0] == dimensional_size - 1:
        print("Error: can't go down")
      else:
        cursor_position[0] += 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X" 
      break
    elif state3:  # left button is pressed (button 3)
      GPIO.wait_for_edge(button3, GPIO.PUD_UP)
      system('clear')
      if cursor_position[1] == 0:
        print("Error: can't go left")
      else:
        cursor_position[1] -= 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
      break
    elif state4: # right button is pressed (button 4)
      GPIO.wait_for_edge(button4, GPIO.PUD_UP)
      system('clear')
      if cursor_position[1] == dimensional_size - 1:
        print("Error: can't go right")
      else:
        cursor_position[1] += 1
        etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
      break
    elif state5:  # reset button is pressed (button 5)
      GPIO.wait_for_edge(button5, GPIO.PUD_UP)
      system('clear')
      etcher_screen == [[""] * dimensional_size for i in range(dimensional_size)]
      break
    
