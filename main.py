import machine
import time
import EEPROM

# Configuration
EEPROM.sda_pin = machine.Pin(0)
EEPROM.scl_pin = machine.Pin(1)
EEPROM.address = 80
EEPROM.delay = 0.01
EEPROM.show_list = False
EEPROM.user_input = "put your data here"

# Commands
EEPROM.erase()
EEPROM.read()
EEPROM.write()

# Visit https://github.com/nowacci/pico-24AA01 for more information