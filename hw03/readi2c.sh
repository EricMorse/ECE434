#!/bin/sh
# From http://wh1t3s.com/2009/05/14/reading-beagleboard-gpio/
#
# Read some i2c addresses
# Mark A. Yoder 20-July-2012

#if [ $# -lt 2 ]; then
#    echo "Usage: $0 i2cBus ic2Addr1 ic2Addr2 ..."
#    exit 0
#fi

#i2cBus=$1
#shift

cleanup() { # echo a newline
  echo ""
  echo "Done"
  exit
}

trap cleanup SIGINT # call cleanup on Ctrl-C

# Read forever

while [ "1" = "1" ]; do
    temp=`i2cget -y 2 0x48`
    temp2=`i2cget -y 2 0x4a`
    temp=$(($temp *9/5+32))
    temp2=$(($temp2 *9/5+32))
    echo "${temp}\\t"
    echo "${temp2}\\t"
    sleep 0.2
    # Return to the start of the line, but not the next line
    echo "\\r"
done

cleanup # call the cleanup routine

