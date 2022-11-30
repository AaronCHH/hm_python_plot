#------------------------------------------
#   CH_12_13_1_EX_1_Pyplot_Ax_Add_Axes.py
#------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x)
#
fig1 = plt.figure()
#----- 先關閉兩圖之 xticklabels
ax1 = fig1.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim = (-1.2, 1.2))
ax2 = fig1.add_axes([0.1, 0.1, 0.8, 0.4], xticklabels=[], ylim = (-1.2, 1.2))
ax1.plot(x, ys, 'r-', lw = 2)
#----- 設定 ax1之 Y 軸標籤文字
ax1.set_ylabel('y')
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
#
ax2.plot(x, yc, 'b--', lw = 2)
#----- 設定 ax2 之xticks, X軸與 Y 軸標籤文字
ax2.set_xticks((0., np.pi/2, np.pi, 1.5*np.pi, 2*np.pi))
ax2.tick_params(which = 'major', direction='in', length=6, width=2, color='r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
#
plt.suptitle('Usage of add_axes')
plt.savefig('CH_12_13_1_EX_1_Pyplot_Ax_Add_Axes.png')
plt.show()














































































	


