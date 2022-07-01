"""
14502번 연구소

1.  그래프 연결 문제를 3개의 벽을 세우기 위한 백트래킹을 응용해 푼 문제.

2.  1)  연결된 그래프를 확인하기 위한 DFS
    2)  벽 3개를 세워보기 위한 백트래킹(조합을 이용한 3개의 좌표 뽑기가 더 효율적일 것)
"""

import copy

N, M = map(int, input().split())

baseArea = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def DFS(area, visited, x, y):
    visited[x][y] = True

    for i in range(4):
        if checkBorder(x + dx[i], y + dy[i]):
            if area[x + dx[i]][y + dy[i]] == 0 and not visited[x + dx[i]][y + dy[i]]:
                area[x + dx[i]][y + dy[i]] = 2
                DFS(area, visited, x + dx[i], y + dy[i])


def checkSafeArea(area, visited):
    count = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                count += 1

    return count


def starting(area, visited):
    tempArea = copy.deepcopy(area)
    for i in range(N):
        for j in range(M):
            if area[i][j] == 2 and not visited[i][j]:
                DFS(tempArea, visited, i, j)

    result = checkSafeArea(tempArea, visited)
    return result


def buildWall(area, walls):
    global maxSafeArea
    count = len(walls)

    startX = 0
    startY = -1

    if walls:
        startX = walls[count - 1][0]

    for i in range(startX, N):
        for j in range(M):
            if area[i][j] == 0:
                if i == startX and j <= startY:
                    continue
                area[i][j] = 1
                walls.append((i, j))
                count = len(walls)

                if count == 3:
                    visited = [[False] * M for _ in range(N)]
                    result = starting(area, visited)

                    if result > maxSafeArea:
                        maxSafeArea = result
                else:
                    buildWall(area, walls)

                area[i][j] = 0
                walls.pop()
                count = len(walls)


walls = []
maxSafeArea = 0

buildWall(baseArea, walls)

print(maxSafeArea)
