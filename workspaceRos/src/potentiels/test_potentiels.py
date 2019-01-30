from roblib import draw_tank
import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt

x = np.array([1,0,0,0,0])

def dx(X,dt):
    x,y, th, v, dth = X
    return x + dt*(np.array(v*cos(th),v*sin(th),dth,))

for i in range(1000):
    draw_tank(x,col='darkblue',r=1,w=2)
    plt.show()
