import lxml
import time
import requests
import matplotlib.pyplot as plt

import calcul

T = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
L1 = [3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4] 
L2 = [103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]

print(f'Moyenne L1 : ',calcul.moyenne(L1))
print(f'Ecart Type L1 : ',calcul.ecart_type(L1))
print(f'Moyenne L2 : ',calcul.moyenne(L2))
print(f'Ecart Type L2 : ',calcul.ecart_type(L2))

'''
Graphique L1,L2
'''

calcul.graph(T,L1,L2,"temps(h)","température (°C)")
#plt.show()
