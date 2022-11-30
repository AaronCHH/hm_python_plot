#-------------------------------------
#   CH_12_6_9_EX_1_Pyplot_Boxplot.py
#-------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# 
# Random test data
data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
#
fig0 = plt.figure(0)
#----- 繪製標準盒鬚圖
plt.subplot(2,1,1)
plt.boxplot(data, vert=True, patch_artist=True, labels=labels)  
plt.grid()
plt.title('boxplot')
#----- 繪製變形(凹凸)盒鬚圖 (notch = True)
plt.subplot(2,1,2)
plt.boxplot(data, notch = True, vert=False, patch_artist=True, labels=labels)
plt.grid()
#
plt.savefig('EX_12_6_9_EX_1_Pyplot_Boxplot.png')
plt.show()






































































	


