import numpy as np
import numpy.linalg as LA

A = np.arange(1, 17).reshape(4, 4)
B = np.eye(4)
print("A的行列式为：", LA.det(A))
print("A的秩为：", LA.matrix_rank(A))
print("A的转置矩阵为：\n", A.T)
print("所求的逆矩阵为：\n", LA.inv(A+10*B))
print("A的平方为：\n", A.dot(A))
print("横连矩阵为：\n", np.r_[A, B])
print("纵连矩阵为：\n", np.r_[A, B])
print("A1为：\n", A[0:2, 0:2])
A2 = A.copy()
A2 = np.delete(A2, 3, axis=0)
print("A2为：\n", A2)
