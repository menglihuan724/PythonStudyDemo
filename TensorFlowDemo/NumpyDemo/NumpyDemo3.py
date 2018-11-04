import numpy as np

x=np.array([1.0,3.0,5.0,7.0])
y=np.array([2.0,4.0,8.0,10.0])
# 加
print(x+y)
# 减
print(y-x)
# 乘
print(x*y)
# 除
print(y/x)
#矢量积
print(np.dot(x,y))

print('2D----------------------------')

#2D
A=np.array([[1,2],[3,4]])
B=np.array([[3,0],[0,6]])
print(A*B)
print(np.dot(A,B))
print(np.multiply(A,B))
#转换成matrix后*就不在点乘,而是计算矢量积
print(np.asmatrix(A)*np.asmatrix(B))

print('broadcast----------------------------')

A=np.array([[1,2],[3,4]])
B=np.array([[1,2]])
print(A*B)