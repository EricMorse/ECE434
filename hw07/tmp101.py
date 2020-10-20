#!/usr/bin/env python3
# Blink read the temperature from a BMP085 and display it
import blynklib
import blynktimer
import os
import smbus
import time

# Run setup.sh to create a new bmp085
#BMP085='/sys/class/i2c-adapter/i2c-2/2-0077/iio:device1/in_temp_input'
bus = smbus.SMBus(2)
address = 0x48

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()

oldtemp = 0
# Code below: register a timer for different pins with different intervals
# run_once flag allows to run timers once or periodically
@timer.register(vpin_num=10, interval=0.5, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    global oldtemp
    # Open the file with the temperature
    temp = bus.read_byte_data(address, 0)
    temp = temp*9/5+32
    # Only display if changed
    if(temp != oldtemp):
        print("Pin: V{} = {} F".format(vpin_num, str(temp)))
        # Send to blynk
        blynk.virtual_write(vpin_num, temp)
        oldtemp = temp

while True:
    blynk.run()
    timer.run()
