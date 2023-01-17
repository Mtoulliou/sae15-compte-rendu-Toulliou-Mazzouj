from lxml import etree
import time
import requests
import matplotlib.pyplot as plt
import os

import calcul
"""
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
"""

#######################################################################################

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
donnees=['DateTime','Name','Status','Free','Total']

def donnee_parking(parking) :
    '''
    Fonction permettant de recuperer les données xml d'un parking renseigné.
    '''
    url_param= "https://data.montpellier3m.fr/sites/default/files/ressources/"+parking+".xml"
    response=requests.get(url_param)
    return response.text

def fichier_parking(parking) :
    '''
    Fonction permettant de créer un fichier contenant les données xml du parking mentionné
    '''
    nom_fichier=parking+".txt"
    f1=open(nom_fichier,"w",encoding='utf8')
    f1.write(donnee_parking(parking))
    f1.close()

def unxml(donnee,fichier_parking) :
    tree = etree.parse(fichier_parking)
    for user in tree.xpath(donnee) :
        return user.text
#######################################################
x=0
for parking in parkings :
    for donnee in donnees :
        name=parking+"."+donnee+'.txt'
        f1="f"+parking+donnee
        f1=open(name,'w',encoding='utf8')

while x!=2 : 
    for parking in parkings :
        fichier_parking(parking)
        for donnee in donnees :
            f1.write(unxml(donnee,parking+'.txt'))
    time.sleep(3)
    x+=1
    
for parking in parkings :
    for donnee in donnees :
        f1="f"+parking+donnee
        f1.close()
