import numpy as np
from scipy.integrate import dblquad

f1 = lambda y, x: x * y ** 2
print("T1", dblquad(f1, 0, 2, 0, 1))
f2 = lambda y, x: np.exp(-x ** 2 / 2) * np.sin(x ** 2 + y)
bd1 = lambda x: np.sqrt(1 - x ** 2)
bd2 = lambda x: -(np.sqrt(1 - x ** 2))
print("T2", dblquad(f2, -1, 1, bd2, bd1))

# 对于三重积分第一步需先化成累次积分，然后按照之前的在后面继续添加一组参数。
# 需要注意的是先要对z进行积分，然后再对y进行积分，最后再对x进行积分
