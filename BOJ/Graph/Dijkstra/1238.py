"""
1238번 파티

1.  개선된 다익스트라 알고리즘을 이용해 주어진 단방향 그래프에서
    각 노드마다 지정된 파티장이 있는 노드에 도달했다가 다시 돌아오는 총 시간을 구해
    그 최대값을 구하는 문제.
    
2.  각 노드들이 파티장에 가는 시간 + 파티장에서 각 노드로 복귀하는 시간(미리 1번 계산 후 저장) 중 최대값

3.  플로이드-와샬 알고리즘으로도 풀 수 있을 것으로 보임
"""

import sys, heapq

N, M, X = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, _time = map(int, sys.stdin.readline().split())

    G[_from].append((_to, _time))


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

    return dist[X]


def dksReturnPQ():
    dist = [float("INF")] * (N + 1)

    q = []

    heapq.heappush(q, (0, X))
    dist[X] = 0

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


maxDist = 0

returnDist = dksReturnPQ()

for i in range(1, N + 1):
    result = dksPQ(i) + returnDist[i]

    if maxDist < result:
        maxDist = result

print(maxDist)
