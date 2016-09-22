import matplotlib.pyplot as plt
import numpy as np


calibration = {10: 509, 20: 496, 30: 385, 40: 288, 50: 230, 60: 186, 70: 158, 80: 134, 90: 122, 100: 106, 110: 95, 120: 83, 130: 73, 140: 65, 160: 64}
keys, values = zip(*calibration.items())

a, b, c, d = np.polyfit(keys, values, 3)
print a, b, c, d

bestfit = []
for key in keys:
    bestfit.append(a*key*key*key + b*key*key + c*key + d)

x = np.linspace(0,160,100)
y = x*x*x*a + x*x*b + c*x + d

plt.plot(keys, values, 'bo')
plt.plot(x, y)

calibration_test = {15: 485, 35: 317, 55: 197, 75: 141, 95: 117, 115: 97, 135: 97, 155: 82}
keys_test, values_test = zip(*calibration_test.items())
plt.plot(keys_test,values_test,'ro')

plt.show()

# 15: 485
# 35: 317
# 55: 197
# 75: 141
# 95: 117
# 115: 97
# 135: 86
# 155: 82
