#----------------------------------------
#   CH_12_7_3_EX_1_Pyplot_Streamplot.py
#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(-10., 10., 11)
y = np.linspace(-10., 10., 11)
X, Y = np.meshgrid(x, y)
#
Z = X*Y
U = 20*Y
V = 20*X
#----- 繪製流線圖 (使用預設 density) (加繪色值表)
plt.subplot(1,2,1)
c1 = plt.contour(x, y, Z)
plt.clabel(c1, colors = 'black')
strm = plt.streamplot(X, Y, U, V, color = U, linewidth = 2, cmap = 'autumn')
plt.colorbar(strm.lines)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.title('Varying Line Color')
#----- 繪製流線圖 (使用自訂 density)
plt.subplot(1,2,2)
values = [-50, -25., 0., 25., 50]
c2 = plt.contour(x, y, Z, values, linewidths = 3, linestyles = 'dashed')
plt.clabel(c2, colors = 'black')
#
speed = np.sqrt(U*U + V*V)
lw_var = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density = 0.6, color = 'k', linewidth = lw_var)
plt.xlabel('x')
plt.axis('square')
plt.title('Varying Line Width')
#
plt.savefig('CH_12_7_3_EX_1_Pyplot_Streamplot.png')
plt.show()









































































	


