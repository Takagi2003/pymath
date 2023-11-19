from scipy.stats import binom

n = 20
p = 0.8
print("所求的数字特征为：", binom.stats(n, p, moments = 'mvsk'))
