from datetime import datetime
from petfeeder.models import Pet
# from petfeeder.arduinoInterface import feedCommand, readCommand

pets = Pet.objects.all()
while True:
    
    input = "01:34"
    feedTime = input.split(':')
    print(feedTime[1])

    now = datetime.now()
    current_time = now.strftime("%H%M")
    print("Current Time =", current_time)
    
    if (now.strftime("%M")==feedTime[1]) and (now.strftime("%H")==feedTime[0]):
        print("yay")

    