"""
11779번 최소비용 구하기 2

1.  양의 가중치만을 가진 그래프 상에서 한 지점에서 다른 지점으로의 최단 경로의 길이와 그 경로를 출력하는 문제.
    다익스트라를 활용하면서 최단거리가 갱신될 때 마다 그 이전의 노드를 저장해 놓고
    도착지로부터 반대로 경로를 추적해가면 지나온 경로를 얻을 수 있다.
"""

import sys, heapq

N = int(input())
M = int(input())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    G[_from].append((_to, _weight))

start, end = map(int, input().split())


def dksPQ(start, end):
    dist = [float("INF")] * (N + 1)
    prev = [-1] * (N + 1)

    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0
    prev[start] = -1

    while q:
        curr = heapq.heappop(q)

        if dist[curr[1]] < curr[0]:
            continue
        else:
            for node in G[curr[1]]:
                if dist[node[0]] > dist[curr[1]] + node[1]:
                    dist[node[0]] = dist[curr[1]] + node[1]
                    prev[node[0]] = curr[1]
                    heapq.heappush(q, (dist[curr[1]] + node[1], node[0]))

    print(dist[end])

    path = [end]
    step = end

    while prev[step] != -1:
        path.append(prev[step])
        step = prev[step]

    path.reverse()

    print(len(path))

    for city in path:
        print(city, end=" ")


dksPQ(start, end)
