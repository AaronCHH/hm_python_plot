#------------------------------------------------
#    CH_12_13_4_EX_1_Pyplot_Ax_Multiple_Scale.py
#------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#
C_temp = np.linspace(0., 100., 101)
F_temp = (9./5.)*C_temp + 32.
K_temp = C_temp + 273.
#
fig1 = plt.figure(1)
#----- 左方 Fahrenheit~ Celsius 溫標
ax_f = plt.subplot(1,1,1)
ax_f.plot(C_temp, F_temp, 'r-', lw = 2)
ax_f.set_xlim(0., 100.)
ax_f.grid('on')
ax_f.set_title('Two scales: Fahrenheit and Kelven vs. Celsius')
ax_f.set_ylabel('Fahrenheit')
ax_f.set_xlabel('Celsius')
#----- 右方 Kelvin~ Celsius 溫標
y1f, y2f = ax_f.get_ylim()
y1K = (5./9.)*(y1f - 32) + 273
y2K = (5./9.)*(y2f - 32) + 273
ax_K = ax_f.twinx()
ax_K.set_ylim(y1K, y2K)
ax_K.figure.canvas.draw()
ax_K.set_ylabel('Kelvin')
#
plt.savefig('CH_12_13_4_EX_1_Pyplot_Ax_Multiple_Scale.png')
plt.show()
















































































	


