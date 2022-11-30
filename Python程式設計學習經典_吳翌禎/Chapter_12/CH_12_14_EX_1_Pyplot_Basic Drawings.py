#-------------------------------------------
#   CH_12_14_EX_1_Pyplot_Basic Drawings.py
#-------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
plt.subplot(1,1,1)
plt.axis([-10, 10, -10, 10])
#----- 定義 3 個圓
circle1 = plt.Circle((0,0), 8, color = 'blue', fill = False, linewidth = 3)
circle2 = plt.Circle((0,0), 6, color = 'green', fill = False, linewidth = 2)
circle3 = plt.Circle((0,0), 1, color = 'red', linewidth = 2)   # fill = True
#----- 定義 2 個矩形
rect1 = plt.Rectangle((1,1), 2, 3, facecolor = 'white', edgecolor = 'magenta', linewidth = 2)
rect2 = plt.Rectangle((3,3), 3, 2, facecolor = 'yellow', edgecolor = 'black', linewidth = 3, linestyle='--')
#----- 定義 1 個多邊形
poly1 = plt.Polygon([[0,0], [-2,0], [-1, 4]], facecolor = 'cyan', edgecolor = 'orange')
#----- 將圖繪出
fig =plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)
fig.gca().add_artist(circle3)
fig.gca().add_artist(rect1)
fig.gca().add_artist(rect2)
fig.gca().add_artist(poly1)
#
plt.suptitle('Usage of Basic Drawings')
plt.savefig('CH_12_14_EX_1_Pyplot_Basic Drawing.png')
plt.show()


















































































	


