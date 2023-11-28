import serial.tools.list_ports

# Load ports to work with
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

#val = input("selct Port: COM")

# Select port to read from
for i in range(len(portList)):
    #if portList[i].startswith("COM" + str(val)):
    if portList[i].find('Arduino'):
        print(i)
        val = str(portList[i])[3]
        portVar = "COM" + str(val)
        print(portList[i])
        

print(portVar)
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
print(serialInst.port)

# command = '600'
# serialInst.write(command.encode('utf-8'))

# Read/write data from/to Arduino
while True:
    # if serialInst.in_waiting:
    packet = serialInst.readline()
    print(packet.decode('utf'))
    # if(packet.startwith("F")):
        # Run Code
#     # print("writing")
#     print("writing")
    command = str(input("Command: "))
    serialInst.write(command.encode('utf-8'))