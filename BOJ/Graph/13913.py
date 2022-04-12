"""
13913번 숨바꼭질 4

1.  1차원 형태의 BFS 최단 거리 문제 + 경로 출력

2.  BFS문제에서 경로를 출력하기 위해서는 처음 방문하는 위치를 방문했을 때 기록하는 visited 배열에
    바로 직전 위치를 단 한번만 기록해 놓으면 최단 경로 중 하나가 기록된다. 이것을 목적지에 도달하면
    거꾸로 출력하면 정답
    
3.  N = k일 경우와 0 ~ 100000까지 등의 반례에서, 시작점과 도착점이 동일할 경우를 예외처리해 주어야 하며
    파이썬이 0과 False를 동일하게 간주하여 인덱스를 침범하게 되는 문제를 고려해야 예외 케이스를 피할 수 있다.
"""

from collections import deque
import sys

N, K = map(int, input().split())

if N == K:
    print("0")
    print(N)
    sys.exit()

visited = [-1] * 100001

q = deque()

q.appendleft((N, 1))
visited[N] = -2

while q:
    curr = q.pop()

    dx = curr[0] - 1
    if dx == K:
        visited[dx] = curr[0]
        print(curr[1])
        break
    if dx > 0 and dx <= 100000:
        if visited[dx] == -1:
            visited[dx] = curr[0]
            q.appendleft((dx, curr[1] + 1))

    dx = curr[0] + 1
    if dx == K:
        visited[dx] = curr[0]
        print(curr[1])
        break
    if dx > 0 and dx <= 100000:
        if visited[dx] == -1:
            visited[dx] = curr[0]
            q.appendleft((dx, curr[1] + 1))

    dx = curr[0] * 2
    if dx == K:
        visited[dx] = curr[0]
        print(curr[1])
        break
    if dx > 0 and dx <= 100000:
        if visited[dx] == -1:
            visited[dx] = curr[0]
            q.appendleft((dx, curr[1] + 1))

x = dx

seq = []

while visited[x] != -2:
    seq.append(x)
    x = visited[x]

seq.append(x)

seq.reverse()

for i in seq:
    print(i, end=" ")
