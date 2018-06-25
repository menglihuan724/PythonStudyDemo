import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
import random

# x = np.arange(4)
# xx = x.reshape(4,1)
# y = np.ones(5)
# z = np.ones((3,4))
# a = np.array([0.0, 10.0, 20.0, 30.0])
# print(a[:, np.newaxis])
# print(x)
# print(xx)
# print(y)
# print(z)
# print(xx+y)
fig = plt.figure()
ax = Axes3D(fig)
x=np.arange(0,20)
y=np.arange(0,10)

z=np.random.randint(0,200,size=(10,20))
x,y=np.meshgrid(x,y)
# y3=np.random.randint(0,500,size=(205,205))
ax.scatter(x,y,z,marker='.',s=10, label='')
plt.show()


# mpl.rcParams['font.size'] = 10
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for z in [2011, 2012, 2013, 2014]:
#     xs = range(1,13)
#     ys = 1000 * np.random.rand(12)
#     color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
#     ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=0.8)
#
# ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
# ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))
# ax.set_xlabel('Month')
# ax.set_ylabel('Year')
# ax.set_zlabel('Sales Net [usd]')
# plt.show()