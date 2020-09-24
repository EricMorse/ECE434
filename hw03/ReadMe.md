# Homework 3: TMP101

### Description
The two TMP101s will trigger an alert and display temperature during an alert when T_high or T_low are reached.

### Instructions
Push finger against either TMP101 to heat them up and trigger an alert.  Release finger to reduce temperature.

### Execution
*hw03.py* takes two arguments.  The first is T_low temperature setting.  The second is T_high temperature setting.
"./hw03.py 0x19 0x1a" will execute the code with 0x19 as T_low alert setting and 0x1a as T_high alert.

*readi2c.py* reads the temperatures in python and does not take arguments.
*readi2c.sh* reads the temperatures in shell and does not take arguments.

# Homework 3: Etch A Sketch

### Description
It uses an LED matrix to display the Etch A Sketch board.
It uses two rotary encoders to move the cursor around the board, and light up the board.

### Instructions
Encoder closest to LED matrix will be referred to as the left encoder; other is the right encoder.
Left encoder moves cursor left and right.
Right encoder moves cursor up and down.

Direction desired | Encoder to move | Direction of rotation
------------------|-----------------|---------------------
left| left | clockwise
right| left | counter-clockwise
up| right | clockwise
down | right | counter-clockwise

### Execution of code
There are no special library calls or arguments for this program.
./hw01.py will execute the code
