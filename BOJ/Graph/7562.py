"""
7562번 나이트의 이동

1.  전형적인 BFS 최단거리 문제.

2.  pypy3에서 sys.stdin.readline을 사용하면 통과
"""
from collections import deque
import sys

T = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    N = int(input())

    startX, startY = map(int, sys.stdin.readline().split())
    endX, endY = map(int, sys.stdin.readline().split())

    visited = [[False] * N for _ in range(N)]

    q = deque()
    found = False

    q.append((startX, startY, 1))
    visited[startX][startY] = True

    while q:
        if found:
            break
        curr = q.popleft()

        for i in range(8):
            x = curr[0] + dx[i]
            y = curr[1] + dy[i]

            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if visited[x][y] == True:
                continue
            if x == endX and y == endY:
                print(curr[2])
                found = True
                break
            visited[x][y] = True
            q.append((x, y, curr[2] + 1))

    if found == False:
        print("0")
