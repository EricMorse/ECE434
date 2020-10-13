# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project - *I like the python project*
|  1 | Makefile - *Makefile missing*
|  4 | Kernel Source
|  2 | Cross-Compiling
|  8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  1 | Extras
| 18 | **Total**

*My comments are in italics. --may*

# Homework 5: Make
### Questions from Part A
1. Target = app.o
2. Dependency = app.c
3. Command = gcc

What does -c do?  It tells compiler to not discard comments.  All comments are passed through to the output file, except for comments in directives.

# Homework 5: Installing the Kernel Source
Uses build_deb.sh method.
### On host
Kernel version = 5.4.0-48
### On bone
Kernel Version = 5.4.66-ri-r18

# Homework 5: Cross-Compiling

### Output of program on host:
```
Hello, World! Main is executing at 0x55f8f41f96aa
This address (0x7ffd98d0ebd0) is in our stack frame
This address (0x55f7f43fa018) is in our bss section
This address (0x55f7f43fa010) is in our data section
```

### Output of program on bone:
```
Hello, World! Main is executing at 0x4b95ad
This address (0xbee1bbe0) is in our stack frame
This address (0x4ca010) is in our bss section
This address (0x4ca008) is in our data section
```

###### Minor additional notes
bone output has ssh messages cleaned from it.

# Homework 5: Kernel Modules

### Gpio_test
This program is located in folder gpio_test1.
gpio_test is a kernel program that turns off an LED when a button is pressed, and turns it back on when the button is released.
###### Setup instructions
button must be connected to P9_15.
LED must be connected to P9_16.
###### Code execution instructions
To run the code, type the following commands:
make.
sudo insmod gpio_test.ko.
###### Code halting instructions
To stop the code, run sudo rmmod gpio_test.
### gpio_test example
This program is located in folder gpio_test2.
gpio_test is a kernel program that changes the state of an LED when the corresponding button is pushed.
Two buttons toggle the two LEDs.
###### Setup instructions
button must be connected to P8_15 and P8_18.
LEDs must be connected to P9_12 and P9_14.
###### Code execution instructions
to run the code, type the following commands:
make.
sudo insmod gpio_test.ko.
###### Code halting instructions
to stop the code, run sudo rmmod gpio_test.
### LED example
This program is located in folder led.
led program blinks two LEDs at different periods.
The default periods are set to 1000 for P9_14 and 100 for P9_12.
###### Setup instructions
LEDs must be connected to P9_12 and P9_14.
###### Code execution instructions
To run the code, type the following commands:
make.
sudo insmod led.ko.
###### Code halting instructions
To stop the code, run sudo rmmod led.

