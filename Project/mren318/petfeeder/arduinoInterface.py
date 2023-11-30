import serial.tools.list_ports

def readFromArduino():
    print("reading")
    packet = serialInst.readline()
    packet = packet.decode('utf-8')
    print(packet)
    if packet.startswith('f'):
        data = str(packet.split("f")[1])
        print(data)
    if packet.startswith('u'):
        data = str(packet.split("u")[1])
        print(data)
    else:
        return
    print("trying to return to views")
    return data

def writeToArduino(writeData):
    command = str(writeData)
    serialInst.write(command.encode('utf-8'))
    print("arduino interface is writing", command)
    


# Load ports to work with
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

portVar = "/dev/ttyACM0"
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
print(serialInst.port)

# data = readFromArduino()
# writeToArduino(600)

