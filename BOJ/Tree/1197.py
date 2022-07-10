"""
1197번 최소 스패닝 트리

1.  최소 스패닝 트리?
    양의 가중치를 가진 그래프에서 사이클을 가지지 않고 모든 정점들을 연결하며
    간선 가중치의 총 합이 최소가 되는 트리

2.  두 가지 MST를 해결하기 위한 방법
    1)  Prim's Algorithm
    2)  Kruskal's Algorithm
    
3.  프림 알고리즘을 사용하는 경우 현재 선택한 정점과 연결된 간선들 중 최소치인 가중치를 가지는 간선을
    트리에 연결시켜나가는 방법으로, 보통 O(N^2)이나 연결된 간선 중 최소 가중치 간선을 찾는 과정을
    우선순위 힙으로 구현하면 O(NlogN)으로 해결할 수 있다.
    
4.  크루스칼 알고리즘은 전체 간선들을 가중치 순으로 오름차순 정렬한 뒤
    가장 작은 가중치를 가진 간선들 순으로 선택해 모든 정점들이 포함될 때까지 계속한다.
    그 과정에서, 선택한 간선들이 서로 사이클을 이루지 않도록 Union-find 방법을 이용해 검사한다.
"""

import sys, heapq

MAX_NUM = sys.maxsize

V, E = map(int, input().split())

G = [[] for _ in range(V + 1)]

parent = [-1] * (V + 1)


def find(node):
    if parent[node] < 0:
        return node
    else:
        root = find(parent[node])
        parent[node] = root
        return root


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

    return True


def kruskal():
    edges = []
    allWeight = 0

    for _ in range(E):
        _from, _to, _weight = map(int, sys.stdin.readline().split())
        edges.append((_from, _to, _weight))

    sorted(edges, key=lambda x: (x[2], x[0], x[1]))

    for edge in edges:
        if union(edge[0], edge[1]):
            allWeight += edge[2]

    print(allWeight)


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


kruskal()
