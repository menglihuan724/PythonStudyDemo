import numpy as np
arr=np.arange(15).reshape(3,5)
print(arr)
#倒置
print(f'T:{arr.T}')
#按区域取
print(f'area:{arr[:2,2:]}')
#按索引取
print(f'index:{arr[[0,1],[0,1]]}')
print(f'0,1行,2,1列{arr[np.ix_([0,1],[2,0])]}')
c = np.linspace(0, 1, 6)
print(c)
p=np.poly1d([3,2,-1])
print(p(0))