#-------------------------------------
#   CH_12_16_3_EX_1_Pyplot_Plt_Rc.py
#-------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#
x = np.linspace(0., 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x)
#
fig1 = plt.figure(figsize=(8, 4))
#
plt.rcdefaults()
plt.subplot(1,2,1)
plt.plot(x, ys, 'r-', lw = 2)
plt.plot(x, yc, 'g--', lw = 2)
plt.xlabel('x')
#
plt.rc('axes', facecolor = 'grey', edgecolor = 'none', grid = True)
plt.rc('xtick', direction = 'in', color = 'gray')
plt.rc('ytick', direction = 'out', color = 'blue')
plt.rc('lines', linewidth = 4, color = 'magenta')
#
plt.subplot(1,2,2)
plt.plot(x, ys)
plt.plot(x, yc)
plt.xlabel('x')
plt.ylabel('y')
#
plt.suptitle('Using plt.rc')
plt.savefig('CH_12_16_3_EX_1_Pyplot_Plt_Rc.png')
plt.show()



	


