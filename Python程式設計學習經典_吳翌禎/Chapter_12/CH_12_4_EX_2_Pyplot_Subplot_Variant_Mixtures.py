#----------------------------------------------------
#   CH_12_4_EX_2_Pyplot_Subplot_Variant_Mixtures.py
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(-10, 10, 101)
y1 = np.sin(x)
y2 = np.cos(x)
#----- (1) 組合-1  (上1下2)
fig0 = plt.figure()
plt.axis([-10, 10,-2, 2])
#
plt.subplot(2,1,1)
plt.plot(x, y1, '-r')
#
plt.subplot(2,2,3)
plt.plot(x, y2, '--r')
#
plt.subplot(2,2,4)
plt.plot(x, y2, '--b')
#
plt.savefig("CH_12_4_EX_2(a)_Pyplot_Subplot_Variant_Mixtures_(a).png")
plt.show()
#----- (2) 組合-2 (左1右 2)
fig1 = plt.figure()
plt.axis([-10, 10,-2, 2])
#
plt.subplot(1,2,1)
plt.plot(x, y1, '-r')
#
plt.subplot(2,2,2)
plt.plot(x, y2, '--r')
#
plt.subplot(2,2,4)
plt.plot(x, y2, '--b')
#
plt.savefig("CH_12_4_EX_2(b)_Pyplot_Subplot_Variant_Mixtures_(b).png")
plt.show()




























































	


