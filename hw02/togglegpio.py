#!/usr/bin/env python3

# Blink pin 60 at 1 Hz
#
# Created by Eric Morse, 14 September 2020
# email: morsee [at] rose-hulman <dot> edu

import Adafruit_BBIO.GPIO as GPIO
import gpiod
import time
import sys

toggle = 0
gpio = 60
filename = "togglegpio.py"
SYSFS_GPIO_DIR = "/sys/class/gpio"
MAX_BUF = 64
ADC_BUF = 1024
SYSFS_AIN_DIR = "/sys/devices/ocp.2/helper.11"

def gpio_export(gpio)

  length = filename + str(len(filename)) + SYSFS_GPIO_DIR + "gpio" + str(gpio)
  if(stat(filename, statBuffer) == 0): #It's already exported
    print("gpio%d is already exported.")
    return 0;
  fd = open(SYSFS_GPIO_DIR + "/export", O_WRONLY)
  return 1;
print("Usage: " + sys.argv[0] + "<on/off time in us>")
print("Toggle gpio 60 at the period given")

onOffTime = int(sys.argv[1])
print("********************************")
print("* Welcome to PIN Blink program *")
print("* ....blinking gpin 60         *")
print("* ....period of " + str(2*onOffTime) + " us...........*")
print("********************************")

#Using sysfs we need to write the gpio number to /sys/class
#This will create the folder /sys/class/gpio/gpio60
gpio_export(gpio)

printf("...export file accessed, new pin now accessible")

#Set Direction
gpio_set_dir(gpio, "out")
printf("...direction set to output")
