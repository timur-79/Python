import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10,10.01, 0.01)
plt.plot(x,x**2)
plt.plot(x, np.sin(x), np.cos(x))
plt.show()