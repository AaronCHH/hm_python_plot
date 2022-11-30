#---------------------------------------------
#   CH_12_11_EX_1_Pyplot_Drawlines_Arrows.py
#---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
fig1 = plt.figure(1)
plt.subplot(1,2,1)
#
x = np.linspace(0, 2*np.pi, 361)
ys = np.sin(x)
plt.plot(x, ys, 'r-', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
#----- 加水平線 (繪製X-軸線) (使用預設參數)
plt.axhline(y=0) 
#----- 加垂直線 (繪製Y-軸線) (使用自訂參數)

plt.axvline(x=0, linewidth = 1, linestyle ='-', color = 'black')
#----- 繪製水平線 (各種參數組合)
plt.subplot(1,2,2)
plt.axis([-10, 10, -10, 10])
plt.axhline(y=-5, linewidth = 2, linestyle ='-', color = 'green')
plt.axhline(y=5, lw = 2, ls ='--', color = 'blue')
#----- 繪製垂直線 (各種參數組合)
plt.axvline(x=-5, linewidth = 2, linestyle ='-.', color = 'red')
plt.axvline(x=5, lw = 2, ls =':', color = 'black')
#----- 繪製寬帶水平垂直條塊與箭頭
plt.axhspan(0, 1, color = 'magenta')
plt.axvspan(0, 2, color = 'yellow')
plt.arrow(0, 0, 4, 4, linewidth = 3, head_width = 0.5, head_length = 0.8,\
 fc = 'yellow', ec = 'blue')
#
plt.savefig('CH_12_11_EX_1_Pyplot_Drawlines_Arrows.png')
plt.show()












































































	


