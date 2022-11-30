#-------------------------------------------------------
#   CH_12_12_EX_2_Pyplot_AxisTicksGrids_Ticks_Grids.py
#-------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x)
#----- 設定 xlim, ylim, grid, xticks, yticks, minorsticks
plt.figure(figsize = (4, 3))
plt.xlim(0, 2*np.pi)
plt.ylim(-1, 1)
plt.xlabel('Radian')
plt.ylabel('Value')
plt.grid(color='orangered')
plt.xticks((0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi))
plt.yticks((0, 1))
plt.minorticks_on()
plt.tick_params(which='major', direction='in', length=6, width=2, color='r')
#
plt.plot(x, ys, 'r-', lw = 2,  label = 'Sin')
plt.plot(x, yc, 'b--',  lw = 2, label= 'Cos')
#
plt.axhline(y=0, color='black', lw = 2)
plt.legend()
#
plt.suptitle('Usage of Ticks and Grids')
plt.savefig('CH_12_12_EX_2_Pyplot_AxisTicksGrids_Ticks_Grids.png')
plt.show()













































































	


