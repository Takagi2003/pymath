import numpy as np
import sympy as sp
A = sp.Matrix([[2, 1, -5, 1],
            [1, -3, 0, -6],
            [0, 2, -1, 2],
            [1, 4, -7, 6]])
B = sp.Matrix([[8, 6, -2, 2]])
B=B.T
print("系数矩阵A的秩为：", A.rank())
print("线性方程组的唯一解为：", A.inv()*B)
