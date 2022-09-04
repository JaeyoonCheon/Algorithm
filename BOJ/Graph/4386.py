"""
4386번 별자리 만들기

1.  2차원 좌표들이 주어지고 그 좌표들을 연결하는 MST를 찾는 문제.

2.  100개의 노드밖에 없으므로, 모든 가능한 간선들을 거리 계산 후 간선 집합에 넣고 정렬 후
    크루스칼 알고리즘을 적용하여 풀이하였다.
"""
import math, sys


N = int(input())

stars = [list(map(float, input().split())) for _ in range(N)]

edges = []


def getDist(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


if N == 1:
    sys.exit(0)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        edges.append((getDist(stars[i], stars[j]), i, j))

edges = sorted(edges, key=lambda x: (x[0], x[1], x[2]))
root = [x for x in range(N)]


def find(v):
    if root[v] == v:
        return v
    root[v] = find(root[v])
    return root[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        root[b] = a
        return True
    return False


totalCost = 0

for edge in edges:
    _dist, _from, _to = edge[0], edge[1], edge[2]

    if union(_from, _to):
        totalCost += _dist

print(totalCost)
