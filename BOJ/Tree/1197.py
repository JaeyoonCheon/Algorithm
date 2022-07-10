"""
1197번 최소 스패닝 트리
"""

import sys, heapq

MAX_NUM = sys.maxsize

V, E = map(int, input().split())

G = [[] for _ in range(V + 1)]


def prim_1():
    for _ in range(E):
        _from, _to, _weight = map(int, sys.stdin.readline().split())
        G[_from].append((_to, _weight))
        G[_to].append((_from, _weight))

    nodes = [1]
    edges = []
    allWeight = 0

    while len(nodes) != V:
        minWeight = MAX_NUM
        minEdge = False

        for node in nodes:
            for next in G[node]:
                if next not in edges and next[0] not in nodes and next[1] < minWeight:
                    minWeight = next[1]
                    minEdge = next

        nodes.append(minEdge[0])
        edges.append(minEdge)
        allWeight += minEdge[1]

    print(allWeight)


def prim_2():
    for _ in range(E):
        _from, _to, _weight = map(int, sys.stdin.readline().split())
        G[_from].append((_weight, _to))
        G[_to].append((_weight, _from))

    nodes = [1]
    q = []
    allWeight = 0

    for edge in G[1]:
        heapq.heappush(q, edge)

    while len(nodes) != V:
        minEdge = heapq.heappop(q)
        if minEdge[1] in nodes:
            continue

        nodes.append(minEdge[1])
        allWeight += minEdge[0]

        for nextEdge in G[minEdge[1]]:
            if nextEdge[1] not in nodes:
                heapq.heappush(q, nextEdge)

    print(allWeight)


prim_2()
