# Homework 5: Make
### Questions from Part A
1. Target = app.o
2. Dependency = app.c
3. Command = gcc

What does -c do?  It tells compiler to not discard comments.  All comments are passed through to the output file, except for comments in directives.

# Homework 5: Installing the Kernel Source
### On host
Kernel version = 5.4.0-48
### On bone
Kernel Version = 5.4.66-ri-r18

# Homework 5: Cross-Compiling

### Output of program on host
Hello, World! Main is execuating at 0x55f8f41f96aa
This address (0x7ffd98d0ebd0) is in our stack frame
This address (0x55f7f43fa018) is in our bss section
This address (0x55f7f43fa010) is in our data section

### Output of program on bone:
Hello, World! Main is execuating at 0x4b95ad
This address (0xbee1bbe0) is in our stack frame
This address (0x4ca010) is in our bss section
This address (0x4ca008) is in our data section

###### Minor additional notes
bone output has ssh messages cleaned from it

# Homework 5: Kernel Modules
### hello output
[  +0.006892] EBB: Hello world from the BBB LKM!
[Oct 5 02:20] EBB: Goodbye world from the BBB LKM!

**after passing parameters**
[Oct 5 02:21] EBB: Hello EricMorse from the BBB LKM!
[Oct 5 02:22] EBB: Goodbye EricMorse from the BBB LKM!

### ebbchar
[Oct 5 02:28] EBBCHar: Initializing the EBBChar LKM
[  +0.000049] EBBChar: registered correctly with major number 238
[  +0.000141] EBBChar: device class registered correctly
[  +0.006519] EBBChar: device class created correctly
[ +11.442904] EBBChar: Device has been opened 1 time(s)
[  +6.877473] EBBChar: Received 14 characters from the user
[ +32.393522] EBBChar: Sent 14 characters to the user
[  +0.000871] EBBChar: Device successfully closed

### Gpio_test
gpio_test turns off the LED when the button is pressed, and turns it back on when the button is released.
The button connects to P9_15 and the LED connects to P9_16.
###### To run Gpio_test
run with commands:
make
sudo insmod gpio_test.ko
sudo rmmod gpio_test
### gpio_test example
gpio_test2
### LED example
needs to be done
