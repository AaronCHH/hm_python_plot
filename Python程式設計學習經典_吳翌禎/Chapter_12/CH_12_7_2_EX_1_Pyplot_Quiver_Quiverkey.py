#----------------------------------------------
#   CH_12_7_2_EX_1_Pyplot_Quiver_Quiverkey.py
#----------------------------------------------
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
#----- 繪製向量圖 (使用預設參數)
plt.subplot(1,2,1)
c1 = plt.contour(x, y, Z)
plt.clabel(c1, colors = 'black')
plt.quiver(X, Y, U, V, angles = 'xy')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.title('quiver')
#----- 繪製等高線圖 (使用自訂參數) 加繪向量註解 (quiverkey)
plt.subplot(1,2,2)
values = [-50, -25., 0., 25., 50]
c2 = plt.contour(x, y, Z, values, linewidths = 3, linestyles = 'dashed')
plt.clabel(c2, colors = 'black')
q2 = plt.quiver(X, Y, U, V, angles = 'xy')
plt.quiverkey(q2, -9, 10.5, 20, '20 m/s', coordinates = 'data')
plt.xlabel('x')
plt.axis('square')
plt.title('quiverkey')
#
plt.savefig('CH_12_7_2_EX_1_Pyplot_Quiver_Quiverkey.png')
plt.show()








































































	


