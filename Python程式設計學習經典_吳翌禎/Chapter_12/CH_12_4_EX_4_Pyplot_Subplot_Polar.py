#------------------------------------------
#    CH_12_4_EX_4_Pyplot_Subplot_Polar.py
#------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
r = 0.5
theta = np.linspace(0., 2.*np.pi, 361)
rho = 2 * r * (1. - np.cos(theta))
#----- 使用 projection 參數為 polar 繪製極座標圖
fig0 = plt.figure()
plt.subplot(111, projection='polar')
plt.plot(theta, rho)
plt.savefig('CH_12_4_EX_4_Pyplot_Subplot_Polar.png')
plt.show()





























































	


