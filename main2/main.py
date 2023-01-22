from module_sae15 import *
import csv

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
donnees=['DateTime','Status','Free']

def numero_parking(parking) :
    for numero in range(0,len(parkings)) :
        if parkings[numero] == parking :
            return int(numero)

def numero_donnee(donnee) :
    for numero in range(0,len(donnees)) :
        if donnees[numero] == donnee :
            return int(numero)

def pourcentage_occupation(parking):
    '''
    Fonction calculant le poucentage d'occupation d'un parking en fonction du temps. Elle renvoie une liste de pourcentage.
    '''
    total = unxml('Total','FR_MTP_COME')
    f1=open('donnees.csv','r')
    tableau = csv.reader(f1)
    print (tableau[1])

    """print(f'Parking n°{numero_parking(parking)}')
    print(f'Donnée n°{numero_donnee("Free")}')
    print (tableau[numero_parking(parking)][numero_donnee('Free')])"""


pourcentage_occupation('FR_MTP_COME')




"""
    L=[]
    f1=open(nom_fichier,'r')
    f2=open(nom_fichier,'r')
    f3=open(nom_fichier,'r')
    for i in range(1,len(f2.readlines())):
        if len(f3.readlines(i))==1:
            print(len(f3.readlines(i)))
            print(str(f1.readlines(i))[2:-4])
            S1=int(str(f1.readlines(i))[2:-4])
            print(S1)
            L.append(calcul.pourcentage(S1,total))
            print (L)
        elif len(f3.readlines(i))==0 :
            break
    f1.close()
    f2.close()
    f3.close()
    return L
"""