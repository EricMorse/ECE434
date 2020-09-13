#!/usr/bin/env python3
# Toggles the P9_14 pin as fast as it can.  P9_14 is line 18 on chip 1.
# Toggles P9_16 pin as fast as it can.  P9_16 is line 19 on chip 1.
# Toggles P9_15 pin as fast as it can.  P9_15 is line 16 on chip 1.
# Toggles P9_12 pin as fast as it can.  P9_12 is line 28 on chip 1.
import gpiod
import time
chip = gpiod.Chip('gpiochip1')
lines = chip.get_lines([16, 18, 19, 28])
lines.request(consumer='blink', type=gpiod.LINE_REQ_DIR_OUT)

while True:
  lines.set_values([0, 0, 0, 0])
  time.sleep(0.1)
  lines.set_values([1, 1, 1, 1])
  time.sleep(0.1)

