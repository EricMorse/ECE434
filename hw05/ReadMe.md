# Homework 5: Make
### Questions from Part A
1. Target = app.o
2. Dependency = app.c
3. Command = gcc

What does -c do?  It tells compiler to not discard comments.  All comments are passed through to the output file, except for comments in directives.

# Homework 5: Installing the Kernel Source
Uses build_deb.sh method
### On host
Kernel version = 5.4.0-48
### On bone
Kernel Version = 4.19.94-ti-r50

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

### Gpio_test
needs to be done
### gpio_test example
needs to be done
### LED example
