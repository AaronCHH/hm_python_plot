#-----------------------------------------
#   CH_12_17_4_EX_1_Mplot3d_Bar3D_Bar.py
#-----------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
fig1 = plt.figure(1, figsize=(8, 6))
#
ax1 = fig1.add_subplot(121, projection = '3d')
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [2,3,4,5,1,6,2,1,7,2]
zpos = [0,0,0,0,0,0,0,0,0,0]
num_elements = len(xpos)
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]
#
ax1.bar3d(xpos,ypos,zpos,dx,dy,dz, color ='#00ceaa')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.title('Using bar3D')
#
ax2 = fig1.add_subplot(122, projection = '3d')
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [2,3,4,5,1,6,2,1,7,2]
zpos = [0,0,0,0,0,0,0,0,0,0]
num_elements = len(xpos)
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]
#
ax2.bar(xpos, ypos, zpos, zdir = 'y', color ='#00ceaa', alpha = 0.8)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.title('Using bar (in 3D)')
#
plt.savefig('CH_12_17_4_EX_1_Mplot3d_Bar3D_Bar.png')
plt.show()






















































































	


