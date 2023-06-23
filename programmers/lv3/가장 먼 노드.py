"""
    lv.3 가장 먼 노드
    
    1.  최단거리 기준으로, 1로부터 각 노드들이 얼마나 멀리 떨어져 있는 지 그 개수를 구하는 문제.
    2.  최단거리룰 구하고 그 개수를 얻기 위해 BFS를 사용해 각 노드들의 최단 거리를 구하면서 step을 같이 계산하여 풀이.
"""

from collections import deque


def solution(n, edges):
    answer = 0

    nodes = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for edge in edges:
        v1, v2 = edge

        nodes[v1].append(v2)
        nodes[v2].append(v1)

    q = deque()
    visited[1] = True

    for node in nodes[1]:
        q.appendleft((node, 0))

    maxStep = 0

    while q:
        next, step = q.pop()

        if visited[next]:
            continue
        else:
            visited[next] = step + 1

            for node in nodes[next]:
                if not visited[node]:
                    q.appendleft((node, step + 1))

            maxStep = max(step + 1, maxStep)

    answer = visited.count(maxStep)

    return answer


result = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
