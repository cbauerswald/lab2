from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
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

def sensor_val_to_distance(val):
    return (val**3)*a + (val**2)*b + val*c + d



test_distances = ["186;49;5/169;50;5/523;5;10/515;6;10/511;7;10/498;8;10/481;9;10/467;10;10/452;11;10/435;12;10/400;13;10/502;5;5/528;6;5/508;7;5/496;8;5/489;9;5/466;10;5/448;11;5/434;12;5/412;13;5/378;14;5/348;15;5/315;16;5/286;17;5/271;18;5/255;19;5/244;20;5/244;21;5/245;22;5/242;23;5/246;24;5/246;25;5/246;26;5/246;27;5/251;28;5/251;29;5/246;30;5/238;31;5/234;32;5/234;33;5/238;34;5/238;35;5/242;36;5/246;37;5/252;38;5/255;39;5/268;40;5/267;41;5/262;42;5/255;43;5/260;44;5/261;45;5/258;46;5/246;47;5/244;48;5/234;49;5/220;50;5/521;5;10/521;6;10/503;7;10/496;8;10/490;9;10/466;10;10/448;11;10/425;12;10/404;13;10/366;14;10/347;15;10/305;16;10/279;17;10/267;18;10/256;19;10/246;20;10/253;21;10/256;22;10/255;23;10/255;24;10/256;25;10/256;26;10/252;27;10/251;28;10/252;29;10/252;30;10/243;31;10/234;32;10/180;33;10/188;34;10/234;35;10/242;36;10/227;37;10/187;38;10/151;39;10/140;40;10/144;41;10/152;42;10/159;43;10/167;44;10/179;45;10/199;46;10/222;47;10/226;48;10/226;49;10/215;50;10/488;5;15/518;6;15/510;7;15/496;8;15/489;9;15/467;10;15/445;11;15/426;12;15/397;13;15/377;14;15/346;15;15/315;16;15/280;17;15/266;18;15/257;19;15/247;20;15/252;21;15/254;22;15/253;23;15/252;24;15/252;25;15/253;26;15/252;27;15/252;28;15/252;29;15/253;30;15/246;31;15/252;32;15/252;33;15/243;34;15/235;35;15/207;36;15/163;37;15/125;38;15/125;39;15/125;40;15/124;41;15/125;42;15/128;43;15/175;44;15/226;45;15/242;46;15/222;47;15/207;48;15/159;49;15/121;50;15/489;5;20/517;6;20/508;7;20/497;8;20/482;9;20/469;10;20/445;11;20/431;12;20/405;13;20/374;14;20/333;15;20/310;16;20/283;17;20/269;18;20/246;19;20/247;20;20/252;21;20/252;22;20/246;23;20/252;24;20/254;25;20/254;26;20/247;27;20/254;28;20/254;29;20/250;30;20/235;31;20/227;32;20/219;33;20/225;34;20/235;35;20/239;36;20/241;37;20/240;38;20/242;39;20/244;40;20/247;41;20/242;42;20/238;43;20/234;44;20/219;45;20/175;46;20/125;47;20/120;48;20/128;49;20/207;50;20/517;5;25/521;6;25/507;7;25/494;8;25/482;9;25/468;10;25/443;11;25/419;12;25/398;13;25/363;14;25/336;15;25/298;16;25/276;17;25/257;18;25/248;19;25/238;20;25/248;21;25/248;22;25/249;23;25/243;24;25/248;25;25/249;26;25/249;27;25/242;28;25/248;29;25/237;30;25/207;31;25/152;32;25/131;33;25/124;34;25/127;35;25/129;36;25/137;37;25/149;38;25/158;39;25/156;40;25/156;41;25/148;42;25/132;43;25/125;44;25/116;45;25/112;46;25/112;47;25/113;48;25/117;49;25/140;50;25/494;5;30/521;6;30/518;7;30/513;8;30/481;9;30/456;10;30/440;11;30/413;12;30/380;13;30/354;14;30/328;15;30/299;16;30/261;17;30/256;18;30/246;19;30/244;20;30/234;21;30/243;22;30/242;23;30/242;24;30/239;25;30/246;26;30/246;27;30/245;28;30/231;29;30/205;30;30/145;31;30/122;32;30/113;33;30/116;34;30/117;35;30/122;36;30/113;37;30/118;38;30/118;39;30/118;40;30/113;41;30/118;42;30/119;43;30/119;44;30/113;45;30/119;46;30/117;47;30/116;48;30/109;49;30/113;50;30/473;5;35/512;6;35/515;7;35/502;8;35/479;9;35/460;10;35/437;11;35/422;12;35/389;13;35/352;14;35/313;15;35/282;16;35/230;17;35/200;18;35/199;19;35/207;20;35/215;21;35/215;22;35/215;23;35/219;24;35/219;25;35/216;26;35/220;27;35/220;28;35/216;29;35/196;30;35/114;31;35/56;32;35/41;33;35/40;34;35/44;35;35/65;36;35/43;37;35/40;38;35/41;39;35/45;40;35/39;41;35/44;42;35/43;43;35/43;44;35/39;45;35/40;46;35/44;47;35/44;48;35/47;49;35/52;50;35/501;5;40/514;6;40/504;7;40/500;8;40/485;9;40/465;10;40/433;11;40/414;12;40/389;13;40/366;14;40/332;15;40/313;16;40/274;17;40/246;18;40/199;19;40/167;20;40/128;21;40/64;22;40/39;23;40/35;24;40/35;25;40/31;26;40/31;27;40/33;28;40/26;29;40/59;30;40/56;31;40/49;32;40/40;33;40/46;34;40/46;35;40/45;36;40/43;37;40/40;38;40/42;39;40/44;40;40/43;41;40/43;42;40/43;43;40/40;44;40/43;45;40/39;46;40/43;47;40/44;48;40/44;49;40/40;50;40/508;5;45/531;6;45/516;7;45/492;8;45/475;9;45/456;10;45/430;11;45/419;12;45/390;13;45/365;14;45/335;15;45/318;16;45/283;17;45/258;18;45/237;19;45/194;20;45/106;21;45/60;22;45/46;23;45/46;24;45/41;25;45/40;26;45/40;27;45/40;28;45/48;29;45/85;30;45/60;31;45/48;32;45/45;33;45/47;34;45/47;35;45/51;36;45/44;37;45/51;38;45/47;39;45/48;40;45/41;41;45/44;42;45/44;43;45/43;44;45/44;45;45/44;46;45/40;47;45/40;48;45/45;49;45/43;50;45/569;5;50/511;6;50/515;7;50/489;8;50/465;9;50/449;10;50/426;11;50/403;12;50/381;13;50/355;14;50/325;15;50/301;16;50/278;17;50/246;18;50/232;19;50/168;20;50/77;21;50/48;22;50/43;23;50/45;24;50/48;25;50/40;26;50/46;27;50/38;28;50/65;29;50/65;30;50/44;31;50/43;32;50/40;33;50/48;34;50/43;35;50/39;36;50/44;37;50/40;38;50/37;39;50/42;40;50/48;41;50/44;42;50/47;43;50/45;44;50/50;45;50/39;46;50/39;47;50/41;48;50/39;49;50/39;50;50/"]

