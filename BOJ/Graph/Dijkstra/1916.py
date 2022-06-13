"""
1916번 최소비용 구하기

1.  다익스트라 알고리즘의 조건에 맞지만 시간 제한이 0.5초인 문제.

2.  일반적인 선형 리스트를 이용해 방문 체크와 거리 갱신을 하는 O(N^2) 다익스트라 알고리즘은 0.5초 안에
    테스트 케이스를 통과하기 힘들다.
    따라서, 우선순위 큐를 적용한 개선된 다익스트라 알고리즘을 이용해 O((N+M)logN)으로 해결할 수 있다.
"""

import sys, heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    G[_from].append((_to, _weight))

startNode, endNode = map(int, sys.stdin.readline().split())


def dksPQ(start, end):
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

    print(dist[end])


dksPQ(startNode, endNode)
