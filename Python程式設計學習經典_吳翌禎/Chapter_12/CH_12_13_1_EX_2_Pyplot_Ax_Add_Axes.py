#------------------------------------------
#   CH_12_13_1_EX_2_Pyplot_Ax_Add_Axes.py
#------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x12 = np.linspace(0, 12*np.pi, 361)
x2 = np.linspace(0, 2*np.pi, 361)
ys12 = np.sin(x12)
ys2 = np.sin(x2)
#
fig1 = plt.figure()
fig1.set_size_inches(8, 4)
#----- 繪製大圖 ax1
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x2, ys2, 'r-', lw = 3)
ax1.set_xticks((0., np.pi/2, np.pi, 1.5*np.pi, 2*np.pi))
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
#----- 在 ax1 中加入小圖 ax2
ax2 = fig1.add_axes([0.2, 0.15, 0.3, 0.3])
ax2.plot(x12, ys12, 'r-', lw = 2)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax2.set_xticks([])
#
plt.suptitle('Usage of add_axes (small one)')
plt.savefig('CH_12_13_1_EX_2_Pyplot_Ax_Add_Axes.png')
plt.show()















































































	


