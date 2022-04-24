"""
1018번 체스판 다시 칠하기

1.  시간 제한이 2초이고 N, M의 크기가 50이하이므로, 완전탐색을 사용해서 문제를 해결해도 시간 안에
    해결 가능할 것이라고 간주
    
2.  N*M 판자에서 8*8 체스판을 떼어내는 문제이기 때문에 완전 탐색을 위해 전체 보드에서는
    (N-8+1)*(M-8+1)만큼만 탐색해 보면 될 것이다.
    
3.  부분 체스판을 선택했다면, 해당 위치에서 8*8 범위의 체스판에 대해 WBWBWBWB패턴으로 시작하는 체스판과
    BWBWBWBW패턴으로 시작하는 체스판 중 어느 것에 대조하여 더 작은 차이를 나타내는 지만 구하면 끝
"""


def check(row, col, board):
    global N, M
    countBlack = 0
    countWhite = 0

    tile = "B"

    for i in range(8):
        for j in range(8):
            if board[row + i][col + j] != tile:
                countBlack += 1
            if j != 7:
                if tile == "W":
                    tile = "B"
                else:
                    tile = "W"

    tile = "W"

    for i in range(8):
        for j in range(8):
            if board[row + i][col + j] != tile:
                countWhite += 1
            if j != 7:
                if tile == "W":
                    tile = "B"
                else:
                    tile = "W"

    return min(countBlack, countWhite)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
minVal = N * M

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        val = check(i, j, board)
        if val < minVal:
            minVal = val

print(minVal)
