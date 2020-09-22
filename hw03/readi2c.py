#!/usr/bin/env python3
# Read a TMP101 sensor

import smbus
import time
from os import system, name

bus = smbus.SMBus(2)
address = 0x48
address2 = 0x4a

while True:
  temp = bus.read_byte_data(address, 0)
  temp2 = bus.read_byte_data(address2, 0)
  system('clear')
  temp = temp*9/5+32
  temp2 = temp2*9/5+32
  print("0x48 reads = " + str(temp))
  print("0x4a reads = " + str(temp2))
  time.sleep(0.25)
