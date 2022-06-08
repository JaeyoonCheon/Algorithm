"""
11404번 플로이드

1.  기본적인 플로이드-와샬 알고리즘을 이용한 각 정점 간의 최단거리 계산 문제.

2.  이차원 배열의 각 축을 출발/도착을 의미하는 각각의 정점으로 간주.
    모든 정점중 하나를 '거쳐가는' 정점이라고 생각할 때 어떤 출발 정점에서
    해당 정점을 '거쳐간 뒤' 도착 정점에 도달하는 경우, 출발 정점에서 도착 정점으로
    직진하는 경우와 해당 정점을 거쳐가는 경로 중 짧은 것을 선택하는데 이 과정을
    모든 정점을 대상으로 시행하면 된다.
    
3.  문제 조건을 잘 살펴봐야 한다.
    어떤 출발 정점에서 도착 정점으로의 주어지는 경로는 하나가 아닐 수 있으며,
    도달하지 못하는 경우 0으로 표시해서 나타내야 한다.
"""

import sys

N = int(input())
M = int(input())

MAX_WEIGHT = int(1e9)

G = [[MAX_WEIGHT] * N for _ in range(N)]

for _ in range(M):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    if G[_from - 1][_to - 1] > _weight:
        G[_from - 1][_to - 1] = _weight

for i in range(N):
    G[i][i] = 0

for i in range(N):
    for y in range(N):
        for x in range(N):
            # if x == i or y == i:
            #     continue
            # if x == y:
            #     continue

            G[y][x] = min(G[y][x], G[y][i] + G[i][x])

for i in range(N):
    for j in range(N):
        if G[i][j] == MAX_WEIGHT:
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()
