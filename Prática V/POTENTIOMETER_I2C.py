from smbus import SMBus
from time import sleep

I2C_PORT = 1
I2CBUS_ADDRESS = 0x8
RECEIVED_DATA_BYTE_NUMBER = 2
I2CDATA_REGISTER = 0

Bus = SMBus(I2C_PORT)

while True:
    I2C_Data = Bus.read_i2c_block_data(I2CBUS_ADDRESS, I2CDATA_REGISTER, RECEIVED_DATA_BYTE_NUMBER)
    Potentiometer_Measure = I2C_Data[0] * 256 + I2C_Data[1]
    print(Potentiometer_Measure)
    sleep(0.5)