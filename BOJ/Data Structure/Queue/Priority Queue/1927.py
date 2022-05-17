"""
1927번 최소 힙

1.  우선순위 큐 중 최소 힙의 구현을 이용한 문제.

2.  처음 시도에는 파이썬 queue 모듈 중 priority queue를 이용하였다.
    하지만 시간 초과가 발생.
    
3.  heapq 모듈의 기능을 사용해 힙을 만들어 구현하니 통과.
    내부적 구현 방법에 따라 시간 복잡도의 차이가 있는 것으로 생각된다.
"""

import heapq
import sys

minHeap = []

N = int(input())

for _ in range(N):
    operation = int(sys.stdin.readline())

    if operation == 0:
        if minHeap:
            print(heapq.heappop(minHeap))
        else:
            print(0)
    else:
        heapq.heappush(minHeap, operation)
