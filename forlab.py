from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp


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

data = test_distances[0].split("/")
data.pop()


servo_lr_vals = []
servo_ud_vals = []
distances = []
for i, datum in enumerate(data):
    [sensorvalue, servo_up_down, servo_left_right] = datum.split(';')

    # converting to int and removing new lines
    sensorvalue = int(sensorvalue)
    servo_up_down= int(servo_up_down.rstrip())
    servo_left_right = int(servo_left_right.rstrip())

    updown_angle = math.radians(servo_up_down)
    leftright_angle = math.radians(servo_left_right)

    sensorvalue = sensorvalue * math.cos(updown_angle)

    distance = sensor_val_to_distance(sensorvalue)
    distances.append(distance)

    servo_lr_vals.append(servo_left_right)
    servo_ud_vals.append(servo_up_down)


servo_ud_vals = servo_ud_vals[24:]
servo_lr_vals = servo_lr_vals[24:]
distances = distances[24:]


X = servo_lr_vals
Y = servo_ud_vals
Z = distances

plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),45),\
                           np.linspace(np.min(Y),np.max(Y),45))
plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap=cm.coolwarm)
plt.show()


X=np.unique(X)
Y=np.unique(Y)
x,y = np.meshgrid(X,Y)
Z = np.array(Z)
z=Z.reshape(len(Y),len(X))
reversed_arr = y[::-1]

plt.pcolormesh(reversed_arr,x,z)
plt.show()

