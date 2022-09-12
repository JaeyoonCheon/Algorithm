"""
10775번 공항

1.  G개의 게이트에 P개의 비행기를 주차시켜야 한다. 이 때 각 비행기가 들어갈 수 있는 게이트는
    0~g_i 사이에 있는 게이트에만 들어갈 수 있다. 잘 생각해보면 가능한 번호가 큰 게이트에 주차시키는 것이
    추후 작은 번호가 부여된 비행기가 들어올 때 가장 많은 경우의 수를 가질 수 있으므로 비행기는 가능한 큰 번호의
    게이트에 주차시키는 것이 바람직하다.
    
2.  단순 그리디로 풀어도 충분히 풀이가능할 것으로 보이나, 어떤 번호가 주어졌을 때 주차시킬 다음 번호를 알 수 있다면
    좀 더 효율적으로 해결할 수 있을 것이다. 따라서, 어떤 비행기를 주차시켰을 때 그 번호에 다음 주차가능한 번호를
    유니온-파인드로 지정해 놓으면 된다.
    어떤 비행기를 주차시켰을 때 바로 이전 번호와 union과정을 진행하고, find를 진행할 때
    부모들의 번호를 갱신하는 과정을 거친다. 게이트 1에 주차했는데 또 주차하게 되면 탐색을 종료하도록 한다.
"""

import sys

sys.setrecursionlimit(10000)

G = int(input())
P = int(input())

gates = [False] * (G + 1)
root = [x for x in range(G + 1)]


def find(v):
    if root[v] == v:
        return root[v]
    else:
        root[v] = find(root[v])
        return root[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        root[b] = a


count = 0

dests = []
for _ in range(P):
    dests.append(int(sys.stdin.readline()))

for dest in dests:
    root[dest] = find(dest)
    if root[dest] == 1 and gates[1]:
        break

    gates[root[dest]] = True
    count += 1
    if root[dest] != 1:
        union(root[dest] - 1, root[dest])

print(count)
