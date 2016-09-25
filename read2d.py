import matplotlib.pyplot as plt
import numpy as np

import serial
import sys
import time
import io
import math

# imported calibration code
calibration = {10: 509, 20: 496, 30: 385, 40: 288, 50: 230, 60: 186, 70: 158, 80: 134, 90: 122, 100: 106, 110: 95, 120: 83, 130: 73, 140: 65, 160: 64}
keys, values = zip(*calibration.items())

a, b, c, d = np.polyfit(values, keys, 3)
# print a, b, c, d

# x_calibration = np.linspace(0,160,10000)
# y_calibration = x_calibration*x_calibration*x_calibration*a + x_calibration*x_calibration*b + c*x_calibration + d

# setting up serial port
ser = serial.Serial('/dev/tty.usbmodem1411', 9600,timeout=5)  # open serial port
time.sleep(2)

print("connected to: " + ser.portstr)

data = []

datacollection = True
# if ser.readline()[-2:] == "30":
#     datacollection = True;
# else:
#     datacollection = False;

while datacollection:
    print ser.readline()
    data.append(ser.readline())
    # print data
    # sys.stdout.write(ser.readline())
    # sys.stdout.flush()
    if (len(data) == 1):
        datacollection = False
    else:
        pass

data = data[0].split("/")
data.pop()
print data

# sensorvals = []
servovals = []
distances = []
for i, datum in enumerate(data):
    [sensorvalue, servovalue] = datum.split(';')
    # print [sensorvalue, servovalue]
    # print sensorvalue
    # print servovalue

    # converting to int and removing new lines
    sensorvalue = int(sensorvalue)
    servovalue = int(servovalue.rstrip())

    # taking calibration info and converting sensor value
    # sensorvalue = np.interp(sensorvalue,x_calibration,y_calibration)
    # using angle to find actual distance
    sensorvalue = sensorvalue*math.cos(math.radians(servovalue))

    print sensorvalue
    sensorvalue = sensorvalue*sensorvalue*sensorvalue*a + sensorvalue*sensorvalue*b + c*sensorvalue + d
    print sensorvalue

    # print math.radians(servovalue)
    distances.append(sensorvalue)
    servovals.append(servovalue)

# start = servovals[0]
# print start
# print servovals[9:].index(start)
# print servovals[:41]
# print servovals[41:82]
# for i, servovalue in enumerate(servovals):
#     l = ['a',' b',' c',' d',' e']
# c_index = l.index("c")
# l2 = l[:c_index]

print servovals
print distances

plt.plot(distances, 'bo')
plt.show()

