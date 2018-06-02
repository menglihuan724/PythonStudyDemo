import numpy as np
from scipy import linalg

arr =np.array([[1,2],[3,4]])
# 逆,转置
print(linalg.inv(arr))
print(arr.T)
a=np.asmatrix(arr,np.int64)
# print (a*(a.I))
# 置换矩阵
b=np.asmatrix([[0,1],[1,0]],np.int64)
print(a*b)
print(b*a)
# 行列式,秩
print(np.linalg.det(a))
rank =np.array([[1,2,6,5],[3,1,1,1]])
print(np.linalg.matrix_rank(rank.T))
