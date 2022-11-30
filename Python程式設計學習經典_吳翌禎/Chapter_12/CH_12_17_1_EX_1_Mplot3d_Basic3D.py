#---------------------------------------
#   CH_12_17_1_EX_1_Mplot3d_Basic3D.py
#---------------------------------------
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#
fig1 = plt.figure(1)
ax1 = plt.axes(projection = '3d')
plt.title("plt.axes(projection = '3d')")
plt.savefig('CH_12_17_1_EX_1(a)_Mplot3d_Basic3D.png')
#
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection = '3d')
plt.title("fig.added_subplot(projection = '3d')")
plt.savefig('CH_12_17_1_EX_1(b)_Mplot3d_Basic3D.png')
#
plt.show()




















































































	


