"""
1780번 종이의 개수

1.  재귀를 통한 부분 검사를 수행하는 재귀 & Divide and Conquer 문제.

2.  행/열 3구간으로 나누어 동일한 색이 아니라면 9가지 부분으로 나뉘는 것을 고려해야 함
"""

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

colors = [0, 0, 0]


def slicing(x, y, length):
    isSame = True
    start = paper[x][y]

    if length == 1:
        colors[start + 1] += 1
        return

    for i in range(x, x + length):
        for j in range(y, y + length):
            if start != paper[i][j]:
                isSame = False

    if isSame:
        colors[start + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                slicing(x + i * (length // 3), y + j * (length // 3), length // 3)


slicing(0, 0, N)

for i in colors:
    print(i)
