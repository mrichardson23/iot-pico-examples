# Import the classes you need from existing Python modules
from machine import Pin
from time import sleep

# "LED" is a special designation for Pico's on-board LED.
# Change it to a number (without quote marks) when you want to use a GPIO pin.
# Pin.OUT is how you tell the board that you want to use the pin as an output.
led = Pin(“LED”, Pin.OUT)

# A while loop setup like this is an easy way to have code do something forever.
while True:
	led.on() # turn the on-board LED on
	sleep(1) # wait here for 1 second
	led.off() # turn the on-board LED off
	sleep(1) # wait here for 1 second

