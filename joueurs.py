# Définition de la structure du dictionnaire joueur
joueur = {
    "nomComplet": "",
    "age": 0,
    "adresse": ""
}

# Fonction pour entrer les détails d'un joueur
def saisir_joueur():
    nom = input("Nom complet du joueur : ")
    age = int(input("Âge du joueur : "))
    adresse = input("Adresse du joueur : ")
    
    return {"nomComplet": nom, "age": age, "adresse": adresse}

# Saisie des joueurs
nombre_joueurs = 3
joueurs = []

for i in range(nombre_joueurs):
    print(f"Joueur {i + 1}:")
    joueur_info = saisir_joueur()
    joueurs.append(joueur_info)

# Affichage des joueurs par catégorie d'âge
print("\nJoueurs juniors (<18 ans):")
for joueur_info in joueurs:
    if joueur_info["age"] < 18:
        print(f"Nom: {joueur_info['nomComplet']}, Age: {joueur_info['age']}, Adresse: {joueur_info['adresse']}")

print("\nJoueurs seniors (>=18 ans):")
for joueur_info in joueurs:
    if joueur_info["age"] >= 18:
        print(f"Nom: {joueur_info['nomComplet']}, Age: {joueur_info['age']}, Adresse: {joueur_info['adresse']}")
