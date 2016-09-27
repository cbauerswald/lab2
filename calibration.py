import matplotlib.pyplot as plt
import numpy as np


calibration = {10: 509, 20: 496, 30: 385, 40: 288, 50: 230, 60: 186, 70: 158, 80: 134, 90: 122, 100: 106, 110: 95, 120: 83, 130: 73, 140: 65, 160: 64}
keys, values = zip(*calibration.items())

a, b, c, d = np.polyfit(values, keys, 3)
print a, b, c, d

bestfit = []
for key in keys:
    bestfit.append(a*key*key*key + b*key*key + c*key + d)

x = np.linspace(0,500,100)
y = x*x*x*a + x*x*b + c*x + d

plt.plot(values, keys, 'bo')
plt.plot(x, y)

calibration_test = {15: 485, 35: 317, 55: 197, 75: 141, 95: 117, 115: 97, 135: 97, 155: 82}
keys_test, values_test = zip(*calibration_test.items())
plt.plot(values_test,keys_test,'ro')

plt.title("Sensor Value to Distance (cm) Calibration Test")
plt.ylabel("Distance (cm)")
plt.xlabel("Sensor Output Value")
legend = plt.legend(['Calibration Values', 'Fit Curve', 'Test Values'])
legend.get_frame().set_linewidth(0.0)

plt.show()


# 15: 485
# 35: 317
# 55: 197
# 75: 141
# 95: 117
# 115: 97
# 135: 86
# 155: 82
