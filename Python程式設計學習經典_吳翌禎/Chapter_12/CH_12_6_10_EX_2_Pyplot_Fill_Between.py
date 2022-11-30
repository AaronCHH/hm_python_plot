#-------------------------------------------
#   CH_12_6_10_EX_2_Pyplot_Fill_Between.py
#-------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0., 4*np.pi, 721)
ys = np.sin(x)
yc = np.cos(x)
y0 = 0.
#
fig0 = plt.figure(0)
#----- 繪製 cos(x) <= sin(x) 填滿差距圖
plt.subplot(3,1,1)
plt.plot(x, ys, 'r-', lw = 2)
plt.plot(x, yc, 'g--', lw = 2)
plt.fill_between(x, ys, yc, where = yc<=ys, facecolor = 'm', interpolate = True)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('fill_between')
#----- 繪製 cos(x) >= sin(x) 填滿差距圖
plt.subplot(3,1,2)
plt.plot(x, ys, 'r-', lw = 2)
plt.plot(x, yc, 'g--', lw = 2)
plt.fill_between(x, ys, yc, where = yc>=ys, facecolor = 'y', interpolate = False)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#----- 繪製 cos(x) <= 0, cos(x)>=0 填滿差距圖
plt.subplot(3,1,3)
plt.plot(x, yc, 'b-.', lw = 2)
plt.fill_between(x, y0, yc, where = yc>=y0, facecolor = 'cyan', interpolate = True)
plt.fill_between(x, y0, yc, where = yc<=y0, facecolor = 'cyan', interpolate = True)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#
plt.savefig('CH_12_6_10_EX_2_Pyplot_Fill_Between.png')
plt.show()






































































	


