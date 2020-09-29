# Homework 4: Memory Map
Memory map is drawn as a table

starting address | ending address | name of memory area | additional info
-----------------|----------------|---------------------|----------------
0x8000_0000|0xBFFF_FFFF|EMIF0 SDRAM| 16 bit External Memory
0x5600_0000|0x56FF_FFFF|SGX530| SGX530 Slave Port
0x54C0_0000|0x54FF_FFFF|ADC_TSC DMA| ADC_TSC DMA Port
0x5000_0000|0x50FF_FFFF|GPMC|GPMC Configuration registers
0x4C00_0000|0x4CFF_FFFF|EM1F0| EMIF0 Configuration Registers
0x4800_0000|0x48FF_FFFF| L4_PER| L4 Peripheral
0x4740_0000|0x4740_3FFF| USB | USB Peripheral registers
0x4600_0000|0x467F_FFFF|McASP Data| McASP Data Registers
0x44C0_0000|0x44FF_FFFF|L4_WKUP|L4_WKUP
ox4400_0000|0x44BF_FFFF| L3 CFG Regs| L3 Configuration Registers
0x4030_0000|0x4030_FFFF| L3 OCMC0| OCMC SRAM
0x402F_0400|0x402F_FFFF| SRAM internal| 32-bit
0x4000_0000|0x4002_BFFF| Boot ROM| 32-bit Ex/R Public
0x0000_0000|0x1FFF_FFFF| GPMC | External Memory


Starting address of EM1F0 SDRAM is 0x8000_0000
base address for each GPIO port registers (contained inside L4_PER address)
GPIO Port| Base Address| Ending Address
---------|-----------------|---------------
GPIO0|0x44E0_7000|0x44E0_7FFF
GPIO1|0x4804_C000|0x4804_CFFF
GPIO2|0x481A_C000|0x481A_CFFF
GPIO3|0x481A_E000|0x481A_EFFF

# Homework 4: GPIO via mmap
two programs that toggle gpio via mmap (togglegpio and gpioToggle)

### description of 2 programs
togglegpio toggles the P9_14 pin at a period set in commandline arguements.
gpioToggle turns on USR3 and USR1 led when P9_14 or P9_16 buttons are pressed.
### Instructions of 2 programs
togglegpio outputs to P9_14.
gpioToggle uses P8_15 and P8_16 as button inputs.  Push P8_15 button and USR3 lights up.  Push P8_16 button and USR1 lights up.
### Execution of 2 programs
togglegpio takes commandline arguement of onOffTime (period/2)
sudo ./togglegpio <onOffTime>
(example: sudo ./togglegpio 10000, will create a period of 20ms)

gpioToggle takes no commandline arguements, but it requires the same pin as togglegpio.
sudo ./gpioToggle will run the program.
If you have trouble running it, running setup_gpioToggle.sh might help

### Table comparison of GPIO port toggle
Sleep Time(s) | new program Period(ms)| old program Period(ms)
--------------|-------------------|-------------------------
0.1|200.2|200.4
0.05|100.1|100.4
0.02|40.2|40.4
0.01|20.17|20.3
0.005|10.17|10.3
0.002|4.17|4.3
0.001|2.17|2.3
0.0005|1.17|2.3
0.0002|0.56|2.3
0.0001|0.36|2.3
0.00005|0.26|2.3
0.00002|0.21|2.3
0.00001|0.18|2.3
usleep set to 0|0.16|2.3
no usleep|0.0003
Is not using usleep faster? yes, commenting out usleep makes period faster than usleep set to 0.

# Homework 4: i2c via Kernel Driver
readTemp is the program that will continuously read temp reading using kernel driver
Only root user can setup TMP101 device.
### instructions
press your finger against it to heat it up and release to cool it down.
### Execution
no commandline arguements, but it requires root access in a new window
Type list of commands below to setup tmp101 and run it
su
cd /sys/class/i2c-adapter/i2c-2
echo tmp101 0x48 > new_device
exit
sudo ./readTemp

#Homework 4: Control LED Matrix from a browser (Etch A Sketch program)

### Description
It uses an LED matrix to display the Etch A Sketch board.
It uses 4 buttons on webpage to move the cursor around the LED matrix
Webpage is at 192.168.7.2:8081
### Instructions
Four buttons appear on the webpage with a direction written on them.
Clicking on the button moves the cursor in that direction.
### Execution of code
There are no special library calls or arguments for this program.
./hw01.py will execute the code
You will need to open a web browser to 192.168.7.2:8081 to access the webpage.

# Homework 4: 2.4 inch TFT LCD Display
needs to be done
