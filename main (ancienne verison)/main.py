# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 1.0
# 19.01.2023

import matplotlib.pyplot as plt
import calcul

def pourcentage_fichier(nom_fichier1,total):
    '''
    Fonction calculant le poucentage d'occupation de chaque ligne de deux fichier. Les pourcentages sont rendus sous forme de liste.
    '''
    L=[]
    f1=open(nom_fichier1,'r')
    f2=open(nom_fichier1,'r')
    f3=open(nom_fichier1,'r')
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

print(pourcentage_fichier('FR_MTP_POLY.Free.txt',1911))

print(calcul.moyenne(pourcentage_fichier('FR_MTP_POLY.Free.txt',1911)))