# 例题3.8只使用工具库中函数quad求定积分
import numpy as np
from scipy.integrate import quad
from sympy import symbols
# x= symbols('x')

f = lambda x: np.sin(np.sqrt(np.cos(x)+x**2))
# f = np.sin(np.sqrt(np.cos(x)+x**2))
print("scipy积分=", quad(f, 0, 1))

# 我注释的代码不运行不通过，看来不能使用定义的符号 可能我还是有一些地方没有搞明白
