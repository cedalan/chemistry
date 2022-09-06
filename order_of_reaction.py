#This program can be used to determine the order of a reaction
import matplotlib.pyplot as plt
import numpy as np

x = []
x = np.array(x)

y = []
y = np.array(y)

plt.plot(x, y, label="Time vs concentration")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("0th order reaction")
plt.legend()
plt.grid()
plt.show()

concentration_log = np.log(y)

plt.plot(x, concentration_log, label="Time vs log(concentration)")
plt.xlabel("Time")
plt.ylabel("log(concentration")
plt.title("First order reaction")
plt.legend()
plt.grid()
plt.show()

concentration_inv = 1/y

plt.plot(x, concentration_inv, label="Time vs 1/concentration")
plt.xlabel("Time")
plt.ylabel("1/Concentration")
plt.title("Second order reaction")
plt.legend()
plt.grid()
plt.show()