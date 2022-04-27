"""
1966번 프린터 큐

1.  큐의 동작 구현 + 문제 시뮬레이션
"""

import collections


def compute(q, N, M):
    count = 1
    if N == 1:
        print(1)
        return
    while q:
        skipped = False
        waiting = q.popleft()
        for i in q:
            if waiting < i:
                q.append(waiting)
                M -= 1
                if M == -1:
                    M = N - 1
                skipped = True
                break
        if not skipped:
            if M == 0:
                print(count)
            N -= 1
            M -= 1
            count += 1


T = int(input())


for _ in range(T):
    N, M = map(int, input().split())
    q = collections.deque()

    numbers = list(map(int, input().split()))
    q.extend(numbers)

    compute(q, N, M)
