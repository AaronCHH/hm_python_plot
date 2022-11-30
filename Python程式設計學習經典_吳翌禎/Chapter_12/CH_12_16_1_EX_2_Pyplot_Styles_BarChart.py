#----------------------------------------------
#   CH_12_16_1_EX_2_Pyplot_Styles_BarChart.py
#----------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#----- 定義不同圖表樣式
styles = ['classic', 'bmh', 'ggplot', 'fast','fivethirtyeight', 'grayscale',\
          'dark_background', 'seaborn']
#----- 依定義依序繪製不同樣式之圖表
fig1 = plt.figure(figsize=(12, 6))
for ii in range(0, 8):   
    with plt.style.context(styles[ii]):
        plt.subplot(4, 2, ii+1)
        plt.hist(np.random.randn(1000))
        plt.xlim(-3, 3)
        plt.text(1., 200, str(styles[ii]))
#
plt.suptitle('Using plt.style.context')
plt.savefig('CH_12_16_1_EX_2_Pyplot_Styles_BarChart.png')
plt.show()




















































































	


