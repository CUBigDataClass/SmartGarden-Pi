import serial

arduino = serial.Serial('/dev/ttyAMA0', 115200, timeout=5)
print(arduino.name)
for i in range(10):
    line = arduino.readline()
    print(line)
