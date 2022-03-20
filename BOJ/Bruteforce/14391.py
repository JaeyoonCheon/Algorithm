"""
14391번 종이 조각

1.  각각의 조각은 오른쪽으로 붙어서 1자가 되거나 아래쪽으로 붙어서 1자가 되는 경우로 나뉜다.
    따라서, 완전 탐색으로 모든 격자를 순회하면서 가로 진행/세로 진행인 지 결정한 2^(N*M) 경우의 수를
    탐색해 주면 그 중 최대값을 선택
    연속된 가로 또는 세로를 같은 가로/세로 조각으로 나누는 것은 수적인 측면에서
    최대값이 될 수 없으므로 계산에 자연스럽게 포함될 것
    
2.  백트래킹
    각 조각은 우측 / 하단으로만 합쳐져 합계에 더해지므로, 종이 판을 오른쪽, 아래 방향으로 각 수가
    더해지는 모든 경우를 순회하여 더해보고 그 중 최대의 값을 판별
"""

import sys

N, M = map(int, sys.stdin.readline().split())
paper = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    paper.append(list(map(int, temp)))

dir = []

for i in range(N):
    dir.append([0 for _ in range(M)])

max = 0


def check():
    sum = 0
    tempVal = 0
    visited = []

    for i in range(N):
        visited.append([False for _ in range(M)])

    for i in range(N):
        for j in range(M):
            row = i
            col = j
            while dir[row][col] == dir[i][j]:
                if visited[row][col] == True:
                    break
                tempVal = tempVal * 10 + paper[row][col]
                visited[row][col] = True
                if dir[i][j] == "R":
                    col += 1
                    if col == M:
                        break
                else:
                    row += 1
                    if row == N:
                        break
            sum += tempVal
            tempVal = 0

    return sum


def attach(row, col):
    global max
    if row == N - 1 and col == M - 1:

        dir[row][col] = "R"
        sum = check()
        if max < sum:
            max = sum

        dir[row][col] = "D"
        sum = check()
        if max < sum:
            max = sum

        return

    nextRow = row
    nextCol = col + 1
    if nextCol == M:
        nextCol = 0
        nextRow += 1

    dir[row][col] = "R"
    attach(nextRow, nextCol)

    dir[row][col] = "D"
    attach(nextRow, nextCol)


attach(0, 0)
print(max)
