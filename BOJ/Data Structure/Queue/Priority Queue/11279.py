"""
11279번 최대 힙

1.  최대 큐의 구현을 물어보는 문제.

2.  파이썬 heapq 모듈에서 제공하는 힙은 최소 힙이다.
    별도 최대 힙에 대한 구현부가 없으므로 최소 힙을 이용하여 최대 힙을 만들어야 한다.

3.  heapq는 튜플로 된 값이 저장될 경우 첫 번째 인덱스의 값을 기준으로 최소 힙을 구성한다.
    따라서, (-input, input)으로 값을 push하면 값의 역순으로 저장되므로 최대 힙을 구현할 수 있다.
"""

import sys
import heapq

N = int(input())

heap = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-data, data))
