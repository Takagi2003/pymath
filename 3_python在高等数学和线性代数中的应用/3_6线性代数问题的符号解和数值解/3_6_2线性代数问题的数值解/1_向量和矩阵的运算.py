import numpy as np

a = np.arange(1, 4)
b = np.arange(4, 7)
print("a的二范数为：", np.linalg.norm(a))
print("a点乘b=", a.dot(b))
print("a,b的内积", np.inner(a, b))
print("a,b的内积", np.dot(a, b))   # 这两个是等价的
print("a叉乘b:", np.cross(a, b))

