#--------------------------------------------------------
#   CH_12_6_3_EX_2_Pyplot_Lines_Continuous_Functions.py
#--------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0., 2.*np.pi, 361)
y1 = np.sin(x)
y2 = np.cos(x)
xm = [0., 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi]
y1m = np.sin(xm)
y2m = np.cos(xm)
#
fig0 = plt.figure(0)
#----- 繪製曲線圖 (線) (line)
plt.subplot(2,1,1)
plt.plot(x, y1, 'r-', label = 'sin(x)')
plt.plot(x, y2, 'b--', lw = 2, label = 'cos(x)')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric functions')
#----- 繪製曲線圖 (線+符號) (line + marker)
plt.subplot(2,1,2)
plt.plot(x, y1, 'r-.', lw = 3, label = 'sin(x)')
plt.plot(x, y2, 'b:', lw = 4, label = 'cos(x)')
plt.plot(xm, y1m, 'rs', markersize = 10)
plt.plot(xm, y2m, 'bo', markersize = 12, mfc = 'yellow', mec = 'darkgreen',\
         mew = 2)
plt.legend(loc = 'best')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('y')
#
plt.savefig('CH_12_6_3_EX_2_Pyplot_Lines_Continuous_Functions.png')
plt.show()

































































	


