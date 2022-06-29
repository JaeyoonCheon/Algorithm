"""
12851번 숨바꼭질 2

1.  1차원 좌표상을 BFS로 탐색하고 최단거리인 경로가 몇 개 인지 찾는 문제.

2.  최단 경로의 수를 찾는 과정에서, 이미 방문했던 지점도 목표지점을 찾기 위해
    다시 방문해야 할 필요가 있다. 
    다만 해당 지점에 방문한 것이 해당 지점에 도달한 최단 경로인 상태에서만
    다른 지점으로 움직이도록 만들면 이미 방문한 지점을 다시 방문하고 다른 곳으로 이동하도록 만들 수 있다.
"""

import collections

MAX_SIZE = 300000

N, K = map(int, input().split())


def BFS(N, K):
    q = collections.deque()
    visited = [False] * MAX_SIZE
    case = [0] * MAX_SIZE

    q.append((N, 0))
    visited[N] = 0
    case[N] += 1

    if N == K:
        print(visited[K])
        print(case[K])
        return

    while q:
        curr = q.popleft()

        if visited[K] and visited[K] == curr[1]:
            break

        move = [curr[0] - 1, curr[0] + 1, curr[0] * 2]

        for i in move:
            if i < 0 or i > 100000:
                continue
            if visited[i]:
                if visited[i] == curr[1] + 1:
                    case[i] += 1
                    q.append((i, curr[1] + 1))
            else:
                visited[i] = curr[1] + 1
                case[i] += 1
                q.append((i, curr[1] + 1))

    print(visited[K])
    print(case[K])


BFS(N, K)
