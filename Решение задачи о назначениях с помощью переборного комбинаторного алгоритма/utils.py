def print_matrix(matrix):
    """
    Красиво выводит матрицу.
    """
    for row in matrix:
        print(" ".join(map(str, row)))
