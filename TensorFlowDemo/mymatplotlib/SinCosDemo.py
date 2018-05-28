import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,endpoint=True)
C=np.cos(x)
S=np.sin(x)
plt.plot(C)
plt.plot(S)
plt.show()