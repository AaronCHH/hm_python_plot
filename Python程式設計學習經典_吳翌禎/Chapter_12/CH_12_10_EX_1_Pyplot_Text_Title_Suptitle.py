#------------------------------------------------
#   CH_12_10_EX_1_Pyplot_Text_Title_Suptitle.py
#------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x) 
#----- 標題使用數學文字
fig1 = plt.figure(1)
plt.subplot(1,2,1)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.title(r'$y = sin(x)$')
#----- 標題使用數學文字
plt.subplot(1,2,2)
plt.plot(x, yc, 'b--', lw = 2)
plt.xlabel('x')
plt.grid(axis = 'both')
plt.title(r'$y = cos(x)$')
#----- 總標題
plt.suptitle('Trigonometric Functions', fontsize = 15)
plt.savefig('CH_12_10_EX_1_Pyplot_Text_Title_Suptitle.png')
plt.show()









































































	


