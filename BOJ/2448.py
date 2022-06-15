"""
2448번 별 찍기 11
"""

import sys

sys.setrecursionlimit(1000000)

N = int(input())

paper = [[" "] * (2 * N - 1) for _ in range(N)]

step = 0
for i in range(N):
    for j in range(N - 1 - step, N + step):
        paper[i][j] = " "
    step += 1


def makeStar(top, bottom, left, right):
    halfV = (bottom - top) // 2
    halfH = (right - left) // 2

    paper[top][(right + left) // 2] = "*"
    paper[top + halfV][left + 1] = "*"
    paper[top + halfV][right - 1] = "*"
    paper[bottom][left] = "*"
    paper[bottom][left + 1] = "*"
    paper[bottom][(right + left) // 2] = "*"
    paper[bottom][right - 1] = "*"
    paper[bottom][right] = "*"


def star(top, bottom, left, right):
    halfV = (bottom - top) // 2
    halfH = (right - left) // 2

    if halfV == 2:
        makeStar(top, bottom, left, right)
        return

    star(top, top + halfV, left + halfH // 2, right - halfH // 2)
    star(top + halfV, bottom, left, halfH)
    star(top + halfV, bottom, halfH, right)


star(0, N - 1, 0, 2 * N - 1 - 1)

for line in paper:
    print(line)
