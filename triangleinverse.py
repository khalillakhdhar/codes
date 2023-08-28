def draw_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print(i, '*' * i)

num_rows = 10
draw_inverted_triangle(num_rows)
