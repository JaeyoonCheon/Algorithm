"""
16928번 뱀과 사다리 게임

1.  1칸에서 100칸 까지의 최단 거리를 찾는 문제.

2.  BFS로 1~6을 더한 칸을 큐에 넣으면서 방문한 곳에 저장된 주사위를 굴린 횟수가
    현재 주사위를 굴린 횟수보다 적으면 갱신하고 큐에 저장.
"""

import sys
import collections

N, M = map(int, sys.stdin.readline().split())

ladder = {}

for _ in range(N + M):
    _from, _to = map(int, sys.stdin.readline().split())
    ladder[_from] = _to

visited = [100] * 101
q = collections.deque()


def jump(curr):
    if ladder.get(curr) != None:
        return ladder[curr]
    else:
        return curr


def BFS():
    q.append((1, 0))
    visited[1] = 0

    while q:
        curr = q.popleft()
        count = curr[1] + 1

        for i in range(1, 7):
            next = curr[0] + i
            if next <= 100:
                if visited[next] > count:
                    visited[next] = count
                    q.append((jump(next), count))

    print(visited[100])


BFS()
