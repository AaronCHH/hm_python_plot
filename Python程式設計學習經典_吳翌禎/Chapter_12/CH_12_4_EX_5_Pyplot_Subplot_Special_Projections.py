#-------------------------------------------------------
#   CH_12_4_EX_5_Pyplot_Subplot_Special_Projections.py
#-------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#
fig0 = plt.figure()
#----- aitoff 投影法
plt.subplot(221, projection="aitoff")
plt.title("Aitoff")
plt.grid(True)
#----- hammer 投影法
plt.subplot(222, projection="hammer")
plt.title("Hammer")
plt.grid(True)
#----- lambert 投影法
plt.subplot(223, projection="lambert")
plt.title("Lambert")
plt.grid(True)
#----- mollweide 投影法
plt.subplot(224, projection="mollweide")
plt.title("Mollweide")
plt.grid(True)
#
plt.savefig('CH_12_4_EX_5_Pyplot_Subplot_Special_Projections.png')
plt.show()






























































	


