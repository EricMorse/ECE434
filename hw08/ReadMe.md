# Homework 8: Project  
BBIO Project information will be updated on wiki.  
BBIO file is mostly finished with the exception of event detection.  
PWM file is finished.  
Pinmux file is briefly started.  
Project is being developed for kernel 4.19 only.  

# Homework 8: PRU  
### TABLE  
Need lots of oscilliscope captures for the table  

# Homework 8: Blinking an LED
### Answers to Questions  
make TARGET=hello.pru0 will run the PRU code.  
The code __halt() stops the PRU code, which is run by the code itself.  
### Installation Instructions
must type these commands to run hello.PRU0:  
config-pin P9_31 gpio
make TARGET=hello.pru0

### Notes to self:  
code works, but I need to run oscilliscope captures  

# Homework 8: PWM Generator

### Installation Instructions
must type these commands to run pwm1.pru0.c:  
config-pin P9_31 pruout  
export TARGET=pwm1.pru0  
make

# Homework 8: Controlling PWM Frequency
### Question Responses
What output pins are being driven: P9_31 P9_29 P9_30 and P9_28  
What's the highest frequency with four channels?  
Is there jitter?  
Does pwm-test.c work?  Yes, output is below:  
Servo tester  
Using /dev/mem.  
CountOn: 1, countOff: 19, count: 20  
countOn: 2, countOff: 18, count: 20  
countOn: 3, countOff: 17, count: 20  
countOn: 4, countOff: 16, count: 20  
munmap succeeded  
