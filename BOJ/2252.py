"""
2252번 줄 세우기
"""

import sys, collections

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
invertedG = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to = map(int, sys.stdin.readline().split())

    G[_from].append(_to)
    invertedG[_to].append(_from)


income = [()]

for i in range(1, N + 1):
    income.append(len(invertedG[i]))

path = []

q = collections.deque()

step = 0

for i in range(1, N + 1):
    if income[i] == 0 and i not in path and i not in q:
        q.append((i, 0))
        path.append(i)

while q:
    curr = q.popleft()

    for nextNode in G[curr]:
        income[nextNode] -= 1

    for i in range(1, N + 1):
        if income[i] == 0 and i not in path and i not in q:
            q.append((i, curr[1] + 1))
            path.append(i)

for i in path:
    print(i, end=" ")
