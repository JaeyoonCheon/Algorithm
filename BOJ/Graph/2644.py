"""
2644번 촌수계산

1.  간단한 그래프 상의 두 점 간 거리를 출력하는 문제.
    BFS에서 거리를 저장하는 방식으로 쉽게 구할 수 있다.
"""

import sys, collections

N = int(input())
one, another = map(int, input().split())

relations = [[] for _ in range(N + 1)]

M = int(input())

for _ in range(M):
    _from, _to = map(int, sys.stdin.readline().split())

    relations[_from].append(_to)
    relations[_to].append(_from)

visited = [False] * (N + 1)
q = collections.deque()
q.append((one, 0))
visited[one] = True

answer = -1

while q:
    curr = q.popleft()
    number, dist = curr[0], curr[1]

    if number == another:
        answer = dist
        break

    for next in relations[number]:
        if not visited[next]:
            q.append((next, dist + 1))
            visited[next] = True

print(answer)
