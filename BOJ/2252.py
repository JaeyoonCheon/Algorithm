"""
2252번 줄 세우기
"""

import sys

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to = map(int, sys.stdin.readline().split())

    G[_from].append(_to)


income = [()]

for i in range(1, N + 1):
    income.append((i, len(G[i])))
