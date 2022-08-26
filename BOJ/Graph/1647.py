"""
1647번 도시 분할 계획

1.  처음에는 문제의 요구사항이 연결된 그래프를 2개로 나누는데 나뉜 각각의 그래프들의 모든 노드가
    서로 연결되어있는 그래프이어야 되는줄 알았으나 나뉜 그래프에서 각 노드가 다른 모든 노드에 도달할 수 있는
    경로가 존재하기만 한다면 상관없는 문제였다.

2.  따라서, 전체 그래프에서 모든 노드를 가중치의 최소로 잇는 큰 경로를 구한 뒤, 그 경로에서 가장 큰 가중치의 간선을
    제거하면 되는, 결국에 MST(최소 스패닝 트리)를 구하는 문제와 동일했다.

3.  간선이 백만개 이하이고, 구현하기 편한 Prim 알고리즘을 MST를 구하는데 이용했다.
    도중에 MST를 구성하는 간선들의 최대값을 저장해놓은 후, MST의 모든 가중치에서 그 최대값을 빼면
    두 개로 나뉜 MST를 구해 합을 구하는 것과 동일하다.
"""

import sys, heapq

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, _weight = map(int, sys.stdin.readline().split())

    G[_from].append((_weight, _to))
    G[_to].append((_weight, _from))


def prim():
    visited = [False] * (N + 1)
    mstEdge = []
    mstWeight = 0

    q = []

    heapq.heappush(q, (0, 1))

    while q:
        _weight, _node = heapq.heappop(q)

        if visited[_node]:
            continue
        else:
            visited[_node] = True
            mstWeight += _weight
            mstEdge.append(_weight)

            for next in G[_node]:
                nextNode = next[1]

                if visited[nextNode]:
                    continue
                else:
                    heapq.heappush(q, next)

    return mstWeight - max(mstEdge)


print(prim())
