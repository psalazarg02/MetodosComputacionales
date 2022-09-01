import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

A=1
omega = 2*np.pi/10
n=200

t=np.linspace(0,10,n)
r=np.zeros((n,2))
v=np.zeros((n,2))

def Get_Position():
    r[:,0]=A*np.cos(omega*t)
    r[:,1]=A*np.sin(omega*t)
    
def Get_Velocity():
    v[:,0]=A*omega*np.cos(omega*t)
    v[:,0]=A*omega*np.sin(omega*t)
    
Get_Position()
Get_Velocity()

# plt.scatter(r[:,0],r[:,1])
# plt.axis('off')
fig=plt.figure(figsize=(2,2))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
# ax3=fig.add_subplot(3,2,1)


def init():
    ax1.set_ylim(-A,A)
    ax2.set_ylim(-A,A)
    
    
def update(i):
    plot=ax1.clear()
    plot=ax2.clear()
    
    init()
    
    plot=ax1.plot(t[:i],r[:i,0])
    plot=ax2.plot(t[:i],r[:i,1])
    return plot

Animation=anim.FuncAnimation(fig,update,frames=n,init_func=init)
# writer=anim.writers['ffmpeg']
# writer_=writer(fps=10,metadata=dict(artist='io'))

plt.show()