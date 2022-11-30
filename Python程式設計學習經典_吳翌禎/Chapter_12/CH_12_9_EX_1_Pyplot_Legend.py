#----------------------------------
#   CH_12_9_EX_1_Pyplot_Legend.py
#----------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x) 
#
fig1 = plt.figure(1)
#----- 標示圖例 (使用預設參數)
plt.subplot(2,2,1)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.plot(x, yc, 'b--', lw = 2, label = r'$Cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.legend(loc='best')
#----- 標示圖例 (使用自訂參數)
plt.subplot(2,2,2)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.plot(x, yc, 'b--', lw = 2, label = r'$Cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.legend(loc = 3, frameon = False, ncol = 2)
#----- 標示圖例 (使用自訂參數)
plt.subplot(2,2,3)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.plot(x, yc, 'b--', lw = 2, label = r'$Cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.legend(loc = 9, fancybox = True, shadow = True, borderpad = 0.1,\
           framealpha = 1, facecolor = 'yellow', edgecolor = 'red',\
           mode = 'expand', ncol = 2, title = 'Trigonometric functions')
#----- 標示圖例 (使用自訂參數)
plt.subplot(2,2,4)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.plot(x, yc, 'b--', lw = 2, label = r'$Cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.legend(bbox_to_anchor = (1, 1), fontsize = 15)
#
plt.savefig('CH_12_9_EX_1_Pyplot_Legend.png')
plt.show()









































































	


