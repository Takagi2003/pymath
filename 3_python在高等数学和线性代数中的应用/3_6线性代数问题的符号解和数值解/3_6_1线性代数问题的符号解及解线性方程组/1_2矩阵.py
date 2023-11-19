import sympy as sp
import numpy as np

A=sp.Matrix([[1, 2, 3, 4],   # 可以用 np.arange(1,17).reshape(4,4)
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]])
B = sp.Matrix([[1, 0, 0, 0],    # sp.eye(4)
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])
print("A的行列式为：", sp.det(A))
print("A的秩为：", A.rank())
print("A的转置为：", A.T)
print("所求的逆矩阵为：", (A+10*B).inv())
print("A的平方为：", A**2)
print("AB为：", A*B)
print("横连矩阵为：", A.row_join(B))
print("纵连矩阵为：", A.col_join(B))
print("A1为：", A[0:2, 0:2])
A2 = A.copy()
A2.row_del(3)
print("A2为：", A2)
