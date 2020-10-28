# Homework 8: Project  
BBIO Project information will be updated on wiki.  
BBIO file is mostly finished with the exception of event detection.  
PWM file is finished.  
Pinmux file is briefly started.  
Project is being developed for kernel 4.19 only.  

# Homework 8: PRU  
### TABLE  
Need lots of oscilliscope captures for the table  
pwm1.pru0 is tek00011.png.  Period is 1s.  
I could not get oscilliscope to capture duty cycle of 0.  Period should be 15ns.  
pwm4.pru0 is tek00014.png.  Period is 3.06us for P9_31.  
pwm5.pru0 is tek00015.png.  Period is 595ns for P9_31.  
pwm6.pru0 is tek00016.png.  Period is 640.2ns for P9_31.  All channels start at the same time now.   
pwm7.pru0 is tek00017.png.  Period is 369.3ns for P9_31.  Last two channels vanished.  
pwm8.pru0 is tek00018.png.  Period is 460ns for P9_31.  
# Homework 8: Blinking an LED  
### Answers to Questions  
make TARGET=hello.pru0 will run the PRU code.   
The code __halt() stops the PRU code, which is run by the code itself.    
The fastest that I can toggle it is 80 ns.  There is a lot of jitter and it is unstable.  
At that speed, the waveform looks more like an analog sinusoid than it does rectangular pwm.  
### Installation Instructions  
must type these commands to run hello.PRU0:  
config-pin P9_31 gpio  
config-pin P9_31 out  
make TARGET=hello.pru0  

### Notes to self:  
code works, but I need to run oscilliscope captures  

# Homework 8: PWM Generator  
### Answers to Questions  
The pwm generator is stable with a Std Dev of 11.4 microseconds.  
It appears to be perfectly rectangular PWM with a slight ripple at the top of the pwm.  
Scope capture is tek000010.png  
### Installation Instructions  
must type these commands to run pwm1.pru0.c:  
config-pin P9_31 pruout  
export TARGET=pwm1.pru0  
make  

# Homework 8: Controlling PWM Frequency  
### Question Responses  
What output pins are being driven: P9_31 P9_29 P9_30 and P9_28  
What's the highest frequency with four channels?  326 Hz
Is there jitter?  Yes, it has a lot of overshoot and ripple.
Does pwm-test.c work?  Yes, output is below:  
Servo tester  
Using /dev/mem.  
CountOn: 1, countOff: 19, count: 20  
countOn: 2, countOff: 18, count: 20  
countOn: 3, countOff: 17, count: 20  
countOn: 4, countOff: 16, count: 20  
munmap succeeded  

# Homework 8: Reading Input at Regular Intevals  
tek00021.png is waveform capture of button press.  Green is the button, and yellow is P9_31.  
There appears to be a 39.62ns delay between the input and output.  

# Homwork 8: AnalogWaveGenerator  

