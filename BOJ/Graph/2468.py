"""
2468번 안전 영역

1.  0~최대 높이까지 모든 높이에 대해 그래프 순회를 하고 분리된 그래프(안전 영역)의 최대 개수를 구하는 문제.
"""

import sys

sys.setrecursionlimit(100 * 100)

N = int(input())

region = []
maxHeight = 0

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))

    rowMax = max(row)

    if maxHeight < rowMax:
        maxHeight = rowMax

    region.append(row)

maxSafeAreas = 0

visited = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def dfs(x, y, threshold):
    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        if (
            checkBorder(nextX, nextY)
            and not visited[nextX][nextY]
            and region[nextX][nextY] > threshold
        ):
            visited[nextX][nextY] = True
            dfs(nextX, nextY, threshold)


for height in range(maxHeight + 1):
    safeAreas = 0

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and region[i][j] > height:
                visited[i][j] = True
                dfs(i, j, height)
                safeAreas += 1

    if maxSafeAreas < safeAreas:
        maxSafeAreas = safeAreas

print(maxSafeAreas)
