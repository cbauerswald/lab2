import matplotlib.pyplot as plt
import numpy as np

#The values we collected to calibrate our function, in the form -  distance : sensor value
calibration = {10: 509, 20: 496, 30: 385, 40: 288, 50: 230, 60: 186, 70: 158, 80: 134, 90: 122, 100: 106, 110: 95, 120: 83, 130: 73, 140: 65, 160: 64}
#Turns the dictionary of values into two lists
keys, values = zip(*calibration.items())

#finds a 3rd degree polynomial that fits the data, with the coefficients a, b, c, and d
a, b, c, d = np.polyfit(values, keys, 3)
print a, b, c, d

#create a list of the values that the calibrated function would return given the distances used to calibrate
bestfit = []
for key in keys:
    bestfit.append(a*key*key*key + b*key*key + c*key + d)

#create the values for the curve 
x = np.linspace(0,500,100)
y = x*x*x*a + x*x*b + c*x + d

#plot the Calibration Values with blue dots
plt.plot(values, keys, 'bo')
plt.plot(x, y)

#the values we collected to test our calibration function
calibration_test = {15: 485, 35: 317, 55: 197, 75: 141, 95: 117, 115: 97, 135: 97, 155: 82}

#Turn the dictionary of test values into two lists
keys_test, values_test = zip(*calibration_test.items())

#plot the Test Values with red dots
plt.plot(values_test,keys_test,'ro')

#label and format the graph
plt.title("Sensor Value to Distance (cm) Calibration Test")
plt.xlabel("Sensor Output Value")
plt.ylabel("Distance (cm)")
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
