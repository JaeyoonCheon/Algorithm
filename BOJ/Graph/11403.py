"""
11403번 경로 찾기

1.  주어진 무가중치 방향그래프 인접 행렬을 가지고 그래프를 구성한 뒤,
    각 정점에서 갈 수 있는 정점을 표시하면 되는 문제.
    
2.  풀이는 그래프 구성한 뒤 dfs로 연결된 정점들을 순회하면서 탐색했으나,
    BFS, 다익스트라, 플로이드 알고리즘 등 다양하게 사용 가능할 것으로 생각됨
"""

import sys

sys.setrecursionlimit(10001)

N = int(input())

G = [[] for _ in range(N)]

path = [[0] * N for _ in range(N)]

for i in range(N):
    adjMatrix = list(map(int, input().split()))
    for j, v in enumerate(adjMatrix):
        if v == 1:
            G[i].append(j)

visited = [False] * N


def dfs(node):
    for next in G[node]:
        if visited[next] != True:
            visited[next] = True
            dfs(next)


for i in range(N):
    visited = [False] * N
    dfs(i)
    for idx, v in enumerate(visited):
        if v == True:
            path[i][idx] = 1

for i in range(N):
    for j in range(N):
        print(path[i][j], end=" ")
    print()
