import  numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6),dpi=120)
plt.subplot(1,1,1)
x=np.linspace(-np.pi,np.pi)
C,S=np.sin(x),np.cos(x)
plt.plot(x,C,color='blue',label="sin", linewidth=3.0, linestyle="--")
plt.plot(x,S, color="green",label="cos", linewidth=3.0, linestyle="-")
plt.xlim(-5.0, 5.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True),)
plt.ylim(-4.0, 4.0)
plt.yticks(np.linspace(-3, 3, 5, endpoint=True),['tom','jerry','terry','jack','marry'])
plt.title("sin&cos")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()