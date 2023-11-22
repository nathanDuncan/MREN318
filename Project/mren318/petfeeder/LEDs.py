# Remember to run sudo pigpiod
from . import models

from gpiozero import LED
from time import sleep

def LED_Blink():
	# Check if the system is Raspberry Pi
	try:
		from gpiozero.pins.pigpio import PiGPIOFactory
		on_raspberry_pi = True
	except ImportError:
		on_raspberry_pi = False

	if on_raspberry_pi:
		# If on Raspberry Pi, use the GPIO Zero Library
		try:
			led1 = LED(17)
			while True:
				led1.on()
				sleep(0.5)
				led1.off()
		except KeyboardInterrupt:
			led1.off()
	else:
		# If not on Raspberry Pi, provide a message
	    print("This code is designed for Raspberry Pi GPIO and won't work on this system.")
