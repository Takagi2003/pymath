# 例3.7 图img_1.png
from sympy import *
x, y =symbols('x y')
z = sin(x)+x**2* exp(y)
print("关于x的二阶偏导为：", diff(z, x, 2))
print("关于y的一阶偏导为：", diff(z, y))
