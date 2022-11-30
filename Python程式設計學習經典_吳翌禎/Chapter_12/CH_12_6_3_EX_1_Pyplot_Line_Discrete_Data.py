#-------------------------------------------------
#   CH_12_6_3_EX_1_Pyplot_Line_Discrete_Data.py
#-------------------------------------------------
import matplotlib.pyplot as plt
#
x = [1, 2, 3, 4]
y1 = [1000, 2000, 1650, 2500]
y2 = [1250, 1500, 2050, 1020]
#
fig0 = plt.figure(0)
#----- 繪製折線圖 (線) (line)
plt.subplot(2,1,1)
plt.plot(x, y1, 'r-', label = 'Taipei')
plt.plot(x, y2, 'b--', label = 'Kaohsiung')
plt.legend(loc = 'best')
plt.xlabel('seasons')
plt.ylabel('sale amount')
plt.title('Sale Amount in Seasons')
#----- 繪製折線圖 (線+符號) (line + marker)
plt.subplot(2,1,2)
plt.plot(x, y1, 'rs-', lw = 4, markersize = 10, alpha = 0.3, label = 'Taipei')
plt.plot(x, y2, 'bo--', lw = 3, markersize = 12, mfc = 'yellow',\
         mec = 'darkgreen', mew = 2, label = 'Kaohsiung')
plt.legend(loc = 'best')
plt.grid()
plt.xlabel('seasons')
plt.ylabel('sale amount')
#
plt.savefig('CH_12_6_3_EX_1_Pyplot_Line_Discrete_Data.png')
plt.show()
































































	


