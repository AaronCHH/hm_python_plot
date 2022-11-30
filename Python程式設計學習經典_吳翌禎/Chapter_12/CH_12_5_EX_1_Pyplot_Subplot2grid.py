#-----------------------------------------
#   CH_12_5_EX_1_Pyplot_Subplot2grid.py
#-----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 2*np.pi, 101)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x)
y4 = np.log(x)
#
fig0 = plt.figure(0)
#----- 第1張子圖，位置在 (0, 0)，列寬1，欄寬3
plt.subplot2grid((3, 3), (0, 0), rowspan = 1, colspan = 3)
plt.plot(x, y1, '-r', lw = 2)
plt.grid()
#----- 第2張子圖，位置在 (1, 0)，列寬2，欄寬2
plt.subplot2grid((3, 3), (1, 0), rowspan = 2, colspan = 2)
plt.plot(x, y2, '-g', lw = 2)
plt.grid()
#----- 第3張子圖，位置在 (1, 2)，列寬1，欄寬1
plt.subplot2grid((3, 3), (1, 2), rowspan = 1, colspan = 1)
plt.plot(x, y3, '-b', lw = 2)
plt.grid()
#----- 第4張子圖，位置在 (2, 2)，列寬1，欄寬1
plt.subplot2grid((3, 3), (2, 2), rowspan = 1, colspan = 1)
plt.plot(x, y4, '-k', lw = 2)
plt.grid()
#
plt.savefig('CH_12_5_EX_1_Pyplot_Subplot2grid.png')
plt.show()































































	


