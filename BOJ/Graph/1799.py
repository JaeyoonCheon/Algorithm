"""
1799번 비숍

1.  단순 장애물이 있는 N-Queen 백트래킹 문제라고 생각했으나, 그 방식으로 풀었을 때 생각보다 시간 제한을 넘지못해
    곤란했던 문제.
    
2.  두번째 접근으로 1차원 배열을 만들어 인덱스에 접근하는 시간을 더 빠르게 줄이려고 했으나, 행을 넘어갈 때 그 색의 구분을 계산하기가 생각보다
    까다로워 다시 생각해 보기로 했다.
    
3.  많은 사람들이 접근한 방식은 놓는 말의 종류가 비숍(대각선으로만 움직임)밖에 없으므로, 체스판의 흰색과 검은색 칸들은 서로 완전히 독립적인
    경우의 수를 가진다는 것이다. 따라서 체스판의 절반의 칸만큼만 탐색할 수 있으므로 시간 복잡도가 줄어들게 되어 해결할 수 있었다.
"""

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

maxBishop = [0, 0]

upper = [False] * (2 * N)
lower = [False] * (2 * N)


def checkOthers(x, y):
    if upper[x + y + 1] or lower[N - x + y]:
        return False

    return True


def putBishop(x, y, count, color):
    global maxBishop

    step = y % 2

    if y >= N:
        x += 1
        if step == 0:
            y = 1
        else:
            y = 0

    if x >= N:
        if count > maxBishop[color]:
            maxBishop[color] = count
        return

    if board[x][y] and checkOthers(x, y):
        upper[x + y + 1] = True
        lower[N - x + y] = True
        putBishop(x, y + 2, count + 1, color)
        upper[x + y + 1] = False
        lower[N - x + y] = False

    putBishop(x, y + 2, count, color)


putBishop(0, 0, 0, 0)
putBishop(0, 1, 0, 1)

print(sum(maxBishop))
