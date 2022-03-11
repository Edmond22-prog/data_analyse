import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv("39-Versanddaten.csv", sep=";")

## 1 - Affichage des titres des colonnes, des 15 premières lignes et du nombres 
## d'enregistrements.
print(df.head(15))
print(f"\nLe nombre total d'enregistrement est de {len(df)}.")


## 2 - Analyse univariée de chaque caractéristique métrique et affichage des résultats
## sous forme de tableau avec enregistrement dans un fichier.
data = df.describe().round(2).iloc[1:3,1:]
print(data)
with open("Résultats d'évaluation.txt", "w") as file:
    file.write(str(data))


## 3 - La partie des diagrammes sont dans le fichier Diagrammes.ipynb


## 4 - Analyse de corrélation selon la méthode de Pearson
cout_produit = df["Produktkosten"]
poids = df["Gewicht"]

corr, _ = pearsonr(cout_produit, poids)
print("Le coefficient de corrélation entre le <cout du produit> et le <poids> vaut {:.3f}".format(corr))
if corr > -0.5 and corr < 0.5:
    print("Il s'agit d'une corrélation Faible.")
elif corr > -0.75 and corr < 0.75:
    print("Il s'agit d'une corrélation Moyenne.")
elif corr > -0.87 and corr < 0.87:
    print("Il s'agit d'une corrélation Forte.")
elif corr > -1 and corr < 1:
    print("Il s'agit d'une corrélation Très Forte.")
elif corr == 1 or corr == -1:
    print("Il s'agit d'une corrélation Parfaite.")
else:
    print("Il s'agit d'une corrélation Nulle.")


## 5 - Cette partie se trouve dans le fichier Diagrammes.ipynb


