#----------------------------------
#   CH_12_6_5_EX_1_Pyplot_Hist.py
#----------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
mu = 100
sigma = 10
x = mu + sigma * np.random.randn(1000)

# the histogram of the data
fig0 = plt.figure(0)
#----- 繪製直方圖 (使用預設參數)
plt.subplot(2,1,1)
plt.hist(x, bins=50)
plt.xlabel('x')
plt.ylabel('y')
#----- 繪製直方圖 (使用自訂參數)
plt.subplot(2,1,2)
plt.hist(x, bins=25, normed=1, facecolor='g', alpha=0.75)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
#
plt.savefig('CH_12_6_5_EX_1_Pyplot_Hist.png')
plt.show()


































































	


