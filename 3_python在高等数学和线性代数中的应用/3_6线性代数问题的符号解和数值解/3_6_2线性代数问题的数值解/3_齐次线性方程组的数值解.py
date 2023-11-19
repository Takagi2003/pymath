import numpy as np
from scipy.linalg import null_space    # 这个是scipy.linalg 不是numpy.linalg

A = np.array([[1, -5, 2, -3],
              [5, 3, 6, -1],
              [2, 4, 2, 1]])
print("A的零空间（即基础解系）为：", null_space(A))
