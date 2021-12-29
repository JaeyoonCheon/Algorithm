N = 11


def makeBoard():
    board = []

    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(0)
        board.append(row)
    return board


def makeBoard1d():
    board = []
    for _ in range(N):
        board.append(-1)
    return board


def checkQueens(board, N, col, pos):
    for i in range(col):
        if board[i] == pos:
            return False
        if abs(col - i) == abs(board[i] - pos):
            return False
    return True


def putQueens(board, currCol, N):
    if currCol == N:
        return True
    else:
        for i in range(N):
            board[currCol] = i
            if checkQueens(board, N, currCol, i):
                if putQueens(board, currCol + 1, N):
                    return True
    return False


def putQueensCase(board, currCol, N):
    global queenCaseCount
    if currCol == N:
        queenCaseCount = queenCaseCount + 1
        return True
    else:
        for i in range(N):
            board[currCol] = i
            if checkQueens(board, N, currCol, i):
                putQueensCase(board, currCol + 1, N)


global queenCaseCount
queenCaseCount = 0

board = makeBoard1d()
print(putQueens(board, 0, N))

putQueensCase(board, 0, N)
print(queenCaseCount)
