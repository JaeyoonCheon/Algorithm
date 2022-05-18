"""
2630번 색종이 만들기
"""

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0


def check(x, y, N):
    isSquare = True

    if N == 1:
        if paper[x][y] == 1:
            return 1
        else:
            return 0

    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != 1:
                isSquare = False

    if isSquare:
        return 1
    else:
        return (
            check(x, y, N // 2)
            + check(x, y + N // 2, N // 2)
            + check(x + N // 2, y, N // 2)
            + check(x + N // 2, y + N // 2, N // 2)
        )


print(check(0, 0, N))
