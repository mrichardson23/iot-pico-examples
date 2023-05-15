# wire up an LED to pin 15
# wire up a button to pin 14 and 3v3

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT) 

# This creates your button object, which is a type of Pin.
# It's an INPUT (Pin.IN) and we're using what's called an internal "pull-down"
# Essentially, it's like saying when you don't have a connection to 3v3,
# Assume it's connected to GND. ("pulled down" to ground).
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
	# Check the value of that button input:
	if button.value():
		# If it's HIGH (connected to 3v3), then do the following:
		led.toggle()

		# This gives you a moment to lift your finger
		sleep(0.5)