#-----------------------------------------------
#   CH_12_10_EX_2_Pyplot_Text_Xlabel_Ylabel.py   
#-----------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x) 
#
fig1 = plt.figure(1)
#----- x軸 y軸標籤文字 (y 軸改水平)
plt.subplot(1,2,1)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 20, rotation = 'horizontal')
plt.grid(axis = 'both')
plt.title(r'$y = sin(x)$')
#----- x軸 y軸標籤文字 (x 軸改小)
plt.subplot(1,2,2)
plt.plot(x, yc, 'b--', lw = 2)
plt.xlabel('x', fontsize = 'small')
plt.grid(axis = 'both')
plt.title(r'$y = cos(x)$')
#
plt.savefig('CH_12_10_EX_2_Pyplot_Text_Xlabel_Ylabel.png')
plt.show()










































































	


