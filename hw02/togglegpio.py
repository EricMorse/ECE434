#!/usr/bin/env python3

# Blink pin 60 at 1 Hz
#
# Created by Eric Morse, 14 September 2020
# email: morsee [at] rose-hulman <dot> edu

import Adafruit_BBIO.GPIO as GPIO
import gpiod
import time
import sys
import signal

#import C Shared library

from ctypes import *
so_file = "./gpio-utils.so"
c_functions = CDLL(so_file)

toggle = 0
gpio = 60
filename = "togglegpio.py"
SYSFS_GPIO_DIR = "/sys/class/gpio"
MAX_BUF = 64
ADC_BUF = 1024
SYSFS_AIN_DIR = "/sys/devices/ocp.2/helper.11"
keepgoing = 1
def signal_handler(sig, frame):
  print("Ctrl-C pressed, cleaning up and exiting..")
  global keepgoing 
  keepgoing = 0

print("Usage: " + sys.argv[0] + "<on/off time in us>")
print("Toggle gpio 60 at the period given")

onOffTime = int(sys.argv[1])
print("********************************")
print("* Welcome to PIN Blink program *")
print("* ....blinking gpin 60         *")
print("* ....period of " + str(2*onOffTime) + " us...........*")
print("********************************")

signal.signal(signal.SIGINT, signal_handler)
#Using sysfs we need to write the gpio number to /sys/class
#This will create the folder /sys/class/gpio/gpio60
c_functions.gpio_export(gpio)

print("...export file accessed, new pin now accessible")

#Set Direction
c_functions.gpio_set_dir(gpio, "out")
print("...direction set to output")

gpio_fd = c_functions.gpio_fd_open(gpio, 'O_RDONLY')

while(keepgoing):
  toggle = not toggle
  c_functions.gpio_set_value(gpio, toggle)
  time.sleep(onOffTime/1000000.0)

c_functions.gpio_fd_close(gpio_fd)
