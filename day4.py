def main():
    # Creazione di un dizionario che mappa le coordinate (i, j) ai caratteri nella matrice
    grid = {
        (row_idx, col_idx): char
        for row_idx, line in enumerate(open("day4.txt"))
        for col_idx, char in enumerate(line.strip())
    }

    # Definizione degli spostamenti (delta) per trovare la parola "XMAS"
    directions = {
        (1, 2, 3, 0, 0, 0),  # Righe (da sinistra a destra)
        (-1, -2, -3, 0, 0, 0),  # Righe (da destra a sinistra)
        (0, 0, 0, 1, 2, 3),  # Colonne (dall'alto in basso)
        (0, 0, 0, -1, -2, -3),  # Colonne (dal basso in alto)
        (1, 2, 3, 1, 2, 3),  # Diagonale principale (da sinistra a destra)
        (-1, -2, -3, 1, 2, 3),  # Diagonale principale (da destra a sinistra)
        (1, 2, 3, -1, -2, -3),  # Diagonale secondaria (da sinistra a destra)
        (-1, -2, -3, -1, -2, -3)  # Diagonale secondaria (da destra a sinistra)
    }

    # PARTE 1
    xmas_count = sum(
        grid.get((i + u, j + x)) == "M" and
        grid.get((i + v, j + y)) == "A" and
        grid.get((i + w, j + z)) == "S"
        for (u, v, w, x, y, z) in directions
        for (i, j) in grid
        if grid[(i, j)] == "X"
    )
    print(xmas_count)

    # PARTE 2
    ams_cross_count = sum(
        1
        for (i, j) in grid
        if grid[(i, j)] == "A" and
        {grid.get((i - 1, j - 1)), grid.get((i + 1, j + 1))} ==
        {grid.get((i - 1, j + 1)), grid.get((i + 1, j - 1))} ==
        {"M", "S"}
    )
    print(ams_cross_count)


if __name__ == '__main__':
    main()
