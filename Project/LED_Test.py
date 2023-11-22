# Remember to run sudo pigpiod

from gpiozero import LED
from time import sleep

# Check if the system is Raspberry Pi
try:
	from gpiozero.pins.pigpio import PiGPIOFactory
	on_raspberry_pi = True
except ImportError:
	on_raspberry_pi = False

if on_raspberry_pi:
	# if on Raspberry Pi, use the GPIO Zero library
	try:
		led1 = LED(17)
		led2 = LED(27)
		led3 = LED(22)
		while True:
			led3.off()
			led1.on()
			sleep(0.5)
			led1.off()
			led2.on()
			sleep(0.5)
			led2.off()
			led3.on()
			sleep(0.5)
	except KeyboardInterrupt:
		led1.off()
		led2.off()
		led3.off()
else:
	# If not on Raspberry Pi, provide a message
	print("This code is designed for Raspberry Pi GPIO and won't work on this system.")
