from datetime import datetime
from time import sleep
from arduinoInterface import writeToArduino
# from petfeeder.arduinoInterface import feedCommand, readCommand

while True:
    now = datetime.now()
    current_time = now.strftime("%H%M")
    print("Current Time =", current_time)    

    dataFile = open("petfeeder/timingData.txt","r")
    times = dataFile.readlines()

    for time in times:
        print(time)
        input = time.split(',')
        if ':' in input[0]:
            feedTime = input[0].split(':')
            if (now.strftime("%M")==feedTime[1]) and (now.strftime("%H")==feedTime[0]):
                print("Time to feed,", input[1])
                writeToArduino(input[1])

    dataFile.close()
    sleep(60)

    