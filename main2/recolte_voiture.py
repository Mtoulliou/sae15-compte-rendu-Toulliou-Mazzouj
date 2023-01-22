# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 2.1
# 22.01.2023

from module_sae15 import *
import csv

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
donnees=['DateTime','Status','Free']

'''
Programme permettant de recuperer les données en temps réel des parkings et de les stocker dans un tableau de tableau. (donnees.csv)
'''
tableau = creation_tableau(parkings,donnees)
while True :
    for parking in range(0,len(parkings)) :
        fichier_parking(parkings[parking])
        for donnee in range(0,len(donnees)) :
            tableau[parking][donnee].append(str(unxml(donnees[donnee],parkings[parking])))
            print (tableau)
    print(f'time sleep')
    f1 = open('donnees.csv','w')
    obj = csv.writer(f1)
    for x in tableau:
        for y in x :
            obj.writerow(y)
    f1.close()
    time.sleep(1)

# FF / Même apres etre repartit de 0 avec une autre approche, impossible de recuperer les données et de les traiter.