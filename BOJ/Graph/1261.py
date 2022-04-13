"""
1261번 알고스팟

1.  maze + BFS 최단 경로 문제

2.  이 문제의 핵심은 방을 뚫고 갈 경우 curr[2]가 증가한 상태로 큐에 저장되고,
    빈 방을 지나갈 경우에는 curr[2]를 증가시키지 않고 큐에 저장한다는 것
    
3.  그래프 간선의 0(빈 방일 경우)은 가중치가 없는 경우이기 때문에(가장 먼저 지나가야 하는 곳)
    큐에서 방을 뚫고 가는 경우보다 우선적으로 처리되어야 한다.
    따라서, 빈 방을 지나가는 경우 큐의 앞쪽으로 데이터가 push되어야 pop할 때 우선적으로
    뽑혀 처리되게 된다.
"""

from collections import deque

M, N = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]

q = deque()

visited = [[False] * M for _ in range(N)]

visited[0][0] = True
q.appendleft((0, 0, 0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    curr = q.pop()
    x = curr[0]
    y = curr[1]

    if x == N - 1 and y == M - 1:
        print(curr[2])

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if nextX >= 0 and nextX < N and nextY >= 0 and nextY < M:
            if visited[nextX][nextY] == False:
                if maze[nextX][nextY] == 0:
                    visited[nextX][nextY] = True
                    q.append((nextX, nextY, curr[2]))
                else:
                    visited[nextX][nextY] = True
                    q.appendleft((nextX, nextY, curr[2] + 1))
