"""
9205번 맥주 마시면서 걸어가기

1.  주어진 시작점으로부터 '맥주'라는 조건을 가지고 축제까지 도달할 수 있는가를 물어보는 문제.

2.  처음에는 -32768~32767 범위의 2차원 좌표에 주어졌으니 단순히 집에서 1칸씩 전파되어나가는 방식으로 생각했었다.
    그러나 이 방식은 맥주 양에 따라 너무나도 많은 경우의 수가 생겨 비효율적일 것으로 생각되었다.
    
3.  곧 잘 생각해보니 어떻게든 집에서 축제장까지 도착만 하면 되는 것이므로, 집이든 편의점이든 축제장에 도착할 수 있는지만 검사하면 되는 것이고
    그래프의 노드는 집과 편의점의 위치만 고려하면 되었다. 왜냐하면 다른 위치는 맥주가 충분해 축제장에 도착할 수 있다면 갈 필요가 없고
    맥주는 편의점에서 새로 보충되므로 궁극적인 거리가 늘어나는 지점이기 때문이다.
    
4.  따라서, BFS로 집-편의점의 좌표를 가지고 축제에 도달할 수 있는 경우를 검사하면 풀이할 수 있는 문제이다.
"""

import sys, collections

MAX_DIST = 32768

T = int(input())


def checkDist(A, B):
    if abs(B[0] - A[0]) + abs(B[1] - A[1]) > 1000:
        return False
    return True


for _ in range(T):
    N = int(input())
    home = list(map(int, sys.stdin.readline().split()))
    conv = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    festival = list(map(int, sys.stdin.readline().split()))

    M = len(conv)

    visited = [False] * N
    q = collections.deque()
    canGo = False

    q.append(home)

    while q:
        curr = q.popleft()

        if checkDist(curr, festival):
            canGo = True
            break

        for i, cv in enumerate(conv):
            if not visited[i] and checkDist(curr, cv):
                visited[i] = True
                q.append(cv)

    if canGo:
        print("happy")
    else:
        print("sad")
