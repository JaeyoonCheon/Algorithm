"""
1753번 최단경로

1.  한 정점에서 다른 정점까지의 최단 거리를 찾는 문제이다.
    주어진 문제에서는 방향 그래프이며, 가중치가 양수이다.
    
2.  이 문제에서는 다익스트라 알고리즘을 사용해야 한다. 문제 조건이 다익스트라 조건에 맞춰져 있기도 하며,
    벨만-포드나 플로이드 알고리즘은 각각 O(VE), O(V^3) 시간복잡도로 O((V+E)logE)인 다익스트라 알고리즘의
    효율성을 따라잡지 못하기 때문이다.
    
3.  다익스트라는 각 정점의 방문 여부와 시작 정점에서 해당 정점까지의 거리를 저장하는 배열
    2개가 필요하다.
    1)  거리 배열은 모두 무한대로 처리해 놓는다.
    2)  시작 정점은 방문처리하고 거리를 0으로 설정한다.
    3)  현재 방문한 정점에서 방문하지 않은 정점 중 가장 가까운 정점은 선택하고 방문처리한다.
    4)  시작 정점에서 현재 방문한 정점까지의 거리 + 현재 정점에서 선택한 정점까지의 거리 vs
        시작 정점에서 선택한 정점까지의 거리를 비교하여 전자가 더 적다면 거리를 갱신하여 저장한다.
    5)  3, 4 과정을 정점 개수 - 1(시작 정점)만큼 반복한다.
    
4.  위의 다익스트라 알고리즘은 최소 거리의 정점을 찾아야 하므로 O(N^2) 시간복잡도를 가진다.
    우선순위 큐를 거리 기준으로 저장하여 사용하면 방문 처리도 자동으로 되고
    시간복잡도 또한 O((V+E)logE)가 된다.
"""

import sys, heapq

V, E = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline())

G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    G[u].append((v, w))


def findShortest(dist, visited):
    minNode = -1
    minDist = float("INF")

    for i, v in enumerate(dist):
        if not visited[i] and minDist > v:
            minDist = v
            minNode = i

    return minNode


def dks(start):
    dist = [float("INF")] * (V + 1)
    visited = [False] * (V + 1)

    visited[start] = True
    dist[start] = 0
    for node in G[start]:
        dist[node[0]] = node[1]

    for node in range(V - 1):
        next = findShortest(dist, visited)
        visited[next] = True

        for node in G[next]:
            if dist[node[0]] > dist[next] + node[1]:
                dist[node[0]] = dist[next] + node[1]

    for i in range(1, V + 1):
        if dist[i] != float("INF"):
            print(dist[i])
        else:
            print("INF")


def dksPQ(start):
    dist = [float("INF")] * (V + 1)

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

    for i in range(1, V + 1):
        if dist[i] != float("INF"):
            print(dist[i])
        else:
            print("INF")


dksPQ(K)
