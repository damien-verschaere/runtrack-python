def print_board(board):
    for row in board:
        print(" ".join(row))


def securise(board, row, col):
    for i in range(col):
        if board[row][i] == "X":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "X":
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == "X":
            return False

    return True


def placer_dames(board, col):
    n = len(board)
    if col >= n:
        return True

    for i in range(n):
        if securise(board, i, col):
            board[i][col] = "X"
            if placer_dames(board, col + 1):
                return True
            board[i][col] = "O"

    return False


def resoudre_n_dames(n):
    plateau = [["O" for _ in range(n)] for _ in range(n)]

    if placer_dames(plateau, 0):
        print_board(plateau)
    else:
        print("Pas de solution possible.")


taille_plateau = int(input("Entrez la taille du plateau (n): "))
resoudre_n_dames(taille_plateau)
