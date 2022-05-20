"""
7662번 이중 우선순위 큐

1.  우선 파이썬의 우선순위 큐로 사용되는 heapq는 최소 힙이다.
    따라서, 이중으로 구성된 우선순위 큐를 만드려면 두 개의 큐를 사용하거나
    Min-Max heap을 적용해야 한다.
    
2.  두 개의 heapq를 사용해 풀이했으나, 한 쪽에서 최대/최소값을 pop했을 때
    다른 힙의 동일한 값을 없애주어야 하는데 사용된 list.remove()연산이 O(N) 시간복잡도를 가져
    시간 초과가 발생
    
3.  remove 연산을 하지 않기 위해, 힙에 튜플로 몇 번째 인덱스인지 저장하고
    - 삽입 시 큐에 들어간 값의 인덱스는 True로 체크
    - 삭제 시 값의 동기화는 각자의 삭제 턴 & 마지막에만 이루어지도록 변경
        1)  우선, pop 연산이 이루어지기 이전에 최대값이라면 최대 힙에서, 최소값이라면 최소 힙에서
        값이 있는 동안 visited에 False로 기록된 값이 pop 될 값이라면 다른 힙에서 이미 삭제된 값이므로
        pop 하여 동기화 시켜준다.
        2)  이후, 힙에 값이 있다면 해당 값을 삭제된 것으로 visited에 표기하고 pop해준다.
        3)  모든 명령이 이루어지고 난 후, 최종 동기화를 한번 더 해준다.
"""

import sys
import heapq


T = int(input())

for _ in range(T):
    N = int(input())
    maxHeap = []
    minHeap = []
    visited = [False] * 1000001

    for i in range(N):
        op, num = sys.stdin.readline().split()
        num = int(num)

        if op == "I":
            heapq.heappush(minHeap, (num, i))
            heapq.heappush(maxHeap, (-num, i))
            visited[i] = True
        else:
            if num == 1:
                while maxHeap and not visited[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
            else:
                while minHeap and not visited[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)

    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)

    if not minHeap and not maxHeap:
        print("EMPTY")
    else:
        maxVal = -heapq.heappop(maxHeap)[0]
        minVal = heapq.heappop(minHeap)[0]

        print(f"{maxVal} {minVal}")
