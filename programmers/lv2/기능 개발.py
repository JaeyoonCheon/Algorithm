"""
    lv.2 기능 개발
    
    1.  무조건 뒤의 작업은 앞의 작업이 완료되어야 같이 종료될 수 있다.
        따라서, 스택을 이용해 top이 100이상일때만 pop되도록 로직을 작성.
    2.  뽑는 방향을 두 리스트 모두 뒤집어 생각하면 편리.
"""


def solution(progresses, speeds):
    answer = []

    stack = list(reversed(progresses))
    speeds.reverse()

    while stack:
        for i in range(len(stack)):
            stack[i] += speeds[i]

        finished = 0

        while stack and stack[-1] >= 100:
            stack.pop()
            speeds.pop()

            finished += 1

        if finished > 0:
            answer.append(finished)

    return answer


result = solution([93, 30, 55], [1, 30, 5])
