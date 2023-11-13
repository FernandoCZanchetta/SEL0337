from smbus import SMBus

I2C_PORT = 1
I2CBUS_ADDRESS = 0x8

Bus = SMBus(I2C_PORT)

flag = True

print("Digite 1 para ON e 0 para OFF")
while flag:
    ledstate = input(">>>>>")
    
    if ledstate == "1":
        Bus.write_byte(I2CBUS_ADDRESS, 0x1)
    elif ledstate == "0":
        Bus.write_byte(I2CBUS_ADDRESS, 0x0)
    else:
        flag = False