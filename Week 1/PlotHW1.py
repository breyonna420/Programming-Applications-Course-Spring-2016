import numpy as np
from np import (sin, cos, pi )
import matplotlib.pyplot as plt

x = np.linspace(0,6*np.pi,100)
#y = np.linspace (0,6*np.pi,100)
plt.plot (x, np.sin(x), '--', linewidth=2)
plt.plot (x,np.cos(x), '-', linewidth=2)
plt.ylabel("y")
plt.xlabel("x")
plt.legend ('sin(x)', 'cos(x)')
plt.show
#Breyonna Pinkney 
#@02730553 
# 1/21/16

