#-------------------------------------------------
#   CH_12_4_EX_1_Pyplot_Subplot_Common_Usages.py
#-------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#----- (1) 水平圖形陣列 (1x2)
rho_s = 2.3
gamma_w = 9810.
gamma_s = rho_s * gamma_w
kh = 0.1
z = np.linspace(0., -3., 101)
sigma_zz = gamma_s * z
sigma_xx = kh * sigma_zz
#
fig0 = plt.figure()
plt.subplot(121)
plt.plot(sigma_zz, z, 'r-', lw = 2)
plt.xlabel(r'$\sigma_{zz}, (Pa)$')
plt.ylabel(r'$z, (m)')
plt.grid(True)
#
plt.subplot(122)
plt.plot(sigma_xx, z, 'r--', lw = 2)
plt.xlabel(r'$\sigma_{xx}, (Pa)$')
plt.grid(True)
#
plt.savefig('CH_12_4_EX_1(a)_Pyplot_Subplot_Common_Usages.png')
plt.show()
#----- (2) 垂直圖形陣列 (3x1)
t = np.linspace(0., 10., 101)
d = 0.1*np.sin(t)
v = -0.1*np.cos(t)
a = -0.1*np.sin(t)
#
fig1 = plt.figure()
plt.subplot(311)
plt.plot(t, d, 'g-', lw = 2)
plt.xlabel('t')
plt.ylabel(r'$d(t), (m)$')
plt.grid(True)
#
plt.subplot(312)
plt.plot(t, v, 'g--', lw = 2)
plt.xlabel('t')
plt.ylabel(r'$v(t), (m/s)$')
plt.grid(True)
#
plt.subplot(313)
plt.plot(t, a, 'g-.', lw = 2)
plt.xlabel('t')
plt.ylabel(r'$a(t), (m/s^2)$')
plt.grid(True)
#
plt.savefig('CH_12_4_EX_1(b)_Pyplot_Subplot_Common_Usages.png')
plt.show()
#----- (3) 矩形圖形陣列 (2x2)
x = np.linspace(-5., 5., 101)
y1 = np.tanh(x)
y2 = 1./(1.+np.exp(-x))
y3 = x
y4 = np.maximum(0, x)
#
fig2 = plt.figure()
plt.subplot(2,2,1)
plt.plot(x, y1, 'b-', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.text(-4, .5, r'$tansig$')
plt.grid(True)
#
plt.subplot(2,2,2)
plt.plot(x, y2, 'b-', lw = 2)
plt.xlabel('x')
plt.text(-4, .75, r'$logsig$')
plt.grid(True)
#
plt.subplot(2,2,3)
plt.plot(x, y3, 'b-', lw = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.text(-4, 2.5, r'$linear$')
plt.grid(True)
#
plt.subplot(2,2,4)
plt.plot(x, y4, 'b-', lw = 2)
plt.xlabel('x')
plt.text(-4, 4, r'$ReLU$')
plt.grid(True)
#
plt.savefig('CH_12_4_EX_1(c)_Pyplot_Subplot_Common_Usages_rectangular_array.png')
plt.show()



























































	


