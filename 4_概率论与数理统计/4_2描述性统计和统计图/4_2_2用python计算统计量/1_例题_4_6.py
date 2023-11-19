from numpy import reshape, hstack, mean, median, ptp, var, std, cov, corrcoef
import pandas as pd
import numpy as np
df = pd.read_excel("Pdata4_6_1.xlsx", header=None)
a = df.values
h = a[:, ::2]
w = a[:, 1::2]
h = reshape(h, (-1, 1))
w = reshape(w, (-1, 1))
hw = hstack([h, w])
# hw1 = np.c_[h, w]  hw可以这样写，我推荐这样吧，毕竟前面都是学这个的
print([mean(h), median(h), ptp(h), var(h), std(h)])
# 平均价 中位数，极差，方差，标准差
print("协方差为：{}\n相关系数为：{}".format(cov(hw.T)[0, 1], corrcoef(hw.T)[0, 1]))
