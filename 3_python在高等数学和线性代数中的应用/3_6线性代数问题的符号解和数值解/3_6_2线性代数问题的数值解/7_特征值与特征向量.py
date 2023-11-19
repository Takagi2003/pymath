import numpy as np
from numpy.linalg import eig

A = np.array([[0, -2, 2],
              [-2, -3, 4],
              [2, 4, -3]])
values, vectors=eig(A)
print("A的特征值为：\n", values)
print("A的特征向量为：\n", vectors)
