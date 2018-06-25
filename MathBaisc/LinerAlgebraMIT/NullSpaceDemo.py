import scipy
import numpy as np
from scipy import linalg, matrix

def null(A, eps=1e-12):
    u, s, vh = scipy.linalg.svd(A)
    padding = max(0,np.shape(A)[1]-np.shape(s)[0])
    null_mask = np.concatenate(((s <= eps), np.ones((padding,),dtype=bool)),axis=0)
    null_space = scipy.compress(null_mask, vh, axis=0)
    return scipy.transpose(null_space)
A = matrix([[2,3,5],[-4,2,3]])


# 奇异矩阵零空间
print(A)
print (A*null(A))
# 方形矩阵零空间
A = matrix([[1,0,1,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
print (null(A))
print (A*null(A))



