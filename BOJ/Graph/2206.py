"""
2206번 벽 부수고 이동하기

1.  간단한 BackTracking 문제라고 생각하여 DFS로 접근하였고 방문 목록에
    벽일 경우 이 벽을 깬 적이 있는지를 체크하여 벽을 부수는 경우를 체크
    하지만, 1000*1000 배열이고 중간 경로를 잘못 체크하면 재귀가 너무 깊어질 뿐만 아니라
    모든 경로를 탐색해야 최적 경로를 찾을 수 있으므로 비효율적인 방법이다.
    
2.  BFS를 적용해야 해당 좌표에 처음으로 닿았을 때 최단거리인 것을 확정지을 수 있으므로
    BFS 방식으로 접근하여 살펴보면, 벽을 깨지 않고 진행하는 경우와 벽을 1칸만 깨고 진행하는
    두 가지 경우의 수가 생긴다. 이 때, 벽을 깨지 않은 경우에는 벽을 깨지 않고 진행하거나
    벽을 깨고 지나가는 2가지 경우가 있으며 벽을 이미 깬 경우에는 벽을 깨지 않고 진행해야만 한다.
    
3.  따라서, 방문 체크 시 벽을 깨지 않고 현재 위치까지 진행한 경우와 벽을 이미 1칸 깨고 현재 위치에
    도달한 2가지 경우를 체크하도록 만들어야 하며 위 3가지 경우 외에는 큐에 좌표가 들어가지 않도록
    작성하여 목표 지점에 도달하도록 했다.
"""

import collections

N, M = map(int, input().split())

maze = [input().rstrip() for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[[False, False] for _ in range(M)] for _ in range(N)]

q = collections.deque()


def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    else:
        return False


def BFS(x, y):
    isFound = False
    q.append((x, y, 1, False))
    visited[x][y][0] = True

    minLength = 1000 * 1000

    while q:
        curr = q.popleft()

        if curr[0] == N - 1 and curr[1] == M - 1:
            isFound = True
            minLength = curr[2]
            break

        for i in range(4):
            nextX, nextY = curr[0] + dx[i], curr[1] + dy[i]
            isBreaked = curr[3]

            if check(nextX, nextY):
                if maze[nextX][nextY] == "0":
                    if visited[nextX][nextY][0] == False and not isBreaked:
                        visited[nextX][nextY][0] = True
                        q.append((nextX, nextY, curr[2] + 1, isBreaked))
                        continue
                    if visited[nextX][nextY][1] == False and isBreaked:
                        visited[nextX][nextY][1] = True
                        q.append((nextX, nextY, curr[2] + 1, isBreaked))
                        continue
                else:
                    if visited[nextX][nextY][1] == False and not isBreaked:
                        visited[nextX][nextY][1] = True
                        q.append((nextX, nextY, curr[2] + 1, True))

    if isFound:
        print(minLength)
    else:
        print(-1)


BFS(0, 0)
