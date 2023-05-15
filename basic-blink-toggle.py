from machine import Pin
from time import sleep
led = Pin("LED", Pin.OUT)

while True:
	led.toggle() # switch the state of the pin
	sleep(1)