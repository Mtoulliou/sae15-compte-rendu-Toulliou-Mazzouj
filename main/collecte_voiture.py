# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 1.0
# 19.01.2023

import time
import requests
import os
from lxml import etree

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
donnees=['DateTime','Status','Free']

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

def unxml(donnee,parking) :
    '''
    Fonction permetant de retourner le contenue de la balise xml du fichier choisis
    '''
    fichier_parking=parking+'.txt'
    tree = etree.parse(fichier_parking)
    for user in tree.xpath(donnee) :
        return user.text


'''
Programme de récolte d'information des parking de la ville de montpellier.
'''

for parking in parkings :
    for donnee in donnees :
        name=parking+"."+donnee+'.txt'
        f1=open(name,'w',encoding='utf8')
        f1.close()

l=0

while l != 25 : 
    for parking in parkings :
        fichier_parking(parking)
        for donnee in donnees :
            name=parking+"."+donnee+'.txt'
            f1=open(name,'r')
            f1.close()
            if os.path.getsize(name) == 0:
                f1=open(name,'w',encoding='utf8')
                f1.write(unxml(donnee,parking)+"\n")
                f1.close()
            else : 
                f1=open(name,'r')
                L=f1.readlines()
                f1.close()
                L.insert(l,unxml(donnee,parking)+"\n")
                f1=open(name,'w',encoding='utf8')
                f1.writelines(L)
                f1.close()
    l+=1
    print('tour ',l)
    time.sleep(0) 


print (f'TERMINE')