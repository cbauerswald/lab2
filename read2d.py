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


# setting up serial port
ser = serial.Serial('/dev/tty.usbmodem1411', 9600,timeout=5)  # open serial port
time.sleep(2)

print("connected to: " + ser.portstr)

data = []

datacollection = True

while datacollection:
    print ser.readline()
    data.append(ser.readline())
    if (len(data) == 1):
        datacollection = False
    else:
        pass

data = data[0].split("/")
data.pop()
print data

servovals = []
distances = []
for i, datum in enumerate(data):
    [sensorvalue, servovalue] = datum.split(';')

    # converting to int and removing new lines
    sensorvalue = int(sensorvalue)
    servovalue = int(servovalue.rstrip())

    # taking calibration info and converting sensor value
    # using angle to find actual distance
    sensorvalue = sensorvalue*math.cos(math.radians(servovalue))

    print sensorvalue
    sensorvalue = sensorvalue*sensorvalue*sensorvalue*a + sensorvalue*sensorvalue*b + c*sensorvalue + d
    print sensorvalue

    # print math.radians(servovalue)
    distances.append(sensorvalue)
    servovals.append(servovalue)


print servovals
print distances

plt.plot(distances, 'bo')
plt.show()

