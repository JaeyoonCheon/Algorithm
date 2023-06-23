"""
    lv.3 섬 연결하기
    
    1.  유니온-파인드를 사용해 최소 비용으로 최소 스패닝 트리를 그리는 간선을 구한다.
"""


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return
    else:
        parent[x] = y


def solution(n, costs):
    answer = 0

    parent = [i for i in range(n)]

    costs = list(sorted(costs, key=lambda x: x[2]))

    connected = 0

    for edge in costs:
        start, end, cost = edge

        if find(parent, start) != find(parent, end):
            union(parent, start, end)
            connected += 1
            answer += cost

        if connected == n:
            break

    return answer


result = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
