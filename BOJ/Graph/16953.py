"""
16953번 A -> B

1.  A에서 2가지 방법을 통해 B로 가는 최단 시간이므로, 곧 1차원 BFS 최단경로의 문제로 해석할 수 있다.

2.  조건을 잘 살펴보면, 수는 무조건 증가하는 방향으로 만들어지고 10^9 크기의 수까지 허용이 된다.
    이 경우, 방문 배열을 만들어 저장하면 메모리 초과가 발생할 것이므로 방문 배열없이 수를 중복을 허용하고
    계속해서 큐에 집어넣는 BFS를 만드는 것이 효율적.
"""

import collections

MAX_NUM_SIZE = 1000000000

A, B = map(int, input().split())


def BFS(A, B):
    q = collections.deque()
    isFound = False

    q.append((A, 0))

    while q:
        curr = q.popleft()

        if curr[0] == B:
            print(curr[1] + 1)
            isFound = True

        nextNum = [curr[0] * 2, curr[0] * 10 + 1]

        for i in nextNum:
            if i < MAX_NUM_SIZE:
                q.append((i, curr[1] + 1))

    if not isFound:
        print(-1)


BFS(A, B)
