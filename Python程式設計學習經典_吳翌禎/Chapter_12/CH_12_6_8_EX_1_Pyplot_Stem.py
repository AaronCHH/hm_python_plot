#-----------------------------------
#   CH_12_6_8_EX_1_Pyplot_Stem.py
#-----------------------------------
import numpy as np
import matplotlib.pyplot as plt
# 
x = np.linspace(0., 2*np.pi, 9)
ys = np.sin(x)
yc = np.cos(x)
#
fig0 = plt.figure(0)
#----- 繪製 sin(x) 之針頭圖
plt.subplot(2,1,1)
markerline, stemlines, baseline = plt.stem(x, ys, '-')
plt.setp(baseline, 'color', 'magenta', 'linewidth', 3)
plt.plot(x, ys, 'r--', label = 'ys')
plt.grid()
plt.legend(loc=1)
plt.title('stem')
#----- 繪製 cos(x) 之針頭圖
plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(x, yc, '-.')
plt.setp(baseline, 'color', 'darkgreen', 'linewidth', 3)
plt.plot(x, yc, 'b--', label = 'yc')
plt.grid()
plt.legend(loc=4)
#
plt.savefig('CH_12_6_8_EX_1_Pyplot_Stem.png')
plt.show()





































































	


