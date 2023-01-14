import requests
from lxml import etree
import calcul
import time
from donnees import *

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 


"""
# Programme permettant de creer une liste du nombre de place libre.

f1 =open("places-libres.txt","w",encoding='utf8')
for i in parkings :
    fichier_parking(i)
    if ouvert(i) == True :
        f1.write(i + " | " + places_libre(i) + "\n")
f1.close
"""


"""
# Programme donnant le pourcentage de place libre dans chaque parking ansi que toute la ville

total_libre = 0
total = 0
for i in parkings :
    print (i," | ",calcul.pourcentage(int(places_libre(i)),int(places_total(i))))
    total_libre+=int(places_libre(i))
    total+=int(places_total(i))
print("Total |",calcul.pourcentage(total_libre,total))
"""


"""
# Programmme recuperant des données sur les places de parking de la gare toute les 10 sec pendant 5 min et les inscrivant dans un fichier "places_FR_MTP_GARE.txt"


start=int(time.time())
f1=open("places_FR_MTP_GARE.txt","w",encoding="utf8")
while int(time.time()) < start+300 :
    start2 = round(time.time(),5)
    print("1",int(time.time()))
    while round(time.time(),5) <= start2+10 :
        if round(time.time(),5) == start2+10 :
            f1.write(str(int(time.time()))+" | "+places_libre("FR_MTP_GARE")+" | "+places_total("FR_MTP_GARE")+"\n")
            print("2",int(time.time()))
f1.close()
"""



# Programme permettant d'enregister avec un nom au choix un relevée des places libre, total et le pourcentage d'occupation de tous les parking de montpellier. Il faut aussi choisir la periode d'échantillonage et la durée d'acquisition.

Te=int(input("Perdiode d'échantillonage (seconde) : \n"))
Duree=int(input("Durée d'acquisition (seconde) : \n"))
Nom=input("Nom du fichiers (sans extentions) : \n")+".txt"
start=int(time.time())
f1=open(Nom,"w",encoding="utf8")
while int(time.time()) < start+Duree :
    start2 = round(time.time(),4)
    print("1",int(time.time()))
    while round(time.time(),4) <= start2+Te :
        if round(time.time(),4) == start2+Te :
            print("2",int(time.time()))
            for i in parkings :
                f1.write(str(int(time.time()))+" | "+i+" | "+places_libre(i)+" | "+places_total(i)+" | "+str(calcul.pourcentage(int(places_libre(i)),int(places_total(i))))+"\n")
                print("3",int(time.time()))
            f1.write("=========================================================\n")
f1.close()


print(f'PROGRAMME TERMINE')
