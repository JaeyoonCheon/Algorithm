"""
2887번 행성 터널

1.  문제 자체는 MST(Mimimum Spanning Tree, 최소 신장 트리)를 구해 모든 노드를
    연결하는 최소의 경로 가중치를 찾는 문제이다.
    
2.  다만 문제는 100000개의 노드와 그 노드가 2차원값이 아닌 3차원값을 가져
    고려해야 할 가중치가 두 행성 간의 각 3개 변수의 차에 의해 결정된다는 것이다.
    
3.  각 N개의 행성이 다른 N-1의 행성과 연결될 수 있는 모든 경로를 찾아 비교하는것은
    연산이 너무 많을 것이므로 탐색할 경로를 제한해야만 한다.
    연결할 때 소요되는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이므로 만약 x축 경로를 택했다면
    나머지 y, z축 경로는 추후 선택되더라도 두 행성이 연결되어있으므로 선택되지 않을 것이다.
    
4.  따라서 x, y, z축 각각의 데이터를 오름차순 정렬을 해 보자. 이렇게 하여 정렬된 각 리스트에서는
    가장 짧은 서로간의 거리를 가진 두 임의의 행성 순으로 나열이 된다. 만약 x축이 1,5,6,2,3,4 순으로 정렬이 되었다면
    1-5, 5-6, 6-2, 2-3, 3-4 간의 거리가 x축에서는 가장 짧은 순으로 나타난다는 것이므로 앞에서부터 선택해보며
    이미 연결되어 있는 지 여부를 체크하는 것이다.
    
5.  위를 x, y, z축에 대해 오름차순 정렬 후 하나의 '간선'리스트에 넣어 짧은 순으로 정렬하고,
    크루스칼이나 프림 알고리즘을 통해 MST를 구하면 문제를 해결할 수 있다.
    도중에 나타나는 중복된 경로(시작점-끝점이 같은 경우)는 서로의 연결 체크 로직이 알고리즘에 포함되어 있으므로
    무시하고 수행하면 풀이 가능하다.
"""

import sys

N = int(input())

planetX, planetY, planetZ = [], [], []


for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())

    planetX.append((x, i))
    planetY.append((y, i))
    planetZ.append((z, i))

planetX = sorted(planetX, key=lambda x: (x[0], x[1]))
planetY = sorted(planetY, key=lambda x: (x[0], x[1]))
planetZ = sorted(planetZ, key=lambda x: (x[0], x[1]))

edges = []

for i in range(N - 1):
    edges.append(
        (abs(planetX[i][0] - planetX[i + 1][0]), planetX[i][1], planetX[i + 1][1])
    )
    edges.append(
        (abs(planetY[i][0] - planetY[i + 1][0]), planetY[i][1], planetY[i + 1][1])
    )
    edges.append(
        (abs(planetZ[i][0] - planetZ[i + 1][0]), planetZ[i][1], planetZ[i + 1][1])
    )

edges = sorted(edges, key=lambda x: (x[0], x[1], x[2]))
root = [x for x in range(N + 1)]


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
    else:
        return False


totalCost = 0

for edge in edges:
    _from, _to, _weight = edge[1], edge[2], edge[0]

    root_from = find(_from)
    root_to = find(_to)

    if union(root_from, root_to):
        totalCost += _weight

print(totalCost)
