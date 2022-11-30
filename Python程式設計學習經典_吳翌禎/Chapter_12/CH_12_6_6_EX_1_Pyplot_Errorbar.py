#--------------------------------------
#   CH_12_6_6_EX_1_Pyplot_Errorbar.py
#--------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# 
x = np.linspace(0., 2*np.pi, 36)
y_undamp = np.sin(x)
y_damp = np.exp(-0.2*x)*np.sin(x)
error = (y_undamp - y_damp)
#
fig0 = plt.figure(0)
#----- 繪製原始數據曲線圖
plt.subplot(3,1,1)
plt.plot(x, y_undamp, 'r-', label = 'undamped')
plt.plot(x, y_damp, 'b--', label = 'damped')
plt.grid()
plt.legend(loc=1)
plt.title('errorbar')
#----- 繪製誤差圖 (使用 yerr)
plt.subplot(3,1,2)
plt.errorbar(x, y_damp, yerr=error, fmt='-o')
plt.grid()
#----- 繪製誤差圖 (使用 xerr)
plt.subplot(3,1,3)
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
plt.errorbar(x, y_damp, xerr=asymmetric_error, fmt='o')
plt.grid()
#
plt.savefig('CH_12_6_6_EX_1_Pyplot_Errorbar.png')
plt.show()



































































	


