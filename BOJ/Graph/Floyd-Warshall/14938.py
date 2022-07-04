"""
14938번 서강그라운드

1.  문제를 살펴보면, 모든 지역에 대해 그 지역에서 수색 거리만큼의 범위 내에서 움직여
    최대의 item을 가질 수 있도록 하는 방법을 찾아야 하는 문제이므로, 모든 노드의
    모든 경로의 최단거리를 찾아 그 경로마다의 item 합을 구해야 한다.
    따라서, 모든 노드에 대해 기본적으로 경로를 갱신해 주는 플로이드-와샬 알고리즘을 선택해
    주어진 그래프의 최단경로를 갱신한다.
    
2.  갱신한 뒤 얻을 수 있는 최단거리 테이블 G(그래프가 최단거리를 저장한 표로 변환됨)에서
    각 노드마다의 item 값을 매핑하여 가장 최대값을 가지는 노드를 선택
"""

import sys

N, M, R = map(int, input().split())

MAX_WEIGHT = int(1e9)

items = list(map(int, input().split()))

G = [[MAX_WEIGHT] * N for _ in range(N)]

for _ in range(R):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    G[_from - 1][_to - 1] = _weight
    G[_to - 1][_from - 1] = _weight

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

starting = [0] * N

for i in range(N):
    for j in range(N):
        if G[i][j] <= M:
            starting[i] += items[j]

print(max(starting))
