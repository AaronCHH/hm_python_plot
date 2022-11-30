#------------------------------------------------
#   CH_12_17_3_EX_1_Mplot3d_Plot3D_Scatter3D.py
#------------------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
fig1 = plt.figure(1)
ax1 = plt.axes(projection = '3d')
#
xline = np.linspace(0., 15, 151)
yline = np.sin(xline)
zline = np.cos(xline)
ax1.plot3D(xline, yline, zline, 'r-')
#
xdata = 15 * np.random.random(100)
ydata = np.sin(xdata) + 0.1*np.random.randn(100)
zdata = np.cos(xdata) + 0.1*np.random.randn(100)
ax1.scatter3D(xdata, ydata, zdata, marker = 'o', s = 40)
#
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
#
plt.title('Plot3D & Scatter3D ')
plt.savefig('CH_12_17_3_EX_1_Mplot3d_Plot3D_ScatterD.png')
#
plt.show()





















































































	


