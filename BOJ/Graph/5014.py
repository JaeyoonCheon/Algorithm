"""
5014번 스타트링크

1.  1~F의 1차원 좌표를 가진 선형 BFS 최단 거리 문제.
"""

import collections

F, S, G, U, D = map(int, input().split())

q = collections.deque()
visited = [False] * (F + 1)

visited[S] = True
q.append((S, 0))

answer = -1

while q:
    curr = q.popleft()
    pos, count = curr[0], curr[1]

    if pos == G:
        answer = count
        break

    if pos + U <= F:
        if not visited[pos + U]:
            visited[pos + U] = True
            q.append((pos + U, count + 1))
    if pos - D > 0:
        if not visited[pos - D]:
            visited[pos - D] = True
            q.append((pos - D, count + 1))

if answer == -1:
    print("use the stairs")
else:
    print(answer)
