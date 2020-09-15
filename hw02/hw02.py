#!/usr/bin/env python3

# Toggles the P9_14 pin as fast as it can.  P9_14 is line 18 on chip 1.
# Toggles P9_16 pin as fast as it can.  P9_16 is line 19 on chip 1.
# Toggles P9_15 pin as fast as it can.  P9_15 is line 16 on chip 1.
# Toggles P9_12 pin as fast as it can.  P9_12 is line 28 on chip 1.
# Get the value of P8_16 and write it to P9_14.
# P8_15 is line 14 on chip 1.  P9_14 is line 18 on chip 1.
import Adafruit_BBIO.GPIO as GPIO
import gpiod
import time
import sys

button1="P8_14"
button2="P9_41"
button3="P9_42"
button4="P9_24"

LED1 = "P9_13"
LED2 = "P9_14"
LED3 = "P9_15"
LED4 = "P9_16"

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)

print("Running...")

def button_response(button, led):
  # callback function
  state = GPIO.input(button)
  if state:
    GPIO.output(led, state)
    if button == button1:
      print("Button1 pressed")
    elif button == button2:
      print("Button2 pressed")
    elif button == button3:
      print("Button3 pressed")
    elif button == button4:
      print("Button4 pressed")
    GPIO.wait_for_edge(button, GPIO.BOTH)
  else:
    GPIO.output(led, 0)
  return 0;

def caller(func, button, led):
  return func(button, led)

while True:
  caller(button_response, button1, LED1)
  caller(button_response, button2, LED2)
  caller(button_response, button3, LED3)
  caller(button_response, button4, LED4)
