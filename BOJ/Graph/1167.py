"""
1167번 트리의 지름

1.  주어지는 정점들에 연결된 정점-거리 정보로 만들어진 가중치 있는 트리에서
    서로 간의 거리가 가장 먼 것을 트리의 지름이라고 하며 이 값을 구하는 문제.
    
2.  BFS나 다익스트라 등으로 해결할까 생각했으나, 어떤 한 시작점에서 어떤 말단까지 연속적으로
    진행했다가 말단을 만나면 거리를 갱신하는 것이 가장 효율적일 것으로 생각하여 DFS로 로직을 구현했다.
    
3.  풀이 자체는 구성된 트리를 DFS로 백트래킹을 수행해 최장거리를 갱신하도록 만들었다.

4.  가장 중요한 점은, 단순히 주어지는 모든 정점에 대해 DFS를 수행하여 해당 정점에서의 지름을 구할
    필요가 없다는 것이다. 어떤 한 점을 임의로 고르고 그 정점에서 갈 수 있는 최장 길이를 가지는 정점을
    찾은 후 그 정점에서의 지름을 구하면 2번만에 트리의 지름을 구할 수 있다.
    이것의 증명은 수학적으모 가능하나, 직관적으로 알아보자면 각 정점들을 구승로 표현하고 그것들을 
    각 거리만큼의 실로 연결한 모형을 만들었다고 할 때 아무 구슬이나 잡고 늘어뜨려 가장 먼 구슬을 선택하고
    다시 그 구슬에서 가장 먼 것을 선택하면 두 구슬 사이의 거리가 지름이라는 것을 직관적으로 알 수 있다.
"""

import sys

V = int(input())

G = {}

for _ in range(V):
    node = list(map(int, sys.stdin.readline().split()))

    number = node[0]

    pick = 1
    temp = []
    while node[pick] != -1:
        temp.append((node[pick], node[pick + 1]))
        pick += 2
    G[number] = temp

visited = []
maxDist = 0
maxNode = -1


def DFS(v, dist):
    global maxDist, maxNode
    visited[v] = True
    for next in G[v]:
        if visited[next[0]] != True:
            DFS(next[0], dist + next[1])
            visited[next[0]] = False

    if dist > maxDist:
        maxDist = dist
        maxNode = v
    return


visited = [False] * (V + 1)

for i in G.keys():
    DFS(i, 0)
    break

visited = [False] * (V + 1)
DFS(maxNode, 0)

print(maxDist)
