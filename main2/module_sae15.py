# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Module SAE 15
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 1.0
# 22.01.2023

import time
import requests
from lxml import etree

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
donnees=['DateTime','Status','Free']

def creation_tableau(liste1,liste2):
    '''
    Fonction permettat de créer le tableau qui va acceuillir les données récoltées.
    '''
    tableau = []
    for l1 in range(0,len(liste1)) :
        tableau.append([])
        for l2 in range(0,len(liste2)) :
            tableau[l1].append([])
    print(f'Tableau Créée')
    return tableau

def donnee_parking(parking) :
    '''
    Fonction permettant de recuperer les données xml d'un parking renseigné.
    '''
    url_param= "https://data.montpellier3m.fr/sites/default/files/ressources/"+parking+".xml"
    response=requests.get(url_param)
    print(f'Données XML de {parking} recupéré')
    return response.text

def fichier_parking(parking) :
    '''
    Fonction permettant de créer un fichier contenant les données xml du parking mentionné
    '''
    nom_fichier=parking+".txt"
    f1=open(nom_fichier,"w",encoding='utf8')
    f1.write(donnee_parking(parking))
    f1.close()
    print(f'Fichier contenant le XML de {parking} créée')

def unxml(donnee,parking) :
    '''
    Fonction permetant de retourner le contenue de la balise xml du fichier choisis
    '''
    nom_fichier=parking+".txt"
    tree = etree.parse(nom_fichier)
    for user in tree.xpath(donnee) :
        print(f'Données de {donnee}, {parking} récupéré : {user.text}')
        return user.text