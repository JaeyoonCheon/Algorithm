"""
16724번 피리 부는 사나이
"""

N, M = map(int, input().split())

maps = [input() for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dir = {"U": 0, "D": 1, "L": 2, "R": 3}
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def dfs(x, y, type):
    direction = dir[maps[x][y]]
    visited[x][y] = type

    if checkBorder(x + dx[direction], y + dy[direction]):
        if not visited[x + dx[direction]][y + dy[direction]]:
            dfs(x + dx[direction], y + dy[direction], type)
        else:
            visited[x][y] = visited[x + dx[direction]][y + dy[direction]]

    return


for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            dfs(i, j, i * N + j)

print()
