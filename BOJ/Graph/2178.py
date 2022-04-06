"""
2178번 미로 탐색

1.  전형적인 BFS를 활용한 미로 최단 거리 탐색
"""

from queue import Queue
import sys

N, M = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

q = Queue()


def BFS(x, y):
    q.put((x, y, 1))
    visited[x][y] = True

    while q.empty() != True:
        curr = q.get()

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j or i == -1 * j:
                    continue
                if curr[0] + i < 0 or curr[0] + i >= N:
                    continue
                if curr[1] + j < 0 or curr[1] + j >= M:
                    continue
                if maze[curr[0] + i][curr[1] + j] == 0:
                    continue
                if visited[curr[0] + i][curr[1] + j] == True:
                    continue
                if curr[0] + i == N - 1 and curr[1] + j == M - 1:
                    print(curr[2] + 1)
                    sys.exit()
                else:
                    visited[curr[0] + i][curr[1] + j] = True
                    q.put((curr[0] + i, curr[1] + j, curr[2] + 1))


BFS(0, 0)
