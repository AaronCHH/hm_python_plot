#----------------------------------------
#   CH_12_17_8_EX_1_Mplot3d_Contourf.py
#----------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
x = np.linspace(-4,4,81)
y = np.linspace(-4,4,81)
X, Y = np.meshgrid(x, y)
Z = np.exp(-0.5*np.sqrt(X**2 + Y**2))
#
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(121, projection='3d')
#
cset1 = ax1.contourf(X, Y, Z, 20, cmap = 'autumn')
ax1.view_init() 
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.title('view_init()')
#
ax2 = fig1.add_subplot(122, projection='3d')
#
cset2 = ax2.contourf(X, Y, Z,20, cmap = 'winter')
ax2.view_init(45, 45) 
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.title('view_init = (45,45)')
#
plt.suptitle('Using contourf')
plt.savefig('CH_12_17_8_EX_1_Mplot3d_Contourf.png')
plt.show()
























































































	


