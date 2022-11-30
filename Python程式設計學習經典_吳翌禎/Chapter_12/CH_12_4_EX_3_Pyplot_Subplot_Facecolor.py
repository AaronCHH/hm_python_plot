#---------------------------------------------
#   CH_12_4_EX_3_Pyplot_Subplot_Facecolor.py
#---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 361)
y = np.sin(x)
#
fig0 = plt.figure()
#----- 依序取值在不同圖序中使用不同色彩
for index, color in enumerate("rgbycw"):
    plt.subplot(2,3,1+index, facecolor = color)
    plt.plot(x, y, 'k-', lw = 2)
    plt.grid()
plt.savefig('CH_12_4_EX_3_Pyplot_Subplot_Facecolor.png')
plt.show()




























































	


