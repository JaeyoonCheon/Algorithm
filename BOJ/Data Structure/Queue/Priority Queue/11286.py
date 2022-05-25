"""
11286번 절댓값 힙

1.  처음 시도에서는 파이썬 내장 함수 중 queue.PriorityQueue를 사용하여
    절대값과 값을 함께 튜플로 저장하는 식으로 구현하였는데 1초 시간 제한에 통과하지 못했다.
    priorityQueue 연산 자체가 O(N)시간복잡도일 것으로 예상되는데 100000개 케이스를
    효율적으로 처리하지 못했기 때문으로 생각된다.
    
2.  O(logN) 또는 O(1)로 구현하기 위해 push/pop이 O(1)인 headq를 사용하도록 변경했더니
    통과할 수 있었다.
"""

import queue
import heapq
import sys

N = int(input())

q = queue.PriorityQueue()

heap = []


def priorityQ():
    for _ in range(N):
        num = int(sys.stdin.readline())

        if num != 0:
            q.put((abs(num), num))
        else:
            if not q.empty():
                poped = q.get()
                print(poped[1])
            else:
                print(0)


def heapQ():
    for _ in range(N):
        num = int(sys.stdin.readline())

        if num != 0:
            heapq.heappush(heap, (abs(num), num))
        else:
            if heap:
                poped = heapq.heappop(heap)
                print(poped[1])
            else:
                print(0)


heapQ()
