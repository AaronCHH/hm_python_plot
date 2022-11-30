#-----------------------------------
#   CH_12_3_EX_1_Pyplot_Figure.py
#-----------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
y = np.sin(x)
#
fig0 = plt.figure()
plt.plot(x, y, 'r-', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('CH_12_3_1_A_Pyplot_Figure1_Default.png')
#
fig1 = plt.figure('My_Figure', figsize = (5, 3.5), dpi = 72,\
                  frameon=True, facecolor ='#FFFF00', edgecolor='blue')
plt.plot(x, y, 'r-', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('CH_12_3_1_B_Pyplot_Figure_Customized.png',\
          facecolor = '#FFFF00', edgecolor = 'blue')
plt.show()



























































	


