import  numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6),dpi=120)
plt.subplot(2,2,2)
x=np.linspace(-np.pi,np.pi)
C,S=np.sin(x),np.cos(x)
plt.plot(x,C,color='blue', linewidth=3.0, linestyle="-")
plt.plot(x,S, color="green", linewidth=3.0, linestyle="-")
plt.xlim(-4.0, 4.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.ylim(-2.0, 2.0)
plt.yticks(np.linspace(-3, 3, 5, endpoint=True))
plt.show()