"""
1679번 숨바꼭질

1.  1차원 형태의 BFS 최단 거리 문제
"""

from collections import deque
import sys

N, K = map(int, input().split())

if N == K:
    print("0")
    sys.exit()

visited = [False] * 100001

q = deque()

q.appendleft((N, 1))
visited[N] = True

while q:
    curr = q.pop()

    dx = curr[0]-1
    if dx == K:
        print(curr[1])
        break
    if dx>0 and dx<=100000:
        if visited[dx] != True:
            visited[dx] = True
            q.appendleft((dx, curr[1]+1))
    
    dx = curr[0]+1
    if dx == K:
        print(curr[1])
        break
    if dx>0 and dx<=100000:
        if visited[dx] != True:
            visited[dx] = True
            q.appendleft((dx, curr[1]+1))

    dx = curr[0]*2
    if dx == K:
        print(curr[1])
        break
    if dx>0 and dx<=100000:
        if visited[dx] != True:
            visited[dx] = True
            q.appendleft((dx, curr[1]+1))