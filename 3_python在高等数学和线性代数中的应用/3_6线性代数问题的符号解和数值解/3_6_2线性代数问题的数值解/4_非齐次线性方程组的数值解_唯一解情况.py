import numpy as np
import numpy.linalg as LA

A = np.array([[2, 1, -5, 1],
              [1, -3, 0, -6],
              [0, 2, -1, 2],
              [1, 4, -7, 6]])
B = np.array([[8, 6, -2, 2]])
B = B.T
print("系数矩阵A的秩\n", LA.matrix_rank(A))
print("线性方程组的唯一解：\n", LA.inv(A).dot(B))   # 使用逆矩阵
print("线性方程组的唯一解：\n", LA.pinv(A).dot(B))  # 使用伪逆
print("线性方程组的唯一解：\n", LA.solve(A, B))     # 利用solve求解
