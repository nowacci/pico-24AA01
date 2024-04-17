import machine
import time

sda_pin = None
scl_pin = None
address = None
delay = None
show_list = None
user_input = None

i2c = machine.I2C(0, scl=scl_pin, sda=sda_pin)

def read():
    devices = i2c.scan()
    data = i2c.readfrom(address, 128)  # show first 128 bytes (all 21AAA01 memory)
    print(data)                        # this must be here              \
    data = i2c.readfrom(address, 0)    # otherwise printing with errors /


def write():
    if len(user_input) <= 128:
        print("Data read:")
        for i in range(len(user_input)):
            user_input_bytes = ord(user_input[i])  # to ASCII
            i2c.writeto_mem(address, i, bytes([user_input_bytes]))
            if show_list is True:
                print(i, user_input[i])
            time.sleep(delay)
    else:
        print("The data is too long. The maximum length is 128 characters.")


def erase():  
    devices = i2c.scan()
    zero_data = bytes([0x00])
    for byte in range(128):
        i2c.writeto_mem(address, byte, zero_data)
        time.sleep(delay)
    print("All data erased")

# Visit https://github.com/nowacci/pico-24AA01 for more information