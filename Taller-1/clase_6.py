import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,10)
h=x[1]-x[0]
sin= lambda x: np.sin(x)
f=sin(x)

def derivadaR(x,f,h):
    return (f(x+h)-f(x))/h

def derivadaL(x,f,h):
    return (f(x)-f(x-h))/h

def derivadaC(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)
    

derivadaR=derivadaR(x,sin,h)
derivadaL=derivadaL(x,sin,h)
derivadaC=derivadaC(x,sin,h)

fig=plt.figure(figsize=(7,3))
# ax=fig.add_subplot(2,2,1)
ax1=fig.add_subplot(1,1,1)
# ax2=fig.add_subplot(2,2,3)

# ax.scatter(x,f)

ax1.scatter(x,derivadaR,label='derecha')
ax1.scatter(x,derivadaL,label='izquierda')
ax1.scatter(x,derivadaC,label='central')
ax1.scatter(x,np.cos(x),label='coseno')
ax1.legend(loc='lower right')

# ax2.scatter(x,np.abs(np.cos(x)-derivadaR))
# ax2.scatter(x,np.abs(np.cos(x)-derivadaL))
# ax2.scatter(x,np.abs(np.cos(x)-derivadaC))