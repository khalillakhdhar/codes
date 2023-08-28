reponse = input("Entrez un nombre de lignes (entier positif): ")
N = int(reponse)

def draw_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

draw_pyramid(N)
