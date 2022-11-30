#--------------------------------------
#   CH_12_17_9_EX_1_Mplot3d_Quiver.py   
#--------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
x = np.linspace(-4,4,21)
y = np.linspace(-4,4,21)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) 
Z = np.exp(-0.5*R)
u = (2*X)
v = (2*Y)
w = 1.
#
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(121, projection='3d')
#
cset1 = ax1.quiver(X, Y, Z, u, v, w, length = 0.2, normalize = True)
ax1.view_init() 
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.title('view_inut()')
#
ax2 = fig1.add_subplot(122, projection='3d')
#
cset2 = ax2.quiver(X, Y, Z, u, v, w, length = 0.1, normalize = True)
ax2.view_init(45, 45)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.title('view_init = (45,45)')
#
plt.suptitle('Using quiver')
plt.savefig('CH_12_17_9_EX_1_Mplot3d_Quiver.png')
plt.show()
























































































	


