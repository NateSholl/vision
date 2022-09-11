import matplotlib.pyplot as plt
import math
import numpy as np

i = 10*10**10
x = np.arange(-i,i)
y = x**2 + x + 10

plt.title('Graph Test')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(x, y)

plt.show()