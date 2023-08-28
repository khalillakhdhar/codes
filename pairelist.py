def main():
    n = int(input("Entrez le nombre d'entiers à saisir : ")) # définir la taille de la liste
    
    entiers = [] #initialisation de la liste
    for i in range(n): #lecture de la liste
        entier = int(input(f"Entrez l'entier #{i+1} : "))
        entiers.append(entier)
    
    entiers_pairs = [x for x in entiers if x % 2 == 0] # la liste paires dans entiers
    
    print("Les entiers pairs sont :", entiers_pairs)

if __name__ == "__main__":
    main()
