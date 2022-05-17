"""
16935번 배열 돌리기 3
"""

import sys

N, M, R = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

operation = list(map(int, sys.stdin.readline().split()))


def action(board, types, N, M):
    height = N
    width = M
    result = []
    for type in types:
        result = []
        if type == 1:
            for i in board:
                result.insert(0, i)

        if type == 2:
            for i in board:
                temp = i
                temp.reverse()
                result.append(temp)

        if type == 3:
            for i in range(width):
                temp = []
                for j in range(height):
                    temp.append(board[j][i])
                temp.reverse()
                result.append(temp)

        if type == 4:
            for i in range(width):
                temp = []
                for j in range(height):
                    temp.append(board[j][i])
                result.insert(0, (temp))

        if type == 5:
            quad1 = [board[i][width // 2 : width] for i in range(0, height // 2)]
            quad2 = [board[i][width // 2 : width] for i in range(height // 2, height)]
            quad3 = [board[i][0 : width // 2] for i in range(height // 2, height)]
            quad4 = [board[i][0 : width // 2] for i in range(0, height // 2)]

            for i in range(height // 2):
                temp = []
                temp = quad3[i] + quad4[i]
                result.append(temp)

            for i in range(height // 2):
                temp = []
                temp = quad2[i] + quad1[i]
                result.append(temp)

        if type == 6:
            quad1 = [board[i][width // 2 : width] for i in range(0, height // 2)]
            quad2 = [board[i][width // 2 : width] for i in range(height // 2, height)]
            quad3 = [board[i][0 : width // 2] for i in range(height // 2, height)]
            quad4 = [board[i][0 : width // 2] for i in range(0, height // 2)]

            for i in range(height // 2):
                temp = quad1[i] + quad2[i]
                result.append(temp)

            for i in range(height // 2):
                temp = []
                temp = quad4[i] + quad3[i]
                result.append(temp)

        board = result.copy()
        height = len(result)
        width = len(result[0])

    return result


modifiedBoard = action(board, operation, N, M)

for i in range(len(modifiedBoard)):
    for j in range(len(modifiedBoard[0])):
        print(modifiedBoard[i][j], end=" ")
    print()
