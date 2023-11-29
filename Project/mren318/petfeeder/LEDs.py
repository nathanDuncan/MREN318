# Remember to run sudo pigpiod
# from . import models

# from gpiozero import LED
# from time import sleep

# def LED_Blink():
# 	# Check if the system is Raspberry Pi
# 	try:
# 		from gpiozero.pins.pigpio import PiGPIOFactory
# 		on_raspberry_pi = True
# 	except ImportError:
# 		on_raspberry_pi = False

# 	if on_raspberry_pi:
# 		# If on Raspberry Pi, use the GPIO Zero Library
# 		try:
# 			led1 = LED(17)
# 			while True:
# 				led1.on()
# 				sleep(0.5)
# 				led1.off()
# 		except KeyboardInterrupt:
# 			led1.off()
# 	else:
# 		# If not on Raspberry Pi, provide a message
# 	    print("This code is designed for Raspberry Pi GPIO and won't work on this system.")



################### Scheduler ####################################
from datetime import datetime
from petfeeder.models import Pet
# from petfeeder.arduinoInterface import feedCommand, readCommand

pets = Pet.objects.all()
while True:
	now = datetime.now()
	current_time = now.strftime("%H%M")

	print("Current Time =", current_time)
	for pet in pets:
		input = "01:34"
		input = pet.servingTime1
		feedTime1 = input.split(':')
		print(feedTime1[1])

		input = pet.servingTime2
		feedTime2 = input.split(':')
		print(feedTime2[1])

		if (((now.strftime("%M")==feedTime1[1]) and (now.strftime("%H")==feedTime1[0])) or
		   ((now.strftime("%M")==feedTime2[1]) and (now.strftime("%H")==feedTime2[0]))):
			print("yay")
			#feedCommand(pet.servingSize)
