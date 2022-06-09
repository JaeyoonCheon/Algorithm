"""
11725번 트리의 부모 찾기

1.  주어진 인접 리스트 트리를 1번을 Root로 삼고 트리를 재구성하는 것.

2.  단순히 1번을 Root로 잡았을 때 각 노드들의 부모만 출력하면 되는 문제이므로,
    트리의 구조를 재구성하는 등의 동작을 불필요하고 1번 노드부터 탐색할 때 각 노드들의
    바로 이전 노드(부모)만 따로 기록해 놓았다가 마지막에 출력하면 되는 문제이다.
"""

import sys, collections

N = int(input())

G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    _from, _to = map(int, sys.stdin.readline().split())

    G[_from].append(_to)
    G[_to].append(_from)

parents = [0] * (N + 1)


def BFS():
    q = collections.deque()

    q.append((1, -1))
    parents[1] = -1

    while q:
        curr = q.popleft()

        for next in G[curr[0]]:
            if parents[next] == 0:
                q.append((next, curr[0]))

        parents[curr[0]] = curr[1]

    for i in range(2, N + 1):
        print(parents[i])


BFS()
