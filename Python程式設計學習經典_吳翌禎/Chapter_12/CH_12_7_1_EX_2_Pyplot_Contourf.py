#---------------------------------------
#    CH_12_7_1_EX_2_Pyplot_Contourf.py
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(-10., 10., 101)
y = np.linspace(-10., 10., 101)
X, Y = np.meshgrid(x, y)
#
Z = X*Y
#----- 繪製填滿等高線圖 (使用預設參數)
plt.subplot(1,2,1)
c1 = plt.contourf(x, y, Z)
plt.colorbar(c1, orientation = 'horizontal')
plt.clabel(c1, colors = 'black')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.title('contour (default)')
#----- 繪製填滿等高線圖 (使用自訂參數)
plt.subplot(1,2,2)
values = [-50, -25., 0., 25., 50]
c2 = plt.contourf(x, y, Z, values, linewidths = 3, linestyles = 'dashed')
plt.colorbar(c2, orientation = 'vertical')
plt.clabel(c2, colors = 'black')
plt.xlabel('x')
plt.axis('square')
plt.title('contour(customized)')
#
plt.savefig('CH_12_7_1_EX_2_Pyplot_Contourf.png')
plt.show()








































































	


