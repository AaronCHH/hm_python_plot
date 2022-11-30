#---------------------------------
#   CH_12_6_2_EX_1_Pyplot_Pie.py
#---------------------------------
import matplotlib.pyplot as plt
#
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
seasons_index = range(len(seasons))
saleamounts = [1000, 2000, 1650, 2500]
#
fig0 = plt.figure(0)
#----- 繪製圓餅圖 (pie)
plt.subplot(1,2,1)
plt.pie(saleamounts, labels = seasons)
plt.title('Sale Amount in Seasons')
#----- 繪製炸開圓餅圖 (pie)
plt.subplot(1,2,2)
plt.pie(saleamounts, explode = [0.2, 0.05, 0.05, 0.05],\
        labels = seasons, colors = ['orange','lightgreen','lightblue','grey'])
#
plt.savefig('CH_12_6_2_EX_1_Pyplot_pie.png')
plt.show()































































	


