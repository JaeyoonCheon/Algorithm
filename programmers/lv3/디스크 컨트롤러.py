"""
    lv.3 디스크 컨트롤러
    
    1.  현재 처리할 수 있는 가장 짧은 소요시간을 가진 작업부터 처리하면 최단시간 소요.
    2.  우선순위 큐를 사용해 현재 시점에 처리할 수 있는 작업을 push / 처리해야할 다음 작업을 pop한 뒤
        작업을 시작한 시간/끝낸 시간을 계산해 포인터를 옮기면서 처리.
"""

import heapq


def solution(jobs):
    answer = 0

    pq = []

    prev = -1
    current = 0
    finishedTasks = 0

    while finishedTasks < len(jobs):
        for job in jobs:
            if prev < job[0] <= current:
                heapq.heappush(pq, job[::-1])

        if len(pq) > 0:
            task = heapq.heappop(pq)

            prev = current
            current += task[0]

            taskRequestedTime = task[1]
            answer += current - taskRequestedTime
            finishedTasks += 1
        else:
            current += 1

    return answer // len(jobs)


result = solution([[0, 3], [1, 9], [2, 6]])
