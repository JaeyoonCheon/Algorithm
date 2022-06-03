"""
1967번 트리의 지름

1.  트리의 지름이란 트리의 정점 중 서로 가장 먼 거리를 가지는 두 정점 간의 거리를 의미

2.  임의의 정점에서 가장 먼 정점을 구한 뒤(가장 먼 정점이 트리의 지름을 구성하는 두 정점 중
    하나가 된다) 그 정점에서 다시 가장 먼 정점을 구하면 그 길이가 트리의 지름이다.
"""

import sys

sys.setrecursionlimit(10001)

N = int(input())

G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    _from, _to, w = map(int, sys.stdin.readline().split())

    G[_from].append((_to, w))
    G[_to].append((_from, w))

maxNode = 1
maxPath = -1

visited = []


def DFS(node, length):
    global maxNode, maxPath

    visited[node] = True
    for next in G[node]:
        if not visited[next[0]]:
            DFS(next[0], length + next[1])

    if maxPath < length:
        maxPath = length
        maxNode = node


for _ in range(2):
    visited = [False] * (N + 1)
    DFS(maxNode, 0)

print(maxPath)
