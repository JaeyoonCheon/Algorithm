"""
2448번 별 찍기 11

1.  재귀를 이용한 별 찍기 문제.
    시어핀스키 삼각형을 만드는 문제이다.
    
2.  이 문제는 삼각형의 세 꼭지점을 받아 재귀적으로 다음 별이 찍힐 위치를 3가지 경우로
    재귀적으로 호출하게 되는데, 이 인덱스를 정확히 다듬기가 굉장히 어려웠던 문제이다.
"""

import sys

sys.setrecursionlimit(10000)

N = int(input())

paper = [[" "] * (2 * N - 1) for _ in range(N)]

for i in range(N):
    for j in range(2 * N - 1):
        paper[i][j] = " "


def makeStar(top, left, right):
    paper[top][(left + right) // 2] = "*"

    paper[top + 1][(left + right) // 2 - 1] = "*"
    paper[top + 1][(left + right) // 2 + 1] = "*"

    for i in range(left, right):
        paper[top + 2][i] = "*"


def star(top, left, right, step):
    if step == 3:
        makeStar(top, left, right)
        return

    star(top, left + step // 2, right - step // 2, step // 2)
    star(top + step // 2, left, left + step - 1, step // 2)
    star(top + step // 2, right - step + 1, right, step // 2)


star(0, 0, 2 * N - 1, N)

for line in paper:
    for s in line:
        print(s, end="")
    print()
