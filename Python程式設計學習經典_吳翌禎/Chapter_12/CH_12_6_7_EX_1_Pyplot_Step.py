#----------------------------------
#   CH_12_6_7_EX_1_Pyplot_Step.py
#----------------------------------
import numpy as np
import matplotlib.pyplot as plt
# 
x = np.linspace(0., 2*np.pi, 9)
y0 = np.sin(x)
y1 = y0 + 0.2
#
fig0 = plt.figure(0)
#----- 繪製原始數據曲線
plt.subplot(4,1,1)
plt.plot(x, y0, 'r-', label = 'y0')
plt.plot(x, y1, 'b--', label = 'y1')
plt.grid()
plt.legend(loc=1)
plt.title('step')
#----- 繪製階梯圖 (使用預設 pre 參數)
plt.subplot(4,1,2)
plt.step(x, y1, lw = 2, label='pre (default)')
plt.plot(x, y1, 'b--', label = 'y1')
plt.grid()
plt.legend(loc=1)
#----- 繪製階梯圖 (使用 mid 參數)
plt.subplot(4,1,3)
plt.step(x, y1, lw = 2, where='mid', label='mid')
plt.plot(x, y1, 'b--', label = 'y1')
plt.grid()
plt.legend(loc=1)
#----- 繪製階梯圖 (使用 post 參數)
plt.subplot(4,1,4)
plt.step(x, y1, lw = 2, where='post', label='post')
plt.plot(x, y1, 'b--', label = 'y1')
plt.grid()
plt.legend(loc=1)
#
plt.savefig('CH_12_6_7_EX_1_Pyplot_Step.png')
plt.show()




































































	


