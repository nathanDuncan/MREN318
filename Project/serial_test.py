import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

#val = input("selct Port: COM")

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

while True:
    # if serialInst.in_waiting:
    packet = serialInst.readline()
    print(packet.decode('utf'))
#     # print("writing")
#     print("writing")
    command = str(input("Command: "))
    serialInst.write(command.encode('utf-8'))