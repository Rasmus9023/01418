import matplotlib.pyplot as plt
import math as mt
import numpy as np

# Default delta is large because that makes it fast, and it illustrates
# the correct registration between image and contours.
delta = 0.1

x = np.arange(-5, 5+delta, delta)
y = np.arange(-5, 5+delta, delta)

X, Y = np.meshgrid(x, y)

f = -np.cos(X) + Y + 1

plt.contour(X,Y,f,100)
plt.colorbar()
plt.xlim(-6,6)
plt.savefig('3_1.png')