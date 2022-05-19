"""
11279번 최대 힙
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
