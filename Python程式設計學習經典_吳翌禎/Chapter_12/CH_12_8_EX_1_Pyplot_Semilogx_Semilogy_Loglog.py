#----------------------------------------------------
#   CH_12_8_EX_1_Pyplot_Semilogx_Semilogy_Loglog.py   
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0., 10., 11)
y1 = np.exp(-0.5*x)
#----- 繪製實數座標曲線 (X-Y)
plt.subplot(2,2,1)
plt.plot(x, y1, 'r-', lw = 3, label = 'x-y')
plt.ylabel('y')
plt.grid()
plt.legend(loc='best')
#----- 繪製半對數座標曲線 (logX-Y)
plt.subplot(2,2,2)
plt.semilogx(x, y1, 'g-', lw = 3, label = 'logx-y')
plt.xlabel('x')
plt.grid()
plt.legend(loc='best')
#----- 繪製半對數座標曲線 (X-logY)
plt.subplot(2,2,3)
plt.semilogy(x, y1, 'b-', lw = 3, label = 'x-logy')
plt.xlabel('x')
plt.ylabel('logy')
plt.grid()
plt.legend(loc='best')
#----- 繪製雙對數座標曲線 (logX-logY)
plt.subplot(2,2,4)
plt.loglog(x, y1, 'k-', lw = 3, label = 'logx-logy')
plt.grid()
plt.xlabel('logx')
plt.legend(loc='best')
#
plt.savefig('CH_12_8_EX_1_Pyplot_Semilogx_Semilogy_Loglog.png')
plt.show()









































































	


