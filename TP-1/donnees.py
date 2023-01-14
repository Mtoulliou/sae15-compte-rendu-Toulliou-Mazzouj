import requests
from lxml import etree
import calcul
import time

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
    nom_fichier= parking+".txt"
    f1=open(nom_fichier,"w",encoding='utf8')
    f1.write(donnee_parking(parking))
    f1.close()


def ouvert(parking) :
    '''
    Fonction permettant de retourner True si le parking est ouvert et False si ce n'est pas le cas.
    '''
    nom_fichier=parking+".txt"
    tree = etree.parse(nom_fichier)
    for user in tree.xpath("Status") :
        if user.text == "Open" :
            return True
        else :
            return False

def places_libre(parking) :
    '''
    Fonction retournant le nombre de places libre d'un parking
    '''
    nom_fichier=parking+".txt"
    tree = etree.parse(nom_fichier)
    for user in tree.xpath("Free") :
        return user.text

def places_total(parking) :
    '''
    Fonction retournant le nombre de places total d'un parking
    '''
    nom_fichier=parking+".txt"
    tree = etree.parse(nom_fichier)
    for user in tree.xpath("Total") :
        return user.text
