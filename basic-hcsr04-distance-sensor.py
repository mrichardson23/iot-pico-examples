# This requires the hcrs04 MicroPython library to be installed:
from hcsr04 import HCSR04

from time import sleep

# Assuming the sensor's trigger is on GPIO15 and echo is on GPIO14:
sensor = HCSR04(trigger_pin=15, echo_pin=14)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(.25)
