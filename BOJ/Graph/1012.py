"""
1012번 유기농 배추

1.  문제 해석을 해 보면, 전형적인 그래프 탐색 문제로,
    연결된 서로 다른 그래프의 개수를 찾는 문제이다.
    따라서, dfs나 bfs를 이용해 전 좌표를 탐색하면서 인접한 그래프를 기록/검사하면 풀 수 있다.
"""

import sys


T = int(input())

for case in range(T):
    M, N, K = map(int, input().split())

    cache = [[0] * M for _ in range(N)]
    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())

        farm[x][y] = 1

    count = 1

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return
        if cache[x][y] != 0:
            return
        if farm[x][y] == 0:
            return
        else:
            cache[x][y] = count
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and cache[i][j] == 0:
                dfs(i, j)
                count += 1

    print(count - 1)
