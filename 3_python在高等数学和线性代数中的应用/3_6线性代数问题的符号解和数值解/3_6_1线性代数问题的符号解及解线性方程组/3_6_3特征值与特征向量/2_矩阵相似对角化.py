import sympy as sp

A = sp.Matrix([[0, -2, 2],
               [-2, -3, 4],
               [2, 4, -3]])
if A.is_diagonalizable():
    print("A的对角化矩阵为：\n", A.diagonalize())
else:
    print("A不能对角化")

# 求可逆矩阵P和对角矩阵D
