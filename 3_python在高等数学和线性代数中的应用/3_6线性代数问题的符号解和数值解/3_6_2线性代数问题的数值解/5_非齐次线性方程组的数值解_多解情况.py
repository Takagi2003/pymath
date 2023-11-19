from numpy import array
from numpy.linalg import pinv

A = array([[1, 1, -3, -1],
           [3, -1, -3, 4],
           [1, 5, -9, -8]])
b = array([[1, 4, 0]])
b= b.T
x = pinv(A).dot(b)
print("最小范数解为：\n", x)
