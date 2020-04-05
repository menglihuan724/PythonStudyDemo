import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import comb, perm

print(comb(5, 3))
plt.subplot(121)
n = 10
p = 0.3
k = np.arange(0, 30)
binomial = stats.binom.pmf(k, n, p)
plt.plot(k, binomial, 'o-')
# 使用rvs函数模拟一个二项随机变量，其中参数size指定你要进行模拟的次数，这里为10000次。
plt.subplot(122)
binom_sim = data = stats.binom.rvs(n=10000000, p=0.1, size=10000)
# print "Mean: %g" % np.mean(binom_sim)
# print "Sd: %g" % np.std(binom_sim, ddof=1)
plt.hist(binom_sim, bins=10, normed=True)

plt.show()

