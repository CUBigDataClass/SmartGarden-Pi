import serial

device = '/dev/cu.usbmodem1411101'
brate = 9600
arduino = serial.Serial(device, brate, timeout=5)
print(arduino.name)
for i in range(10):
    line = arduino.readline()
    print(line)
