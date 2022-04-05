"""
1707번 이분 그래프

1.  난이도 상.

2.  이분 그래프란 모든 정점을 두 가지 색으로 칠하되, 인접한 정점끼리는 같은 색이 아닌
    두 그룹으로 나눠질 수 있는 그래프를 말한다.
    
3.  이 문제에서 주어지는 케이스에서는 연결되지 않은 다수의 그래프가 나타날 수 있으므로 이것을 고려해야 한다.

4.  먼저, 연결된 그래프에 인접한 정점끼리 색이 다르도록 dfs를 이용해 순회, 색칠하고
    이후 색칠된 그래프에 대해 모든 정점을 검사하면서 인접한 정점이 색이 같은 지 다른 지 검사
"""

import sys

sys.setrecursionlimit(10 ** 6)

K = int(input())

V, E = 0, 0
edge = []
colors = []


def coloring(vertex, color):
    colors[vertex] = color

    for i in edge[vertex]:
        if colors[i] != False:
            continue
        coloring(i, color * -1)


for _ in range(K):
    flag = True
    V, E = map(int, input().split())

    edge = [[] for _ in range(V + 1)]
    colors = [False] * (V + 1)
    colors[0] = True
    for i in range(E):
        _from, _to = map(int, sys.stdin.readline().split())
        edge[_from].append(_to)
        edge[_to].append(_from)

    for i in range(1, V + 1):
        if colors[i] == False:
            coloring(i, 1)

    for i in range(1, V + 1):
        for j in edge[i]:
            if colors[i] == colors[j]:
                flag = False

    if flag == True:
        print("YES")
    else:
        print("NO")
