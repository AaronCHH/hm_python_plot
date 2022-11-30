#----------------------------------------
#   CH_12_17_10_EX_1_Mplot3d_3d_Text.py
#----------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
xs = (1, 4, 4, 9, 4, 1)
ys = (2, 5, 8, 10, 1, 2)
zs = (10, 3, 8, 9, 1, 8)
#
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(121, projection='3d')
#
for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
    ax1.text(x, y, z, label, zdir)
ax1.text(9, 0, 0, "red", color='red')
ax1.text2D(0.05, 0.95, "2D Text", transform = ax1.transAxes)
ax1.view_init() 
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_zlim(0, 10)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
plt.title('view_init()')
ax2 = fig1.add_subplot(122, projection='3d')
for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
    ax2.text(x, y, z, label, zdir)
ax2.text(9, 0, 0, "red", color='red')
ax2.text2D(0.05, 0.95, "2D Text", transform = ax2.transAxes)
ax2.view_init(45, 45) 
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_zlim(0, 10)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
plt.title('view_init = (45,45)')
#
plt.suptitle('Using 3D Text')
plt.savefig('CH_12_17_10_EX_1_Mplot3d_3d_Text.png')
plt.show()

























































































	


