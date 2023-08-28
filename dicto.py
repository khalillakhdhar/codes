p1={"nom":"Lakhdhar", "prenom":"Khalil", "age":33,"profession":"enseignant"}
p2={"nom":"Lakhdhar", "prenom":"Adel", "age":40,"profession":"médecin"}
#p1["tel"]="20999333"
print(p1)
personnes=[]
personnes.append(p1)
personnes.append(p2)
for p in personnes:
    print(p["profession"])
# définir un dictionnaire joueur et lisez un liste des joueur avec ( nomComplet, age , adresse) au clavier
# créer et remplissez un tableau de joueur puis
# afficher les joueur en indiquant selon leurs age >18 sénior <18 juniors