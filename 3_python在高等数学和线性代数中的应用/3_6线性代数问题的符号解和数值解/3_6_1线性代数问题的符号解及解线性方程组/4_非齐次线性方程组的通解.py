import sympy as sp

A = sp.Matrix([[1, 1, -3, -1],
               [3, -1, -3, 4],
               [1, 5, -9, -8]])
B = sp.Matrix([[1, 4, 0]])
B = B.T
C = A.row_join(B)
print("增广矩阵的行最简形为：", C.rref())
