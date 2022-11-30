#---------------------------------------
#   CH_12_17_6_EX_1_Mplot3d_Surface.py
#---------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
x = np.linspace(-4,4,81)
y = np.linspace(-4,4,81)
X, Y = np.meshgrid(x, y)
Z = np.exp(-0.5*np.sqrt(X**2 + Y**2))
#
fig1 = plt.figure()
ax1 = plt.axes(projection='3d')
ax1.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap = 'spring')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.title('Using plot_surface')
#
plt.savefig('CH_12_17_6_Mplot3d_Surface.png')
plt.show()























































































	


