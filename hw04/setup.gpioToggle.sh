#!/bin/bash
# Set up gpio 50 to read and gpio 51 to read
cd /sys/class/gpio
#echo 50 > export
#echo 51 > export
#echo 60 > export
#echo 07 > export
#echo 03 > export
echo 46 > export
echo 47 > export
#echo in  > gpio50/direction
#echo in > gpio51/direction
#echo in > gpio60/direction
#echo in > gpio07/direction
#echo in > gpio03/direction
echo in > gpio46/direction
echo in > gpio47/direction
