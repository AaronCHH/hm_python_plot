#--------------------------------------------
#   CH_12_2_EX_1_Basic_Plot_Using_Pyplot.py
#--------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
y = np.sin(x)
#
fig1 = plt.figure(1, figsize = (8, 6), dpi = 80)
plt.plot(x, y, 'r-', lw = 2, label = r'$Sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.text(3.14, 0, r'$\pi$', fontsize = 20)
plt.text(2*3, 0, r'$2\pi$', fontsize = 20)
plt.title('Example of plotting ${\it sin(x)}$')
plt.grid(axis = 'both')
plt.legend(loc = 'best')
plt.axhline(y = 0, color='black')
plt.axis([0., 2.*np.pi, -1., 1.])
plt.savefig('CH_12_2_1_Basic Plot Using Pyplot.png')
plt.show()


























































	


