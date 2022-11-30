#-------------------------------------------------
#   CH_12_13_2_EX_1_Pyplot_Ax_Subplots_Adjust.py   
#-------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#----- fig1 中使用預設之子圖間距
fig1 = plt.figure(1)
#
for ii in range(1, 7):
    plt.subplot(2, 3, ii)
    plt.text(0.5, 0.5, str((2, 3, ii)), fontsize = 15, ha = 'center')
plt.suptitle('Subplots with tight spacings')
#----- fig2 中使用調整之子圖間距(hspace = 0.4, wspace = 0.4)
fig2 = plt.figure(2)
fig2.subplots_adjust(hspace = 0.4, wspace = 0.4)
for ii in range(1, 7):
    ax2 = fig2.add_subplot(2, 3, ii)
    ax2.text(0.5, 0.5, str((2, 3, ii)), fontsize = 15, ha = 'center')
    plt.suptitle('Subplots with loose spacings')
#
plt.savefig('CH_12_13_2_EX_1_Pyplot_Ax_Subplots_Adjust.png')
plt.show()















































































	


