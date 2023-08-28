def main():
    n = int(input("Entrez le nombre d'entiers à saisir : "))
    
    entiers = []
    for i in range(n):
        entier = int(input(f"Entrez l'entier #{i+1} : "))
        entiers.append(entier)
    
    entiers_pairs = [x for x in entiers if x % 2 == 0]
    
    print("Les entiers pairs sont :", entiers_pairs)

if __name__ == "__main__":
    main()
