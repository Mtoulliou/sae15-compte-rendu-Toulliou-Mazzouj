import time
import requests
import os

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

def unjson(donnee,fichier_parking) :