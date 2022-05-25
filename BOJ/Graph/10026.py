"""
10026번 적록색약

1.  주어진 그림에서 적색/초록색/파란색을 노드로 그래프화 하여
    서로 연결된 그래프가 몇 개 인지 구하는 문제.
    
2.  최대 재귀 깊이를 10000까지 늘려야 할 수 있다.
"""

import sys

sys.setrecursionlimit(2000)

import copy

N = int(input())

grid = [list(input()) for _ in range(N)]

grid_conversed = copy.deepcopy(grid)

for i in range(N):
    for j in range(N):
        if grid_conversed[i][j] == "G":
            grid_conversed[i][j] = "R"

visited = [[False] * N for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def checkBorder(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False


def dfs(x, y, _grid, color):

    visited[x][y] = True

    for dir in range(4):
        if checkBorder(x + dx[dir], y + dy[dir]):
            if _grid[x + dx[dir]][y + dy[dir]] == color:
                if visited[x + dx[dir]][y + dy[dir]] == True:
                    continue
                dfs(x + dx[dir], y + dy[dir], _grid, color)


COUNT_NO = 0
COUNT_YES = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid, grid[i][j])
            COUNT_NO += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid_conversed, grid_conversed[i][j])
            COUNT_YES += 1

print(f"{COUNT_NO} {COUNT_YES}")
