#-------------------------------------------------
#   CH_12_15_2_EX_1_Pyplot_Drawings_Functions.py
#-------------------------------------------------
import numpy as np
from numpy import *
from numpy.linalg import norm, pinv
from matplotlib import pyplot as plt
fig1 = plt.figure(figsize=(4.5, 4.))
#----- 繪製函數之 Fourier 級數展開
plt.subplot(1,3,1)
plt.axis([-15, 15, -10, 10])
#----- 繪製座標軸
#----- x-軸
plt.arrow(-14, 0, 28, 0,  lw =1, head_width=0.4, head_length=0.8)
plt.text(14.8, 0, 'x')
#----- y-軸
plt.arrow(0, -4, 0, 10,  lw =1, head_width=0.8, head_length=0.4)
plt.text(-0.5, 7., 'y')
#----- 繪製離散數據點
x_train = np.mat('2., 2.3; 4., 2.; 6., 3.; 8., 2.5; 10., 3.5')
for ii in range(0,5):
        plt.plot(x_train[ii, 0], x_train[ii, 1], 'o', c='r', markersize = 8)
plt.plot(x_train[:, 0], x_train[:, 1], linestyle = '--', lw = 2, c='r')
#----- 標示右半周期
plt.arrow(5, -0.5, 4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.arrow(5, -0.5, -4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.plot([10, 10], [-2, 5], '--', lw = 1)
plt.text(5, -1., r'$ L$')
#----- 繪製左半周期函數
x_trainE = np.zeros((5,2))
for ii in range(0, 5):
        x_trainE[ii, 0] = x_train[ii, 0] -10.
        x_trainE[ii, 1] = x_train[ii, 1]
for ii in range(0,5):
        plt.plot(x_trainE[ii, 0], x_trainE[ii, 1], 'o', c='r', markersize = 8)
plt.plot(x_trainE[:, 0], x_trainE[:, 1], linestyle = '--', lw = 2, c='r')
#----- 繪製半周期區間標示
plt.plot([0, 0], [0, -1], '-', lw = 1)
plt.arrow(-5, -0.5, 4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.arrow(-5, -0.5, -4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.text(-5, -1, r'$ L$')
#----- 繪製右半周期區間標示
plt.plot([10, 10], [-2, 5], '--', lw = 1)
plt.arrow(5, -1.5, 4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.arrow(5, -1.5, -4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.text(5, -2., r'$ T = L$')
#----- 繪製左半周期區間標示
plt.plot([-10, -10], [-2, 5], '--', lw = 1)
plt.arrow(-5, -1.5, 4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.arrow(-5, -1.5, -4.5, 0,  lw =1, head_width=0.25, head_length=0.5)
plt.text(-5, -2., r'$ T = L$')
plt.text(-0.5, -6, '(a) FS', fontsize=10)
#
plt.axis('off')
#
plt.savefig('CH_12_15_2_EX_1_Pyplot_Drawings_Functions.png')
plt.show()


















































































	


