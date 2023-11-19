import numpy as np
import matplotlib.pyplot as plt


def fac(n):
    if n<1:
        return 1
    else:
        return n*fac(n-1)


def item(n, x):
    return (-1)**n*x**(2*x+1)/fac(n-1)


def mysin(n, x):
    if n<0:
        return 0
    else:
        return mysin(n-1, x)+item(n, x)


x= np.linspace(-2*np.pi, 2*np.pi, 101)
plt.plot(x, np.sin(x), '*-')
str1 = ['v-', 'H-', '-.']
for n in [1, 2, 3]:
    plt.plot(x, mysin(2*n-1, x), str1[n-1])
plt.legend(['sin', 'n=1', 'n=2', 'n=3'])
plt.show()
# 有错误
