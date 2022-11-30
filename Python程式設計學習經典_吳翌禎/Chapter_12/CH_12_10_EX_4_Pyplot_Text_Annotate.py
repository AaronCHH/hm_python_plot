#------------------------------------------
#   CH_12_10_EX_4_Pyplot_Text_Annotate.py
#------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
fig1 = plt.figure(1)
#----- Annotate 用法(1) 
plt.subplot(1,2,1)
#
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.plot(t, s, lw=2)
#
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
#----- Annotate 用法(2) 
plt.subplot(1,2,2, polar = True)
r = np.arange(0,1,0.001)
theta = 2*2*np.pi*r
plt.plot(theta, r, color='#ee8d18', lw=3)
#
ind = 800
thisr, thistheta = r[ind], theta[ind]
plt.plot([thistheta], [thisr], 'o')
plt.annotate('a polar annotation', 
xy=(thistheta, thisr),  # theta, radius
            xytext=(0.6, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left', verticalalignment='bottom',)
#
plt.savefig('CH_12_10_EX_4_Pyplot_Text_Annotate.png')
plt.show()











































































	


