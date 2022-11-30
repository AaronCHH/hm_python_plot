#------------------------------------------------
#   CH_12_12_EX_1_Pyplot_AxisTicksGrids_Axis.py
#------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
theta = np.linspace(0, 2*np.pi, 361)
x = 3 * np.cos(theta)
y = 3 * np.sin(theta)
#
fig1 = plt.figure(1)
plt.subplot(2,2,1)
#----- 設定數值
plt.plot(x, y, 'r-', lw = 2)
plt.axis([-5, 5, -5, 5])
plt.text(-2, 0., '[-5, 5, -5, 5]')
#----- 設定 square
plt.subplot(2,2,2)
plt.plot(x, y, 'r-', lw = 2)
plt.axis('square')
plt.text(-1, 0., 'square')
#----- 設定 equal
plt.subplot(2,2,3)
plt.plot(x, y, 'r-', lw = 2)
plt.axis('equal')
plt.text(-1, 0., 'equal')
#----- 設定 off
plt.subplot(2,2,4)
plt.plot(x, y, 'r-', lw = 2)
plt.axis('off')
plt.text(-1, 0., 'off', fontsize = 15)
#
plt.suptitle('Usage of plt.axis')
plt.savefig('CH_12_12_EX_1_Pyplot_AxisTicksGrids_Axis.png')
plt.show()












































































	


