#---------------------------------------------------
#   CH_12_13_3_EX_1_Pyplot_Ax_Xaxis_Set_Visible.py
#---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x)
#----- 上圖使用隱藏 xaxis 之顯示
fig1 = plt.figure()
ax1 = plt.subplot(2,1,1)
ax1.plot(x, ys, 'r-', lw=2, label = 'sin(x)')
ax1.set_ylabel('y')
ax1.xaxis.set_visible(False)
ax1.legend()
#----- 下圖正常 xaxis 之顯示
ax2 = plt.subplot(2,1,2)
ax2.plot(x, yc, 'b--', lw=2, label = 'cos(x))')
ax2.set_ylabel('y')
ax2.set_xlabel('x')
ax2.legend()
#
plt.suptitle('Usage of set_visible')
plt.savefig('CH_12_13_3_EX_1_Pyplot_Ax_Xaxis_Set_Visible.png')
plt.show()
















































































	


