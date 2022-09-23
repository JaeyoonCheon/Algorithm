"""
2573번 빙산

1.  그래프 탐색을 이용한 구현 문제.

2.  한 year에 대해 물에서 빙산에 1번씩 닿는 경우를 체크해 빙산의 변화를 구현해야 한다.
    이 때 '물'의 기준은 현재 변하고 있는 빙산의 기준이 아닌, 전년도의 빙산의 형태에서의 물만 해당되므로
    deepcopy를 이용해 이전 빙산을 저장해 놓고 이용해야 한다.
    
3.  빙산 용해가 끝났다면 빙산에 대해 분리된 그래프의 개수가 2개 이상인 지 체크해 주면 된다.

4.  재귀 깊이가 90000이어서 DFS로도 가능할 것으로 보이나 BFS로 구현해 보았다.
"""

import sys, collections, copy

N, M = map(int, input().split())

ice = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = []
prev = []
q = collections.deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

isEmpty = False


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def melt(initX, initY):
    visited[initX][initY] = True
    q.append((initX, initY))

    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]

        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]

            if checkBorder(nextX, nextY):
                if prev[nextX][nextY] != 0 and ice[nextX][nextY] > 0:
                    ice[nextX][nextY] -= 1
                if prev[nextX][nextY] == 0 and not visited[nextX][nextY]:
                    visited[nextX][nextY] = True
                    q.append((nextX, nextY))


def checkIce(initX, initY):
    visited[initX][initY] = True
    q.append((initX, initY))

    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]

        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]

            if checkBorder(nextX, nextY):
                if ice[nextX][nextY] != 0 and not visited[nextX][nextY]:
                    visited[nextX][nextY] = True
                    q.append((nextX, nextY))


count = 0

while not isEmpty:
    count += 1
    prev = copy.deepcopy(ice)
    q = collections.deque()
    visited = [[False] * M for _ in range(N)]
    iceberg = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and prev[i][j] == 0:
                melt(i, j)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ice[i][j] != 0:
                checkIce(i, j)
                iceberg += 1

    if iceberg >= 2:
        break

    isEmpty = True
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                isEmpty = False

if isEmpty:
    print(0)
else:
    print(count)
