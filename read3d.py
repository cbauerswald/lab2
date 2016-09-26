import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
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

def sensor_val_to_distance(val):
    return (val**3)*a + (val**2)*b + val*c + d

# print a, b, c, d

# x_calibration = np.linspace(0,160,10000)
# y_calibration = x_calibration*x_calibration*x_calibration*a + x_calibration*x_calibration*b + c*x_calibration + d

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

# sensorvals = []
servo_lr_vals = []
servo_ud_vals = []
x_distances = []
y_distances = []
x_distances = []
for i, datum in enumerate(data):
    [sensorvalue, servo_up_down, servo_left_right] = datum.split(';')

    # converting to int and removing new lines
    sensorvalue = int(sensorvalue)
    servo_up_down= int(servo_up_down.rstrip())
    servo_left_right = int(servo_left_right.rstrip)

    updown_angle = math.radians(servo_up_down)
    leftright_angle = math.radians(servo_left_right)

    # using angles to find actual distance
    # resource used for spherical coordinates: http://tutorial.math.lamar.edu/Classes/CalcIII/SphericalCoords.aspx
    x_sensor_distance = sensorvalue * math.sin(updown_angle) * math.cos(leftright_angle)
    y_sensor_distance = sensorvalue * math.sin(updown_angle) * math.sin(leftright_angle)
    z_sensor_distance = sensorvalue * math.cos(updown_angle)

    print sensor_distance
    x_distance = sensor_val_to_distance(x_sensor_distance)
    y_distance = sensor_val_to_distance(y_sensor_distance)
    z_distance = sensor_val_to_distance(z_sensor_distance)

    print distance

    # print math.radians(servovalue)
    x_distances.append(x_distance)
    y_distances.append(y_distance)
    x_distances.append(z_distance)

    servo_lr_vals.append(servo_left_right)
    servo_ud_vals.append(servo_up_down)

print servo_lr_vals
print servo_ud_vals
print distances

# http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', rstride=4, cstride=4, color='b') 
ax.plot_surface(x_distances, y_distances, z_distances)
plt.show()

