#------------------------------------------------
#   CH_12_15_1_EX_1_Pyplot_Drawings_Sketches.py
#------------------------------------------------
from numpy import *
from numpy.linalg import norm, pinv
from matplotlib import pyplot as plt
#
fig1 = plt.figure(figsize=(9, 8.))
#----- (1) 繪製擋土牆背填土區域示意圖
plt.subplot(1,2,1)
plt.axis([-10, 30, -5, 10])
#----- 繪製座標線
#----- X 軸
plt.arrow(0, 0, 22.5, 0,  lw =1, head_width=0.4, head_length=0.8)
plt.text(24, 0, 'x')
#----- Z 軸
plt.arrow(0, 0, 0, 7,  lw =1, head_width=0.4, head_length=0.8)
plt.text(-0.5, 8.5, 'y')
#------ 繪製擋土牆
plt.plot([0, 0], [0, 5], '-', lw = 2)
plt.plot([0, -1], [5, 5], '-',lw = 2)
plt.plot([-1, -3], [5, 0],'-', lw = 2)
plt.plot([-3, 0], [0, 0], '-',lw = 2)
plt.text(-2.5, 1, 'WALL', fontsize=8)
#------ 繪製背填區
plt.plot([0, 0], [5, 0], '-', lw = 2) # AB
plt.plot([0, 20], [0, 0], '-',lw = 2) #BC
plt.plot([20, 20], [0, 5],'-', lw = 2) #CD
plt.plot([20, 0], [5, 5], '-',lw = 2) #DA
plt.text(10, 2.5, 'Backfilled Zone', fontsize=10)
plt.text(10, 1.5, '(Soil, CLSMs)', fontsize=10 )
#
plt.text(-1, 5.5, 'A')
plt.text(-1, -1, 'B')
plt.text(20.1, -1, 'C')
plt.text(20.1, 5.5, 'D')
#----- 標示尺寸
plt.plot([0, 0], [0, -2], '-', lw = 1)
plt.plot([20, 20], [0, -2], '-', lw = 1)
plt.plot([0, 20], [-1, -1], '-', lw = 1)
plt.text(9, -2.5, r'$ L = 20 m$')
plt.plot([20, 22], [5, 5], '-', lw = 1)
plt.plot([20, 22], [0, 0], '-', lw = 1)
plt.plot([21.5, 21.5], [0, 5], '-', lw = 1)
plt.text(22, 2.5, r'$ H = 5 m$')
#----- 繪製集中力 (Q_0 = 72.5 kN)
plt.plot([2.5, 2.5], [9, 6.5], '-', lw = 2)   # Concentrated load '|'
plt.plot([2.1, 2.9],[6.5, 6.5], '-', lw = 2)# Concentrated load '_\'
plt.plot([2.1, 2.5], [6.5, 5.5], '-', lw = 2)# Concentrated load '\'
plt.plot([2.9, 2.5], [6.5, 5.5], '-', lw = 2)# Concentrated load '/'
plt.text(1, 9, r'$Q_0 = 72.5 kN$')# Concentrated load
plt.text(2.8, 5.5, 'a')
#----- 繪製位移應力標示點
circle_Uy1 = plt.Circle([5, 5], 0.5, facecolor='black', lw = 1, linestyle = '-')
circle_Uy2 = plt.Circle([10, 5], 0.5, facecolor='black', lw = 1, linestyle = '-')
#
circle_Sx1 = plt.Circle([0, 5.*3/4], 0.5, facecolor='black', lw = 1, linestyle = '-')
circle_Sx2 = plt.Circle([0, 5.*1/2], 0.5, facecolor='black', lw = 1, linestyle = '-')
#
fig1.gca().add_artist(circle_Uy1)
fig1.gca().add_artist(circle_Uy2)
fig1.gca().add_artist(circle_Sx1)
fig1.gca().add_artist(circle_Sx2)
#
plt.text(5, 5.5, r'$ 1  (U_{y1}) $')
plt.text(10, 5.5, r'$ 2  (U_{y2}) $')
plt.text(0.5,  5.*3/4 -0.5, r'$ 3  (S_{x1}) $')
plt.text(0.5, 5.*1/2 -0.5, r'$ 4  (S_{x2}) $')
#
plt.axis('equal')
plt.axis('off')
#----- (2) 繪製 PLANE42 元素示意圖
plt.subplot(1,2,2)
plt.axis([1, 6, 0, 5])
#----- 繪製平行四邊形元素
x1 = 2.
y1 = 2.
x2 = 5.
y2 = 1.4
x3 = 5.3
y3 = 3.6
x4 = 3.
y4 = 3.5
#
plt.plot([x1, x2], [y1, y2], '-', lw = 2)
plt.plot([x2, x3], [y2, y3], '-',lw = 2)
plt.plot([x3, x4], [y3, y4],'-', lw = 2)
plt.plot([x4, x1], [y4, y1], '-',lw = 2)
#
plt.text(x1-0.1, y1-0.1, 'I', fontsize = 10)
plt.text(x2+0.1, y2-0.1, 'J', fontsize = 10)
plt.text(x3+0.1, y3+0.1, 'K', fontsize = 10)
plt.text(x4-0.1, y4+0.1, 'L', fontsize = 10)
#----- 繪製局部座標
#----- x 軸
plt.arrow(x1, y1, 1, -0.2,  lw =2.5, head_width=0.1, head_length=0.2)
plt.text(x1+1.2, y1, 'x ')
#----- y 軸
plt.arrow(x1, y1, 0.1, 1.,  lw =2.5, head_width=0.1, head_length=0.2)
plt.text(x1, y1+1.25, 'y')
plt.text(2.5, 2.2, 'Element Coordinate System')
#----- 繪製總體座標
#----- X 軸
plt.arrow(1.5, 1.5, 0.3, 0,  lw =1, head_width=0.1, head_length=0.2)
plt.text(2., 1.5, 'X ')
#----- Y 軸
plt.arrow(1.5, 1.5, 0., 0.3,  lw =1, color ='black', head_width=0.1, head_length=0.2)
plt.text(1.5, 2, 'Y')
plt.text(2., 1., 'Global Coordinate System')
#
plt.axis('off')
#
plt.savefig('CH_12_15_1_EX_1_Pyplot_Drawings_Sketches.png')
plt.show()


















































































	


