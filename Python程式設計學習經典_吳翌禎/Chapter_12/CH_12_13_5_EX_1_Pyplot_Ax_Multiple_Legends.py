#--------------------------------------------------
#   CH_12_13_5_EX_1_Pyplot_Ax_Multiple_Legends.py
#--------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
lines = []
styles = ['-', '--', '-.', ':']
colors = ['r', 'g', 'b', 'k']
#
fig1, ax1 = plt.subplots()
#
for ii in range(4):
    lines += ax1.plot(x, np.sin(x - ii*np.pi/2), styles[ii], color = colors[ii], lw = 3)
#----- 原來一組圖例 (line-1, line-2)
ax1.axis('equal')
ax1.grid('on')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
#
ax1.legend(lines[:2], ['Line 1', 'Line 2'],\
           loc = 'upper left', frameon = True)
#----- 增加另一組圖例 (line-3, line-4)
from matplotlib.legend import Legend
leg1 = Legend(ax1, lines[2:], ['Line 3', 'Line 4'], loc='lower left', frameon=False)
ax1.add_artist(leg1)
#
plt.suptitle('Usage of Multiple_Legends')
plt.savefig('CH_12_13_5_EX_1_Pyplot_Ax_Multiple_Legends.png')
plt.show()

















































































	


