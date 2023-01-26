# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2023 Mattéo Toulliou, Mazzouj Kenzo
# Version 1.0
# 19.01.2023

import time
import requests
import os
import json

parkings=["Rue Jules Ferry - Gare Saint-Roch","Comédie","Esplanade","Hôtel de Ville","Corum","Place Albert 1er - St Charles","Foch","Halles Castellane","Observatoire","Rondelet","Plan Cabanes","Boutonnet","Emile Combes","Beaux-Arts","Les Aubes","Antigone centre","Médiathèque Emile Zola","Nombre d'Or","Louis Blanc","Gambetta","Port Marianne","Clemenceau","Les Arceaux","Cité Mion","Nouveau Saint-Roch","Renouvier","Odysseum","Saint-Denis","Richter","Charles Flahault","Voltaire","Prés d'Arènes","Garcia Lorca","Vert Bois","Malbosc","Occitanie","FacdesSciences","Fac de Lettres","Aiguelongue","Jeu de Mail des Abbés","Euromédecine","Marie Caizergues","Sabines","Celleneuve","Jardin de la Lironde","Père Soulas","Place Viala","Hôtel du Département","Tonnelles","Parvis Jules Ferry - Gare Saint-Roch","Pont de Lattes - Gare Saint-Roch","Deux Ponts - Gare Saint-Roch","Providence - Ovalie","Pérols Etang de l'Or","Albert 1er - Cathédrale","Saint-Guilhem - Courreau","Sud De France"]
donnees=["num_bikes_available","num_bikes_disabled","num_docks_available","is_installed","is_renting","is_returning"]

def fichier_parking() :
    '''
    Fonction permettant de recuperer les données json des parkings a vélo et les inscrit dans un fichier json.
    '''
    response=requests.get('https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json')
    f1=open("station_status.json","w",encoding='utf8')
    f1.write(response.text)
    f1.close()



'''
Programme de récolte d'information des parking vélo de la ville de montpellier.
'''

for parking in parkings :
    for donnee in donnees :
        nom_fichier=parking+'.'+donnee+'.txt'
        f1=open(nom_fichier,"w",encoding='utf8')
        f1.close()

l=0
while True :
    for parking in parkings :
        fichier_parking()
        fileObject = open("station_status.json","r")
        jsonContent = fileObject.read()
        a = json.loads(jsonContent)
        x=0
        for donnee in donnees :
            nom_fichier=parking+'.'+donnee+'.txt'
            f1=open(nom_fichier,'r')
            f1.close()
            if os.path.getsize(nom_fichier) == 0:
                f1=open(nom_fichier,"w",encoding='utf8')
                f1.write(str(a['data']['stations'][x][donnee])+'\n')
                f1.close()
            else : 
                f1=open(nom_fichier,'r')
                L=f1.readlines()
                f1.close()
                L.insert(l,str(a['data']['stations'][x][donnee])+'\n')
                f1=open(nom_fichier,'w',encoding='utf8')
                f1.writelines(L)
                f1.close()
        x+=1
    l+=1
    print('tour : ',l)
    time.sleep(1)
 

print(f'TERMINE')