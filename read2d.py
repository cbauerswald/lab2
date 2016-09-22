import serial
import sys
import time
import io

ser = serial.Serial('/dev/tty.usbmodem1411')  # open serial port

print("connected to: " + ser.portstr)

data = []

datacollection = True;

while datacollection:
    print ser.readline()
    data.append(ser.readline())
    # print data
    # sys.stdout.write(ser.readline())
    # sys.stdout.flush()
    if (len(data) == 10):
        datacollection = False
    else:
        pass

sensorvalues = []
motorvalues = []
for i, datum in enumerate(data):
    print datum.split(';')

print sensorvalues
print motorvalues
