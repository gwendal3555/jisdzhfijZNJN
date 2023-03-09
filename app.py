import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

# charger le fichier CSV avec Pandas
#Dog_licensing = pd.read_csv(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\Python\NYC_Dog_Licensing_Dataset.csv", sep=";")
#Dog_Bite= pd.read_csv(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\Python\DOHMH_Dog_Bite_Data.csv", sep=";")


# initialiser un dictionnaire pour stocker les occurrences
#occurrences = {}

# boucler sur chaque ligne du fichier
#for index, row in Dog_Bite.iterrows():

    # extraire la valeur que vous voulez compter, par exemple, la huitième colonne
'''    value = row[3]

    # si la valeur est déjà dans le dictionnaire, incrémenter son occurrence
    if value in occurrences:
        occurrences[value] += 1

    # sinon, ajouter la valeur au dictionnaire avec une occurrence de 1
    else:
        occurrences[value] = 1

# trier le dictionnaire par valeurs en ordre décroissant
sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

# afficher les 15 premières occurrences
for item in sorted_occurrences[:15]:
    print(item)
'''

# charger le fichier CSV avec Pandas
DL = pd.read_csv(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\Python\NYC_Dog_Licensing_Dataset.csv", sep=";")

# créer un tableau croisé de deux colonnes
tableau_croise = pd.crosstab(DL["BreedName"], DL["ZipCode"])

# afficher le tableau croisé
print(tableau_croise)