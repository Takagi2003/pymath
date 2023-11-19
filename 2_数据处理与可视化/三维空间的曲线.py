# 画出三维曲线 x = tsint, y = tcost, z = t (t E [O, 100] ）的图形  P71
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')  # 设置三维图形模式
z = np.linspace(0, 100, 1000)
x = np.sin(z) * z
y = np.cos(z) * z
ax.plot3D(x, y, z, 'k')
plt.show()
