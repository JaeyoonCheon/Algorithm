"""
7569번 토마토

1.  BFS 최단 거리 찾기 문제의 3차원 변형 문제.

2.  2차원 BFS와 동일하게 6방향 진행방향만 잘 설정해 주면 무난하게 풀이할 수 있고
    토마토가 없는 빈 곳은 방문처리를 미리 해 주어야 예외가 없는 것으로 보임
"""

import collections

M, N, H = map(int, input().split())

container = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]

q = collections.deque()

dirX = [-1, 0, 0, 0, 0, 1]
dirY = [0, 0, 1, 0, -1, 0]
dirZ = [0, 1, 0, -1, 0, 0]


def check(q, curr):
    for i in range(6):
        if (
            curr[0] + dirZ[i] >= 0
            and curr[0] + dirZ[i] < H
            and curr[1] + dirY[i] >= 0
            and curr[1] + dirY[i] < N
            and curr[2] + dirX[i] >= 0
            and curr[2] + dirX[i] < M
        ):
            if not visited[curr[0] + dirZ[i]][curr[1] + dirY[i]][curr[2] + dirX[i]]:
                if (
                    container[curr[0] + dirZ[i]][curr[1] + dirY[i]][curr[2] + dirX[i]]
                    == 0
                ):
                    q.append((curr[0] + dirZ[i], curr[1] + dirY[i], curr[2] + dirX[i]))
                    visited[curr[0] + dirZ[i]][curr[1] + dirY[i]][
                        curr[2] + dirX[i]
                    ] = True
                # elif (
                #     container[curr[0] + dirZ[i]][curr[1] + dirY[i]][curr[2] + dirX[i]]
                #     == -1
                # ):
                #     visited[curr[0] + dirZ[i]][curr[1] + dirY[i]][
                #         curr[2] + dirX[i]
                #     ] = True


for i in range(H):
    for j in range(N):
        for k in range(M):
            if container[i][j][k] == 1:
                q.append((i, j, k))
            elif container[i][j][k] == -1:
                visited[i][j][k] = True

days = -1
isAll = True

while q:
    for _ in range(len(q)):
        curr = q.popleft()
        visited[curr[0]][curr[1]][curr[2]] = True
        check(q, curr)
    days += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == 0:
                isAll = False

if isAll:
    print(days)
else:
    print(-1)
