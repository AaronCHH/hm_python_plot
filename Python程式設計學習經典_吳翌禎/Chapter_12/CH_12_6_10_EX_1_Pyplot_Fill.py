#-----------------------------------
#   CH_12_6_10_EX_1_Pyplot_Fill.py
#-----------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0., 4*np.pi, 721)
ys = np.sin(x)
yc = np.cos(x)
#
fig0 = plt.figure(0)
#----- 繪製 sin(x) 填滿圖
plt.subplot(3,1,1)
plt.plot(x, ys, 'r-', lw = 2)
plt.fill(x, ys, 'm')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('fill')
#----- 繪製 cos(x) 填滿圖
plt.subplot(3,1,2)
plt.plot(x, yc, 'g--', lw = 2)
plt.fill(x, yc, 'y')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#----- 繪製 cos(x)-sin(x) 填滿圖
plt.subplot(3,1,3)
plt.plot(x, yc-ys, 'b-.', lw = 2)
plt.fill(x, yc-ys, 'c')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#
plt.savefig('CH_12_6_10_EX_1_Pyplot_Fill.png')
plt.show()






































































	


