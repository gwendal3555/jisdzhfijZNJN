import pandas as pd

# Charger le fichier CSV avec Pandas
DL = pd.read_csv(r"C:\Users\33782\Desktop\M2 MSI\S2\Certification\Python\NYC_Dog_Licensing_Dataset.csv", sep=";")

# Créer un tableau croisé de deux colonnes
tableau_croise = pd.crosstab(DL["ZipCode"], DL["BreedName"])

# Ajouter le comptage de la valeur "Shih Tzu" à la colonne BreedName
tableau_croise["Shih Tzu"] = DL[DL["BreedName"] == "Shih Tzu"].groupby("ZipCode")["BreedName"].count()

# Ajouter le comptage de la valeur "Shih Tzu" à la colonne BreedName
tableau_croise["Yorkshire Terrier"] = DL[DL["BreedName"] == "Yorkshire Terrier"].groupby("ZipCode")["BreedName"].count()


# Ajouter le comptage de la valeur "Chihuahua" à la colonne BreedName
tableau_croise["Chihuahua"] = DL[DL["BreedName"] == "Chihuahua"].groupby("ZipCode")["BreedName"].count()

# Ajouter le comptage de la valeur "Maltese" à la colonne BreedName
tableau_croise["Maltese"] = DL[DL["BreedName"] == "Maltese"].groupby("ZipCode")["BreedName"].count()

# Ajouter le comptage de la valeur "Labrador Retriever" à la colonne BreedName
tableau_croise["Labrador Retriever"] = DL[DL["BreedName"] == "Labrador Retriever"].groupby("ZipCode")["BreedName"].count()

# Définir les pondérations pour chaque race de chien
poids = {"Yorkshire Terrier": 0.18, "Shih Tzu": 0.17, "Chihuahua": 0.14, "Maltese": 0.11, "Labrador Retriever": 0.09}

# Calculer le total pondéré pour chaque zone ZIP
def calcul_total(row):
    total = sum([row[breed] * poids[breed] for breed in poids])
    return total

tableau_croise["Total pondéré"] = tableau_croise.apply(calcul_total, axis=1)

# Trier le tableau croisé par ordre décroissant sur la colonne "Total pondéré"
tableau_croise = tableau_croise.sort_values(by="Total pondéré", ascending=False)

# Afficher le résultat de la colonne "Total pondéré" pour les 10 zones ZIP les plus occupées par ces chiens
resultats = tableau_croise["Total pondéré"].head(10)
print(resultats)
