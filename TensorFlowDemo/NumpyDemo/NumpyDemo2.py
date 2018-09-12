#!/usr/bin/python
#coding:utf8

import numpy as np

arr=np.arange(10)
print(f'开方:{np.sqrt(arr)}')
print(f'科学技术法:{np.exp(arr)}')
print(f'平均数:{np.mean(arr)}')
print(f'大于0:{arr>0}')
print(f'any:{arr.any()}',f'all:{arr.all()}')
np.save("text",arr)
arr2=np.load("text.npy")
print(arr2)

