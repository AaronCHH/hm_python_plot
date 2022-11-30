#--------------------------------------------
#   CH_12_10_EX_3_Pyplot_Text_Greek_Math.py
#--------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x) 
#----- 文字標示 (希臘字母及上下標)
fig1 = plt.figure(1)
plt.subplot(1,2,1)
plt.plot(x, ys, 'r-', lw = 2, label = r'$Sin(x)$')
plt.xlabel(r'$\omega \/ \tau$')
plt.ylabel('y')
plt.grid(axis = 'both')
plt.text(0.1, -0.5, r'$\sigma_{ij}^2 = \/ -\infty$', fontsize = 15)
plt.title(r'$y = \sin(\omega \/\tau)$')
#----- 文字標示 (希臘字母及頂線)
plt.subplot(1,2,2)
plt.plot(x, yc, 'b--', lw = 2)
plt.xlabel('t')
plt.grid(axis = 'both')
plt.text(0.2, 0.8, r'${\tilde x}_\theta \/with\/ \omega = 1$', fontsize = 15)
plt.title(r'$y = cos(t)$')
#
plt.savefig('CH_12_10_EX_3_Pyplot_Text_Greek_Math.png')
plt.show()










































































	


