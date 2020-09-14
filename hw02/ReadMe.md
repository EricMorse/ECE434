# Homework 2: Buttons and LEDs

###Description
Buttons and LEDs is a program that turns on an LED when corresponding button is pushed.
While a button is pushed, the LED that is immediately to the left of the button will turn on.

##Instructions
Push the buttons, the lights will turn off when the corresponding button to the right of it is released

# Homework 2: Measuring a gpio pin

## Answer to Questions
Measurement | togglegpio.sh | togglegpio.py | togglegpio.c
Min Voltage | 3.52 |3.52 |3.52
Max Voltage |-0.16 |-0.08 |-0.08
Close to 100ms|No|Yes |Yes
Why they differ|Processor burden |NA |NA
Processor%|3.9 |0 |0
sleep time attempts| See Table 2-1| See Table 2-2| See Table 2-3
is period stable|yes|yes |yes
stable in vi|no|yes |yes
clean up impact|No |NA |NA
Do sh lessen period| |NA |NA
shortest period|18.6 |0.42 |0.36

**Explanation of Processor burden on why they differ**
The shell script has noticable processor % usage which causes the processor to lag when toggling, because it has to run other shell processes in the shell code

### Table 2-1 Togglegpio.sh sleep time attempts
Sleep Time(s) | Period(ms) | Processor%| Stable
0.1|244|3.9|yes
0.05|144|5.9|yes
0.02|83|10.5|no
0.01|63.5|13.5|no
0.005|52.5|23|no
0.002|48|19.2|no
0.001|52|18.6|no


### Table 2-1.2 Togglegpio.sh shell version
Sleep Time(s) | Period(ms) | Processor%| Stable
0.1|231|2.6| yes
0.05|131|3.3| yes
0.02|70|6.6| yes
0.01|50.7|9.8 | no
0.005|41 |12.2|no
0.002|35 |14.6|no
0.001|33.5 |16.8|no

### Table 2-2 Togglegpio.py sleep time attempts
Sleep Time(s) | Period(ms) | Processor%|Stable
0.1|200.4|0|Yes
0.05|100.8|0.7|Yes
0.02|40.5|1.3|Yes
0.01|20.44|2.0|Yes
0.005|10.44|4.0|Yes
0.002|4.4|8.6|No
0.001|2.44|13.6|No
0.0005|1.4|22.3|No
0.0002|0.8|34.5|No
0.0001|0.58|47|No
0.00005|0.5|58.8|No
0.00002|0.42|75|No

### Table 2-2.2 Togglegpio.py shell comparison
Sleep Time(s)| Python period(ms)| Shell period(ms)
0.1|200.4|244
0.05|100.8|144
0.02|40.5|83
0.01|20.44|63.5
0.005|10.44|52.5
0.002|4.4|48
0.001|2.44|52


### Table 2-3 Togglegpio.c sleep time attempts
Sleep Time(s) | Period(ms) | Processor%|Stable
0.1|200.4|0|Yes
0.05|100.4|0.7|Yes
0.02|40.4|0.7|Yes
0.01|20.3|1.3|No
0.005|10.3|2|No
0.002|4.3|5.4|No
0.001|2.3|10.4|No
0.0005|1.32|18.3|No
0.0002|0.7|23.5|No
0.0001|0.5|50.8|No
0.00005|0.4|59.1|No
0.00002|0.36|100|No

### Table 2-3.2 Togglegpio.c lseek() comparison
Sleep Time| OpenFile Period(ms)| lseek() Period(ms)
0.1| |

# Homework 2: GPIOD Toggle

## Toggle 1 bit comparison
C 1bit| Python 1bit| Shell 1 bit
3.36 us|17 us| 100 us

## Toggle 2 bit comparison
C 2bit| Python 2 bit
3.6 us|18 us

# Homework2 : Security
nothing to report.  

# Homework 2: Etch-a-sketch

## Description
It takes a command line to input the dimensions of the Etcher Etcher Sketch board
The board is square so argument 1 is the only input for the dimensions
It creates a blank board and allows user to move cursor with buttons

## Instructions
Locate the button closest to the power jack of the Beaglebone Black, I will call that the leftmost button.
Rotate the board so that it is to the left of the other buttons.
Pushing the leftmost button will move the cursor up.
The button to the right of it will move the cursor down.
The middle button will move the cursor left.
The button to the right of that will move the cursor right.
The rightmost button will clear the board of X.

Leftmost|next|middle|right of middle|rightmost
up|down|left|right|clear
