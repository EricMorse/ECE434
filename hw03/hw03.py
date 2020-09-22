#!/usr/bin/env python3
# Read a TMP101 sensor

# library imports for the program
import Adafruit_BBIO.GPIO as GPIO
import smbus
import sys
import time
from os import system, name

# initializes the temp sensor
bus = smbus.SMBus(2)
address = 0x48  # address of the first temp sensor
address2 = 0x4a # address of the second temp sensor

# initializes the alert pins of temp sensor
alert1 = "P9_21"
alert2 = "P9_22"
GPIO.setup(alert1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(alert2, GPIO.IN, GPIO.PUD_UP)
T_low = 0x18
T_high = 0x1A
if sys.argv[1]:
  T_low = sys.argv[1]

if sys.argv[2]:
  T_high = sys.argv[2]

# sets the temp sensor settings
system('i2cset -y 2 0x48 1 0x02')  # sets config register for 0x48
system('i2cset -y 2 0x4a 1 0x02')  # sets config register for 0x4a
system("i2cset -y 2 0x48 2 " + str(T_low))  # sets T_low register for 0x48
system("i2cset -y 2 0x4a 2 " + str(T_low))  # sets T_low register for 0x4a
system("i2cset -y 2 0x48 3 " + str(T_high))  # sets T_high register for 0x48
system("i2cset -y 2 0x4a 3 " + str(T_high))  # sets T_high register for 0x4a

# main loop 
while True:
  # stores alert input
  state1 = GPIO.input(alert1)
  state2 = GPIO.input(alert2)
  # processes 0x48 alert triggering
  if state1 == 0:
    time.sleep(0.25)
    temp = bus.read_byte_data(address, 0)
    temp3 = temp*9/5+32
    print("Temp = " + str(temp3))
  # processes 0x4a alert triggering
  if state2 == 0:
    time.sleep(0.25)
    temp2 = bus.read_byte_data(address2, 0)
    temp4 = temp2*9/5 + 32
    print("Temp2 = " + str(temp4))
