#----------------------------------------------
#   CH_12_16_1_EX_1_Pyplot_Styles_LinePlot.py
#----------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#----- 定義不同圖表樣式
x = np.linspace(0., 2.*np.pi, 361)
ys = np.sin(x)
yc = np.cos(x)
styles = ['classic', 'bmh', 'ggplot', 'fast', 'fivethirtyeight', 'grayscale',\
          'dark_background', 'seaborn']
#----- 依定義依序繪製不同樣式之圖表
fig1 = plt.figure(figsize=(12, 6))
for ii in range(0, 8):   
    with plt.style.context(styles[ii]):
        plt.subplot(4, 2, ii+1)
        plt.plot(x, ys, 'r-', lw = 2, label = 'sin(x)')
        plt.plot(x, yc, 'g--', lw = 2, label = 'cos(x)')
        plt.text(3., 0.8, str(styles[ii]))
#
plt.suptitle('Using plt.style.context')
plt.savefig('CH_12_16_1_EX_1_Pyplot_Styles_LinePlot.png')
plt.show()



















































































	


