# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 3.0
# 19.01.2023

import matplotlib.pyplot as plt
import calcul
from lxml import etree



def pourcentage_parking(nom_parking):
    '''
    Fonction calculant le poucentage d'occupation d'un parking de chaque ligne par rapport a son maximum. Resultat sous forme de liste.
    '''
    L=[]
    test=[]
    f1 = open(nom_parking+'.Free.txt','r') 
    liste = f1.readlines()
    f1.close()
    f1 = open(nom_parking+'.txt')
    tree = etree.parse(nom_parking+'.txt')
    for user in tree.xpath('Total') :
        total = user.text
    for x in range(len(liste)) :
        liste[x]=int(liste[x][:-1])
        L.append(calcul.pourcentage(liste[x],int(total)))
    return L
    

def pourcentage_parkings() :
    '''
    Fonction calculant le poucentage d'occupation des parking par rapport à leur maximum. Resultat sous forme de liste.
    '''
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
    L=[]
    for parking in parkings :
        L.append(calcul.moyenne(pourcentage_parking(parking)))
    return L

def places_libres_totales():
    '''
    Fonction retournant le nombre de places libres totales.
    ''' 
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
    total = 0
    for parking in parkings :
        tree = etree.parse(parking+'.txt')
        for user in tree.xpath('Free') :
            total += int(user.text)
    return total

def places_occupees_totales(x):
    '''
    Fonction retournant le nombre de places occupées totale a la ligne x des fichiers.
    ''' 
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
    total = 0
    for parking in parkings :
        f1 = open(parking+'.Free.txt','r') 
        liste = f1.readlines()
        f1.close()
        f1 = open(parking+'.Free.txt','r') 
        Free=int(liste[x][:-1])
        tree = etree.parse(parking+'.txt')
        for user in tree.xpath('Total') :
            Total = int(user.text)
        total += Total-Free
    return total

def places_totales():
    '''
    Fonction retournant le nombre de places totales.
    ''' 
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
    total = 0
    for parking in parkings :
        tree = etree.parse(parking+'.txt')
        for user in tree.xpath('Total') :
            total += int(user.text)
    return total

def places_occupees_totales_24h():
    '''
    Fonction mettant dans une liste le nombre de place occupée par ligne. 
    '''
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY']
    Total=[]
    for x in range(24):
        Total.append(places_occupees_totales(x))
    return Total


def graph_moyenne_occupation_24h(val,maxi,moye,nom) :
    '''
    Fonction créeant un graph rescencant le nombre de places occupées des parking de montpellier sur 24h. Il y a aussi le seuil de places totales et la moyenne d'ocupation sur la journée.
    '''
    ref = []
    maxi_liste = []
    moye_liste = []
    for i in range(24) :
        ref.append(i)
        maxi_liste.append(maxi)
        moye_liste.append(moye)

    plt.clf()
    plt.bar(ref,val, label='Places Occupées')
    plt.plot(ref,maxi_liste,color='red', label='Places Totales')
    plt.plot(ref,moye_liste,color='green', label='Occupation moyenne')
    plt.legend()
    plt.xlabel('Temps (en heure)')
    plt.ylabel('Places')
    plt.xlim(0,23)
    plt.ylim(0,maxi+100)
    plt.title('Places occupées par heures sur une journée.')
    plt.savefig(nom)


#1 
print(f'1 : {places_occupees_totales(0)}/{places_totales()} Places occupées')

#2
print(f'2 : {round(100-calcul.moyenne(pourcentage_parkings()),2)}% De remplissage moyen')

#3
graph_moyenne_occupation_24h(places_occupees_totales_24h(),places_totales(),calcul.moyenne(places_occupees_totales_24h()),"grph_prctg_myn_cptn.png")

def places_libres(parking):
    '''
    Fonction retournant le nombre de places libres d'un parking.
    ''' 
    total = 0
    for parking in parkings :
        tree = etree.parse(parking+'.txt')
        for user in tree.xpath('Free') :
            total += int(user.text)
    return total

def places_occupees(x,parking):
    '''
    Fonction retournant le nombre de places occupées d'un parking a la ligne x des fichiers.
    ''' 
    f1 = open(parking+'.Free.txt','r') 
    liste = f1.readlines()
    f1.close()
    f1 = open(parking+'.Free.txt','r') 
    Free=int(liste[x][:-1])
    tree = etree.parse(parking+'.txt')
    for user in tree.xpath('Total') :
        Total = int(user.text)
    return Total-Free

def places(parking):
    '''
    Fonction retournant le nombre de places d'un parking.
    ''' 
    tree = etree.parse(parking+'.txt')
    for user in tree.xpath('Total') :
        return int(user.text)

def places_occupees_24h(parking):
    '''
    Fonction mettant dans une liste le nombre de place occupée par ligned'un parking. 
    '''
    Total=[]
    for x in range(24):
        Total.append(places_occupees(x,parking))
    return Total


#4
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY'] 
print(f'4 :')
for parking in parkings :
    print(f'{parking} : {places_occupees(0,parking)}/{places(parking)} Places occupées.\n{calcul.moyenne(pourcentage_parking(parking))}% Libre.')
    graph_moyenne_occupation_24h(places_occupees_24h(parking),places(parking),calcul.moyenne(places_occupees_24h(parking)),"grph_cptn"+parking+".png")