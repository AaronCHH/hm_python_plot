#-------------------------------------
#   CH_12_6_4_EX_1_Pyplot_Scatter.py
#-------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.random.rand(10)
y = np.random.rand(10)
z = np.sqrt(x**2 + y**2)
s = 500*z
#
fig0 = plt.figure(0)
#----- 繪製散點圖 (使用預設參數)
plt.subplot(2,1,1)
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
#----- 繪製散點圖 (使用自訂參數)
plt.subplot(2,1,2)
plt.scatter(x, y, s = s, c = z, alpha = 0.8, marker = (5, 0))
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
#
plt.savefig('CH_12_6_4_EX_1_Pyplot_Scaatter.png')
plt.show()

































































	


