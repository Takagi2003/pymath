import numpy as np
import numpy.linalg as LA
from matplotlib.pyplot import plot, rc, legend, show

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.c_[x, np.ones_like(x)]
m, c = LA.lstsq(A, y, rcond=None)[0]
print(m, c)
rc('font', size=10)
plot(x, y, 'o', label='原始数据', markersize=10)
plot(x, m * x + c, 'r', label='拟合直线')
rc('font', family='Fangsong')  # 用来正常显示中文标签
rc('axes', unicode_minus=False)  # 用来正常显示负号
legend()
show()
