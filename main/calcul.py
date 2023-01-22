# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Module calcul
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 1.0
# 07.01.2023

import matplotlib.pyplot as plt

'''
Module python permettant des calculs de statisiques comme la moyenne, la Variance, l'ecart-type, la covariance, la corelation ainsi que le pourcentage.
'''

def moyenne(liste) :
    '''
    Fonction permettant de calculer la moyenne d'une liste. Le résultat est arrondie à 2 décimales.

    '''
    somme = 0
    for i in liste : 
        somme += i 
    return round(somme/len(liste),2)


def variance(liste) :
    '''
    Fonction permettant de calculet la variance d'une liste. Le résultat est arrondie à 2 décimales.

    '''
    somme = 0
    x = moyenne(liste)
    for i in liste :
        somme +=(i-x)**2
    return round(somme/len(liste),2)


def ecart_type(liste) :
    '''
    Fonction permettant de calculer l'ecart type d'une liste. Le résultat est arrondie à 2 décimales.

    '''
    return round(variance(liste)**0.5,2)


def covariance(liste1,liste2) :
    '''
    Fonction permettant de calculer la covariance de deux listes. Le résultat est arrondie à 2 décimales.

    '''
    somme = 0
    x = moyenne(liste1)
    y = moyenne(liste2)
    for i in range(len(liste1)) :
        somme +=(liste1[i]-x)*(liste2[i]-y)
    return round(somme/len(liste1),2)


def corelation(liste1,liste2) :
    '''
    Fonction permettant de calculer la corelation entre deux listes. Le résultat est arrondie à 2 décimales.
    '''
    return round(covariance(liste1,liste2)/(ecart_type(liste1)*(ecart_type(liste2))),2)


def pourcentage(a,b) :
    '''
    Fonction permettant de calculer le pourcentage du nombre a par rapport à la reference du nombre b. Le résultat est arrondie à deux décimales. 
    '''
    return round(a*100/b,2)


def graph(ref,liste1,liste2,nom1,nom2):
    '''
    Fonction permettant, à l'aide du module pyplot, de réaliser un graphe comparatif de deux listes avec une reference (comme le temps par exemple).
    '''
    plt.plot(ref,liste1)
    plt.plot(ref,liste2)
    plt.xlabel(nom1)
    plt.ylabel(nom2)
    plt.savefig("grph.png")


#Vérification des fonctions.
assert(moyenne([1,2,3,4,5,6]) == 3.5)
assert(variance([1,2,3,4,5,6]) == 2.92)
assert(ecart_type([1,2,3,4,5,6]) == 1.71)
assert(covariance([1,2,3,4,5,6],[7,8,9,10,11,12]) == 2.92)
assert(corelation([1,2,3,4,5,6],[7,8,9,10,11,12]) == 1)
assert(pourcentage(2,4) == 50)

"""
T=[]
L1=[]
L2=[]
f1=open("FR_MTP_ANTI.Free.txt","r")
f2=open("FR_MTP_COME.Free.txt","r")
for x in range(1,68) :
    S1=int(str(f1.readlines(x))[2:-4])
    L1.append(S1)
    S2=int(str(f2.readlines(x))[2:-4])
    L2.append(S2)
f1.close()
f2.close()
print(L1,L2)
graph(T,L1,L2,"Temps","Places occupées")
"""