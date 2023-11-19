import numpy as np
from scipy.optimize import fminbound, fmin

f = lambda x: np.exp(x) * np.cos(2 * x)
x0 = fminbound(f, 0, 3)
x1 = fmin(f, 0)
print("极小值点{}，极小值为{}".format(x0, f(x0)))
# 在0附近的一个极小值点
print("极小值点{}，极小值为{}".format(x1, f(x1)))
