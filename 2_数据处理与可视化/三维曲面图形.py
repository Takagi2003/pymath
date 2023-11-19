# 画出三维曲面 z = sin(np.sqrt(x**2+y**2))的三维表面图形和三维网格图形 p71
from mpl_toolkits import mplot3d
from matplotlib import pyplot as ply
import numpy as np

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y=np.meshgrid(x, y)
Z =np.sin(np.sqrt(X ** 2 + Y ** 2))
ax1 = ply.subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax2 = ply.subplot(1, 2, 2, projection='3d')
ax2.plot_wireframe(X, Y, Z, color='c')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ply.show()


