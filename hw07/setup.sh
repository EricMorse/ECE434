export BLYNK_AUTH='4CGBPaoEzjFhc9lU4zaNZwWRFhRQj5gy'

# If useing BMP085 Temp/Pressure sensor

I2C=/sys/class/i2c-adapter/i2c-2
echo tmp101 0x4a > $I2C/new_device

