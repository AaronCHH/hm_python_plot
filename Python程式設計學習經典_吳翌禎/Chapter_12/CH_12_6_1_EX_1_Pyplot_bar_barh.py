#--------------------------------------
#   CH_12_6_1_EX_1_Pyplot_bar_barh.py
#--------------------------------------
import matplotlib.pyplot as plt
#
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
seasons_index = range(len(seasons))
saleamounts = [1000, 2000, 1650, 2500]
#
fig0 = plt.figure(0)
#----- 繪製垂直長條圖 (bar)
plt.subplot(2,1,1)
plt.bar(seasons_index, saleamounts, align ='center', color='darkblue')
plt.xticks(seasons_index, seasons, rotation = 0, fontsize = 'small')
plt.xlabel('Seasons')
plt.ylabel('Sale Amounts')
plt.title('Sale Amount in Seasons')
#----- 繪製水平長條圖 (barh)
plt.subplot(2,1,2)
plt.barh(seasons_index,saleamounts,height = 0.5, align ='edge',\
         color=['orange','lightgreen','lightblue','grey'],\
         edgecolor = ['black','black','black','black'], lw = 2)
plt.yticks(seasons_index, seasons, rotation = 60, fontsize = 'small')
plt.ylabel('Seasons')
plt.xlabel('Sale Amounts')
plt.grid()
#
plt.savefig('CH_12_6_1_EX_1_Pyplot_bar_barh.png')
plt.show()































































	


