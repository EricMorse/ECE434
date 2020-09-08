#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
from os import system, name

# Created by Eric Morse
# displays instructions for user
system('clear')
print("Etcher Sketch program created by Eric Morse")
print("program will ask for a command for the cursor")
print("up makes cursor go up; down makes the cursor go down")
print("left makes cursor go left; right makes the cursor go right")
print("stop quits the program; clear creates an X where the cursor is")
print("reset will reset the screen")
# initializes etcher sketch
dimensional_size = int(input("Input dimesion size of Etcher Sketch = "))
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
  print("stop will quit program; clear will create X; reset clears screen")
  move_command = str(input("Which direction to move? ")).lower()
  system('clear')
  print("You chose " + move_command)
  if move_command == "clear":
    etcher_screen[cursor_position[0]][cursor_position[1]] = "X"
  elif move_command == "reset":
    etcher_screen = [[" "] * dimensional_size for i in range(dimensional_size)]
  elif move_command == "left":
    if cursor_position[1] == 0:
      print("Error: can't go left")
    else:
      cursor_position[1] -= 1
  elif move_command == "right":
    if cursor_position[1] == dimensional_size - 1:
      print("Error: can't go right")
    else:
      cursor_position[1] += 1
  elif move_command == "up":
    if cursor_position[0] == 0:
      print("Error: can't go up")
    else:
      cursor_position[0] -= 1
  elif move_command == "down":
    if cursor_position[0] == dimensional_size - 1:
      print("Error: can't go down")
    else:
      cursor_position[0] += 1
  elif move_command != "stop": print("Invalid command")
  if move_command != "stop": 
    print("cursor position=  " + str(cursor_position[0]) + " " + str(cursor_position[1]))