data = test_distances[0].split("/")
data.pop()
#print data


servo_lr_vals = []
servo_ud_vals = []
distances = []
# x_distances = []
# y_distances = []
# z_distances = []
for i, datum in enumerate(data):
    [sensorvalue, servo_up_down, servo_left_right] = datum.split(';')

    # converting to int and removing new lines
    sensorvalue = int(sensorvalue)
    servo_up_down= int(servo_up_down.rstrip())
    servo_left_right = int(servo_left_right.rstrip())

    updown_angle = math.radians(servo_up_down)
    leftright_angle = math.radians(servo_left_right)

    distance = sensor_val_to_distance(sensorvalue)
    distances.append(distance)

   # print distances
   # print servo_lr_vals

#     # using angles to find actual distance
#     # resource used for spherical coordinates: http://tutorial.math.lamar.edu/Classes/CalcIII/SphericalCoords.aspx
#     x_sensor_distance = sensorvalue * math.sin(updown_angle) * math.cos(leftright_angle)
#     y_sensor_distance = sensorvalue * math.sin(updown_angle) * math.sin(leftright_angle)
#     z_sensor_distance = sensorvalue * math.cos(updown_angle)

#     # print sensor_distance
#     x_distance = sensor_val_to_distance(x_sensor_distance)
#     y_distance = sensor_val_to_distance(y_sensor_distance)
#     z_distance = sensor_val_to_distance(z_sensor_distance)

#     # print distance

#     # print math.radians(servovalue)
#     x_distances.append(x_distance)
#     y_distances.append(y_distance)
#     z_distances.append(z_distance)

    servo_lr_vals.append(servo_left_right)
    servo_ud_vals.append(servo_up_down)


servo_ud_vals = servo_ud_vals[11:]
servo_lr_vals = servo_lr_vals[11:]
distances = distances[11:]






import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = servo_lr_vals
Y = servo_ud_vals
Z = distances

# plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),10),\
#                            np.linspace(np.min(Y),np.max(Y),10))
# plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis')
#plt.show()


X=np.unique(X)
Y=np.unique(Y)
x,y = np.meshgrid(X,Y)
print len(Y)
print len(X)

Z = np.array(Z)

z=Z.reshape(len(Y),len(X))

plt.pcolormesh(x,y,z)

plt.show()


# x = np.arange(0,11)
# y = np.arange(0,11)
# xv, yv = np.meshgrid(x,y)
# print xv
# print yv
# c = np.random.rand(10,10)
# print c

# plt.pcolormesh(xv,yv,c)

# plt.show()

#x,y = np.meshgrid(servo_lr_vals,servo_ud_vals)
# print x 
# print len(y)
# c = np.random.rand(471,471)
# print c

# c1,c2 = np.meshgrid(distances,distances)
# c = zip(c1,c2)

# plt.pcolormesh(x, y, c)
# plt.show()

# plt.plot(servo_lr_vals,servo_ud_vals)
# plt.show()

# print x_distances
# print y_distances
# print z_distances

# fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # ax.scatter(x_distances, y_distances, z_distances)
# # plt.show()

# ax = fig.gca(projection='3d')

# #X, Y = np.meshgrid(x_distances, y_distances)
# surf = ax.plot_surface(x_distances, y_distances, z_distances, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# #ax.set_zlim(-1.01, 1.01)

# #ax.zaxis.set_major_locator(LinearLocator(10))
# #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()




