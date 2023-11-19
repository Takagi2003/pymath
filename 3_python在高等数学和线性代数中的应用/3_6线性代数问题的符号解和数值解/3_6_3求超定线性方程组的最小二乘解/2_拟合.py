import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

t = np.arange(0, 8)
y = np.array([27.0, 26.8, 26.5, 26.3, 26.2, 25.7, 25.3, 24.8])
y1 = np.array([[27.0, 26.8, 26.5, 26.3, 26.2, 25.7, 25.3, 24.8]])
A = np.c_[t, np.ones_like(t)]
a, b = LA.lstsq(A, y, rcond=None)[0]
print(a, b)
plt.rc('font', size = 16)
plt.plot(t, y, 'o', label='riginal data', markersize=5)
plt.plot(t, a*t+b, 'r', label='fitted line')
plt.legend()
plt.show()

print(t)
print(y1)

