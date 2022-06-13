"""
1504번 특정한 최단 경로

1.  노드 1에서 노드 N까지의 최단거리를 구하는 중 노드 v1, v2를 거쳐가야 하는 문제로
    처음에는 다익스트라 조건에 맞지만 어떻게 풀어야 하는 지 생각이 잘 나지 않음
    
2.  v1, v2를 거쳐가는 경우의 수는 4가지이다.
    1) 1에서 v1 -> v1에서 v2 -> v2에서 N
    2) 1에서 v2 -> v2에서 v1 -> v1에서 N
    3) 1에서 v1 -> v1에서 v2 -> v2에서 v1 -> v1에서 N
    4) 1에서 v2 -> v2에서 v1 -> v1에서 v2 -> v2에서 N
    
3.  따라서, 1 / v1 / v2에서 다익스트라를 3번 실행해 각 조건에 맞게 값을 구한 뒤
    최소값을 결정하면 된다.
"""

import sys, heapq
from unittest import result

N, E = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N + 1)]

for _ in range(E):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    G[_from].append((_to, _weight))
    G[_to].append((_from, _weight))

v1, v2 = map(int, sys.stdin.readline().split())


def dksPQ(start):
    dist = [float("INF")] * (N + 1)

    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        curr = heapq.heappop(q)

        if dist[curr[1]] < curr[0]:
            continue
        else:
            for node in G[curr[1]]:
                if dist[node[0]] > dist[curr[1]] + node[1]:
                    dist[node[0]] = dist[curr[1]] + node[1]
                    heapq.heappush(q, (dist[curr[1]] + node[1], node[0]))

    return dist


fromNode1 = dksPQ(1)

toV1 = fromNode1[v1]
toV2 = fromNode1[v2]

fromNodeV1 = dksPQ(v1)
fromNodeV2 = dksPQ(v2)

bridge = fromNodeV1[v2]
fromV1ToN = fromNodeV1[N]
fromV2ToN = fromNodeV2[N]

case1 = toV1 + bridge + fromV2ToN
case2 = toV2 + bridge + fromV1ToN
case3 = toV1 + 2 * bridge + fromV1ToN
case4 = toV2 + 2 * bridge + fromV2ToN

result = min(case1, case2, case3, case4)

if result == float("INF"):
    print(-1)
else:
    print(result)
