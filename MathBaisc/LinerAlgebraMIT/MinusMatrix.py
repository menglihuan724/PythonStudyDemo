import numpy as np
from scipy import linalg

arr =np.array([[1,2],[3,4]])
print(linalg.inv(arr))
print(arr.T)
a=np.asmatrix(arr,np.int64)
print (a*(a.I))
